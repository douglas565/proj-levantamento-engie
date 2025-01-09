import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook

def salvar_dados():
    # Obtendo os valores dos campos
    id_raag = entry_id_raag.get()
    via = entry_via.get()
    classificacao = entry_classificacao.get()
    distribuicao = entry_distribuicao.get()
    largura_passeio_adj = entry_largura_passeio_adj.get()
    largura_passeio_opo = entry_largura_passeio_opo.get()
    largura_gramado_adj = entry_largura_gramado_adj.get()
    largura_gramado_opo = entry_largura_gramado_opo.get()
    largura_estac_adj = entry_largura_estac_adj.get()
    largura_estac_opo = entry_largura_estac_opo.get()
    largura_pista1 = entry_largura_pista1.get()
    largura_canteiro_central = entry_largura_canteiro_central.get()
    largura_pista2 = entry_largura_pista2.get()
    ciclovia = entry_ciclovia.get()
    distancia_postes = entry_distancia_postes.get()
    altura = entry_altura.get()
    projecao = entry_projecao.get()
    interferencia_arborea = entry_interferencia_arborea.get()

    # Carregar a planilha
    caminho_planilha = 'C:\\Users\\dougl\\OneDrive\\Área de Trabalho\\Monitoramento_mercado-main\\Lev  PPP Curitiba - Douglas2.xlsm'
    workbook = load_workbook(caminho_planilha, keep_vba=True)
    sheet = workbook['Levantamento']

    # Encontrar a próxima linha vazia
    prox_linha = sheet.max_row + 1

    # Preencher os dados na planilha
    sheet[f"A{prox_linha}"] = id_raag
    sheet[f"B{prox_linha}"] = via
    sheet[f"C{prox_linha}"] = classificacao
    sheet[f"D{prox_linha}"] = distribuicao
    sheet[f"E{prox_linha}"] = largura_passeio_adj
    sheet[f"F{prox_linha}"] = largura_passeio_opo
    sheet[f"G{prox_linha}"] = largura_gramado_adj
    sheet[f"H{prox_linha}"] = largura_gramado_opo
    sheet[f"I{prox_linha}"] = largura_estac_adj
    sheet[f"J{prox_linha}"] = largura_estac_opo
    sheet[f"K{prox_linha}"] = largura_pista1
    sheet[f"L{prox_linha}"] = largura_canteiro_central
    sheet[f"M{prox_linha}"] = largura_pista2
    sheet[f"N{prox_linha}"] = ciclovia
    sheet[f"O{prox_linha}"] = distancia_postes
    sheet[f"P{prox_linha}"] = altura
    sheet[f"Q{prox_linha}"] = projecao
    sheet[f"R{prox_linha}"] = interferencia_arborea

    # Salvar a planilha
    workbook.save(caminho_planilha)

    # Mensagem de confirmação
    tk.messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

# Criar a interface gráfica
root = tk.Tk()
root.title("Preencher Dados na Planilha")

# Campos do formulário
fields = [
    ("ID RAAG", "entry_id_raag"),
    ("Via", "entry_via"),
    ("Classificação", "entry_classificacao"),
    ("Distribuição", "entry_distribuicao"),
    ("Largura do Passeio Adjacente", "entry_largura_passeio_adj"),
    ("Largura do Passeio Oposto", "entry_largura_passeio_opo"),
    ("Largura do Gramado Adjacente", "entry_largura_gramado_adj"),
    ("Largura do Gramado Oposto", "entry_largura_gramado_opo"),
    ("Largura do Estacionamento Adjacente", "entry_largura_estac_adj"),
    ("Largura do Estacionamento Oposto", "entry_largura_estac_opo"),
    ("Largura da Pista 1", "entry_largura_pista1"),
    ("Largura do Canteiro Central", "entry_largura_canteiro_central"),
    ("Largura da Pista 2", "entry_largura_pista2"),
    ("Ciclovia", "entry_ciclovia"),
    ("Distância entre Postes", "entry_distancia_postes"),
    ("Altura", "entry_altura"),
    ("Projeção", "entry_projecao"),
    ("Interferência Arbórea", "entry_interferencia_arborea"),
]

# Criar os widgets
entries = {}
for idx, (label_text, entry_var) in enumerate(fields):
    label = ttk.Label(root, text=label_text)
    label.grid(row=idx, column=0, padx=5, pady=5, sticky=tk.W)
    entry = ttk.Entry(root)
    entry.grid(row=idx, column=1, padx=5, pady=5, sticky=tk.E)
    entries[entry_var] = entry

# Associar os widgets às variáveis globais
globals().update(entries)

# Botão para salvar os dados
button_salvar = ttk.Button(root, text="Salvar Dados", command=salvar_dados)
button_salvar.grid(row=len(fields), column=0, columnspan=2, pady=10)

root.mainloop()
