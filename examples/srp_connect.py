import srp._pysrp as srp
import grpc
import utilities_pb2 as util
import utilities_pb2_grpc as util_grpc


class SrpConnectExample:
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

        req = util.StartLoginSrpRequest(UserName=self.user, Domain=self.domain)
        srp_start_response = util_stub.StartLoginSrp(req)
        print('Start SRP result: ', srp_start_response.Response)

        if srp_start_response.Response == 'success':
            identity = '{0}@{1}'.format(self.user, self.domain)
            g_hex = hex(int(srp_start_response.srpg))
            n_hex = hex(int(srp_start_response.srpN))
            srp.rfc5054_enable(True)
            usr = srp.User(identity, self.password, hash_alg=srp.SHA256,
                        ng_type=srp.NG_CUSTOM, n_hex=n_hex, g_hex=g_hex)
            srp.rfc5054_enable(False)

            _, A = usr.start_authentication()

            bytes_B = int(srp_start_response.srpb).to_bytes(128, 'big')
            bytes_s = bytes.fromhex(srp_start_response.srpSalt)
            M = usr.process_challenge(bytes_s, bytes_B)

            strMc = hex(int.from_bytes(M, 'big')).lstrip('0x')
            strEphA = str(int.from_bytes(A, 'big'))
            srpTransactId = srp_start_response.srpTransactId
            req = util.CompleteLoginSrpRequest(Identity=identity,
                                            srpTransactId=srpTransactId,
                                            strEphA=strEphA, strMc=strMc,
                                            UserName=self.user, Domain=self.domain,
                                            Locale=self.locale)

            connect_response = util_stub.CompleteLoginSrp(req)
            print('Connect result: ', connect_response.Response)

            if connect_response.Response == 'success':
                req = util.DisconnectRequest(UserToken=connect_response.UserToken)
                disconnect_response = util_stub.Disconnect(req)
                print('Disconnect result: ', disconnect_response.ServerResponse)


if __name__ == "__main__":
    example = SrpConnectExample()
    example.run()
