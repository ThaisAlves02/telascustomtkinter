import customtkinter as ctk
from PIL import Image

#----------------------------------------------------------
# CONFIGURAÇÕES GERAIS / CORES
#----------------------------------------------------------

ctk.set_appearance_mode('dark')

cor_fundo = '#1e1b2e'
cor_card = '#2a2740'
cor_verde = '#3ecf8e'
cor_texto = '#e6e6e6'
cor_texto_sec = "#9c98b0"

#----------------------------------------------------------
# JANELA PRINCIPAL
#----------------------------------------------------------

janela = ctk.CTk()
janela.title('Seleção de Usuário')
janela.geometry('960x600')
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
card1 = ctk.CTkButton(
    area_card, 
    text='',
    fg_color= cor_card,
    hover_color= '#3a3656',
    corner_radius= 12,
    width= 160,
    height= 180
)
card1.grid(row= 0, column = 0, padx = 12, pady= 12)


# -- CARD 2: ANDRÉ --
card2 = ctk.CTkButton(
    area_card, 
    text='',
    fg_color= cor_card,
    hover_color= '#3a3656',
    corner_radius= 22,
    width= 160,
    height= 180
)
card2.grid(row= 0, column = 1, padx = 12, pady= 12)


# -- CARD 3: OLAVO --
card3 = ctk.CTkButton(
    area_card, 
    text='',
    fg_color= cor_card,
    hover_color= '#3a3656',
    corner_radius= 22,
    width= 160,
    height= 180
)
card3.grid(row= 0, column = 2, padx = 12, pady= 12)


# -- CARD 4 MARIA:  --
card4 = ctk.CTkButton(
    area_card, 
    text='',
    fg_color= cor_card,
    hover_color= '#3a3656',
    corner_radius= 22,
    width= 160,
    height= 180
)
card4.grid(row= 0, column = 3, padx = 12, pady= 12)


# -- CARD 5 BRUNA:  --
card5 = ctk.CTkButton(
    area_card, 
    text='',
    fg_color= cor_card,
    hover_color= '#3a3656',
    corner_radius= 22,
    width= 160,
    height= 180
)
card5.grid(row= 0, column = 4, padx = 12, pady= 12)

nome1 = ctk.CTkLabel(
    card1,
    text = 'Aluno',
    font = ctk.CTkFont(size = 14, weight= 'bold'),
    text_color= cor_texto,
)

nome1.place(x = 57, y = 130)


nome2 = ctk.CTkLabel(
    card2,
    text = 'André',
    font = ctk.CTkFont(size = 14, weight= 'bold'),
    text_color= cor_texto,
)

nome2.place(x = 57, y = 130)

nome3 = ctk.CTkLabel(
    card3,
    text = 'Olavo',
    font = ctk.CTkFont(size = 14, weight= 'bold'),
    text_color= cor_texto,
)

nome3.place(x = 57, y = 130)

nome4 = ctk.CTkLabel(
    card4,
    text = 'Maria',
    font = ctk.CTkFont(size = 14, weight= 'bold'),
    text_color= cor_texto,
)

nome4.place(x = 57, y = 130)

nome5 = ctk.CTkLabel(
    card5,
    text = 'Bruna',
    font = ctk.CTkFont(size = 14, weight= 'bold'),
    text_color= cor_texto,
)

nome5.place(x = 57, y = 130)






janela.mainloop()