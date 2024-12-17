from main import *
from cryptography import fernet
import json

def test_generate_key():
    password = "pippi"

    key = generate_key(password)

    assert isinstance(key, bytes)
    assert len(key) == 44

##############################################################################################

def test_encrypt():
    password = "pippi"
    key = generate_key(password)
    fernet = Fernet(key)

    message = {"username": "testing_user", "message": "Heeeej på daaaaaj"}

    encrypt_this_message = encrypt(message, fernet)

    assert isinstance(encrypt_this_message, bytes)
    assert encrypt_this_message != json.dumps(message).encode()

##############################################################################################

def test_decrypt():
    password = "pippi"
    key = generate_key(password)
    fernet = Fernet(key)

    message = {"username": "testing_user", "message": "Heeeej på daaaaaj" }

    encrypt_this_message = encrypt(message,fernet)

    decrypt_this_message = decrypt(encrypt_this_message, fernet)

    assert decrypt_this_message == message

##############################################################################################


