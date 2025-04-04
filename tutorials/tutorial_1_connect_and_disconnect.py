import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc


class ConnectAndDisconnectExample:
    def __init__(self):
        self.server = '__SERVER__'
        self.user = '__USER__'
        self.domain = '__DOMAIN__'
        self.password = '__PASSWORD__'
        self.locale = '__LOCALE__'

    def run(self):
        with open(r'roots.pem', 'rb') as f:
            cert = f.read()
        channel = grpc.secure_channel(
            f'{self.server}:{self.port}',
            grpc.ssl_channel_credentials(root_certificates=cert)
        )

        util_stub = util_grpc.UtilityServicesStub(channel)
        connect_request = util.ConnectRequest(
            UserName=self.user,
            Domain=self.domain,
            Password=self.password,
            Locale=self.locale
        )
        connect_response = util_stub.Connect(connect_request)
        print('Connect result: ', connect_response.Response)

        if connect_response.Response == 'success':
            disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
            print('Disconnect result: ', disconnect_response.ServerResponse)


if __name__ == "__main__":
    example = ConnectAndDisconnectExample()
    example.run()
