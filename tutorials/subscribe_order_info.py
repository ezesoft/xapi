import grpc
import time
from threading import Thread
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import order_pb2 as ord
import order_pb2_grpc as ord_grpc


class SubscribeOrderInfoExample:
    def __init__(self):
        self.server = '__SERVER__'
        self.user = '__USER__'
        self.domain = '__DOMAIN__'
        self.password = '__PASSWORD__'
        self.locale = '__LOCALE__'
        self.account = '__ACCOUNT__'
        self.route = '__ROUTE__'

    def callback(self, iter):
        try:
            for data in iter:
                print('Received order: {0}, {1}, {2}, {3}, {4}, {5}'.format(
                    data.Symbol, data.Volume, data.CurrentStatus, data.OrderId,
                    data.TicketId, data.ExtendedFields['OrderTag']))
        except Exception as e:
            print(e)

    def run(self):
        with open(r'roots.pem', 'rb') as f:
            cert = f.read()

        credentials = grpc.ssl_channel_credentials(root_certificates=cert)
        channel = grpc.secure_channel(f'{self.server}:{self.port}', credentials)
        util_stub = util_grpc.UtilityServicesStub(channel)

        req = util.ConnectRequest(UserName=self.user, Domain=self.domain,
                                  Password=self.password, Locale=self.locale)
        connect_response = util_stub.Connect(req)
        print('Connect result: ', connect_response.Response)

        if connect_response.Response == 'success':
            token = connect_response.UserToken
            ord_stub = ord_grpc.SubmitOrderServiceStub(channel)
            req = ord.SubscribeOrderInfoRequest(Level=0, UserToken=token)
            iter = ord_stub.SubscribeOrderInfo(req)

            t = Thread(target=self.callback, args=(iter,))
            t.start()

            for i in range(1, 10):
                print('Sending order from main thread: ', i)
                req = ord.SubmitSingleOrderRequest(Symbol='GOOG', Side='BUY',
                                                   Quantity=i*100,
                                                   Route=self.route,
                                                   Account=self.account,
                                                   OrderTag='MyOrderId',
                                                   UserToken=token)
                order_response = ord_stub.SubmitSingleOrder(req)
                print('Send order result: ', order_response)
                time.sleep(1)

            iter.cancel()
            t.join()

            req = util.DisconnectRequest(UserToken=token)
            disconnect_response = util_stub.Disconnect(req)
            print('Disconnect result: ', disconnect_response.ServerResponse)


if __name__ == "__main__":
    example = SubscribeOrderInfoExample()
    example.run()

