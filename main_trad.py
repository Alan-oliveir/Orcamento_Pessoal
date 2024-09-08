from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

################# Colors ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # - Profit
co6 = "#038cfc"  # Azul
co7 = "#3fbfb9"  # Verde
co8 = "#263238"  # + Verde
co9 = "#e9edf5"  # + Verde
colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

################# Creating window ###############
window = Tk()
window.title("")
window.geometry('900x650')
window.configure(background=co9)

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9))  # Modify the font of the body

################# Frames ####################
frame_top = Frame(window, width=1043, height=50, bg=co1, relief="flat")
frame_top.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

frame_center = Frame(window, width=1043, height=361, bg=co1, pady=20, relief="raised")
frame_center.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_bottom = Frame(window, width=1043, height=300, bg=co1, relief="flat")
frame_bottom.grid(row=2, column=0, padx=10, pady=0, sticky=NSEW)

frame_gra_2 = Frame(frame_center, width=580, height=250, bg=co2)
frame_gra_2.place(x=415, y=5)

# Abrindo imagem
app_img = Image.open('/images/icons/icon-budget.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_top, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief=RAISED,
                 anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


# Percentagem ------------------------------------

def percentagem():
    l_nome = Label(frame_center, text="Porcentagem da receita gasta", height=1, anchor=NW, font=('Verdana 12 '), bg=co1,
                   fg=co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frame_center, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50
    print(valor)
    l_percentagem = Label(frame_center, text='{:,.2f} %'.format(valor), height=1, anchor=NW, font=('Verdana 12 '), bg=co1,
                          fg=co4)
    l_percentagem.place(x=200, y=35)


percentagem()


# Função para gráfico de barras ------------------------

def grafico_bar():
    # Obtendo valores de meses
    lista_meses = ['Renda', 'Despesa', 'Saldo']
    lista_valores = [345, 225, 534]

    # Crie a figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)

    ax.bar(lista_meses, lista_valores, color=colors, width=0.9)

    # Crie uma lista para coletar os dados de plt.patches
    c = 0

    # Defina rótulos individuais de barra usando a lista acima
    for i in ax.patches:
        ax.text(i.get_x() - .001, i.get_height() + .5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom',
                color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_meses, fontsize=16)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canvas = FigureCanvasTkAgg(figura, frame_center)
    canvas.get_tk_widget().place(x=10, y=70)


grafico_bar()


# -----------------------------------------------------------------------------------------
# Função para resumo total
def resumo():
    valor = [345, 225, 534]

    l_linha = Label(frame_center, text="", width=215, height=1, anchor=NW, font=('arial 1 '), bg='#545454', )
    l_linha.place(x=309, y=52)
    l_sumario = Label(frame_center, text="Total Renda Mensal      ".upper(), height=1, anchor=NW, font=('Verdana 12'),
                      bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=35)
    l_sumario = Label(frame_center, text='R$ {:,.2f}'.format(valor[0]), height=1, anchor=NW, font=('arial 17 '), bg=co1,
                      fg='#545454')
    l_sumario.place(x=306, y=70)

    l_linha = Label(frame_center, text="", width=215, height=1, anchor=NW, font=('arial 1 '), bg='#545454', )
    l_linha.place(x=309, y=132)
    l_sumario = Label(frame_center, text="Total Despesas Mensais".upper(), height=1, anchor=NW, font=('Verdana 12'),
                      bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=115)
    l_sumario = Label(frame_center, text='R$ {:,.2f}'.format(valor[1]), height=1, anchor=NW, font=('arial 17 '), bg=co1,
                      fg='#545454')
    l_sumario.place(x=306, y=150)

    l_linha = Label(frame_center, text="", width=215, height=1, anchor=NW, font=('arial 1 '), bg='#545454', )
    l_linha.place(x=309, y=207)
    l_sumario = Label(frame_center, text="Total Saldo da Caixa    ".upper(), height=1, anchor=NW, font=('Verdana 12'),
                      bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=190)
    l_sumario = Label(frame_center, text='R$ {:,.2f}'.format(valor[2]), height=1, anchor=NW, font=('arial 17 '), bg=co1,
                      fg='#545454')
    l_sumario.place(x=306, y=220)


resumo()


# ----------------------------------------------------------------------------------------

# Função para gráfico de pizza
def grafico_pie():
    # Crie a figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # Exploda as fatias
    explode = [0.05 for _ in lista_categorias]
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors, shadow=True,
           startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canvas_categoria = FigureCanvasTkAgg(figura, frame_gra_2)
    canvas_categoria.get_tk_widget().grid(row=0, column=0)


grafico_pie()

window.mainloop()
