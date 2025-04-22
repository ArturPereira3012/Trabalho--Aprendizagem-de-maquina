"""
Trabalho em Grupo - Aprendizagem de Máquina
Módulo para Cálculo de Investimento na Caixinha Super Cofrinho

Integrantes:
1. Artur Pereira Medeiros - 2314290019
2. João Vítor de Oliveira Sampaio - 2314290084
3. Igor Nachi Santos - 2314290013
4. Eduardo Noronha Picoli - 2314290140

"""

def calcular_investimento():
    # Dados de entrada
    valor_inicial = float(input("Digite o valor inicial do investimento: R$ "))
    dias_investimento = int(input("Digite o número de dias do investimento: "))
    
    # Taxa de rendimento anual
    taxa_rendimento_anual = 0.1415  # 14.15% ao ano
    
    # Converter taxa anual para diária (considerando ano de 365 dias)
    taxa_rendimento_diaria = (1 + taxa_rendimento_anual) ** (1/365) - 1
    
    # Calcular valor bruto com rendimento
    valor_bruto = valor_inicial * (1 + taxa_rendimento_diaria) ** dias_investimento
    
    # Tabela IOF (dicionário com dias como chave e alíquota como valor)
    tabela_iof = {
        1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83,
        6: 0.80, 7: 0.76, 8: 0.73, 9: 0.70, 10: 0.66,
        11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53, 15: 0.50,
        16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33,
        21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16,
        26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03, 30: 0.00
    }
    
    # Calcular IOF
    if dias_investimento <= 30:
        aliquota_iof = tabela_iof.get(dias_investimento, 0.00)
    else:
        aliquota_iof = 0.00
    
    valor_iof = (valor_bruto - valor_inicial) * aliquota_iof
    
    # Calcular IR
    if dias_investimento <= 180:
        aliquota_ir = 0.225  # 22.5%
    elif 181 <= dias_investimento <= 360:
        aliquota_ir = 0.20   # 20%
    elif 361 <= dias_investimento <= 720:
        aliquota_ir = 0.175  # 17.5%
    else:
        aliquota_ir = 0.15   # 15%
    
    valor_ir = (valor_bruto - valor_inicial - valor_iof) * aliquota_ir
    
    # Calcular valor líquido
    valor_liquido = valor_inicial + (valor_bruto - valor_inicial) - valor_iof - valor_ir
    
    # Exibir resultados
    print("\n--- Resultado do Investimento ---")
    print(f"Valor Inicial: R$ {valor_inicial:.2f}")
    print(f"Período: {dias_investimento} dias")
    print(f"Valor Bruto (com rendimento): R$ {valor_bruto:.2f}")
    print(f"IOF descontado: R$ {valor_iof:.2f} ({aliquota_iof*100:.0f}%)")
    print(f"IR descontado: R$ {valor_ir:.2f} ({aliquota_ir*100:.1f}%)")
    print(f"Valor Líquido: R$ {valor_liquido:.2f}")
    print("---------------------------------")

# Executar o programa
if __name__ == "__main__":
    print("Calculadora de Investimento - Caixinha Super Cofrinho")
    print("-----------------------------------------------------")
    calcular_investimento()