# app.py - Calculadora de Consumo de Energia

#calculadora de consumo de energia
  
# Entrada de dados

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do(a) {aparelho} em Watts (W): "))
horas_dia = float(input(f"Quantas horas por dia o(a) {aparelho} fica ligado(a)? "))
    
# Cálculo do consumo mensal (30 dias) em kWh
# Fórmula: (Watts * horas * dias) / 1000
consumo_mensal = (potencia * horas_dia * 30) / 1000
    
# Cálculo de custo estimado (R$ 0,75 por kWh)
custo_estimado = consumo_mensal * 0.75
    
# Exibição dos resultados
print("--- RESULTADO ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} (Base: R$ 0,75/kWh)")
print("="*30)

