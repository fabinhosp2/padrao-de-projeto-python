from Exemplo003_CalculaTempo.decorator import Calcula_Tempo_Decorator
from Exemplo003_CalculaTempo.decorator2 import Mostra_Frase_Decorator


@Calcula_Tempo_Decorator
def soma():
    soma = 1 + 1
    print(soma)

soma()

@Mostra_Frase_Decorator
def subtrai():
    subtrai = 10 - 5
    print(subtrai)

subtrai()