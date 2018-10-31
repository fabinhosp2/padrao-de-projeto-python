import datetime

def Calcula_Tempo_Decorator(funcao):

    def Calcula_Tempo():
        print(datetime.datetime.now())
        funcao()
        print(datetime.datetime.now())

    return Calcula_Tempo