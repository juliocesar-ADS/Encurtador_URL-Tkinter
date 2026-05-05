import tkinter as tk
import definicoes

janela = tk.Tk()
janela.title("Encurtador de URL")

entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(padx=10, pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

botao = tk.Button(
    janela,
    text="Encurtar",
    command=lambda: definicoes.encurtar(entrada_url, resultado_label)
)
botao.pack()


janela.mainloop()