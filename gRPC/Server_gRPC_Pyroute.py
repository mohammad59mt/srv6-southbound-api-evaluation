from concurrent import futures
import time, grpc, parameters_pb2, parameters_pb2_grpc, os, sys
from socket import AF_INET
from pyroute2 import IPRoute

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SegmentRoutingServicer(parameters_pb2_grpc.SegmentRoutingServicer):
  def __init__(self):
    pass

  def AddSrRoute(self,addSrRouteMessage,context):
    ip = IPRoute()
    idx = ip.link_lookup(ifname=addSrRouteMessage.device)[0]
    ip.route('add',
      dst=addSrRouteMessage.prefix+'/128',
      oif=idx,
      encap={'type': 'seg6','mode': addSrRouteMessage.encapmode,'segs': addSrRouteMessage.segments})
    ip.close()
    return parameters_pb2.AddSrRouteReply(message=str(0))

  def RemoveRoute(self,removeRouteMessage,context):
    ip = IPRoute()
    idx = ip.link_lookup(ifname=removeRouteMessage.device)[0]
    ip.route('delete',
      dst=removeRouteMessage.prefix+'/128',
      oif=idx)
    ip.close()
    return parameters_pb2.RmRouteReply(message=str(0))

  def BunchAddSrRoute(self,addSrRouteMessage,context):
    start_time = time.time()
    prefixes=addSrRouteMessage.prefix.split(';')
    Allsegments=addSrRouteMessage.segments.split('-')
    devices=addSrRouteMessage.device.split(';')
    encapmodes=addSrRouteMessage.encapmode.split(';')
    n = len(prefixes)
    ip = IPRoute()
    for i in range(0,n-1):
      idx = ip.link_lookup(ifname=devices[i])[0]
      ip.route('add',
        dst=prefixes[i]+'/128',
        oif=idx,
        encap={'type': 'seg6','mode': encapmodes[i],'segs': Allsegments[i]})     
    #executionTime=time.time() - start_time
    #print("Execution time: " + str(executionTime))
    ip.close()
    return parameters_pb2.AddSrRouteReply(message=str(0))

  def BunchRemoveRoute(self,removeRouteMessage,context):
    prefixes=removeRouteMessage.prefix.split(';')
    devices=removeRouteMessage.device.split(';')
    n = len(prefixes)
    ip = IPRoute()
    for i in range(0,n-1):
      idx = ip.link_lookup(ifname=devices[i])[0]
      ip.route('delete',
        dst=prefixes[i]+'/128',
        oif=idx)
    ip.close()
    return parameters_pb2.RmRouteReply(message=str(0))

def serve(security_mode):
  if security_mode=="insecure":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    parameters_pb2_grpc.add_SegmentRoutingServicer_to_server(
        SegmentRoutingServicer(), server)
    server.add_insecure_port('[::]:50052')
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
    server.add_secure_port('[::]:50051', server_credentials)
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
