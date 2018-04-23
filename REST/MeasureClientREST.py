# !/usr/bin/python

import requests,sys,argparse
import psutil
import time
import math
import os
import urllib3
urllib3.disable_warnings()
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
         '-n', '--number', type=str, help='Number', required=True)
     parser.add_argument(
         '-s', '--segments', type=str, help='Segments', required=False)
     parser.add_argument(
         '-d', '--device', type=str, help='Device', required=True)
     parser.add_argument(
         '-o', '--operation', type=str, help='Operation (Add, Del)', required=True)
     parser.add_argument(
         '-u', '--secured', type=str, help='secured with TLS (yes, no)', required=True)
     parser.add_argument(
         '-m', '--mode', type=str, help='mode (bunch, seq)', required=True)
     parser.add_argument(
       '-f', '--fileName', type=str, help='Index for file name (1, 2, 3, ...)', required=True)
     # Array for all arguments passed to script
     args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
     return args

def run(args):
    prefix = args.prefix
    device = args.device
    if args.secured == "yes":
        conncectionType = "https://["
        connectionPort = "443"
    elif args.secured == "no":
        conncectionType = "http://["
        connectionPort = "80"
    else:
        print(bcolors.FAIL + "-u must be either yes or no" + bcolors.ENDC)
        return

    if args.operation=='add':
        seg = args.segments.split(",")
        length = len(seg)
        segments = ""
        for i in range(0,length):
            if i == length-1:
                segments += "\""+seg[i]+"\""
            else:
                segments += "\""+seg[i]+"\","
        url = conncectionType +args.server+"]:"+ connectionPort+ "/addsr" 
        headers = {'Content-Type': "application/json"}
        payload = ""
        if args.mode == "s":
            for i in range(1,int(args.number)+1):
                payload = "{  \n \"n\":\"1\",\n \"prefix1\":\""+prefix+str(i)+"\",\n   \"encapmode1\":\"encap\",\n   \"segments1\":["+segments+"],\n   \"device1\":\""+device+"\"\n}"
                #print(payload)
                if args.secured == "yes":
                    response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
                else:
                    response = requests.request("POST", url, data=payload, headers=headers)

        if args.mode == "b":
            payload="{  \n \"n\":\""+args.number+"\""
            for i in range(1,int(args.number)+1):
                payload += ", \n \"prefix" + str(i) +"\":\""+prefix+str(i)+"\",\n   \"encapmode"+str(i)+"\":\"encap\",\n   \"segments"+str(i)+"\":["+segments+"],\n   \"device"+str(i)+"\":\""+device+"\""
            payload+="\n}"
            if args.secured == "yes":
                response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
            else:
                response = requests.request("POST", url, data=payload, headers=headers)

    elif args.operation=='del':
        url = conncectionType+args.server+"]:"+ connectionPort+ "/del"
        headers = {'Content-Type': "application/json"}
        if args.mode == "s":
            for i in range(1,int(args.number)+1):
                payload = "{  \n    \"n\":\"1\", \n\"prefix1\":\""+prefix+str(i)+"\",\n   \"device1\":\""+device+"\"\n}"
                if args.secured == "yes":
                    response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
                else:
                    response = requests.request("POST", url, data=payload, headers=headers)
        if args.mode == "b":
            payload="{  \n   \"n\":\""+args.number+"\""
            for i in range(1,int(args.number)+1):
                payload += ", \n \"prefix"+str(i)+"\":\""+prefix+str(i)+"\",\n   \"device"+str(i)+"\":\""+device+"\""
            payload+="\n}"
            #print(payload)
            if args.secured == "yes":
                response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
            else:
                response = requests.request("POST", url, data=payload, headers=headers)

    elif args.operation=='nul':
        seg = args.segments.split(",")
        length = len(seg)
        segments = ""
        for i in range(0,length):
            if i == length-1:
                segments += "\""+seg[i]+"\""
            else:
                segments += "\""+seg[i]+"\","
        url = conncectionType +args.server+"]:"+ connectionPort+ "/addsr" 
        headers = {'Content-Type': "application/json"}
        payload = ""
        if args.mode == "s":
            for i in range(1,int(args.number)+1):
                payload = "{  \n \"n\":\"1\",\n \"prefix1\":\""+prefix+str(i)+"\",\n   \"encapmode1\":\"encap\",\n   \"segments1\":["+segments+"],\n   \"device1\":\""+device+"\"\n}"
                #print(payload)
                if args.secured == "yes":
                    response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
                else:
                    response = requests.request("POST", url, data=payload, headers=headers)

        if args.mode == "b":
            payload="{  \n \"n\":\""+'0'+"\""
            for i in range(1,int(args.number)+1):
                payload += ", \n \"prefix" + str(i) +"\":\""+prefix+str(i)+"\",\n   \"encapmode"+str(i)+"\":\"encap\",\n   \"segments"+str(i)+"\":["+segments+"],\n   \"device"+str(i)+"\":\""+device+"\""
            payload+="\n}"
            if args.secured == "yes":
                response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
            else:
                response = requests.request("POST", url, data=payload, headers=headers)

    else:
        print "-o must be add or del"

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
  #f1 = open('RESTResults20.txt','a+')
  f1.write(str(executionTime) + '\n')
  f1.write( str(appCPUUsage) + '\n')
  f1.write(str(SystemCPUUsage) + '\n')
  f1.write(str(memoryUsage) + '\n\n')
  f1.close()
