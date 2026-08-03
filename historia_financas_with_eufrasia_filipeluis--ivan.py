import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

COLOR_AZUL = "#22AED1"
COLOR_VERDE_CLARO = "#00FF00"
COLOR_ROXO_ESCURO = "#800080"
COLOR_LARANJA = "#FFA500"
COLOR_ROSA_ESCURO = "#FF1493"
COLOR_AMARELO = "#FFFF00"
COLOR_MARROM_ESCURO = "#8B4513"

# 1. Função que exibe a mensagem do evento
def mostrar_fato(detalhe):
    #messagebox.showinfo("Fato Histórico", detalhe)
    messagebox.showinfo("Curiosidade Eufrasia", detalhe)


# 2. Configuracão da janela principal
janela = tk.Tk()
janela.title("Curiosidades Eufrasia Teixeira Leite")
#janela.geometry("500x500") # Ajustado o tamanho da tela
janela.geometry("500x580") # Ajusatado o tamanho da tela
janela.configure(bg="#f4f4f9")

