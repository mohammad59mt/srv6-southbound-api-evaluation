#!/usr/bin/python

from threading import Thread

import paramiko
import re
import os
import time
import sys
from datetime import datetime

# Object representing a generic ssh node
class sshNode(object):

  # Initialization
  def __init__(self, host, name):
    # Store the internal state
    self.host = host
    self.name = name
    self.passwd = "rocks"
    # Explicit stop
    self.stop = False
    # Spawn a new thread and connect in ssh
    self.t_connect()

  # Connect in ssh using a new thread
  def t_connect(self):
    # Main function is self.connect
    self.conn_thread = Thread(target=self.connect)
    # Start the thread
    self.conn_thread.start()
    # Wait for the end
    self.conn_thread.join()

  # Connect function
  def connect(self):
    # Spawn a ssh client
    self.client = paramiko.SSHClient()
    # Auto add policy
    self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to the Mininet host
    self.client.connect(self.host, username=self.name, password=self.passwd)
    # Spawn a channel to send commands
    self.chan = self.client.invoke_shell()
    # Wait for the end
    self.wait()

  # Wait for the end of the previous command
  def wait(self):
    # Init steps
    buff  = ''
    # Exit conditions
    s     = re.compile('[^#]# ')
    u     = re.compile('[$] ')
    # Iterate until the stdout ends or the stop condition has been triggered
    while not u.search(buff) and not s.search(buff) and self.stop == False:
      # Rcv from the channel the stdout
      resp = self.chan.recv(1024)
      # if it is a sudo command, send the password
      if re.search(".*\[sudo\].*", resp):
        self.chan.send("%s\r" %(self.passwd))
      # Add response on buffer
      buff += resp
      # Write on the log file if not init
      #self.log.write(resp)
    # if not init write \n
    #self.log.write("\n")
    # Done, return the response
    return buff

  # Run the command and wait for the end
  def run_command(self, command):
    # Send the command on the channel with \r
    self.chan.send(command + "\r")
    # Wait for the end and take the stdout
    buff = self.wait()
    # Save in data the stdout of the last cmd
    self.data = buff
    
  # Create a new worker thread
  def run(self, command):
    # Create a new Thread
    self.op_thread = Thread(
      target=self.run_command,
      args=([command])
      )
    # Start the thread
    self.op_thread.start()

  # Stop any running execution and close the connection
  def terminate(self):
    # Terminate signal for the thread
    self.stop = True
    # If the connection has been initialized
    if self.client != None:
      # Let's close it
      self.client.close()
    # Close log file
    if hasattr(self, 'log'):
      self.log.close()
    # Wait for the termination of the worker thread
    if hasattr(self, 'op_thread'):
      self.op_thread.join()

  # Join with the thread
  def join(self):   
    self.op_thread.join()

# Utility function to set bw and start an iperf server
def iperf_server(node, server_port):
  # Start iperf3 server
  node.run("iperf3 -s -1 -p %s -i 10" %(server_port))

# Utility function to set bw and start an iper client
def iperf_client(node, server, server_port, time):
  # Start iperf3 client
  node.run("iperf3 -c %s -p %s -i 10 -t %s" % (server, server_port, time))

# Utility function to setup metering
def setup_metering(node, flow_id, bw, ip_src, ip_dst, dport):
  # Let's clean the filter
  node.run_command("sudo tc filter del dev %s-eth1 parent 1: handle 800::%d prio 10 protocol \
    ip u32" %(node.name, flow_id))
  # Let's clean the class
  node.run_command("sudo tc class del dev %s-eth1 classid 1:%d" %(node.name, flow_id))
  # Create class for the provided flow_id and the given bw
  node.run_command("sudo tc class add dev %s-eth1 parent 1: classid 1:%d cbq rate %dmbit \
    allot 1500 prio 5 bounded isolated" %(node.name, flow_id, bw)) 
  # Create filter for the class
  node.run_command("sudo tc filter add dev %s-eth1 parent 1: handle ::%d protocol ip prio 10 \
    u32 match ip src %s match ip dst %s match ip dport %d 0xffff flowid 1:%d" \
    %(node.name, flow_id, ip_src, ip_dst, dport, flow_id))

# Utility function to wait an iper c/s
def wait_iperf(clients, servers):
  # Join with servers
  for server in servers:
    server.join()
  # Join with clients
  for client in clients:
    client.join()
  
if __name__ == '__main__':

  # Generic params
  client_ip   = "10.0.4.1"
  server_ip   = "10.0.5.1"
  flow_id     = 1
  server_port = 5000 + flow_id
  bw          = 2
  exp_time    = 120
  # Server params
  server      = "cer6"
  server_host = "10.255.251.1" 
  # Client params
  client      = "cer5"
  client_host = "10.255.252.1" 

  # Create server node
  server1 = sshNode(host=server_host, name=server)
  iperf_server(server1, server_port)
  # Create client node
  client1 = sshNode(host=client_host, name=client)
  setup_metering(client1, flow_id, bw, client_ip, server_ip, server_port)
  iperf_client(client1, server_ip, server_port, exp_time)

  client_ip   = "10.0.4.1"
  server_ip   = "10.0.5.1"
  flow_id     = 2
  server_port = 5000 + flow_id
  bw          = 5
  exp_time    = 120
  server      = "cer6"
  server_host = "10.255.251.1" 
  client      = "cer5"
  client_host = "10.255.252.1"

  server2 = sshNode(host=server_host, name=server)
  iperf_server(server2, server_port)
  client2 = sshNode(host=client_host, name=client)
  setup_metering(client2, flow_id, bw, client_ip, server_ip, server_port)
  iperf_client(client2, server_ip, server_port, exp_time) 

  # Wait the end
  print "Running"
  wait_iperf([client1, client2], [server1, server2])
  