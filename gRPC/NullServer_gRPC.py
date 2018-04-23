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
# Python implementation of the gRPC SRv6 functions server side.
#
# @author Pier Luigi Ventre <pier.luigi.ventre@uniroma2.it>
# @author Stefano Salsano <stefano.salsano@uniroma2.it>
# @author Alessandro Masci <mascialessandro89@gmail.com>
#

from concurrent import futures
import time
import math
import subprocess

import grpc

import parameters_pb2
import parameters_pb2_grpc
import os,sys
#import parameters_resources


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SegmentRoutingServicer(parameters_pb2_grpc.SegmentRoutingServicer):
  """Provides methods that implement functionality of route guide server."""
  def __init__(self):
    pass

  def AddSrRoute(self,addSrRouteMessage,context):
    #if the action is performed successfully it returns 0 otherwise the error number
    #Shell Command to add the route
    return parameters_pb2.AddSrRouteReply(message=str(0))

  def RemoveRoute(self,removeRouteMessage,context):
    return parameters_pb2.RmRouteReply(message=str(0))

  def BunchAddSrRoute(self,addSrRouteMessage,context):
    #if the action is performed successfully it returns 0 otherwise the error number
    #Shell Command to add the route
    return parameters_pb2.AddSrRouteReply(message=str(0))

  def BunchRemoveRoute(self,removeRouteMessage,context):
    return parameters_pb2.RmRouteReply(message=str(0))

def serve():
  if security_mode=="insecure":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    parameters_pb2_grpc.add_SegmentRoutingServicer_to_server(
        SegmentRoutingServicer(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
  elif security_mode=="secure":
    with open('server.key') as f:
      private_key = f.read()
    with open('server.crt') as f:
      certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials(
          ((private_key, certificate_chain,),))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    parameters_pb2_grpc.add_SegmentRoutingServicer_to_server(
        SegmentRoutingServicer(), server)
    server.add_secure_port('[::]:50053', server_credentials)
    server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  if sys.argv[1] is not None:
    security_mode = sys.argv[1]
    serve(security_mode)
  else:
    print("select either secure or inscure mode (e.g., sudo python <fileName.py> secure ....)")