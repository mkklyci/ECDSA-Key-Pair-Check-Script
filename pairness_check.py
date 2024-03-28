from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)

# the private key
with open("ec_private_key.pem", "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None)

    extracted_public_key = private_key.public_key()

# open public key
with open("ec_public_key.pem", "rb") as key_file:
    provided_public_key = load_pem_public_key(key_file.read())

# convert both public keys to bytes for comparison
extracted_public_bytes = extracted_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

provided_public_bytes = provided_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# compare the keys
if extracted_public_bytes == provided_public_bytes:
    print("Match. They are pair.")
else:
    print("They don't match. They are not pair.")
