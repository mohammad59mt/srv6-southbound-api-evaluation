# !/usr/bin/python

from sshnode import sshNode 
import argparse
import sys
import paramiko
import psutil
import time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Object representing a SRv6 ssh node
class SRv6sshNode(sshNode):

  def __init__(self, host, loginName, loginPass):
    # Store the internal state
    self.host = host
    self.name = loginName
    self.passwd = loginPass
    # Explicit stop
    self.stop = False
    # Spawn a new thread and connect in ssh
    self.connect()

def get_args(functionName):
  if functionName == 'addsr':
     '''This function parses and return arguments passed in'''
     # Assign description to the help doc
     parser = argparse.ArgumentParser(
         description='Parameters to add SRv6 route')
     # Add arguments
     parser.add_argument(
         '-i', '--server', type=str, help='Server ip and port', required=True)
     parser.add_argument(
         '-p', '--prefix', type=str, help='Prefix', required=True)
     parser.add_argument(
         '-e', '--encapmode', type=str, help='Encapmode', required=True)
     parser.add_argument(
         '-s', '--segments', type=str, help='Segments', required=True)
     parser.add_argument(
         '-d', '--device', type=str, help='Device', required=True)
     parser.add_argument(
         '-u', '--username', type=str, help='Login Username', required=False)
     parser.add_argument(
         '-w', '--password', type=str, help='Login Password', required=False)
     parser.add_argument(
         '-n', '--number', type=str, help='Number of entries to be enforced', required=True)
     parser.add_argument(
         '-m', '--mode', type=str, help='Mode (bunch: b, sequential: s, sequentialInOneConnection: si', required=True)
     parser.add_argument(
       '-f', '--fileName', type=str, help='Index for file name (1, 2, 3, ...)', required=True)
     parser.add_argument('addsr')
     # Array for all arguments passed to script
     args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
     return args

  elif functionName == 'del':
    parser = argparse.ArgumentParser(
         description='Parameters to delete route')
     # Add arguments
    parser.add_argument(
         '-i', '--server', type=str, help='Server ip and port', required=True)
    parser.add_argument(
         '-p', '--prefix', type=str, help='Prefix', required=True)
    parser.add_argument(
         '-d', '--device', type=str, help='Device', required=True)
    parser.add_argument(
         '-u', '--username', type=str, help='Login Username', required=False)
    parser.add_argument(
         '-w', '--password', type=str, help='Login Password', required=False)
    parser.add_argument(
         '-n', '--number', type=str, help='Number of entries to be enforced', required=True)
    parser.add_argument(
         '-m', '--mode', type=str, help='Mode (bunch: b, sequential: s, sequentialInOneConnection: si', required=True)
    parser.add_argument(
       '-f', '--fileName', type=str, help='Index for file name (1, 2, 3, ...)', required=True)
    parser.add_argument('del')
     # Array for all arguments passed to script
    args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
    return args

  elif functionName == 'changesr':
    parser = argparse.ArgumentParser(
         description='Parameters to change SRv6 route')
     # Add arguments
    parser.add_argument(
         '-i', '--server', type=str, help='Server ip and port', required=True)
    parser.add_argument(
         '-p', '--prefix', type=str, help='Prefix', required=True)
    parser.add_argument(
         '-s', '--segments', type=str, help='Segments', required=True)
    parser.add_argument(
         '-d', '--device', type=str, help='Device', required=True)
    parser.add_argument(
         '-u', '--username', type=str, help='Login Username', required=False)
    parser.add_argument(
         '-w', '--password', type=str, help='Login Password', required=False)
    parser.add_argument(
         '-n', '--number', type=str, help='Number of entries to be enforced', required=True)
    parser.add_argument(
         '-m', '--mode', type=str, help='Mode (bunch: b, sequential: s, sequentialInOneConnection: si', required=True)
    parser.add_argument(
       '-f', '--fileName', type=str, help='Index for file name (1, 2, 3, ...)', required=True)
    parser.add_argument('changesr')
    # Array for all arguments passed to script
    args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
    return args

