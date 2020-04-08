import os
import random
import hashlib
import json

hashsenha = input("Digite o Hash: ")

filepath = 'users.json'

with open(filepath) as json_file:
    data = json.load(json_file)
    for usuario in data:
        for usuarioDados in data[usuario]:
            if (usuarioDados == 'password' and data[usuario][usuarioDados] == hashsenha):
                print('Hash Encontrado!')
                print('Usuario: ' + usuario)
                print('Hash: ' + data[usuario][usuarioDados])
            # print('Campo '+m+' Valor - '+data[p][m])
        print('')
