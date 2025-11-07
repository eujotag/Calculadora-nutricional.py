import tkinter as tk
from tkinter import ttk, messagebox
from calculos import (
    calcular_imc,
    classificar_imc,
    calcular_tmb,
    calcular_gct,
    calcular_macros
)

# --- Mapeamentos para os ComboBoxes (Conforme suas imagens) ---
ESFORCO_TRABALHO = [
    'Trabalho com pouco esforço físico',
    'Trabalho com esforço físico moderado',
    'Trabalho com esforço físico intenso',
    'Atleta Profissional'
]

EXERCICIO_SEMANAL = [
    'Pouco ou nada', '1 hora', '2 horas', '3 horas',
    '5 horas', '7 horas', 'Mais de 7 horas'
]


def calcular():
    """Função chamada pelo botão para realizar todos os cálculos."""
    try:
        # 1. Coletar dados da interface
        peso = float(entry_peso.get())
        # A altura na sua imagem está em CM, então convertemos para M para o IMC/TMB
        altura = float(entry_altura.get()) / 100
        idade = int(entry_idade.get())
        sexo = var_sexo.get()
        objetivo = var_objetivo.get()
        exercicio = var_exercicio.get()
        trabalho = var_trabalho.get()

        # 2. Validações básicas
        if not sexo or not objetivo or not exercicio or not trabalho:
            messagebox.showerror(
                "Erro de Entrada", "Por favor, preencha todas as seleções (Sexo, Objetivo, Exercício e Trabalho).")
            return

        # 3. Executar os Cálculos

        # IMC e TMB
        imc = calcular_imc(peso, altura)
        classificacao_imc = classificar_imc(imc)
        tmb = calcular_tmb(peso, altura, idade, sexo)

        # GCT (usando a nova matriz de fatores)
        gct_manutencao = calcular_gct(tmb, exercicio, trabalho)

        # Macros e Calorias Ajustadas
        macros = calcular_macros(gct_manutencao, peso, objetivo)
        calorias_ajustadas = macros['calorias_totais']

        # 4. Formatar e exibir os resultados

        resultado_texto = f"""
        --- Resultados ---
        
        *IMC:* {imc:.2f} ({classificacao_imc})
        
        *TMB (Basal):* {tmb:.0f} kcal/dia
        *GCT (Manutenção):* {gct_manutencao:.0f} kcal/dia
        
        *🎯 Objetivo Selecionado ({objetivo}):*
        *CALORIAS TOTAIS:* {calorias_ajustadas:.0f} kcal/dia
        
        *Macronutrientes Sugeridos:*
        - Proteína: {macros['proteina_g']:.1f}g 
        - Gordura: {macros['gordura_g']:.1f}g
        - Carboidrato: {macros['carboidrato_g']:.1f}g
        """

        # Atualiza a área de resultados
        label_resultado.config(text=resultado_texto, justify=tk.LEFT)

    except ValueError as e:
        messagebox.showerror(
            "Erro de Entrada", f"Dados inválidos: {e}\nVerifique se os campos numéricos (Peso, Altura, Idade) estão corretos.")
    except Exception as e:
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")


# --- Configuração da Janela Principal ---
janela = tk.Tk()
janela.title("Calculadora Nutricional e de Macros")
janela.geometry("450x700")
janela.resizable(False, False)  # Evita redimensionamento para manter o layout

# --- Criação do Frame de Entrada ---
frame_entrada = ttk.LabelFrame(janela, text="Dados Pessoais")
frame_entrada.pack(padx=10, pady=10, fill="x")

# Usamos o Grid para o layout
# --- Linha 1: Peso, Altura, Idade ---
ttk.Label(frame_entrada, text="Peso atual:").grid(
    row=0, column=0, padx=5, pady=5)
entry_peso = ttk.Entry(frame_entrada, width=8)
entry_peso.grid(row=0, column=1, padx=2, pady=5)
ttk.Label(frame_entrada, text="kg").grid(
    row=0, column=2, padx=0, pady=5, sticky="w")

