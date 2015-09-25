import binascii
import hashlib
import json
import random
import struct

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import _modinv
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from flask import Flask


app = Flask(__name__)

with open("dsa.key") as f:
    pem_data = f.read().encode('ascii')

key = load_pem_private_key(pem_data, password=None, backend=default_backend())


@app.route('/sign/<data>')
def signer(data):
    r, s = sign(key, data)
    return json.dumps({'r': r, 's': s})


@app.route('/forgotpass')
def returnrand():
    # Generate a random value for the reset URL so it isn't guessable
    random_value = binascii.hexlify(struct.pack(">Q", random.getrandbits(64)))
    return "https://innitech.local/resetpass/{}".format(
        random_value.decode('ascii')
    )


@app.route('/resetpass/<key>')
def resetpass(key):
    # TODO: Implement this later. Innitech doesn't utilize users in this system
    # right now anyway.
    return "", 500


@app.route('/public_key')
def public_key():
    pn = key.private_numbers()
    return json.dumps({
        'g': pn.public_numbers.parameter_numbers.g,
        'q': pn.public_numbers.parameter_numbers.q,
        'p': pn.public_numbers.parameter_numbers.p,
        'y': pn.public_numbers.y
    })


def sign(key, data):
    data = data.encode('ascii')
    pn = key.private_numbers()
    g = pn.public_numbers.parameter_numbers.g
    q = pn.public_numbers.parameter_numbers.q
    p = pn.public_numbers.parameter_numbers.p
    x = pn.x
    k = random.randrange(2, q)
    kinv = _modinv(k, q)
    r = pow(g, k, p) % q
    h = hashlib.sha1(data).digest()
    h = int.from_bytes(h, "big")
    s = kinv * (h + r * x) % q
    return (r, s)

if __name__ == '__main__':
    app.run()
