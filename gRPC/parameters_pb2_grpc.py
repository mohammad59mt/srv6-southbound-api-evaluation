# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import parameters_pb2 as parameters__pb2


class SegmentRoutingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddSrRoute = channel.unary_unary(
        '/parameters.SegmentRouting/AddSrRoute',
        request_serializer=parameters__pb2.AddSrRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.AddSrRouteReply.FromString,
        )
    self.RemoveRoute = channel.unary_unary(
        '/parameters.SegmentRouting/RemoveRoute',
        request_serializer=parameters__pb2.RmRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.RmRouteReply.FromString,
        )
    self.ListRoute = channel.unary_unary(
        '/parameters.SegmentRouting/ListRoute',
        request_serializer=parameters__pb2.ListRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.ListRouteReply.FromString,
        )
    self.ChangeRoute = channel.unary_unary(
        '/parameters.SegmentRouting/ChangeRoute',
        request_serializer=parameters__pb2.ChangeRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.ChangeRouteReply.FromString,
        )
    self.ChangeSrRoute = channel.unary_unary(
        '/parameters.SegmentRouting/ChangeSrRoute',
        request_serializer=parameters__pb2.ChangeSrRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.ChangeSrRouteReply.FromString,
        )
    self.BunchAddSrRoute = channel.unary_unary(
        '/parameters.SegmentRouting/BunchAddSrRoute',
        request_serializer=parameters__pb2.AddSrRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.AddSrRouteReply.FromString,
        )
    self.BunchRemoveRoute = channel.unary_unary(
        '/parameters.SegmentRouting/BunchRemoveRoute',
        request_serializer=parameters__pb2.RmRouteRequest.SerializeToString,
        response_deserializer=parameters__pb2.RmRouteReply.FromString,
        )


class SegmentRoutingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddSrRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangeSrRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BunchAddSrRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BunchRemoveRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SegmentRoutingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddSrRoute': grpc.unary_unary_rpc_method_handler(
          servicer.AddSrRoute,
          request_deserializer=parameters__pb2.AddSrRouteRequest.FromString,
          response_serializer=parameters__pb2.AddSrRouteReply.SerializeToString,
      ),
      'RemoveRoute': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveRoute,
          request_deserializer=parameters__pb2.RmRouteRequest.FromString,
          response_serializer=parameters__pb2.RmRouteReply.SerializeToString,
      ),
      'ListRoute': grpc.unary_unary_rpc_method_handler(
          servicer.ListRoute,
          request_deserializer=parameters__pb2.ListRouteRequest.FromString,
          response_serializer=parameters__pb2.ListRouteReply.SerializeToString,
      ),
      'ChangeRoute': grpc.unary_unary_rpc_method_handler(
          servicer.ChangeRoute,
          request_deserializer=parameters__pb2.ChangeRouteRequest.FromString,
          response_serializer=parameters__pb2.ChangeRouteReply.SerializeToString,
      ),
      'ChangeSrRoute': grpc.unary_unary_rpc_method_handler(
          servicer.ChangeSrRoute,
          request_deserializer=parameters__pb2.ChangeSrRouteRequest.FromString,
          response_serializer=parameters__pb2.ChangeSrRouteReply.SerializeToString,
      ),
      'BunchAddSrRoute': grpc.unary_unary_rpc_method_handler(
          servicer.BunchAddSrRoute,
          request_deserializer=parameters__pb2.AddSrRouteRequest.FromString,
          response_serializer=parameters__pb2.AddSrRouteReply.SerializeToString,
      ),
      'BunchRemoveRoute': grpc.unary_unary_rpc_method_handler(
          servicer.BunchRemoveRoute,
          request_deserializer=parameters__pb2.RmRouteRequest.FromString,
          response_serializer=parameters__pb2.RmRouteReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'parameters.SegmentRouting', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
