# !/usr/bin/python


# Copyright (C) 2018 Pier Luigi Ventre, Stefano Salsano, Alessandro Masci - (CNIT and University of Rome "Tor Vergata")
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Python implementation of route guide client over SSH
#
# @author Pier Luigi Ventre <pier.luigi.ventre@uniroma2.it>
# @author Stefano Salsano <stefano.salsano@uniroma2.it>
# @author Alessandro Masci <mascialessandro89@gmail.com>
#

from sshnode import sshNode 
import argparse
import sys
import paramiko

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
    parser.add_argument('del')
     # Array for all arguments passed to script
    args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
    return args

  elif functionName == 'list':
    parser = argparse.ArgumentParser(
         description='Parameters to show ipv6 routes')
     # Add arguments
    parser.add_argument(
         '-i', '--server', type=str, help='Server ip and port', required=True)
    parser.add_argument(
         '-u', '--username', type=str, help='Login Username', required=False)
    parser.add_argument(
         '-w', '--password', type=str, help='Login Password', required=False)
    parser.add_argument('list')
    # Array for all arguments passed to script
    args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
    return args

  elif functionName == 'change':
    parser = argparse.ArgumentParser(
         description='Parameters to change route')
     # Add arguments
    parser.add_argument(
         '-i', '--server', type=str, help='Server ip and port', required=True)
    parser.add_argument(
         '-p', '--prefix', type=str, help='Prefix', required=True)
    parser.add_argument(
         '-v', '--via', type=str, help='Via', required=True) 
    parser.add_argument(
         '-u', '--username', type=str, help='Login Username', required=False)
    parser.add_argument(
         '-w', '--password', type=str, help='Login Password', required=False)
    parser.add_argument('change')
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

  # Create client node
  client = SRv6sshNode(host=args.server, loginName=loginUsername, loginPass=loginPass)
  
  if 'addsr' in args:
    command = "sudo ip -6 route add %s encap seg6 mode %s segs %s dev %s" %(args.prefix, args.encapmode, args.segments, args.device)

  elif 'del' in args:    
    command = "sudo ip -6 route del %s dev %s" %(args.prefix, args.device)

  elif 'list' in args:
    command ="sudo ip -6 route"

  elif 'change' in args: 
    command = "sudo ip -6 route change %s via %s"%(args.prefix, args.via)

  elif 'changesr' in args:
    command = "sudo ip -6 r change %s encap seg6 mode encap segs %s dev %s" %(args.prefix, args.egments, args.device)

  print command

  client.run_command(command)
  
  if 'list' in args:
    print client.data

  client.terminate()

if __name__ == '__main__':
  functionName = sys.argv[1]
  args = get_args(functionName)
  run(args)