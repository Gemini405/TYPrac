# !pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)
pubKey = keyPair.public_key()

print(f"Public key: (n: {hex(pubKey.n)}, e: {hex(pubKey.e)})")
pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n:{hex(pubKey.n)}, d: {hex(keyPair.d)})")
privKeyPEM = keyPair.export_key()

msg = b"MANDY"
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)

print(f"Encrypted: {binascii.hexlify(encrypted)} \n{privKeyPEM.decode('ascii')}")
