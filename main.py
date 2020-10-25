import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5, AES
from Crypto import Random
from Crypto.Util.Padding import unpad


def decrypt_aes_key():
    # open file and read data: our private key
    private_key = open('files/privat.pem').read()
    # create private key object
    private_key = RSA.importKey(private_key)

    # open file and read data: encrypted aes key
    enc_aes_key = open('files/encAesKey').read()
    # decode from base64
    enc_aes_key = base64.b64decode(enc_aes_key)
    # create object for decrypt
    cipher = PKCS1_v1_5.new(private_key)

    dsize = SHA.digest_size
    sentinel = Random.new().read(15 + dsize)

    # decrypt our aes key
    result_aes_key = cipher.decrypt(enc_aes_key, sentinel)
    return result_aes_key

def decrypt_aes_iv():
    # open file and read data: our private key
    private_key = open('files/privat.pem').read()
    # create private key object
    private_key = RSA.importKey(private_key)

    # open file and read data: encrypted aes iv
    enc_aes_iv = open('files/encAesIV').read()
    # decode from base64
    enc_aes_iv = base64.b64decode(enc_aes_iv)
    # create object for decrypt
    cipher = PKCS1_v1_5.new(private_key)

    # decrypt our iv
    result_aes_iv = cipher.decrypt(enc_aes_iv, 128)
    return result_aes_iv


def decrypt_aes_message(key, iv):
    enc_message = open('files/encMessage').read()
    enc_message = base64.b64decode(enc_message)

    # create object for aes-CBC-mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # default block_size 16
    # we need 128
    AES.block_size = 128
    message = unpad(cipher.decrypt(enc_message), AES.block_size)
    return message


def main():
    aes_key = decrypt_aes_key()
    aes_iv = decrypt_aes_iv()
    message = decrypt_aes_message(aes_key, aes_iv)
    # decode bytes to utf-8 (NOT ASCII)
    message = message.decode('utf-8')
    print(message)


if __name__ == '__main__':
    main()