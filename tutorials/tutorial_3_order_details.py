import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import pandas as pd
import numpy as np

with open(r'.\roots.pem', 'rb') as f: cert = f.read()

channel = grpc.secure_channel('__SERVER__:__PORT__', grpc.ssl_channel_credentials(root_certificates=cert))
util_stub = util_grpc.UtilityServicesStub(channel)

connect_response = util_stub.Connect(util.ConnectRequest(UserName='__USER__', Domain='__DOMAIN__', Password='__PASSWORD__', Locale='__LOCALE__'))
print('Connect result: ', connect_response.Response)

if connect_response.Response == 'success':
    activity_response = util_stub.GetTodaysActivityJson(util.TodaysActivityJsonRequest(IncludeUserSubmitOrder=True, UserToken=connect_response.UserToken))
    df = pd.read_json(activity_response.TodaysActivityJson, convert_dates=False)

    if not df.empty:
        xapi_order_id = df[(df['OrderTag']=='MyOrderId')]['OrderId'][0]
        print('The xAPI OrderId for my order is ', xapi_order_id)
        
    disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
    print('Disconnect result: ', disconnect_response.ServerResponse)