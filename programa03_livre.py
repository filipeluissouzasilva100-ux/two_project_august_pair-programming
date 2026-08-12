import tkinter as tk
from tkinter import messagebox, ttk


class SimuladorFinanceiroB3(tk.Tk):
    # 1. Constantes da Identidade Visual (Inspirada na B3)
    COLOR_AZUL_ESC = "#004d6e"  # Fundo das abas e headers
    COLOR_AZUL_MED = "#0081ab"  # Bordas e detalhes
    COLOR_AZUL_CLA = "#00b1cd"  # Destaque e seleções
    COLOR_VERDE = "#a6c844"     # Entrada / Sucesso
    COLOR_ROSA = "#b83764"      # Saída / Alertas
    COLOR_AMARELO = "#edce01"   # Destaque Cripto / Seleção
    COLOR_ACO = "#4a3336"       # Texto escuro / Fundo principal

    COTAÇÃO_BTC = 300000.00

    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Simulador Financeiro - Padrão B3")
        self.geometry("600x480")
        self.configure(bg=self.COLOR_AZUL_ESC)

        # 2. Gerenciamento de Estado da Aplicação
        self.saldo = 1000.00
        self.cripto_btc = 0.0
        self.historico = ["Saldo inicial depositado: R$ 1000.00"]

        # Configuração de Estilos e Layout
        self._configurar_estilos()
        self._criar_header()
        self._criar_abas()

        # Carrega dados iniciais na interface
        self.atualizar_interface()

    def _configurar_estilos(self):
        """Define os estilos visuais para os componentes TTK."""
        style = ttk.Style()
        style.theme_use("default")
        
        # Estilização do Notebook (Sistema de Abas)
        style.configure("TNotebook", background=self.COLOR_AZUL_ESC)
        style.configure(
            "TNotebook.Tab",
            background=self.COLOR_AZUL_MED,
            foreground="white",
            padding=[12, 6],
            font=("Arial", 10, "bold"),
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", self.COLOR_AMARELO)],
            foreground=[("selected", self.COLOR_ACO)],
        )

    def _criar_header(self):
        """Cria o cabeçalho superior da aplicação."""
        header = tk.Frame(self, bg=self.COLOR_AZUL_ESC, height=50)
        header.pack(fill="x")
        
        lbl_titulo = tk.Label(
            header,
            text="B3 - SIMULADOR EDUCACIONAL",
            font=("Arial", 14, "bold"),
            fg="white",
            bg=self.COLOR_AZUL_ESC,
        )
        lbl_titulo.pack(pady=10)

    def _criar_abas(self):
        """Constrói a estrutura de abas e seções da interface."""
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Criação dos frames das abas
        self.aba_conta = tk.Frame(self.notebook, bg="white")
        self.aba_cripto = tk.Frame(self.notebook, bg="white")
        self.aba_extrato = tk.Frame(self.notebook, bg="white")

        self.notebook.add(self.aba_conta, text="Conta Corrente")
        self.notebook.add(self.aba_cripto, text="Criptoativos")
        self.notebook.add(self.aba_extrato, text="Extrato")

        # Construção dos elementos internos
        self._montar_aba_conta()
        self._montar_aba_cripto()
        self._montar_aba_extrato()

    # --- MONTAGEM DAS ABAS ---

    def _montar_aba_conta(self):
        self.lbl_saldo = tk.Label(
            self.aba_conta,
            text="",
            font=("Arial", 13, "bold"),
            fg=self.COLOR_AZUL_ESC,
            bg="white",
        )
        self.lbl_saldo.pack(pady=20)

        lbl_instrucao = tk.Label(
            self.aba_conta,
            text="Valor da Operação (R$):",
            font=("Arial", 10),
            fg=self.COLOR_ACO,
            bg="white",
        )
        lbl_instrucao.pack()

        self.ent_valor_conta = tk.Entry(
            self.aba_conta,
            font=("Arial", 11),
            relief="solid",
            bd=1,
            highlightbackground=self.COLOR_AZUL_MED,
        )
        self.ent_valor_conta.pack(pady=5)

        btn_frame = tk.Frame(self.aba_conta, bg="white")
        btn_frame.pack(pady=15)

        btn_entrada = tk.Button(
            btn_frame,
            text="Entrada (+)",
            bg=self.COLOR_VERDE,
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            relief="flat",
            command=self.creditar,
        )
        btn_entrada.grid(row=0, column=0, padx=8)

        btn_saida = tk.Button(
            btn_frame,
            text="Saída (-)",
            bg=self.COLOR_ROSA,
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            relief="flat",
            command=self.debitar,
        )
        btn_saida.grid(row=0, column=1, padx=8)

    def _montar_aba_cripto(self):
        lbl_cripto_titulo = tk.Label(
            self.aba_cripto,
            text="Mercado Digital - Bitcoin (Simulado)",
            font=("Arial", 12, "bold"),
            fg=self.COLOR_AZUL_ESC,
            bg="white",
        )
        lbl_cripto_titulo.pack(pady=15)

        lbl_cotacao = tk.Label(
            self.aba_cripto,
            text=f"Cotação Fixa: 1 BTC = R$ {self.COTAÇÃO_BTC:,.2f}",
            font=("Arial", 9, "italic"),
            fg="gray",
            bg="white",
        )
        lbl_cotacao.pack()

        self.lbl_btc = tk.Label(
            self.aba_cripto,
            text="",
            font=("Arial", 11, "bold"),
            fg=self.COLOR_AZUL_MED,
            bg="white",
        )
        self.lbl_btc.pack(pady=15)

        btn_comprar_btc = tk.Button(
            self.aba_cripto,
            text="Comprar R$ 100,00 em BTC",
            bg=self.COLOR_AMARELO,
            fg=self.COLOR_ACO,
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=10,
            pady=5,
            command=self.comprar_btc,
        )
        btn_comprar_btc.pack(pady=10)

    def _montar_aba_extrato(self):
        self.lst_extrato = tk.Listbox(
            self.aba_extrato,
            font=("Consolas", 10),
            fg=self.COLOR_ACO,
            bg="#F9F9F9",
            selectbackground=self.COLOR_AZUL_CLA,
            relief="solid",
            bd=1,
        )
        self.lst_extrato.pack(padx=15, pady=15, fill="both", expand=True)

    # --- REGRAS DE NEGÓCIO E AÇÕES ---

    def creditar(self):
        try:
            valor = float(self.ent_valor_conta.get())
            if valor <= 0:
                messagebox.showwarning("Aviso", "Digite um valor positivo.")
                return

            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f}")
            self.ent_valor_conta.delete(0, tk.END)
            self.atualizar_interface()
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número.")

    def debitar(self):
        try:
            valor = float(self.ent_valor_conta.get())
            if valor <= 0:
                messagebox.showwarning("Aviso", "Digite um valor positivo.")
                return

            if valor <= self.saldo:
                self.saldo -= valor
                self.historico.append(f"Saque/Pagamento: -R$ {valor:.2f}")
                self.ent_valor_conta.delete(0, tk.END)
                self.atualizar_interface()
            else:
                messagebox.showwarning("Erro", "Saldo insuficiente.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Digite um número.")

    def comprar_btc(self):
        custo = 100.00
        if self.saldo >= custo:
            self.saldo -= custo
            qtd = custo / self.COTAÇÃO_BTC
            self.cripto_btc += qtd
            self.historico.append(
                f"Compra Cripto: R$ {custo:.2f} em BTC ({qtd:.6f} BTC)"
            )
            self.atualizar_interface()
        else:
            messagebox.showwarning(
                "Erro", "Saldo insuficiente para comprar R$ 100,00 em BTC."
            )

    # --- ATUALIZAÇÃO DA INTERFACE ---

    def atualizar_interface(self):
        """Atualiza todos os componentes visuais com os dados mais recentes do estado."""
        self.lbl_saldo.config(text=f"Saldo Disponível: R$ {self.saldo:.2f}")
        self.lbl_btc.config(text=f"Seu Saldo BTC: {self.cripto_btc:.6f}")
        
        # Atualiza a caixa do Extrato
        self.lst_extrato.delete(0, tk.END)
        for item in self.historico:
            self.lst_extrato.insert(tk.END, item)


# Ponto de Entrada da Aplicação
if __name__ == "__main__":
    app = SimuladorFinanceiroB3()
    app.mainloop()