from data import Data

opcoes = None 

def escolha():
  global opcoes
  opcoes = int(input('Selecione uma opção: \n 1.Data do sistema \n 2.Data manual\n'))

data = Data(1, 2, 3)

def definir():
  if opcoes == 1:
    data = Data(1, 2, 3)
    data.defineData(opcoes)
    data.toString()
  elif opcoes == 2:
    dia = int(input('Qual o dia?\n'))
    mes = int(input('Qual o mes?\n'))
    ano = int(input('Qual o ano?\n'))
    data = Data(dia, mes, ano)
    data.defineData(opcoes)
    data.toString()
  else:
    print('Dados inválidos')
    escolha()
    definir()

def adicionar():
  opcao = int(input('Selecione uma opção: \n 1.Adicionar dia \n 2.Sair\n'))
  if opcao == 1:
    data.adicionar()
    data.toString()
  elif opcao == 2:
    exit()
  else:
    print('Dados inválidos')
    adicionar()

escolha()
definir()
adicionar()
