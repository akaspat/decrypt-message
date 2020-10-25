import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5, AES
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Util.Padding import unpad


def decrypt_aes_key():
    f = open('privat.pem').read()
    private_key = RSA.importKey(f)
    f = open('encAesKey')
    encAesKey = f.read()
    encAesKey = base64.b64decode(encAesKey)
    cipher = PKCS1_v1_5.new(private_key)

    dsize = SHA.digest_size
    sentinel = Random.new().read(15 + dsize)
    result_aes_key = cipher.decrypt(encAesKey, sentinel)
    print(result_aes_key)
    return result_aes_key


def decrypt_aes_iv():
    f = open('privat.pem').read()
    private_key = RSA.importKey(f)
    f = open('encAesIV')
    enc_aes_iv = f.read()
    f.close()
    enc_aes_iv = base64.b64decode(enc_aes_iv)
    cipher = PKCS1_v1_5.new(private_key)
    result_aes_iv = cipher.decrypt(enc_aes_iv, 128)
    print(result_aes_iv)
    return result_aes_iv


def decrypt_aes_message(key, iv):
    f = open('encMessage')
    encMessage= f.read()
    f.close()
    encMessage = base64.b64decode(encMessage)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print(AES.block_size)
    AES.block_size = 128
    print(AES.block_size)
    message = unpad(cipher.decrypt(encMessage), AES.block_size)
    return message


def main():
    aes_key = decrypt_aes_key()
    aes_iv = decrypt_aes_iv()
    message = decrypt_aes_message(aes_key, aes_iv)
    print(message.decode('utf-8'))


if __name__ == '__main__':
    main()