def run(args):
  #set username and password for login
  if hasattr(args,'username'):
    loginUsername= args.username
  else:
    loginUsername='root'
  if hasattr(args,'password'):
    loginPass= args.password
  else:
    loginPass='root'

  if args.mode == 'b':
    command = ''
    for i in range(1, int(args.number)+1):
      if 'addsr' in args:
        command += "ip -6 route add %s encap seg6 mode %s segs %s dev %s; " %(args.prefix+str(i), args.encapmode, args.segments, args.device)
      elif 'del' in args:    
        command += "ip -6 route del %s dev %s; " %(args.prefix+str(i), args.device)
      elif 'changesr' in args:
        command += "ip -6 r change %s encap seg6 mode encap segs %s dev %s; " %(args.prefix+str(i), args.egments, args.device)
    client = SRv6sshNode(host=args.server, loginName=loginUsername, loginPass=loginPass)
    client.run_command(command)
    client.terminate()
  elif args.mode == 's':
    for i in range(1, int(args.number)+1):
      if 'addsr' in args:
        command = "ip -6 route add %s encap seg6 mode %s segs %s dev %s; " %(args.prefix+str(i), args.encapmode, args.segments, args.device)
      elif 'del' in args:    
        command = "ip -6 route del %s dev %s; " %(args.prefix+str(i), args.device)
      elif 'changesr' in args:
        command = "ip -6 r change %s encap seg6 mode encap segs %s dev %s; " %(args.prefix+str(i), args.egments, args.device)
      client = SRv6sshNode(host=args.server, loginName=loginUsername, loginPass=loginPass)
      client.run_command(command)
      client.terminate()
  elif args.mode == 'si':
    client = SRv6sshNode(host=args.server, loginName=loginUsername, loginPass=loginPass)
    for i in range(1, int(args.number)+1):
      if 'addsr' in args:
        command = "ip -6 route add %s encap seg6 mode %s segs %s dev %s; " %(args.prefix+str(i), args.encapmode, args.segments, args.device)
      elif 'del' in args:    
        command = "ip -6 route del %s dev %s; " %(args.prefix+str(i), args.device)
      elif 'changesr' in args:
        command = "ip -6 r change %s encap seg6 mode encap segs %s dev %s; " %(args.prefix+str(i), args.egments, args.device)
      client.run_command(command)
    client.terminate()
  else:
    print(bcolors.FAIL + "mode should be: b(bunch), s(sequential), si (sequentialInOneConnection)"+ bcolors.ENDC)

if __name__ == '__main__':

  functionName = sys.argv[1]
  args = get_args(functionName)

  p=psutil.Process(os.getpid())
  p.cpu_percent()
  psutil.cpu_percent()
  start_time = time.time()
  run(args)
  executionTime=time.time() - start_time
  appCPUUsage = p.cpu_percent()*executionTime
  SystemCPUUsage = psutil.cpu_percent()*executionTime
  memoryUsage = p.memory_info()[0]/2.**10

  print(bcolors.OKBLUE + "Execution time: " + str(executionTime) + bcolors.ENDC)
  print(bcolors.OKBLUE + "App CPU Usage: " + str(appCPUUsage) + bcolors.ENDC)
  print(bcolors.OKBLUE + "Total CPU Usage: " + str(SystemCPUUsage) + bcolors.ENDC)
  print(bcolors.OKBLUE + "Memory Usage (KB): " + str(memoryUsage) + bcolors.ENDC)

  f1 = open(args.fileName +'.txt','a+')
  f1.write(str(executionTime) + '\n')
  f1.write( str(appCPUUsage) + '\n')
  f1.write(str(SystemCPUUsage) + '\n')
  f1.write(str(memoryUsage) + '\n\n')
  f1.close()
