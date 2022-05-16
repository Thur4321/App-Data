from datetime import date, timedelta

data = date.today()
dia = None 
mes = None 
ano = None 

class Data(object):

  def __init__(self, dia, mes, ano):
    self.__dia = int(dia)
    self.__mes = int(mes)
    self.__ano = int(ano)

  def getDia(self):
    return self.__dia

  def setDia(self, dia):
    self.__dia = dia
    
  def getMes(self):
    return self._mes

  def setMes(self, mes):
    self._mes = mes

  def getAno(self):
    return self.__ano

  def setAno(self, ano):
    self.__ano = ano

  def defineData(self, opcoes):
    global data
    global dia
    global mes
    global ano
    if opcoes == 1:
      data = date.today()
    else:
      data = date(ano, mes, dia)
    
  def toString(self):
    print('Data: ', data.strftime('%d/%m/%Y'))

  def adicionar(self):
    global data
    data = data+timedelta(1) 
      
