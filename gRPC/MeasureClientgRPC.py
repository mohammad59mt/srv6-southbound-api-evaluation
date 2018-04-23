# !/usr/bin/python

from __future__ import print_function

import grpc
import parameters_pb2
import parameters_pb2_grpc
import time
import sys,getopt
import argparse,psutil,os
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
       description='Parameters to add SRv6 route')
   # Add arguments
   parser.add_argument(
       '-i', '--server', type=str, help='Server ip and port', required=True)
   parser.add_argument(
       '-p', '--prefix', type=str, help='Prefix', required=True)
   parser.add_argument(
       '-s', '--segments', type=str, help='Segments', required=False)
   parser.add_argument(
         '-e', '--encapmode', type=str, help='Encapmode', required=False)
   parser.add_argument(
       '-d', '--device', type=str, help='Device', required=True)
   parser.add_argument(
       '-o', '--operation', type=str, help='Operation (Add, Del)', required=True)
   parser.add_argument(
       '-u', '--secured', type=str, help='secured with TLS (yes, no)', required=True)
   parser.add_argument(
       '-n', '--number', type=str, help='Number of entries to be enforced', required=True)
   parser.add_argument(
       '-m', '--mode', type=str, help='Mode (bunch: b, sequential: s, sequentialInOneConnection: si)', required=True)
   parser.add_argument(
       '-f', '--fileName', type=str, help='Index for file name (1, 2, 3, ...)', required=True)
   # Array for all arguments passed to script
   args = parser.parse_args()
   # Assign args to variables
   # Return all variable values
   return args

def run(args):
  if args.mode == 's':
    if args.operation=='add':
      for i in range(1,int(args.number)+1):
        if args.secured == 'yes':
          creds = grpc.ssl_channel_credentials(open('server.pem').read())
          channel = grpc.secure_channel(args.server,creds)
        elif args.secured == 'no':
          channel = grpc.insecure_channel(args.server)
        else:
          print('-u must be either yes or no')
          return
        stub = parameters_pb2_grpc.SegmentRoutingStub(channel)
        response = stub.AddSrRoute(parameters_pb2.AddSrRouteRequest(prefix=args.prefix+str(i),encapmode=args.encapmode,segments=args.segments,device=args.device))
    elif args.operation=='del':
      for i in range(1,int(args.number)+1):
        if args.secured == 'yes':
          creds = grpc.ssl_channel_credentials(open('server.pem').read())
          channel = grpc.secure_channel(args.server,creds)
        elif args.secured == 'no':
          channel = grpc.insecure_channel(args.server)
        else:
          print('-u must be either yes or no')
          return
        stub = parameters_pb2_grpc.SegmentRoutingStub(channel)
        response = stub.RemoveRoute(parameters_pb2.RmRouteRequest(prefix=args.prefix+str(i),device=args.device))
    else:
        print("-o must be add or del")

  elif args.mode == 'si':
    if args.secured == 'yes':
      creds = grpc.ssl_channel_credentials(open('server.pem').read())
      channel = grpc.secure_channel(args.server,creds)
    elif args.secured == 'no':
      channel = grpc.insecure_channel(args.server)
    else:
      print('-u must be either yes or no')
      return
    stub = parameters_pb2_grpc.SegmentRoutingStub(channel)
    if args.operation=='add':
      for i in range(1,int(args.number)+1):
        response = stub.AddSrRoute(parameters_pb2.AddSrRouteRequest(prefix=args.prefix+str(i),encapmode=args.encapmode,segments=args.segments,device=args.device))
    elif args.operation=='del':
      for i in range(1,int(args.number)+1):
        response = stub.RemoveRoute(parameters_pb2.RmRouteRequest(prefix=args.prefix+str(i),device=args.device))
    else:
        print("-o must be add or del")

  elif args.mode == 'b':
    if args.operation=='add':
      if args.secured == 'yes':
        creds = grpc.ssl_channel_credentials(open('server.pem').read())
        channel = grpc.secure_channel(args.server,creds)
      elif args.secured == 'no':
        channel = grpc.insecure_channel(args.server)
      else:
        print('-u must be either yes or no')
        return
      stub = parameters_pb2_grpc.SegmentRoutingStub(channel)
      prefixes=""
      segments=""
      devices=""
      encapmodes=""
      for i in range(1,int(args.number)+1):
        prefixes+=args.prefix+str(i)+';'
        segments+=args.segments+"-"
        devices+=args.device+';'
        encapmodes+='encap;'
      response = stub.BunchAddSrRoute(parameters_pb2.AddSrRouteRequest(prefix= prefixes,encapmode=encapmodes,segments=segments,device=devices))
    elif args.operation=='del':
      if args.secured == 'yes':
        creds = grpc.ssl_channel_credentials(open('server.pem').read())
        channel = grpc.secure_channel(args.server,creds)
      elif args.secured == 'no':
        channel = grpc.insecure_channel(args.server)
      else:
        print('-u must be either yes or no')
        return
      stub = parameters_pb2_grpc.SegmentRoutingStub(channel)
      prefixes = ''
      devices = ''
      for i in range(1,int(args.number)+1):
        prefixes+=args.prefix+str(i)+';'
        devices+=args.device+';'
      response = stub.BunchRemoveRoute(parameters_pb2.RmRouteRequest(prefix= prefixes,device=devices))
    else:
        print("-o must be add or del")
  else:
    print('-m must be -> bunch: b, sequential: s, or sequentialInOneConnection: si')


if __name__ == '__main__':
  args = get_args()

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
