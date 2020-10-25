import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random


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

    # decrypt out aes key
    result_aes_key = cipher.decrypt(enc_aes_key, sentinel)
    return result_aes_key

def main():
    aes_key = decrypt_aes_key()


if __name__ == '__main__':
    main()