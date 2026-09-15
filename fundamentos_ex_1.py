

"""Exercicio - 1 apenas para coleta de dados do usuário e impressão da mensagem na tela,
não foi realizado nenhum tratamento de erro."""


def mensagem(nome: str, idade: int) -> str:
    return f"Olá, {nome}! Você tem {idade} anos."


def main():

    nome = input("Qual seu nome ?\n")
    idade_texto = input("Qual sua idade?\n")

    idade = int(idade_texto)

    mensagem_final = mensagem(nome, idade)

    print(mensagem_final)
    print("*** FIM ***")

if __name__ == "__main__":

    main()
