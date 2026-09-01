import customtkinter as ctk
from PIL import Image #py -m pip install pillow
import os

#---------------------------------------------------------
#CONFIGURAÇÃO GERAL
#---------------------------------------------------------
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

base_dir = os.path.dirname(os.path.abspath(__file__))
assent_dir = os.path.join(base_dir,'assents')

'''
1. __file__

É uma variável especial do Python que representa
o caminho do arquivo que está sendo executado.

Por exemplo, se seu arquivo estiver em: C:\projeto\main.py. 
Então: __file__, pode representar:C:\projeto\main.py

-------------------------------------------------------------------------------------------------

os.path.abspath(__file__)

Transforma o caminho em um caminho absoluto. Resultado: C:\projeto\main.py

os.path.dirname(...)

Pega somente a pasta, retirando o nome do arquivo. Resultado:C:\projeto
------------------------------------------------------------------------------------------------

'''

cor_fundo = "#1e1b2e"
cor_card = "#2c2942"
cor_input ="#4a4560"
cor_verde = "#3ddc84"
cor_texto_sec = "#e6e6e6"

app = ctk.CTk()
app.title('Login')
app.geometry('1100x650')
app.configure(fg_color=cor_fundo)


#---------------------------------------------------------
#CONFIGURAÇÃO DE IMAGEM
#---------------------------------------------------------

imagem_astronauta = ctk.CTkImage(
    dark_image = Image.open(os.path.join(assent_dir,"astronauta.png")),
    size = (380,375)# 380 px de largura 375 px de altura
)

#---------------------------------------------------------
#FRAM_ESQUERDO TÍTULO + ILUSTRAÇÃO
#---------------------------------------------------------

frame_esquerdo = ctk.CTkFrame(app, fg_color='transparent')
frame_esquerdo.grid(row= 0,column= 0)

titulo1 = ctk.CTkLabel(
    frame_esquerdo,
    text='Faça login',
    font=ctk.CTkFont(size=30,weight='bold'),
    text_color=cor_verde
)

titulo1.pack(anchor='w', padx = 40, pady = (40, 0)) #alinha o obj a esquerda

titulo2 = ctk.CTkLabel(
    frame_esquerdo,
    text='E entre para o nosso time',
    font=ctk.CTkFont(size=30,weight='bold'),
    text_color= cor_texto_sec
)

titulo2.pack(anchor='w', padx = 40)

#---------------------------------------------------------
#LABEL PARA COLOCAR A IMAGEM
#---------------------------------------------------------
label_imagem = ctk.CTkLabel(frame_esquerdo, image = imagem_astronauta, text='')
label_imagem.pack(padx= 50, pady= 80)

#---------------------------------------------------------
#LADO DIREITO - CARD LOGIN
#---------------------------------------------------------
card = ctk.CTkFrame(app, fg_color= cor_card, corner_radius= 20, width= 340, height= 360)
card.grid(row= 0 , column= 1, padx = (160, 0))
card.propagate(False)

label_login = ctk.CTkLabel(
    card, 
    text= 'LOGIN',
    font = ctk.CTkFont(size= 22, weight= 'bold'),
    text_color= cor_texto_sec                      
)
label_login.pack(pady = (25, 15))

label_usuario = ctk.CTkLabel(card, text='Usuário', anchor='w', padx = 30 )
label_usuario.pack(fill = 'x')

entry_usuario = ctk.CTkEntry(
    card,
    placeholder_text='Usuário',
    fg_color= cor_input,
    border_width= 0,
    height= 38
)

entry_usuario.pack(fill = 'x', padx = 30, pady = (5,15))


label_senha = ctk.CTkLabel(
    card, 
    text= 'Senha',
    anchor='w',            
)
label_senha.pack(fill = 'x', padx = 30 )

entry_senha = ctk.CTkEntry(
    card,
    placeholder_text='Senha',
    show = '*',
    fg_color= cor_input,
    border_width= 0,
    height= 38
)

entry_senha.pack(fill = 'x', padx = 30, pady = (5,15))

botao_login = ctk.CTkButton(
    card, 
    text='LOGIN',
    fg_color= cor_verde,
    text_color= '#1e1b2e',
    font= ctk.CTkFont(size = 14, weight='bold'),
    height= 42,
    #command= fazer_login
)

botao_login.pack(fill = 'x', padx = 30)

#---------------------------------------------------------
# FRAME PARA OS BOTÕES INFERIORES (Lado a lado)
#---------------------------------------------------------

frame_botoes_inferiores = ctk.CTkFrame(card, fg_color="transparent")
frame_botoes_inferiores.pack(fill='x', padx= 18, pady=(15, 20))

botao_esqueci_senha = ctk.CTkButton(
    frame_botoes_inferiores,
    text= 'Esqueci minha senha',
    font= ctk.CTkFont(size = 11, underline=True),
    fg_color="transparent",
    hover_color=cor_card,    
    text_color=cor_texto_sec,
    cursor="hand2"
)

botao_esqueci_senha.pack(side='left')


botao_cadastrar = ctk.CTkButton(
    frame_botoes_inferiores,
    text= 'Não tem conta? Cadastre-se',
    font= ctk.CTkFont(size = 11, underline=True),
    fg_color="transparent",
    hover_color=cor_card,  
    text_color=cor_texto_sec,
    cursor="hand2"
)

botao_cadastrar.pack(side='right') 




app.mainloop()