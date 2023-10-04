import pytest
def decorator_imprimir(func):
   
    def imprimindo(capital,taxa,tempo):
        """
        Função interna do decorator que imprime os valores dos parâmetros e o resultado da função.
        
        Args:
            capital (float): O capital principal.
            taxa (float): A taxa de juros.
            tempo (float): O tempo (em anos).
        """
        print(f'CAPITAL: {capital} TAXA: {taxa} TEMPO:{tempo}')

        resultado = func(capital,taxa,tempo) # vai me trazer o resultado da função

        print(f'Resultado:{resultado}') #imprime o resultado da soma 
        
    return imprimindo

@decorator_imprimir
def juros_simples(capital,taxa,tempo):
    '''
    função para calcular juros simples 

    Args:
        capital (float): O capital principal.
        taxa (float): A taxa de juros.
        tempo (float): O tempo (em anos).

    '''
    return capital* (taxa/100)* tempo # retorna calculo juros simples
   
juros_simples(1000,5,6)
print('TUDO OK')
