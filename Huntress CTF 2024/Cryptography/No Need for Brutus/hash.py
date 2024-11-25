import hashlib
plaintext = "caesarissimplenoneedforbrutus"
hashed = hashlib.md5(plaintext.encode()).hexdigest()
print(f"flag{{{hashed}}}")