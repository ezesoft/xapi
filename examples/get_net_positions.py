import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc


class GetNetPositionsExample:
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
            req = util.TodaysNetPositionsRequest(UserToken=token)
            response = util_stub.GetTodaysNetPositions(req)
            print('GetTodaysNetPositions result: ', response.Acknowledgement.ServerResponse)
            if response.Acknowledgement.ServerResponse == 'success':
                num_pos = len(response.AggregatePositionsList)
                print('Found {0} positions'.format(num_pos))
                for pos in response.AggregatePositionsList:
                    print(pos)
            
            req = util.DisconnectRequest(UserToken=token)
            disconnect_response = util_stub.Disconnect(req)
            print('Disconnect result: ', disconnect_response.ServerResponse)

if __name__ == "__main__":
    example = GetNetPositionsExample()
    example.run()
