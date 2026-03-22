
# Função Validação de entrada numérica
def validacaoEntrada (mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("Por favor, insira um valor maior ou igual a ZERO para continuar")
        except ValueError:
            print("Entrada inválida, insira um valor numérico para continuar")


def main():
    # Entrada
    nomeAparelho = input("Escreva o nome do aparelho: ")
    potencia = (validacaoEntrada("Escreva a potência do aparelho em watts: "))
    tempo = (validacaoEntrada("Escreva o tempo médio de uso diário em horas: "))

    # Processamento
    consumoMensal = (potencia * tempo * 30) / 100
    valorMensal = consumoMensal * 0.71

    # Saida
    print(f"\n{nomeAparelho}")
    print(f"Consumo Estimado: {consumoMensal:.2f} kWh/mês")
    print(f"Custo Estimado: R$ {valorMensal:.2f}")

if __name__ == "__main__":
    main()