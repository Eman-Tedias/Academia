import json
import pandas as pd

with open('data2.json', 'r') as file:
    data_list = json.load(file)

with open('data.json', 'r') as file2:
    data_list2 = json.load(file2)

json_data = []
json_data2 = []

for data in data_list:
    for exercicios in data['exercicios']:
        series = exercicios['series']
        for s in series:
            if 'x' in s:
                peso = s.split('x')[0]
                repeticao = s.split('x')[1]
            else:
                peso = s
                repeticao = None
            cardio = data.get('cardio', None)
            if cardio is not None:
                cardio_tipo = cardio[0]['tipo']
                cardio_tempo = cardio[0]['tempo']
            else:
                cardio_tipo = None
                cardio_tempo = None
            json_data.append(
                {   
                    "data": data['data'],
                    "nome": exercicios['nome'],
                    "peso": peso,
                    "repeticao": repeticao,
                    # "peso_add": exercicios['series'],
                    # "rep_add": exercicios['series'],
                    "cardio": cardio_tipo,
                    "tempo": cardio_tempo
            }
        )

for data in data_list2:
    for exercicios in data['exercicios']:
        series = exercicios['series']
        for s in series:
            if 'x' in s[0]:
                peso = s[0].split('x')[0]
                repeticao = s[0].split('x')[1]
            else:
                peso = s[0]
                repeticao = None
            if len(s) > 1 and 'x' in s[1]:
                peso_add = s[1].split('x')[0]
                rep_add = s[1].split('x')[1]
            cardio = data.get('cardio', None)
            if cardio is not None:
                cardio_tipo = cardio[0]['tipo']
                cardio_tempo = cardio[0]['tempo']
            else:
                cardio_tipo = None
                cardio_tempo = None
            json_data2.append(
                {   
                    "data": data['data'],
                    "nome": exercicios['nome'],
                    "peso": peso,
                    "repeticao": repeticao,
                    "peso_add": peso_add,
                    "rep_add": rep_add,
                    "cardio": cardio_tipo,
                    "tempo": cardio_tempo
            }
        )

df = pd.DataFrame(json_data)
df2 = pd.DataFrame(json_data2)

tabela = pd.concat([df, df2])

tabela.to_csv('table.csv', index=False)