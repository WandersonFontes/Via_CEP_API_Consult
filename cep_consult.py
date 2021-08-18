import requests

class ViaCepApi:
    def __init__(self):
        print('Olá!\nSeja bem vindo.\nEu me chamo Via CEP, vou retornar dados de algum CEP brasileiro que você me passar!')
        cep = str(input('\nEstou a sua disposição!\nInsira o CEP aqui: '))
        data = self.validateCEP(cep)
        self.consultarCep(data)

    def consultarCep(self, cep):
        print(f'https://viacep.com.br/ws/{cep}/json/')
        request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if request.status_code != 200:
            print('Algo deu errado!\nVerifique sua conexão com a internet e tente mais tarde.')
        elif request.status_code == 200:
            print("Deu certinho!")
            print(request.json())

    def validateCEP(self, cep):
        #data = cep.replace('-', '')
        if type(cep) != str:
            print(f'{cep} - Esse não é um CEP válido!\nPor gentileza corriga e tente novamente.')
        else:
            return cep

chamarApi = ViaCepApi()