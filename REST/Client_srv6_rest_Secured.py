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
# Python implementation of SRv6 functions over HTTP client side
#
# @author Pier Luigi Ventre <pier.luigi.ventre@uniroma2.it>
# @author Stefano Salsano <stefano.salsano@uniroma2.it>
# @author Alessandro Masci <mascialessandro89@gmail.com>
#

import requests,sys,argparse

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
    parser.add_argument('changesr')
    # Array for all arguments passed to script
    args = parser.parse_args()
     # Assign args to variables
     # Return all variable values
    return args

def run(args):

    if 'list' not in args:
        prefix = args.prefix
        print ("Prefix : " + args.prefix)

    print ("IPv6 server address: " + args.server)

    if 'addsr' in args:
        print ("Encapmode : "+ args.encapmode)
        print ("Segments : " + args.segments)
        print ("Device : " + args.device)

        encapmode = args.encapmode
        device = args.device

        seg = args.segments.split(",")
        length = len(seg)
        segments = ""
        for i in range(0,length):
            if i == length-1:
                segments += "\""+seg[i]+"\""
            else:
                segments += "\""+seg[i]+"\","

        url = "https://["+args.server+"]:443/addsr"
        payload = "{  \n   \"prefix\":\""+prefix+"\",\n   \"encapmode\":\""+encapmode+"\",\n   \"segments\":["+segments+"],\n   \"device\":\""+device+"\"\n}"

    elif 'del' in args:
        print ("Device : " + args.device)

        device = args.device

        url = "https://["+args.server+"]:443/del"
        payload = "{  \n   \"prefix\":\""+prefix+"\",\n   \"device\":\""+device+"\"\n}"

    elif 'list' in args:
        url = "https://["+args.server+"]:443/list"
        response = requests.request("GET",url,verify='./server.pem')
        print(response.content)
        return

    elif 'change' in args:
        print ("Via : " + args.via)

        via = args.via

        url = "https://["+args.server+"]:443/change"
        payload = "{  \n   \"prefix\":\""+prefix+"\",\n   \"via\":\""+via+"\"\n}"

    elif 'changesr' in args:
        print ("Segments : " + args.segments)
        print ("Device : " + args.device)

        seg = args.segments.split(",")
        length = len(seg)
        segments = ""
        for i in range(0,length):
            if i == length-1:
                segments += "\""+seg[i]+"\""
            else:
                segments += "\""+seg[i]+"\","
        device = args.device

        url = "https://["+args.server+"]:443/changesr"
        payload = "{  \n   \"prefix\":\""+prefix+"\",\n   \"segments\":["+segments+"],\n   \"device\":\""+device+"\"\n}"

    headers = {'Content-Type': "application/json"}
    response = requests.request("POST", url, data=payload, headers=headers, verify='./server.pem')
    print(response.text)

if __name__ == '__main__':
  functionName = sys.argv[1]
  args = get_args(functionName)
  run(args)