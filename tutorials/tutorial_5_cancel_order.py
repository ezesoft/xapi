from io import StringIO

import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import order_pb2 as ord
import order_pb2_grpc as ord_grpc
import pandas as pd


class CancelOrderExample:
    def __init__(self):
        self.server = '__SERVER__'
        self.port = '__PORT__'
        self.user = '__USER__'
        self.password = '__PASSWORD__'
        self.domain = '__DOMAIN__'
        self.locale = '__LOCALE__'
        self.my_order_id = 'MyOrderId'

    def run(self):
        with open(r'roots.pem', 'rb') as f:
            cert = f.read()
        channel = grpc.secure_channel(
            f'{self.server}:{self.port}',
            grpc.ssl_channel_credentials(root_certificates=cert)
        )
        util_stub = util_grpc.UtilityServicesStub(channel)

        connect_response = util_stub.Connect(util.ConnectRequest(
            UserName=self.user,
            Domain=self.domain,
            Password=self.password,
            Locale=self.locale
        ))
        print('Connect result: ', connect_response.Response)

        if connect_response.Response == 'success':
            activity_response = util_stub.GetTodaysActivityJson(util.TodaysActivityJsonRequest(
                IncludeUserSubmitOrder=True,
                UserToken=connect_response.UserToken
            ))
            # Assuming activity_response.TodaysActivityJson contains the JSON string
            json_str = activity_response.TodaysActivityJson

            # Wrap the JSON string in a StringIO object
            json_io = StringIO(json_str)
            # Read the JSON data into a DataFrame
            df = pd.read_json(json_io, convert_dates=False)

            if not df.empty:
                xapi_order_id = df.loc[df['OrderId'] == self.my_order_id, 'OrderId'].values[0]
                print('The xAPI OrderId for my order is ', xapi_order_id)

                ord_stub = ord_grpc.SubmitOrderServiceStub(channel)
                cancel_response = ord_stub.CancelSingleOrder(ord.CancelSingleOrderRequest(
                    OrderId=xapi_order_id,
                    UserToken=connect_response.UserToken
                ))
                print('Cancel result: ', cancel_response.ServerResponse)

            disconnect_response = util_stub.Disconnect(util.DisconnectRequest(
                UserToken=connect_response.UserToken
            ))
            print('Disconnect result: ', disconnect_response.ServerResponse)


if __name__ == "__main__":
    example = CancelOrderExample()
    example.run()

