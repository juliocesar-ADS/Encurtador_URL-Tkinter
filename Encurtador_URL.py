import tkinter as tk
import definicoes

janela = tk.Tk()
janela.title("Encurtador de URL")


entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(padx=10, pady=8)


resultado_label = tk.Label(janela, text="")
resultado_label.pack()

botao = tk.Button(
    janela,
    text="Encurtar",
    command=lambda: definicoes.encurtar(entrada_url, resultado_label)
)
botao.pack(pady=4)

botao_copiar = tk.Button(
    janela,
    text="Copiar",
    command=lambda: definicoes.copiar_link(janela, resultado_label)
)
botao_copiar.pack(pady=1)

janela.mainloop()