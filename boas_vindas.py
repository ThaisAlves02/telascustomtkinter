import customtkinter as ctk
from PIL import Image

#----------------------------------------------------------
# CONFIGURAÇÕES GERAIS / CORES
#----------------------------------------------------------

ctk.set_appearance_mode('dark')

cor_fundo = '#1e1b2e',
cor_card = '#2a2740',
cor_verde = '#3ecf8e',
cor_texto = '#e6e6e6',
cor_texto_sec = "#9c98b0"

#----------------------------------------------------------
# JANELA PRINCIPAL
#----------------------------------------------------------

janela = ctk.CTk()
janela.title('Seleção de Usuário')
janela.geometry('900x600')
janela.configure(fg_color = cor_fundo)
janela.resizable(False, False)


#----------------------------------------------------------
# TITULO
#----------------------------------------------------------

titulo = ctk.CTkLabel(
    janela,
    text="Quem está usando o sistema?",
    font= ctk.CTkFont(size = 26, weight='bold'),
    text_color= cor_verde
)

titulo.pack(pady=(60, 10))

#----------------------------------------------------------
# SUBTITULO
#----------------------------------------------------------

subtitulo = ctk.CTkLabel(
    janela,
    text="Selecione seu usuário para continuar, ou cadastre um novo.",
    font= ctk.CTkFont(size = 13),
    text_color= cor_texto_sec
)

subtitulo.pack(pady=(0, 40))

#----------------------------------------------------------
# ÁREA DOS CARDS
#----------------------------------------------------------

area_card = ctk.CTkFrame(janela, fg_color= cor_fundo)
area_card.pack()

# -- CARD 1: ALUNO --







janela.mainloop()