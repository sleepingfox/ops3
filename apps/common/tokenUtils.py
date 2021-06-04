
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import datetime
import base64

from jwt.contrib.algorithms.pycrypto import RSAAlgorithm





import jwt

from ops3 import settings


class TokenUtils():


    def update_secret_key(self,):
        # 伪随机数生成器
        random_generator = Random.new().read
        # rsa算法生成实例
        rsa = RSA.generate(1024, random_generator)

        # master的秘钥对的生成
        private_pem = rsa.exportKey()

        with open('master-private.pem', 'wb') as f1:
            f1.write(private_pem)


        public_pem = rsa.publickey().exportKey()
        with open('master-public.pem', 'wb') as f2:
            f2.write(public_pem)


    def update_access_token_exp(self):
        print("更新token exp 时间")
        settings.JWT_PAYLOAD["exp"]= datetime.datetime.utcnow()+datetime.timedelta(days=1)
        print("exp")
        print(settings.JWT_PAYLOAD["exp"])
        print('iat')
        print(settings.JWT_PAYLOAD['iat'])


class GetToken(TokenUtils):

    def jwt_get_secret_key(payload=None):
        """
        返回secret凭据
        """

        return settings.JWT_SECRET_PRIVATE_KEY








    def jwt_get_payload(self,token_type):

        obj = getattr(settings,token_type)


        return settings.JWT_PAYLOAD



    def jwt_set_payload(self,dic,token_type,exp,iat):

        l1 =["exp","fbf","iss","aud","iat"]

        dic["iat"] = iat

        # dic["exp"] = datetime.datetime.utcnow()+datetime.timedelta(seconds=20)

        dic["exp"] = exp



        obj = getattr(settings,token_type)

        print("+++++++++++++")
        print(obj)
        # print(obj[0])
        print(type(obj))

        print("##############")
        for key, val in dic.items():

            if key not in l1:
                obj["data"][key]=val
            else:
                obj[key]=val

        return obj



    def get_token(self,payload):


        secret_key = self.jwt_get_secret_key()

        token  = jwt.encode(payload,secret_key,algorithm="RS256")
        return token



    #
    # def get_access_token(self):
    #
    #
    #     return self.get_token(token_type="JWT_PAYLOAD")
    #
    #
    #
    # def get_refresh_token(self):
    #
    #
    #     return  self.get_token(token_type="JWT_REFRESH_PAYLOAD")




    def jwt_payload_handler(user):
        username_field = get_username_field()
        username = get_username(user)

        warnings.warn(
            'The following fields will be removed in the future: '
            '`email` and `user_id`. ',
            DeprecationWarning
        )

        payload = {
            'user_id': user.pk,
            'username': username,
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
        }
        if hasattr(user, 'email'):
            payload['email'] = user.email

        if isinstance(user.pk, uuid.UUID):
            payload['user_id'] = str(user.pk)

        payload[username_field] = username

        # Include original issued at time for a brand new token,
        # to allow token refresh
        if api_settings.JWT_ALLOW_REFRESH:
            payload['orig_iat'] = timegm(
                datetime.utcnow().utctimetuple()
            )

        if api_settings.JWT_AUDIENCE is not None:
            payload['aud'] = api_settings.JWT_AUDIENCE

        if api_settings.JWT_ISSUER is not None:
            payload['iss'] = api_settings.JWT_ISSUER

        return payload

    def jwt_get_user_id_from_payload_handler(payload):
        """
        Override this function if user_id is formatted differently in payload
        """
        warnings.warn(
            'The following will be removed in the future. '
            'Use `JWT_PAYLOAD_GET_USERNAME_HANDLER` instead.',
            DeprecationWarning
        )

        return payload.get('user_id')

    def jwt_get_username_from_payload_handler(payload):
        """
        Override this function if username is formatted differently in payload
        """
        return payload.get('username')

    def jwt_encode_handler(payload):
        key = api_settings.JWT_PRIVATE_KEY or jwt_get_secret_key(payload)
        return jwt.encode(
            payload,
            key,
            api_settings.JWT_ALGORITHM
        ).decode('utf-8')

    def jwt_decode_handler(token):
        options = {
            'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
        }
        # get user from token, BEFORE verification, to get user secret key
        unverified_payload = jwt.decode(token, None, False)
        secret_key = jwt_get_secret_key(unverified_payload)
        return jwt.decode(
            token,
            api_settings.JWT_PUBLIC_KEY or secret_key,
            api_settings.JWT_VERIFY,
            options=options,
            leeway=api_settings.JWT_LEEWAY,
            audience=api_settings.JWT_AUDIENCE,
            issuer=api_settings.JWT_ISSUER,
            algorithms=[api_settings.JWT_ALGORITHM]
        )

    def jwt_response_payload_handler(token, user=None, request=None):
        """
        Returns the response data for both the login and refresh views.
        Override to return a custom response such as including the
        serialized representation of the User.

        Example:

        def jwt_response_payload_handler(token, user=None, request=None):
            return {
                'token': token,
                'user': UserSerializer(user, context={'request': request}).data
            }

        """
        return {
            'token': token
        }




class RefreshToken(TokenUtils):

    def token_check(self):
        """
        更新
        :return:
        """

        return "ok"


    def update_refresh_token_expire(self):

        """
        更新refresh的有效期
        :return:
        """
        pass










