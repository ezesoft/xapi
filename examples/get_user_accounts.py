import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import order_pb2 as ord
import order_pb2_grpc as ord_grpc


class GetUserAccountsExample:
    def __init__(self):
        self.password = '__PASSWORD__'
        self.server = '__SERVER__'
        self.user = '__USER__'
        self.domain = '__DOMAIN__'
        self.locale = '__LOCALE__'
        self.port = '__PORT__'

    def run(self):
        with open(r'roots.pem', 'rb') as f:
            cert = f.read()

        credentials = grpc.ssl_channel_credentials(root_certificates=cert)
        channel = grpc.secure_channel('{0}:{1}'.format(self.server, self.port),
                                      credentials)
        util_stub = util_grpc.UtilityServicesStub(channel)

        req = util.ConnectRequest(UserName=self.user, Domain=self.domain,
                                  Password=self.password, Locale=self.locale)
        connect_response = util_stub.Connect(req)
        print('Connect result: ', connect_response.Response)

        if connect_response.Response == 'success':
            token = connect_response.UserToken
            ord_stub = ord_grpc.SubmitOrderServiceStub(channel)
            req = ord.UserAccountsRequest(UserToken=token)            
            response = ord_stub.GetUserAccounts(req)
            print('GetUserAccounts result: ', response.Acknowledgement.ServerResponse)
            if (response.Acknowledgement.ServerResponse == 'success'):
                print(response.Accounts)
            
            req = util.DisconnectRequest(UserToken=token)
            disconnect_response = util_stub.Disconnect(req)
            print('Disconnect result: ', disconnect_response.ServerResponse)

if __name__ == "__main__":
    example = GetUserAccountsExample()
    example.run()
