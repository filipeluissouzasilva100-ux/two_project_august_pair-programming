import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "tarefas.json"

# Definição das cores dos temas
TEMAS = {
    "claro": {
        "bg_janela": "#17B2D9",
        "fg_texto": "#333333",
        "bg_entrada": "#ffffff",
        "fg_entrada": "#000000",
        "bg_lista": "#ffffff",
        "fg_lista": "#000000",
        "btn_tema_txt": "🌙 Modo Escuro"
    },
    "escuro": {
        "bg_janela": "#02497f",
        "fg_texto": "#ffffff",
        "bg_entrada": "#2d2d2d",
        "fg_entrada": "#ffffff",
        "bg_lista": "#2d2d2d",
        "fg_lista": "#ffffff",
        "btn_tema_txt": "☀️ Modo Claro"
    }
}

tema_atual = "claro"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            tarefas = json.load(f)
            for t in tarefas:
                lista_box.insert(tk.END, t)

def salvar_tarefas():
    tarefas = lista_box.get(0, tk.END)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(list(tarefas), f, ensure_ascii=False, indent=4)

def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        lista_box.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa válida!")

def remover_tarefa():
    try:
        selecionado = lista_box.curselection()[0]
        lista_box.delete(selecionado)
        salvar_tarefas()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

def alternar_tema():
    global tema_atual
    tema_atual = "escuro" if tema_atual == "claro" else "claro"
    cores = TEMAS[tema_atual]

    # Atualiza as cores dos componentes na tela
    janela.configure(bg=cores["bg_janela"])
    titulo.configure(bg=cores["bg_janela"], fg=cores["fg_texto"])
    entrada_tarefa.configure(bg=cores["bg_entrada"], fg=cores["fg_entrada"], insertbackground=cores["fg_entrada"])
    lista_box.configure(bg=cores["bg_lista"], fg=cores["fg_lista"])
    btn_tema.configure(text=cores["btn_tema_txt"])

# Janela Principal
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("350x500")
janela.configure(bg=TEMAS["claro"]["bg_janela"])

# Botão de alternar tema (no topo)
btn_tema = tk.Button(janela, text="🌙 Modo Escuro", command=alternar_tema)
btn_tema.pack(anchor="ne", padx=10, pady=5)

# Título
titulo = tk.Label(janela, text="Minhas Tarefas", font=("Arial", 16, "bold"), bg=TEMAS["claro"]["bg_janela"], fg=TEMAS["claro"]["fg_texto"])
titulo.pack(pady=5)

# Campo de Entrada
entrada_tarefa = tk.Entry(janela, font=("Arial", 12), width=25)
entrada_tarefa.pack(pady=5)

# Botão Adicionar
btn_add = tk.Button(janela, text="Adicionar Tarefa", bg="#28a745", fg="white", width=20, font=("Arial", 10, "bold"), command=adicionar_tarefa)
btn_add.pack(pady=5)

# Lista de Tarefas
lista_box = tk.Listbox(janela, font=("Arial", 11), width=30, height=12)
lista_box.pack(pady=10)

# Botão Remover
btn_remove = tk.Button(janela, text="Concluir / Remover", bg="#dc3545", fg="white", width=20, font=("Arial", 10, "bold"), command=remover_tarefa)
btn_remove.pack(pady=5)

# Carrega os dados salvos
carregar_tarefas()

janela.mainloop()