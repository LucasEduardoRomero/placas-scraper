import json

with open('./produtos_all.jl', 'r', encoding='utf-8') as fl:
    for line in fl:
        linha = json.loads(line)
        print(linha['produto'])
        break