ttk.Label(frame_entrada, text="Altura:").grid(row=0, column=3, padx=5, pady=5)
entry_altura = ttk.Entry(frame_entrada, width=8)
entry_altura.grid(row=0, column=4, padx=2, pady=5)
ttk.Label(frame_entrada, text="cm").grid(
    row=0, column=5, padx=0, pady=5, sticky="w")

ttk.Label(frame_entrada, text="Idade:").grid(row=0, column=6, padx=5, pady=5)
entry_idade = ttk.Entry(frame_entrada, width=8)
entry_idade.grid(row=0, column=7, padx=2, pady=5)
ttk.Label(frame_entrada, text="anos").grid(
    row=0, column=8, padx=0, pady=5, sticky="w")

# --- Linha 2: Sexo (Radio Buttons) ---
ttk.Label(frame_entrada, text="Sexo:").grid(
    row=1, column=0, padx=5, pady=5, sticky="w")
var_sexo = tk.StringVar()
# Adicione um estilo simples para destacar os botões de rádio (como no protótipo)
ttk.Radiobutton(frame_entrada, text="Masculino", variable=var_sexo, value="M").grid(
    row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame_entrada, text="Feminino", variable=var_sexo, value="F").grid(
    row=1, column=3, columnspan=2, padx=5, pady=5, sticky="w")

# --- Linha 3: Objetivo (Radio Buttons) ---
ttk.Label(frame_entrada, text="Objetivo:").grid(
    row=2, column=0, padx=5, pady=5, sticky="w")
var_objetivo = tk.StringVar()
ttk.Radiobutton(frame_entrada, text="Cutting", variable=var_objetivo, value="Cutting").grid(
    row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame_entrada, text="Bulking", variable=var_objetivo, value="Bulking").grid(
    row=2, column=3, columnspan=2, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frame_entrada, text="Manutenção", variable=var_objetivo, value="Manutenção").grid(
    row=2, column=5, columnspan=2, padx=5, pady=5, sticky="w")

# --- Linha 4: Exercício Semanal (Combobox) ---
ttk.Label(frame_entrada, text="Exercício físico semanal:").grid(
    row=3, column=0, columnspan=4, padx=5, pady=5, sticky="w")
var_exercicio = tk.StringVar(janela)
var_exercicio.set(EXERCICIO_SEMANAL[0])
combo_exercicio = ttk.Combobox(frame_entrada, textvariable=var_exercicio,
                               values=EXERCICIO_SEMANAL, state="readonly", width=18)
combo_exercicio.grid(row=4, column=0, columnspan=4,
                     padx=5, pady=5, sticky="ew")

# --- Linha 5: Esforço no Trabalho (Combobox) ---
ttk.Label(frame_entrada, text="Esforço físico no trabalho:").grid(
    row=3, column=4, columnspan=5, padx=5, pady=5, sticky="w")
var_trabalho = tk.StringVar(janela)
var_trabalho.set(ESFORCO_TRABALHO[0])
combo_trabalho = ttk.Combobox(frame_entrada, textvariable=var_trabalho,
                              values=ESFORCO_TRABALHO, state="readonly", width=25)
combo_trabalho.grid(row=4, column=4, columnspan=5, padx=5, pady=5, sticky="ew")

# --- Botão de Calcular ---
btn_calcular = ttk.Button(janela, text="Calcular", command=calcular)
btn_calcular.pack(pady=10, padx=10, fill="x")

# --- Área de Resultados ---
frame_resultado = ttk.LabelFrame(janela, text="Resultados Detalhados")
frame_resultado.pack(padx=10, pady=10, fill="both", expand=True)

label_resultado = ttk.Label(
    frame_resultado, text="Preencha os dados e clique em 'Calcular'.", anchor="nw")
label_resultado.pack(padx=10, pady=10, fill="both", expand=True)

# --- Loop Principal da Aplicação ---
janela.mainloop()
