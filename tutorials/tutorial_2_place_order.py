import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import order_pb2 as ord
import order_pb2_grpc as ord_grpc


class PlaceOrderExample:
    def __init__(self):
        self.server = '__SERVER__'
        self.port = '__PORT__'
        self.user = '__USER__'
        self.password = '__PASSWORD__'
        self.domain = '__DOMAIN__'
        self.locale = '__LOCALE__'
        self.account = '__ACCOUNT__'
        self.route = '__ROUTE__'
        self.my_order_id = 'MyOrderId'

    def run(self):
        with open(r'roots.pem', 'rb') as f:
            cert = f.read()

        channel = grpc.secure_channel('{0}:{1}'.format(self.server, self.port), grpc.ssl_channel_credentials(root_certificates=cert))
        util_stub = util_grpc.UtilityServicesStub(channel)

        connect_response = util_stub.Connect(util.ConnectRequest(UserName=self.user, Domain=self.domain, Password=self.password, Locale=self.locale))
        print('Connect result: ', connect_response.Response)

        if connect_response.Response == 'success':

            ord_stub = ord_grpc.SubmitOrderServiceStub(channel)
            order_response = ord_stub.SubmitSingleOrder(ord.SubmitSingleOrderRequest(Symbol='GE', Side='BUY', Quantity=5000, Route=self.route, Account=self.account, OrderTag=self.my_order_id, UserToken=connect_response.UserToken))
            print('Order result: ', order_response)

            disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
            print('Disconnect result: ', disconnect_response.ServerResponse)

if __name__ == "__main__":
    example = PlaceOrderExample()
    example.run()
