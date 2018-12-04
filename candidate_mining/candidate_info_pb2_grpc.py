# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import candidate_info_pb2 as candidate__info__pb2


class ChatServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.BuildChatTemplate = channel.unary_unary(
        '/ai_custom_service.ChatService/BuildChatTemplate',
        request_serializer=candidate__info__pb2.ChatTemplate.SerializeToString,
        response_deserializer=candidate__info__pb2.BuildChatTemplateResponse.FromString,
        )
    self.CloseChatTemplate = channel.unary_unary(
        '/ai_custom_service.ChatService/CloseChatTemplate',
        request_serializer=candidate__info__pb2.CloseChatTemplateRequest.SerializeToString,
        response_deserializer=candidate__info__pb2.CloseChatTemplateResponse.FromString,
        )
    self.GetQuestion = channel.unary_unary(
        '/ai_custom_service.ChatService/GetQuestion',
        request_serializer=candidate__info__pb2.QuestionRequest.SerializeToString,
        response_deserializer=candidate__info__pb2.QuestionResponse.FromString,
        )


class ChatServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def BuildChatTemplate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseChatTemplate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetQuestion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'BuildChatTemplate': grpc.unary_unary_rpc_method_handler(
          servicer.BuildChatTemplate,
          request_deserializer=candidate__info__pb2.ChatTemplate.FromString,
          response_serializer=candidate__info__pb2.BuildChatTemplateResponse.SerializeToString,
      ),
      'CloseChatTemplate': grpc.unary_unary_rpc_method_handler(
          servicer.CloseChatTemplate,
          request_deserializer=candidate__info__pb2.CloseChatTemplateRequest.FromString,
          response_serializer=candidate__info__pb2.CloseChatTemplateResponse.SerializeToString,
      ),
      'GetQuestion': grpc.unary_unary_rpc_method_handler(
          servicer.GetQuestion,
          request_deserializer=candidate__info__pb2.QuestionRequest.FromString,
          response_serializer=candidate__info__pb2.QuestionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai_custom_service.ChatService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))