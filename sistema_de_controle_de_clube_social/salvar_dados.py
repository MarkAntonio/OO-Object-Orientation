from os.path import isfile
import pickle

banco_de_dados = {}


def set_data(data):
    global banco_de_dados
    banco_de_dados = data


file = 'banco_de_dados.pkl'


def carregar():
    if not isfile(file):
        with open(file, 'xb') as data:
            pickle.dump(banco_de_dados, data)
        return
    with open(file, 'rb') as data:
        loaded_data = pickle.load(data)
        set_data(loaded_data)


def save_info():
    with open(file, 'wb') as data:
        pickle.dump(banco_de_dados, data)


def get_banco():
    return banco_de_dados


def set_banco(key, value):
    banco_de_dados[key] = value


def set_dependente(id: str, dep):
    banco_de_dados[id].dependentes.append(dep)
