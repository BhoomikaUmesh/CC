from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import ec
private_key=ec.generate_private_key(ec.SECP256R1())
public_key=private_key.public_key()
public_pem=public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(public_pem.decode())
message=input("enter the message ").encode()
signature=private_key.sign(message, ec.ECDSA(hashes.SHA256()))
print(signature)
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
except:
    print("invalid")
