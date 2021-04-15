import grpc
import time
from threading import Thread
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import market_data_pb2 as md
import market_data_pb2_grpc as md_grpc

def handle_data(response):
    try:
        for tick in response:
            if tick.Trdprc1.DecimalValue == 0.0:
                continue
            print('Receieved market data for {0}, Last: {1}'.format(tick.DispName, tick.Trdprc1.DecimalValue))
    except Exception as e:
        print(e)

with open(r'./roots.pem', 'rb') as f: cert = f.read()

channel = grpc.secure_channel('__SERVER__:__PORT__', grpc.ssl_channel_credentials(root_certificates=cert))
util_stub = util_grpc.UtilityServicesStub(channel)

connect_response = util_stub.Connect(util.ConnectRequest(UserName='__USER__', Domain='__DOMAIN__', Password='__PASSWORD__', Locale='__LOCALE__'))
print('Connect result: ', connect_response.Response)

if connect_response.Response == 'success':
    md_stub = md_grpc.MarketDataServiceStub(channel)
    response = md_stub.SubscribeLevel1Ticks(md.Level1MarketDataRequest(Symbols=['TSLA'], Request=True, Advise=True, UserToken=connect_response.UserToken))
    
    t = Thread(target=handle_data, args=(response, ))
    t.start()
    for i in range(5):
        print('Hello from main thread: ', i)
        time.sleep(1)

    response.cancel()
    t.join()

    disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
    print('Disconnect result: ', disconnect_response.ServerResponse)
