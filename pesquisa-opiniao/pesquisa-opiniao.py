def main():

    entrevistados = 1
    excelente = 0
    bom = 0
    ruim = 0

    for entrevistados in range(1,51):
        nome = input("Digite o seu nome: \n")
        while True:
            try:
                idade = int(input("Digite sua idade: \n"))
                if idade >= 0:
                    break
                else:
                    print("Por favor, insira uma idade válida para prosseguirmos\n")
            except ValueError:
                print("Por favor, insira uma idade válida para prosseguirmos\n")
        
        while True:
            avaliacao = input("Avalie o atendimento prestado conforme as indicações abaixo:\nDigite 1 para EXCELENTE\nDigite 2 para BOM\nDigite 3 para RUIM\n")
            if avaliacao in ["1", "2", "3"]:
                match avaliacao:
                    case "1":
                        print("Agradecemos sua participação!\n")
                        excelente += 1
                        break
                    case "2":
                        print("Agradecemos sua participação!\n")
                        bom += 1
                        break
                    case "3":
                        print("Agradecemos sua participação!\n")
                        ruim += 1
                        break
            else: print("Entrada inválida, por favor digite o número correspondente a sua avaliação.\nAvalie o atendimento prestado conforme as indicações abaixo:\nDigite 1 para EXCELENTE\nDigite 2 para BOM\nDigite 3 para RUIM\n")

    excPorcentagem = excelente * 100 / entrevistados
    bomPorcentagem = bom * 100 / entrevistados
    ruimPorcentagem = ruim * 100 / entrevistados

    print("Pesquisa finalizada!\nAvaliações Excelentes:",excelente, f"({excPorcentagem:.2f}%)\nAvaliações Ruins:",ruim,f"({excPorcentagem:.2f}%)\n") 

if __name__ == "__main__":
    main()
