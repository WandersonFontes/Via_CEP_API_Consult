import requests

class ViaCepApi:
    def __init__(self):
        print('Olá!\nSeja bem vindo.\nEu me chamo Cepinho, vou te trazer dados de algum CEP brasileiro que você me passar!')
        try:
            consultar = requests.get('https://www.google.com/')
            if (consultar.status_code == 200):
                return self.consultarCep()
        except:
            print('Parece que estamos sem Internet.\nVerifique a sua conexão e tente novamente!')

    def consultarCep(self):
        cep = str(input('Informe o código do CEP: '))
        while(cep == None or cep == ""):
            cep = str(input('Por gentileza informe o código do CEP: '))
        request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if request.status_code != 200:
            if(len(cep) != 8 or not cep.isdigit()):
                return print('Verifique se você está inserido o CEP corretamente!')
            print('Algo deu errado!\nTente novamente mais tarde.')
        elif request.status_code == 200:
            print("Deu certinho!")
            print(request.json())

    def validateCEP(self, cep):
        cep = cep.replace('-', '')
        if type(cep) != str:
            print('Esse não é um CEP válido!\nPor gentileza corriga e tente novamente.')
            replay = int(input("Deseja tentar novamente?\n0 = Não - 1 = Sim"))
            while(replay == 1):
                self.consultarCep(cep)
        else:
            return cep

executar = ViaCepApi()
