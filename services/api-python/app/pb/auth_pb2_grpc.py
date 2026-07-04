import grpc
from app.pb import auth_pb2

class AuthServiceStub(object):
    def __init__(self, channel):
        self.ValidateToken = channel.unary_unary(
            '/auth.AuthService/ValidateToken',
            request_serializer=auth_pb2.ValidateTokenRequest.SerializeToString if hasattr(auth_pb2.ValidateTokenRequest, 'SerializeToString') else lambda x: b'',
            response_deserializer=lambda x: auth_pb2.ValidateTokenResponse()
        )
        self.CheckPermission = channel.unary_unary(
            '/auth.AuthService/CheckPermission',
            request_serializer=lambda x: b'',
            response_deserializer=lambda x: None
        )
