# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the gRPC route guide server."""

from __future__ import print_function
from concurrent import futures
import psutil
import time
import math
import sys
import grpc

import os

import argparse

from socket import AF_INET
from pyroute2 import IPRoute

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_args():
  '''This function parses and return arguments passed in'''
  # Assign description to the help doc
  parser = argparse.ArgumentParser(
     description='Script retrieves schedules from a given server')
  # Add arguments
  parser.add_argument(
     '-p', '--prefix', type=str, help='Prefix', required=True)
  parser.add_argument(
     '-n', '--number', type=str, help='Number of requests to send', required=True)
  parser.add_argument(
     '-d', '--device', type=str, help='Device', required=False)
  parser.add_argument(
     '-s', '--segments', type=str, help='Segments', required=False)
  parser.add_argument(
     '-a', '--approach', type=str, help='approach (shell, pyroute2)', required=True)
  parser.add_argument(
     '-o', '--operation', type=str, help='operation (add, delete, change)', required=True)
  # Array for all arguments passed to script
  args = parser.parse_args()
  # Assign args to variables
  # Return all variable values
  return args

def ServerPyroute2(args):
  ip = IPRoute()
  idx = ip.link_lookup(ifname=args.device)[0]

  if args.operation == 'add':
    for i in range(1,int(args.number)+1):
      ip.route('add',
      dst=args.prefix+str(i)+'/128',
      oif=idx,
      encap={'type': 'seg6','mode': 'encap','segs': args.segments})
  elif args.operation=='delete':
    for i in range(1,int(args.number)+1):
      ip.route('delete',
      dst=args.prefix+str(i)+'/128',
      oif=idx)
  elif args.operation=='change':
    for i in range(1,int(args.number)+1):
      ip.route('change',
      dst=args.prefix+str(i)+'/128',
      oif=idx,
      encap={'via': args.segments})
  else:
    print(bcolors.FAIL +'please select \'change\', \'delete\', or \'add\' for input parameter -m'+ bcolors.ENDC)

def ServerShell(args):
  if args.operation == 'add':
    for i in range(1,int(args.number)+1):
      shellCommandToAddRouting="ip -6 route add "+args.prefix+str(i)+'/128'+" encap seg6 mode encap"+" segs "+ args.segments+" dev "+args.device
      os.system(shellCommandToAddRouting)
  elif args.operation=='delete':
    for i in range(1,int(args.number)+1):
      shellCommandToRemoveRouting="ip -6 route del "+args.prefix+str(i)+'/128'+" dev "+args.device
      os.system(shellCommandToRemoveRouting)
  elif args.operation=='change':
    for i in range(1,int(args.number)+1):
      shellCommandToChangeRouting="ip -6 route change "+args.prefix+str(i)+'/128'+" via "+args.segments 
      result=os.system(shellCommandToChangeRouting)
  else:
    print(bcolors.FAIL +'please select \'change\', \'delete\', or \'add\' for input parameter -m'+ bcolors.ENDC)

def serve():
  args = get_args()
  try:
    if args.approach=='pyroute2':
      ServerPyroute2(args)
    elif args.approach=='shell':
      ServerShell(args)
    else:
      print(bcolors.FAIL +'please select \'pyroute2\' or \'shell\' for input parameter -a'+ bcolors.ENDC)
      return
  except KeyboardInterrupt:
    print('Interrupted by user')
    return

if __name__ == '__main__':
  p=psutil.Process(os.getpid())
  p.cpu_percent()
  psutil.cpu_percent()
  start_time = time.time()

  serve()

  executionTime=time.time() - start_time
  appCPUUsage = p.cpu_percent()*executionTime
  SystemCPUUsage = psutil.cpu_percent()*executionTime
  memoryUsage = p.memory_info()[0]/2.**10

  print(bcolors.OKBLUE + "Execution time: " + str(executionTime) + bcolors.ENDC)
  print(bcolors.OKBLUE + "App CPU Usage: " + str(appCPUUsage) + bcolors.ENDC)
  print(bcolors.OKBLUE + "Total CPU Usage: " + str(SystemCPUUsage) + bcolors.ENDC)
  print(bcolors.OKBLUE + "Memory Usage (KB): " + str(memoryUsage) + bcolors.ENDC)

  f1 = open('LocalRuleEnforcement20.txt','a+')
  f1.write(str(executionTime) + '\n')
  f1.write( str(appCPUUsage) + '\n')
  f1.write(str(SystemCPUUsage) + '\n')
  f1.write(str(memoryUsage) + '\n\n')
  f1.close()