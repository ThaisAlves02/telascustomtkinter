import customtkinter as ctk
from PIL import Image #py -m pip install pillow
import os

app = ctk.CTk()
app.title('Login')
app.geometry('1100x650')

card_direito = "#E9E9E9"

#painel verde a esquerda
verde = ctk.CTkFrame(app, fg_color= '#3cB878', width= 420, corner_radius= 0)
verde.pack(side='left', fill = 'y')
verde.propagate(False)

base_dir = os.path.dirname(os.path.abspath(__file__))
assent_dir = os.path.join(base_dir,'assents')

imagem_foguete = ctk.CTkImage(
    dark_image = Image.open(os.path.join(assent_dir,"foguete.png")),
    size = (220,220)
)

#Cria uma label exclusiva para exibir a imagem
label_imagem = ctk.CTkLabel(verde, text="", image=imagem_foguete)
label_imagem.place(x= 100, y= 300)


titulo1 = ctk.CTkLabel(
    verde,
    text='Junte-se a nós',
    font=ctk.CTkFont(size=25,weight='bold'),
    text_color= '#FFFFFF'
)

titulo1.pack(anchor='w', padx = 35, pady = (40,0))

label_texto1 = ctk.CTkLabel(
    verde,
    text= 'Crie sua conta e comece'
)

label_texto1.place(x = 35, y = 64)


label_texto2 = ctk.CTkLabel(
    verde,
    text= 'sua jornada com o time.'
)

label_texto2.place(x = 35, y = 85)


label_texto3 = ctk.CTkLabel(
    verde,
    font=ctk.CTkFont(size=12,weight='bold'),
    text= 'já tem conta? Entrar',
    text_color= '#FFFFFF'
)

label_texto3.place(x = 35, y = 560)

# LADO DIREITO - CARD CADASTRO

frame_direito = ctk.CTkFrame(app, fg_color="white", )
frame_direito.pack(fill="both", expand=True)

# TÍTULOS:

titulo_direito1 = ctk.CTkLabel(
    frame_direito,
    text="Criar conta",
    font=ctk.CTkFont(size=38, weight="bold"),
    fg_color="white",
    text_color="black"
    
)

titulo_direito1.place(x=105, y=80)

titulo_direito2 = ctk.CTkLabel(
    frame_direito,
    text="Preencha os campos abaixo para começar",
    font=ctk.CTkFont(size=16),
    fg_color="white",
    text_color="gray"
)

titulo_direito2.place(x=108, y=138)


# CAMPOS DE ENTRADA:

label_nome = ctk.CTkLabel(
    frame_direito,
    text="Nome",
    text_color="black",
    fg_color="white",
    font=ctk.CTkFont(size=16) 
)

label_nome.place(x=110, y=217)

entry_nome = ctk.CTkEntry(
    frame_direito,
    placeholder_text="Seu nome",
    border_width=2,
    width=280,
    height=42,
    text_color="gray",
    fg_color="white",
    border_color="gray",
)

entry_nome.place(x=110, y=245)

label_sobrenome = ctk.CTkLabel(
    frame_direito,
    text="Sobrenome",
    text_color="black",
    fg_color="white",
    font=ctk.CTkFont(size=16) 
)

label_sobrenome.place(x=427, y=217)

entry_sobrenome = ctk.CTkEntry(
    frame_direito,
    placeholder_text="Seu sobrenome",
    border_width=2,
    width=280,
    height=42,
    text_color="gray",
    fg_color="white",
    border_color="gray",
)

entry_sobrenome.place(x=425, y=245)


label_email = ctk.CTkLabel(
    frame_direito,
    text="E-mail",
    text_color="black",
    fg_color="white",
    font=ctk.CTkFont(size=16)
)

label_email.place(x=110, y=325)


entry_email = ctk.CTkEntry(
    frame_direito,
    placeholder_text="Seu e-mail",
    border_width=2,
    width=598,
    height=45,
    text_color="gray",
    fg_color="white",
    border_color="gray",
)

entry_email.place(x=110, y=355)


label_senha = ctk.CTkLabel(
    frame_direito,
    text="Senha",
    text_color="black",
    fg_color="white",
    font=ctk.CTkFont(size=16)
)

label_senha.place(x=110, y=435)


entry_senha = ctk.CTkEntry(
    frame_direito,
    placeholder_text="* * * * * * *",
    placeholder_text_color="black",
    border_width=2,
    width=280,
    height=42,
    text_color="black",
    fg_color="white",
    border_color="gray",
)

entry_senha.place(x=110, y=470)


label_confirmar_senha = ctk.CTkLabel(
    frame_direito,
    text="Confirmar senha",
    text_color="black",
    fg_color="white",
    font=ctk.CTkFont(size=16)
)

label_confirmar_senha.place(x=427, y=437)


entry_confirmar_senha = ctk.CTkEntry(
    frame_direito,
    placeholder_text="* * * * * * *",
    placeholder_text_color="black",
    border_width=2,
    width=280,
    height=42,
    text_color="black",
    fg_color="white",
    border_color="gray",
)

entry_confirmar_senha.place(x=427, y=469)


# BOTÃO:

botao_criar_conta = ctk.CTkButton(
    frame_direito,
    text="Criar minha conta",
    fg_color="#3ddc84",
    hover_color="#1e1b2e",
    text_color="white",
    height=45,
    width=560,
    corner_radius=25,
    font=ctk.CTkFont(size=17, weight="bold")
)

botao_criar_conta.place(x=120, y=570)



app.mainloop()