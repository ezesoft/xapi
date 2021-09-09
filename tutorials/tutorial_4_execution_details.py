import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import pandas as pd
import numpy as np


class ExecutionDetailsExample:
    def __init__(self):
        self.server = '__SERVER__'
        self.port = '__PORT__'
        self.user = '__USER__'
        self.password = '__PASSWORD__'
        self.domain = '__DOMAIN__'
        self.locale = '__LOCALE__'

    def run(self):
        with open(r'roots.pem', 'rb') as f:
            cert = f.read()

        channel = grpc.secure_channel('{0}:{1}'.format(self.server, self.port), grpc.ssl_channel_credentials(root_certificates=cert))
        util_stub = util_grpc.UtilityServicesStub(channel)

        connect_response = util_stub.Connect(util.ConnectRequest(UserName=self.user, Domain=self.domain, Password=self.password, Locale=self.locale))
        print('Connect result: ', connect_response.Response)

        if connect_response.Response == 'success':
            activity_response = util_stub.GetTodaysActivityJson(util.TodaysActivityJsonRequest(IncludeExchangeTradeOrder=True, UserToken=connect_response.UserToken))
            df = pd.read_json(activity_response.TodaysActivityJson, convert_dates=False)

            if not df.empty:
                g = df.groupby(["Symbol", "Side"]).agg(
                    tot_filled_vol = pd.NamedAgg('Volume', 'sum'),
                    num_fills = pd.NamedAgg('Volume', 'count'),
                    vwap = pd.NamedAgg('Price', lambda x: np.average(x, weights=df.loc[x.index, 'Volume'])))
                print('fills:\n', g)

            disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
            print('Disconnect result: ', disconnect_response.ServerResponse)

if __name__ == "__main__":
    example = ExecutionDetailsExample()
    example.run()