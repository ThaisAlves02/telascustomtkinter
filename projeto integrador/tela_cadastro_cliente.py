import customtkinter as ctk

#----------------------------------------------------------
# CONFIGURAÇÃO DE COR
#----------------------------------------------------------
cor_fundo = "#E9E9E9"
cor_frame = "#f8f9fa"
borda_frame = "#e0e0e0"

app = ctk.CTk()
app.title('Cadastro')
app.geometry('700x550')
app.configure(fg_color = cor_fundo)
# Centraliza o container principal na tela
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)


frame_cadastro = ctk.CTkFrame(
    app, width=300,
    height=350,
    fg_color= cor_frame,
    border_width=1,
    border_color= borda_frame
    )
frame_cadastro.grid(row = 0, column = 0, sticky="")







app.mainloop()