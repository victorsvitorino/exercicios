""" ### Exercício 2 — Conversor de Celsius para Fahrenheit

**Como pensar:** a fórmula é `F = C * 9/5 + 32`. A única decisão de design aqui é: devo colocar a fórmula 
direto no `main()` ou em uma função separada? **Sempre em uma função separada** — mesmo sendo uma linha de
 cálculo, isso permite reaproveitar e (mais pra frente) testar isoladamente.
"""


def formula_fahrenheit(celsius):

    formula = (celsius * 9/5) + 32

    return formula

def mensagem(texto_1, texto_2):

    print(f"A temperatura de {texto_1:.2f} Celsius representa {texto_2:.2f} em Fahrenheit\n")



def main():

    print("### Calculadora para realizar a conversão de Celsius em Fahrenheit ###")

    celsius_texto = input("Digite uma temperatura em celsius\n")

    celsius = int(celsius_texto)
    fahrenheit = formula_fahrenheit(celsius)

    mensagem(celsius, fahrenheit)

if __name__ == "__main__":
    main()

