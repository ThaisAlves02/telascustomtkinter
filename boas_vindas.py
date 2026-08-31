import customtkinter as ctk
from PIL import Image
import os

#----------------------------------------------------------
# CONFIGURAÇÕES GERAIS / CORES
#----------------------------------------------------------

ctk.set_appearance_mode('dark')

cor_fundo = '#1e1b2e'
cor_card = '#2a2740'
cor_verde = '#3ecf8e'
cor_texto = '#e6e6e6'
cor_texto_sec = "#9c98b0"
cor_card_hover = '#3d3957'

#----------------------------------------------------------
# CONFIGURAÇÕES DE IMAGEM
#----------------------------------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
assent_dir = os.path.join(base_dir,'assents')

#----------------------------------------------------------
# ABRIR IMAGEM
#----------------------------------------------------------
imagem_icone = ctk.CTkImage(
    Image.open(os.path.join(assent_dir,"icon_usuario.png")),
    size = (90,90)
)

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

#----------------------------------------------------------
# FUNÇÃO PARA ADICIONAR EFEITOS
#----------------------------------------------------------

def configurar_interacao(frame, componentes, nome_usuario):
    """
    Esta função funciona como um 'molde' para dar vida aos cards.
    Ela recebe o frame do card, a lista de itens que estão dentro dele
    (como imagem e texto) e o nome do usuário correspondente.
    """
    
    def ao_clicar(event):
        # O parâmetro 'event' registra o clique do mouse
        print(f"Usuário selecionado: {nome_usuario}")

    # O que acontece quando o ponteiro do mouse ENTRA no card
    def ao_entrar(event):
        # Altera a cor de fundo do frame para uma cor mais clara (efeito hover)
        frame.configure(fg_color=cor_card_hover)

    # O que acontece quando o ponteiro do mouse SAI do card
    def ao_sair(event):
        # Restaura a cor de fundo original do frame
        frame.configure(fg_color=cor_card)

    # Isso garante que o efeito funcione mesmo se o mouse estiver em cima do texto ou da foto.
    for elemento in [frame] + componentes:
        
        # 1. Muda a seta do mouse para o ícone de 'mãozinha' de clique
        elemento.configure(cursor="hand2") 
        
        # 2. Vincula o movimento de ENTRADA do mouse à função 'ao_entrar'
        elemento.bind("<Enter>", ao_entrar)   
        
        # 3. Vincula o movimento de SAÍDA do mouse à função 'ao_sair'
        elemento.bind("<Leave>", ao_sair)     
        
        # 4. Vincula o CLIQUE com o botão esquerdo do mouse à função 'ao_clicar'
        elemento.bind("<Button-1>", ao_clicar) 


# -- CARD 1: ALUNO --
card1 = ctk.CTkFrame(
    area_card, 
    fg_color= cor_card,
    corner_radius= 12,
    width= 160,
    height= 180
)
card1.grid(row= 0, column = 0, padx = 12, pady= 12)

imagem01 = ctk.CTkLabel(card1, text="", image=imagem_icone)
imagem01.place(relx=0.225, rely=0.083)

texto01 = ctk.CTkLabel(card1, text="ALUNO", font=ctk.CTkFont(size=14, weight='bold'), text_color=cor_texto)
texto01.place(relx=0.5, rely=0.75, anchor="center")

configurar_interacao(card1, [imagem01, texto01], "ALUNO")

# -- CARD 2: ANDRÉ --
card2 = ctk.CTkFrame(
    area_card, 
    fg_color= cor_card,
    corner_radius= 22,
    width= 160,
    height= 180
)
card2.grid(row= 0, column = 1, padx = 12, pady= 12)

imagem02 = ctk.CTkLabel(card2, text="", image=imagem_icone)
imagem02.place(relx=0.225, rely=0.083)

texto02 = ctk.CTkLabel(card2, text="ANDRÉ", font=ctk.CTkFont(size=14, weight='bold'), text_color=cor_texto)
texto02.place(relx=0.5, rely=0.75, anchor="center")

configurar_interacao(card2, [imagem02, texto02], "ANDRÉ")

# -- CARD 3: OLAVO --
card3 = ctk.CTkFrame(
    area_card, 
    fg_color= cor_card,
    corner_radius= 22,
    width= 160,
    height= 180
)
card3.grid(row= 0, column = 2, padx = 12, pady= 12)

imagem03 = ctk.CTkLabel(card3, text="", image=imagem_icone)
imagem03.place(relx=0.225, rely=0.083)

texto03 = ctk.CTkLabel(card3, text="OLAVO", font=ctk.CTkFont(size=14, weight='bold'), text_color=cor_texto)
texto03.place(relx=0.5, rely=0.75, anchor="center")

configurar_interacao(card3, [imagem03, texto03], "OLAVO")

# -- CARD 4 MARIA:  --
card4 = ctk.CTkFrame(
    area_card, 
    fg_color= cor_card,
    corner_radius= 22,
    width= 160,
    height= 180
)
card4.grid(row= 0, column = 3, padx = 12, pady= 12)

imagem04 = ctk.CTkLabel(card4, text="", image=imagem_icone)
imagem04.place(relx=0.225, rely=0.083)

texto04 = ctk.CTkLabel(card4, text="MARIA", font=ctk.CTkFont(size=14, weight='bold'), text_color=cor_texto)
texto04.place(relx=0.5, rely=0.75, anchor="center")

configurar_interacao(card4, [imagem04, texto04], "MARIA")

# -- CARD 5 BRUNA:  --
card5 = ctk.CTkFrame(
    area_card, 
    fg_color= cor_card,
    corner_radius= 22,
    width= 160,
    height= 180
)
card5.grid(row= 0, column = 4, padx = 12, pady= 12)

imagem05 = ctk.CTkLabel(card5, text="", image=imagem_icone)
imagem05.place(relx=0.225, rely=0.083)

texto05 = ctk.CTkLabel(card5, text="BRUNA", font=ctk.CTkFont(size=14, weight='bold'), text_color=cor_texto)
texto05.place(relx=0.5, rely=0.75, anchor="center")

configurar_interacao(card5, [imagem05, texto05], "BRUNA")




janela.mainloop()