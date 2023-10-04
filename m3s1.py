        
import requests

class TabelaFIPE:
    def __init__(self):
        self.IDAtual = 0

        self.marcas = self.get_marcas()

        for marca in self.marcas:
            print(f"ID: {marca['codigo']} | Nome: {marca['nome']}")

        self.ID_MARCASELECIONADA = self.obtem_id_da_marca()

        self.modelos = self.get_modelos()
        
        #for modelo in self.modelos['modelos']:
           # print(f"ID: {modelo['codigo']} | Nome: {modelo['nome']}")
        
        self.qtd_modelos = len(self.modelos)
    
    def obtem_id_da_marca(self):
        id_buscado = int(input("Digite o ID do modelo desejado: "))
        return id_buscado

    def get_marcas(self):
        r = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas', headers = {'user-agent': 'MyStudyApp'})
        marcas = r.json() #Conversão dos dados para JSON (Dicionário)
        return marcas

    def get_modelos (self):
        r = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.ID_MARCASELECIONADA}/modelos', headers = {'user-agent': 'MyStudyApp'})
        modelos = r.json() #Conversão dos dados para JSON (Dicionário)
        return modelos['modelos']
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.IDAtual > self.qtd_modelos:
            raise StopIteration
        
        if self.IDAtual < len(self.modelos):
            id_buscado = self.IDAtual
            self.IDAtual += 1
            return self.modelos[id_buscado]
        else:
            raise StopIteration

carros = TabelaFIPE()     #Cria o objeto
carro = iter(carros)
for carro1 in carros:
        print(f"ID: {carro1['codigo']} | NOME: {carro1['nome']}")

