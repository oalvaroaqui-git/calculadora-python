def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("não é possível dividir por zero")
    return a / b


OPERACOES = {
    "1": ("Soma", somar),
    "2": ("Subtração", subtrair),
    "3": ("Multiplicação", multiplicar),
    "4": ("Divisão", dividir),
}


def exibir_menu():
    print("\n=== Calculadora ===")
    for chave, (nome, _) in OPERACOES.items():
        print(f"{chave} - {nome}")
    print("0 - Sair")


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido, digite um número.")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Encerrando a calculadora.")
            break

        operacao = OPERACOES.get(escolha)
        if operacao is None:
            print("Opção inválida.")
            continue

        nome, funcao = operacao
        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        try:
            resultado = funcao(a, b)
            print(f"{nome} = {resultado}")
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
