def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II (Severa)"
    else:
        return "Obesidade Grau III (Mórbida)"

def calcular_tmb(peso, altura, idade, sexo):
    # Altura deve estar em cm
    altura_cm = altura * 100
    if sexo.upper() == 'M':
        tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
    elif sexo.upper() == 'F':
        tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
    else:
        raise ValueError("Sexo inválido. Use 'M' ou 'F'.")
    return tmb

# --- NOVA LÓGICA DE CÁLCULO DE GCT ---
def calcular_gct(tmb, horas_exercicio, esforco_trabalho):
    """
    Calcula o GCT baseado na TMB e nos novos fatores de atividade.
    """
    # Mapeamento do Esforço no Trabalho para índices de linha
    mapa_trabalho = {
        'Trabalho com pouco esforço físico': 0,
        'Trabalho com esforço físico moderado': 1,
        'Trabalho com esforço físico intenso': 2,
        'Atleta Profissional': 3
    }
    
    # Mapeamento das Horas de Exercício para índices de coluna
    mapa_exercicio = {
        'Pouco ou nada': 0, '1 hora': 1, '2 horas': 2, '3 horas': 3, 
        '5 horas': 4, '7 horas': 5, 'Mais de 7 horas': 6
    }
    
    # Matriz de Fatores de Atividade (FA) - Adaptada e simplificada
    FA_MATRIX = [
        # Pouco ou nada, 1h, 2h, 3h, 5h, 7h, >7h
        [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8], # Trabalho Pouco Esforço
        [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9], # Trabalho Moderado
        [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0], # Trabalho Intenso
        [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1], # Atleta Profissional
    ]

    try:
        linha = mapa_trabalho[esforco_trabalho]
        coluna = mapa_exercicio[horas_exercicio]
        fator = FA_MATRIX[linha][coluna]
    except KeyError:
        raise ValueError("Seleção de atividade ou esforço inválida.")

    gct = tmb * fator
    return gct

def calcular_macros(gct, peso, objetivo):
    """
    Calcula os macros baseados no GCT de Manutenção e no Objetivo.
    """
    CAL_PROT = 4
    CAL_GORD = 9
    
    # Ajuste calórico baseado no objetivo (Bulking +500, Cutting -500, Manutenção 0)
    ajuste_calorico = 0
    if objetivo == 'Bulking':
        ajuste_calorico = 500
    elif objetivo == 'Cutting':
        ajuste_calorico = -500

    gct_ajustado = gct + ajuste_calorico
    gct_ajustado = max(1200, gct_ajustado) # Garante um mínimo saudável (1200 kcal)

    # Proteína: 2.0g/kg (Pode ser ajustado)
    proteina_g = 2.0 * peso
    calorias_proteina = proteina_g * CAL_PROT

    # Gordura: 0.8g/kg (Pode ser ajustado)
    gordura_g = 0.8 * peso
    calorias_gordura = gordura_g * CAL_GORD

    # Carboidratos: preenchem o restante
    calorias_restantes = max(0, gct_ajustado - calorias_proteina - calorias_gordura)
    carboidrato_g = calorias_restantes / CAL_PROT if calorias_restantes > 0 else 0

    return {
        'calorias_totais': gct_ajustado,
        'proteina_g': proteina_g,
        'gordura_g': gordura_g,
        'carboidrato_g': carboidrato_g,
    }