def main():

    entrevistados = 1
    excelente = 0
    bom = 0
    ruim = 0

    for entrevistados in range(1,50):
        nome = input("Digite o seu nome: ")
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                if idade >= 0:
                    break
                else:
                    print("Por favor, insira uma idade válida para prosseguirmos")
            except ValueError:
                print("Por favor, insira uma idade válida para prosseguirmos")
        
        while True:
            avaliacao = input("Avalie o atendimento prestado conforme as indicações abaixo:\nDigite 1 para EXCELENTE\nDigite 2 para BOM\nDigite 3 para RUIM\n")
            if avaliacao in ["1", "2", "3"]:
                match avaliacao:
                    case "1":
                        print("Agradecemos sua participação!")
                        excelente += 1
                        break
                    case "2":
                        print("Agradecemos sua participação!")
                        bom += 1
                        break
                    case "3":
                        print("Agradecemos sua participação!")
                        ruim += 1
                        break
            else: print("Entrada inválida, por favor digite o número correspondente a sua avaliação.")

    excPorcentagem = excelente * 100 / entrevistados
    bomPorcentagem = bom * 100 / entrevistados
    ruimPorcentagem = ruim * 100 / entrevistados

    print("Pesquisa finalizada!\nAvaliações Excelentes:",excelente,"(",excPorcentagem,"% )\nAvaliações Ruins:",ruim,"(",ruimPorcentagem,"% )\n")

if __name__ == "__main__":
    main()
