import base64
from Crypto import Random
from Crypto.Cipher import AES

AKEY = b'lzskdosjklfsdf%$%$%@RTED'  # AES key must be either 16, 24, or 32 bytes long

iv = Random.new().read(AES.block_size)


def encode(message):
    obj = AES.new(AKEY, AES.MODE_CFB, iv)
    return base64.urlsafe_b64encode(obj.encrypt(message.encode("utf-8")))


def decode(cipher):
    obj2 = AES.new(AKEY, AES.MODE_CFB, iv)
    return obj2.decrypt(base64.urlsafe_b64decode(cipher))


if __name__ == "__main__":
    key = b'Sixteen byte key'
    ciphertext = encode("hi")
    plain = decode(b'mQ==')
    print("decrypted:",str(plain),"type: ",type(plain))
