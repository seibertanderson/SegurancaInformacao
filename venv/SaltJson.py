import os
import random
import hashlib
import json

usuario = input("Digite seu Usuário: ")
senha = input("Digite sua senha: ")
tipoHash = 'sha1'

filepath = 'users.json'
hashFunc = getattr(hashlib, tipoHash)
salt = str.join('', [str(random.randint(0, 4)) for x in range(2 ** 5)])
hash = hashFunc(bytearray(senha + salt, 'utf8')).hexdigest()

users = {}
if (os.path.exists(filepath)):
    with open(filepath, 'r') as fout:
        fcontent = fout.read()
        if fcontent is not None or fcontent != '':
            users = json.loads(fcontent)

users[usuario] = {'password': hash, 'salt': salt, 'type': tipoHash}

with open(filepath, 'w') as fout:
    fout.write(json.dumps(users, indent=2))
