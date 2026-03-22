# Entrada
nomeAparelho = input("Escreva o nome do aparelho: ")
potencia = float(input("Escreva a potência do aparelho em watts: "))
tempo = float(input("Escreva o tempo médio de uso diário em horas: "))

# Processamento
consumoMensal = (potencia * tempo * 30) / 100
valorMensal = consumoMensal * 0.71

# Saida
print(f"{nomeAparelho}")
print(f"Consumo Estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo Estimado: R$ {valorMensal:.2f}")