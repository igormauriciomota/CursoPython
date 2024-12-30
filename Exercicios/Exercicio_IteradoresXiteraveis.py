'''
Exercicio Iteradores X iteraveis


'''
def desmembra_iteravel(iteravel):
    iterador = iter(iteravel)
    while True:
        try:
            print(next(iterador))
        except StopIteration:
            print('Chegamos ao ultimo elemento')
            break
        
desmembra_iteravel([1,2,3,4,5,6,7,8])

