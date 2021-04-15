import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc
import order_pb2 as ord
import order_pb2_grpc as ord_grpc

with open(r'.\roots.pem', 'rb') as f: cert = f.read()

channel = grpc.secure_channel('__SERVER__:__PORT__', grpc.ssl_channel_credentials(root_certificates=cert))
util_stub = util_grpc.UtilityServicesStub(channel)

connect_response = util_stub.Connect(util.ConnectRequest(UserName='__USER__', Domain='__DOMAIN__', Password='__PASSWORD__', Locale='__LOCALE__'))
print('Connect result: ', connect_response.Response)

if connect_response.Response == 'success':

    ord_stub = ord_grpc.SubmitOrderServiceStub(channel)
    order_response = ord_stub.SubmitSingleOrder(ord.SubmitSingleOrderRequest(Symbol='TSLA', Side='BUY', Quantity=5000, Route='__ROUTE__', Account='__ACCOUNT__', OrderTag='MyOrderId', UserToken=connect_response.UserToken))
    print('Order result: ', order_response)

    disconnect_response = util_stub.Disconnect(util.DisconnectRequest(UserToken=connect_response.UserToken))
    print('Disconnect result: ', disconnect_response.ServerResponse)