import hashlib

val = input("Digite um texto: ")
print("Hash String => ", hashlib.md5(val.encode()).hexdigest())