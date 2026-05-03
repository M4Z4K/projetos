from colorama import Fore, Back, Style                          # Importação da biblioteca colorama após sua instalação via pip
from random import choice                                       # Importação da biblioteca random para simular o nível do reservatório
from time import sleep                                          # Importaçãpo da biblioteca time para loop de monitoramento                                                

nivel_info = [                                                  # Lista de tuplas para armazenar os dados necessários do sistema (Nível, Situação, Cor)
    (1, "Muito baixo (crítico)", Fore.RED),
    (2, "Baixo", Fore.YELLOW),
    (3, "Médio", Fore.GREEN),
    (4, "Alto", Fore.CYAN),
    (5, "Muito alto (alerta)", Fore.BLUE)
]

def obter_alerta(nivel):                                        # Função de nome "obter_alerta" com o parâmetro (nivel)
    for info in nivel_info:                                     # Para cada iteração na lista "nivel_info", faz:
        if info[0] == nivel:                                    # Verifica se info[0] é igual ao parâmetro (nivel):
            return info[1], info[2]                             # Se for, retorna as informações em info[1] e info[2]
    return None, None                                           # Se o valor do parâmetro não existir na lista "nivel_info", retorne "None, None" para evitar erros

mensagem_boas_vindas = (                                        # Trecho do código com uma breve interface de boas-vindas utilizando a biblioteca colorama, explicando o sistema e como utilizá-lo.
    f"{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}"
    "\nBem-vindo(a) ao SVNAR - Sistema de Verificação do Nível da Água do Reservatório"
    f"{Style.RESET_ALL}\n\n"
    "O SVNAR irá verificar o atual nível da água no reservatório e repetirá esse processo a cada 5 segundos.\n"
    f"Ao apertar a tecla {Style.BRIGHT}ENTER{Style.RESET_ALL} no seu teclado, o monitoramento se incia.\n"
    f"Para encerrar o monitoramento, aperte as teclas {Style.BRIGHT}CTRL+C{Style.RESET_ALL}.\n\n"
    f"{Back.BLACK}{Fore.CYAN}{Style.BRIGHT}"
    "Aperte a tecla ENTER para inciar o monitoramento"
    f"{Style.RESET_ALL}"
)

input(mensagem_boas_vindas)                                     # Chamada da mensagem de boas-vindas através de um input.

def main():                                                     # Função principal "main"
    try:
        while True:                                             # Loop para repetir a verificação do nivel da água a cada 5 segundos.
            nivel_reservatorio = choice([1, 2, 3, 4, 5])        # Utilização da biblioteca random para simular o nível do reservatório
            situacao, cor = obter_alerta(nivel_reservatorio)    # Chamada da função "obter_alerta" usando "nivel_reservatorio" como argumento

            if situacao is None:                                # Boa prática para evitar que o programa imprima "None, None" como resultado
                print("\nErro: nível inválido\n")               # Impressão em caso de erro.
            else:                                               
                print(f"\nNível atual do reservatório - {nivel_reservatorio}: {cor}{situacao}{Style.RESET_ALL}") # Impressão do nível e situação do reservatório, essa, impressa na cor correspondente. 

            sleep(5)                                            # Utilização da biblioteca time para criar a repetição infinita

    except KeyboardInterrupt:                                   # Caso o usuário interrompa a execução do loop a mensagem abaixo será apresentada.
        print("\nMonitoramento encerrado.\n")           
        
if __name__ == "__main__":
    main()
