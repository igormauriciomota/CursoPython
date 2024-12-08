'''
criar um sistema de apuração de Imposto de renda em Python com as aliquotas e valores Faixas do IR	Base de Cálculo	Alíquota

Faixa 1	até R$ 2.259,20	zero
Faixa 2	de R$ 2.259,21 até R$ 2.828,65	7,5%
Faixa 3	de R$ 2.826,66 até R$ 3.751,05	15%
Faixa 4	de R$ 3.751,06 até R$ 4.664,68	22,5% 

deve conter tambem calculos de pessoas que receban salarios diversos para que calcule de acordo com o salario recebido
''' 
def calcular_imposto(salario):
    if salario <= 2259.20:
        return 0
    elif salario <= 2828.65:
        return (salario - 2259.20) * 0.075
    elif salario <= 3751.05:
        return (2828.65 - 2259.20) * 0.075 + (salario - 2828.65) * 0.15
    elif salario <= 4664.68:
        return (2828.65 - 2259.20) * 0.075 + (3751.05 - 2828.65) * 0.15 + (salario - 3751.05) * 0.225
    else:
        return (2828.65 - 2259.20) * 0.075 + (3751.05 - 2828.65) * 0.15 + (4664.68 - 3751.05) * 0.225 + (salario - 4664.68) * 0.275

def main():
    print("Sistema de Apuração de Imposto de Renda")
    salarios = []

    while True:
        try:
            salario = float(input("Digite o salário (ou digite '0' para sair): "))
            if salario == 0:
                break
            salarios.append(salario)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    for salario in salarios:
        imposto = calcular_imposto(salario)
        print(f"Salário: R$ {salario:.2f} - Imposto devido: R$ {imposto:.2f}")

if __name__ == "__main__":
    main()
    
    