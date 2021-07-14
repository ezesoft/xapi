import grpc
import time
from uuid import uuid4
from threading import Thread
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import order_pb2 as ord
import order_pb2_grpc as ord_grpc


class CreateBasketOrderExample:
    def __init__(self):
        self.password = '__PASSWORD__'
        self.server = '__SERVER__'
        self.user = '__USER__'
        self.domain = '__DOMAIN__'
        self.locale = '__LOCALE__'
        self.account = '__ACCOUNT__'
        self.route = '__ROUTE__'
        self.port = '__PORT__'

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
            req = ord.SubscribeOrderInfoRequest(Level=0, UserToken=token)
            iter = ord_stub.SubscribeOrderInfo(req)

            t = Thread(target=self.callback, args=(iter, ))
            t.start()

            # Place multiple orders in 1 request
            account = self.account.split(';')

            ord_request  = ord.OrderRow()
            ord_request.DispName = 'GOOG'
            ord_request.Buyorsell = 'BUY'
            ord_request.Volume.value = 1000
            ord_request.Bank = account[0]
            ord_request.Branch = account[1]
            ord_request.Customer = account[2]
            ord_request.Deposit = account[3]
            ord_request.GoodUntil = 'DAY'
            ord_request.Type = 'UserSubmitOrder'
            ord_request.Route = self.route
            ord_request.ExtendedFields['ORDER_TAG'] = 'XAP-{0}'.format(str(uuid4()))

            ord_request1 = ord.OrderRow()
            ord_request.DispName = 'MSFT'
            ord_request.Buyorsell = 'BUY'
            ord_request.Volume.value = 1000
            ord_request.Bank = account[0]
            ord_request.Branch = account[1]
            ord_request.Customer = account[2]
            ord_request.Deposit = account[3]
            ord_request.GoodUntil = 'DAY'
            ord_request.Type = 'UserSubmitOrder'
            ord_request.Route = self.route
            ord_request.ExtendedFields['ORDER_TAG'] = 'XAP-{0}'.format(str(uuid4()))
            
            basket_order = ord.BasketOrderRequest()
            basket_order.Orders.extend([ord_request, ord_request1])  
            basket_order.UserToken = token
            response = ord_stub.SubmitBasketOrder(basket_order)

            if response.ServerResponse == 'success':
                print("Successfully Submitted Basket Order")
            else: 
                print(response.OptionalFields["ErrorMessage"]) 

            time.sleep(10)

            iter.cancel()
            t.join()

            req = util.DisconnectRequest(UserToken=token)
            disconnect_response = util_stub.Disconnect(req)
            print('Disconnect result: ', disconnect_response.ServerResponse)


if __name__ == "__main__":
    example = CreateBasketOrderExample()
    example.run()
