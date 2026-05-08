import pyshorteners

def encurtar(entrada_url, resultado_label):
    link_digitado = entrada_url.get()

    if not link_digitado:
        resultado_label.config(text="Erro: Digite uma URL primeiro!", fg="red")
        return

    s = pyshorteners.Shortener()
    link_curto = s.tinyurl.short(link_digitado)


    resultado_label.config(text=f"Link encurtado: {link_curto}")


def copiar_link(janela, resultado_label):

    texto = resultado_label.cget("text")

    link = texto.replace("Link encurtado: ", "")

    print(link)

    janela.clipboard_clear()

    janela.clipboard_append(link)

    janela.update()