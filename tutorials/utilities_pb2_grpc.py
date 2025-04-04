# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import utilities_pb2 as utilities__pb2


class UtilityServicesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTodaysBalances = channel.unary_unary(
                '/UtilityServices/GetTodaysBalances',
                request_serializer=utilities__pb2.TodaysBalancesRequest.SerializeToString,
                response_deserializer=utilities__pb2.TodaysBalancesResponse.FromString,
                )
        self.GetTodaysActivity = channel.unary_unary(
                '/UtilityServices/GetTodaysActivity',
                request_serializer=utilities__pb2.TodaysActivityRequest.SerializeToString,
                response_deserializer=utilities__pb2.TodaysActivityResponse.FromString,
                )
        self.GetTodaysBrokenDownPositions = channel.unary_unary(
                '/UtilityServices/GetTodaysBrokenDownPositions',
                request_serializer=utilities__pb2.TodaysBrokenDownPositionsRequest.SerializeToString,
                response_deserializer=utilities__pb2.TodaysBrokenDownPositionsResponse.FromString,
                )
        self.GetTodaysNetPositions = channel.unary_unary(
                '/UtilityServices/GetTodaysNetPositions',
                request_serializer=utilities__pb2.TodaysNetPositionsRequest.SerializeToString,
                response_deserializer=utilities__pb2.TodaysNetPositionsResponse.FromString,
                )
        self.SubscribeTodaysNetPositions = channel.unary_stream(
                '/UtilityServices/SubscribeTodaysNetPositions',
                request_serializer=utilities__pb2.SubscribeNetPositionsRequest.SerializeToString,
                response_deserializer=utilities__pb2.SubscribeNetPositionsResponse.FromString,
                )
        self.UnSubscribeTodaysNetPositions = channel.unary_unary(
                '/UtilityServices/UnSubscribeTodaysNetPositions',
                request_serializer=utilities__pb2.UnSubscribeNetPositionsRequest.SerializeToString,
                response_deserializer=utilities__pb2.UnSubscribeNetPositionsResponse.FromString,
                )
        self.Connect = channel.unary_unary(
                '/UtilityServices/Connect',
                request_serializer=utilities__pb2.ConnectRequest.SerializeToString,
                response_deserializer=utilities__pb2.ConnectResponse.FromString,
                )
        self.SubscribeHeartBeat = channel.unary_stream(
                '/UtilityServices/SubscribeHeartBeat',
                request_serializer=utilities__pb2.SubscribeHeartBeatRequest.SerializeToString,
                response_deserializer=utilities__pb2.SubscribeHeartBeatResponse.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/UtilityServices/Disconnect',
                request_serializer=utilities__pb2.DisconnectRequest.SerializeToString,
                response_deserializer=utilities__pb2.DisconnectResponse.FromString,
                )
        self.StartLoginSrp = channel.unary_unary(
                '/UtilityServices/StartLoginSrp',
                request_serializer=utilities__pb2.StartLoginSrpRequest.SerializeToString,
                response_deserializer=utilities__pb2.StartLoginSrpResponse.FromString,
                )
        self.CompleteLoginSrp = channel.unary_unary(
                '/UtilityServices/CompleteLoginSrp',
                request_serializer=utilities__pb2.CompleteLoginSrpRequest.SerializeToString,
                response_deserializer=utilities__pb2.CompleteLoginSrpResponse.FromString,
                )
        self.ChangePasswordSRP = channel.unary_unary(
                '/UtilityServices/ChangePasswordSRP',
                request_serializer=utilities__pb2.ChangePasswordSRPRequest.SerializeToString,
                response_deserializer=utilities__pb2.ChangePasswordSRPResponse.FromString,
                )
        self.GetStrategyList = channel.unary_unary(
                '/UtilityServices/GetStrategyList',
                request_serializer=utilities__pb2.StrategyListRequest.SerializeToString,
                response_deserializer=utilities__pb2.StrategyListResponse.FromString,
                )
        self.GetTodaysActivityJson = channel.unary_unary(
                '/UtilityServices/GetTodaysActivityJson',
                request_serializer=utilities__pb2.TodaysActivityJsonRequest.SerializeToString,
                response_deserializer=utilities__pb2.TodaysActivityJsonResponse.FromString,
                )


class UtilityServicesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTodaysBalances(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodaysActivity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodaysBrokenDownPositions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodaysNetPositions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeTodaysNetPositions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeTodaysNetPositions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeHeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartLoginSrp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteLoginSrp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePasswordSRP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStrategyList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodaysActivityJson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UtilityServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTodaysBalances': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodaysBalances,
                    request_deserializer=utilities__pb2.TodaysBalancesRequest.FromString,
                    response_serializer=utilities__pb2.TodaysBalancesResponse.SerializeToString,
            ),
            'GetTodaysActivity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodaysActivity,
                    request_deserializer=utilities__pb2.TodaysActivityRequest.FromString,
                    response_serializer=utilities__pb2.TodaysActivityResponse.SerializeToString,
            ),
            'GetTodaysBrokenDownPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodaysBrokenDownPositions,
                    request_deserializer=utilities__pb2.TodaysBrokenDownPositionsRequest.FromString,
                    response_serializer=utilities__pb2.TodaysBrokenDownPositionsResponse.SerializeToString,
            ),
            'GetTodaysNetPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodaysNetPositions,
                    request_deserializer=utilities__pb2.TodaysNetPositionsRequest.FromString,
                    response_serializer=utilities__pb2.TodaysNetPositionsResponse.SerializeToString,
            ),
            'SubscribeTodaysNetPositions': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTodaysNetPositions,
                    request_deserializer=utilities__pb2.SubscribeNetPositionsRequest.FromString,
                    response_serializer=utilities__pb2.SubscribeNetPositionsResponse.SerializeToString,
            ),
            'UnSubscribeTodaysNetPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeTodaysNetPositions,
                    request_deserializer=utilities__pb2.UnSubscribeNetPositionsRequest.FromString,
                    response_serializer=utilities__pb2.UnSubscribeNetPositionsResponse.SerializeToString,
            ),
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=utilities__pb2.ConnectRequest.FromString,
                    response_serializer=utilities__pb2.ConnectResponse.SerializeToString,
            ),
            'SubscribeHeartBeat': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeHeartBeat,
                    request_deserializer=utilities__pb2.SubscribeHeartBeatRequest.FromString,
                    response_serializer=utilities__pb2.SubscribeHeartBeatResponse.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=utilities__pb2.DisconnectRequest.FromString,
                    response_serializer=utilities__pb2.DisconnectResponse.SerializeToString,
            ),
            'StartLoginSrp': grpc.unary_unary_rpc_method_handler(
                    servicer.StartLoginSrp,
                    request_deserializer=utilities__pb2.StartLoginSrpRequest.FromString,
                    response_serializer=utilities__pb2.StartLoginSrpResponse.SerializeToString,
            ),
            'CompleteLoginSrp': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteLoginSrp,
                    request_deserializer=utilities__pb2.CompleteLoginSrpRequest.FromString,
                    response_serializer=utilities__pb2.CompleteLoginSrpResponse.SerializeToString,
            ),
            'ChangePasswordSRP': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePasswordSRP,
                    request_deserializer=utilities__pb2.ChangePasswordSRPRequest.FromString,
                    response_serializer=utilities__pb2.ChangePasswordSRPResponse.SerializeToString,
            ),
            'GetStrategyList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStrategyList,
                    request_deserializer=utilities__pb2.StrategyListRequest.FromString,
                    response_serializer=utilities__pb2.StrategyListResponse.SerializeToString,
            ),
            'GetTodaysActivityJson': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodaysActivityJson,
                    request_deserializer=utilities__pb2.TodaysActivityJsonRequest.FromString,
                    response_serializer=utilities__pb2.TodaysActivityJsonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UtilityServices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UtilityServices(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTodaysBalances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/GetTodaysBalances',
            utilities__pb2.TodaysBalancesRequest.SerializeToString,
            utilities__pb2.TodaysBalancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodaysActivity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/GetTodaysActivity',
            utilities__pb2.TodaysActivityRequest.SerializeToString,
            utilities__pb2.TodaysActivityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodaysBrokenDownPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/GetTodaysBrokenDownPositions',
            utilities__pb2.TodaysBrokenDownPositionsRequest.SerializeToString,
            utilities__pb2.TodaysBrokenDownPositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodaysNetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/GetTodaysNetPositions',
            utilities__pb2.TodaysNetPositionsRequest.SerializeToString,
            utilities__pb2.TodaysNetPositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeTodaysNetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/UtilityServices/SubscribeTodaysNetPositions',
            utilities__pb2.SubscribeNetPositionsRequest.SerializeToString,
            utilities__pb2.SubscribeNetPositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeTodaysNetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/UnSubscribeTodaysNetPositions',
            utilities__pb2.UnSubscribeNetPositionsRequest.SerializeToString,
            utilities__pb2.UnSubscribeNetPositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/Connect',
            utilities__pb2.ConnectRequest.SerializeToString,
            utilities__pb2.ConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeHeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/UtilityServices/SubscribeHeartBeat',
            utilities__pb2.SubscribeHeartBeatRequest.SerializeToString,
            utilities__pb2.SubscribeHeartBeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/Disconnect',
            utilities__pb2.DisconnectRequest.SerializeToString,
            utilities__pb2.DisconnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartLoginSrp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/StartLoginSrp',
            utilities__pb2.StartLoginSrpRequest.SerializeToString,
            utilities__pb2.StartLoginSrpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteLoginSrp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/CompleteLoginSrp',
            utilities__pb2.CompleteLoginSrpRequest.SerializeToString,
            utilities__pb2.CompleteLoginSrpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePasswordSRP(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/ChangePasswordSRP',
            utilities__pb2.ChangePasswordSRPRequest.SerializeToString,
            utilities__pb2.ChangePasswordSRPResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStrategyList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/GetStrategyList',
            utilities__pb2.StrategyListRequest.SerializeToString,
            utilities__pb2.StrategyListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodaysActivityJson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UtilityServices/GetTodaysActivityJson',
            utilities__pb2.TodaysActivityJsonRequest.SerializeToString,
            utilities__pb2.TodaysActivityJsonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
