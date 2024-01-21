from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def sign_data(private_key, data):
    key = RSA.import_key(private_key)
    hashed_data = SHA256.new(data.encode("utf-8"))
    signature = pkcs1_15.new(key).sign(hashed_data)
    return signature


def verify_signature(public_key, data, signature):
    key = RSA.import_key(public_key)
    hashed_data = SHA256.new(data.encode("utf-8"))
    try:
        pkcs1_15.new(key).verify(hashed_data, signature)
        return True
    except (ValueError, TypeError):
        return False
