def Mostra_Frase_Decorator(funcao):

    def Mostra_Frase():
        print("Executando com o decorator 2 sem dados")

        funcao()

    return Mostra_Frase