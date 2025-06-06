import grpc
import time
from threading import Thread
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import market_data_pb2 as md
import market_data_pb2_grpc as md_grpc


class MarketDataExample:
    def __init__(self):
        self.server = '__SERVER__'
        self.port = '__PORT__'
        self.user = '__USER__'
        self.password = '__PASSWORD__'
        self.domain = '__DOMAIN__'
        self.locale = '__LOCALE__'

    def handle_data(self, response):
        try:
            for tick in response:
                if tick.Trdprc1.DecimalValue == 0.0:
                    continue
                print(f'Received market data for {tick.DispName}, Last: {tick.Trdprc1.DecimalValue}')
        except Exception as e:
            print(e)

    def run(self):
        # Load the SSL/TLS certificates
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
            md_stub = md_grpc.MarketDataServiceStub(channel)
            response = md_stub.SubscribeLevel1Ticks(md.Level1MarketDataRequest(
                Symbols=['GE'],
                Request=True,
                Advise=True,
                UserToken=connect_response.UserToken
            ))

            t = Thread(target=self.handle_data, args=(response,))
            t.start()
            for i in range(5):
                print('Hello from main thread: ', i)
                time.sleep(1)

            response.cancel()
            t.join()

            disconnect_response = util_stub.Disconnect(util.DisconnectRequest(
                UserToken=connect_response.UserToken
            ))
            print('Disconnect result: ', disconnect_response.ServerResponse)


if __name__ == "__main__":
    example = MarketDataExample()
    example.run()

