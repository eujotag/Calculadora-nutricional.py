# Calculadora Nutricional e de Macros em Python

Este projeto é uma calculadora nutricional completa desenvolvida em **Python** com uma Interface Gráfica de Usuário (GUI) usando a biblioteca **Tkinter**.

O objetivo é fornecer ao usuário uma estimativa precisa de seu gasto calórico diário e uma sugestão de distribuição de Macronutrientes (Proteína, Gordura e Carboidrato) com base em seus objetivos (Bulking, Cutting ou Manutenção).

## Funcionalidades Principais

* **Cálculo do IMC:** Calcula e classifica o Índice de Massa Corporal.
* **Cálculo da TMB:** Estima a Taxa Metabólica Basal (calorias gastas em repouso) usando a fórmula de **Mifflin-St Jeor**.
* **Cálculo do GCT Preciso:** Estima o Gasto Calórico Total (GCT) combinando dois fatores detalhados para maior precisão:
    1.  **Esforço Físico no Trabalho.**
    2.  **Horas de Exercício Semanal.**
* **Sugestão de Macros:** Ajusta as calorias totais de acordo com o objetivo (`+500 kcal` para Bulking, `-500 kcal` para Cutting) e sugere a divisão ideal de Proteína, Gordura e Carboidrato.

## Estrutura do Projeto

O projeto é modularizado para maior clareza e manutenção:

1.  **`calculos.py`:** Contém toda a lógica de negócio (fórmulas matemáticas, matriz de fatores, funções de cálculo).
2.  **`app_gui.py`:** Responsável pela Interface Gráfica (Tkinter), coleta de dados do usuário e exibição dos resultados.

## Como Executar

Para rodar a calculadora em sua máquina, siga os passos abaixo:

### Pré-requisitos
* Python 3.x instalado.
* O Tkinter é nativo, portanto, nenhuma instalação adicional é necessária (a menos que sua distribuição Linux o exija).

### Passos
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/eujotag/Calculadora-nutricional.py.git]
    cd calculadora-nutricional-python
    ```
2.  **Execute o arquivo principal:**
    ```bash
    python app_gui.py
    # OU
    py app_gui.py
    ```

## Interface Gráfica

A interface permite a inserção de dados como Peso, Altura, Idade e a seleção do Nível de Atividade e Objetivo via menus e botões de rádio para uma experiência de usuário simples e controlada.