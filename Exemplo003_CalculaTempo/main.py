import datetime

def Calcula_Tempo_Decorator(funcao):

    def Calcula_Tempo():
        print(datetime.datetime.now())

        funcao()
        print(datetime.datetime.now())

    return Calcula_Tempo

@Calcula_Tempo_Decorator
def Outra_Funcao():
    for i in range(100000):
        continue

Outra_Funcao()