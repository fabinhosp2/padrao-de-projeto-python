#Função que retorna ela mesma

def Cria_Soma(x):
    def Soma(num):
        return x + num
    return Soma

#Funções = "x"
Soma_2 = Cria_Soma(2)
Soma_3 = Cria_Soma(2)

# "num"
print(Soma_2(8))
print(Soma_3(18))
