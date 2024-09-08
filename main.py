# ==========================
# Tkinter
# ==========================
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar

# ==========================
# Matplotlib
# ==========================
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ==========================
# Pillow
# ==========================
from PIL import Image, ImageTk

# ==========================
# Tkcalendar
# ==========================
from tkcalendar import DateEntry

# ==========================
# Import functions from view
# ==========================
from view import (bar_valores, pie_valores, inserir_categoria, ver_categorias,
                  inserir_receita, inserir_gastos, tabela, deletar_gastos,
                  deletar_receitas, percentagem_valor)

# Defining tree as global
global tree

# ==========================
# Colors
# ==========================
co0 = "#2e2d2b"  # Black
co1 = "#feffff"  # White
co2 = "#4fa882"  # Green
co3 = "#38576b"  # Value
co4 = "#403d3d"  # Text
co5 = "#e06636"  # Negative profit
co6 = "#038cfc"  # Blue
co7 = "#3fbfb9"  # Green
co8 = "#263238"  # Positive green
co9 = "#e9edf5"  # Positive green
colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

# ==========================
# Creating window
# ==========================
janela = Tk()
janela.title("")
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9))  # Modify the font of the body

# ==========================
# Frames
# ==========================
frameTop = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameTop.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

frameCenter = Frame(janela, width=1043, height=361, bg=co1, pady=20, relief="raised")
frameCenter.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frameBottom = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBottom.grid(row=2, column=0, padx=10, pady=0, sticky=NSEW)

frame_right = Frame(frameCenter, width=580, height=250, bg=co2)
frame_right.place(x=415, y=5)

# ==========================
# Logo
# ==========================
app_img = Image.open("images/icons/icon-budget.png")
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameTop, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief=RAISED,
                 anchor=NW, font='Verdana 20 bold', bg=co1, fg=co4)

app_logo.place(x=0, y=0)


# ==============================
# Function to insert categories
# ==============================
def inserir_categoria_main():
    nome = e_n_categoria.get()

    lista_inserir = [nome]

    for item in lista_inserir:
        if item == '':
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
    # Passing the list to the insert function in the view
    inserir_categoria(lista_inserir)

    messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso!")

    e_n_categoria.delete(0, END)

    # Fetching category values
    categorias_funcao = ver_categorias()
    categoria = []

    for item in categorias_funcao:
        categoria.append(item[1])

    # Updating the category list
    combo_categoria_despesas['values'] = categoria


# ==============================
# Function to insert income
# ==============================
def inserir_receitas_main():
    nome = 'Receitas'
    data = e_cal_receitas.get()
    quantia = e_valor_receitas.get()

    lista_inserir = [nome, data, quantia]

    for item in lista_inserir:
        if item == '':
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

    # Call insert function in the view
    inserir_receita(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

    e_cal_receitas.delete(0, END)
    e_valor_receitas.delete(0, END)

    # Updating data
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()


# ==============================
# Function to insert expenses
# ==============================
def inserir_gastos_main():
    nome = combo_categoria_despesas.get()
    data = e_cal_despesas.get()
    quantia = e_valor_despesas.get()

    lista_inserir = [nome, data, quantia]

    for item in lista_inserir:
        if item == '':
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

    # Call insert function in the view
    inserir_gastos(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

    combo_categoria_despesas.delete(0, END)
    e_cal_despesas.delete(0, END)
    e_valor_despesas.delete(0, END)

    # Updating data
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()


# ==============================
# function to delete data
# ==============================
def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicinario = tree.item(treev_dados)
        treev_lista = treev_dicinario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]

        if nome == 'Receitas':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

            # Updating data
            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

            # Updating data
            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

    except IndexError:
        messagebox.showerror("Erro", "Selecione um dos dados da tabela!")


# ===============================
# Function that show percent data
# ===============================
def percentagem():
    l_nome = Label(frameCenter, text="Porcentagem da receita restante", height=1, anchor=NW, font=('Verdana 12 '),
                   bg=co1, fg=co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameCenter, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = percentagem_valor()[0]

    valor = percentagem_valor()[0]
    print(valor)
    l_percentagem = Label(frameCenter, text='{:,.2f} %'.format(valor), height=1, anchor=NW, font=('Verdana 12 '),
                          bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)


percentagem()


# ==============================
# Function for bar chart
# ==============================
def grafico_bar():
    # Obtaining month values
    lista_meses = ['Renda', 'Despesa', 'Saldo']
    lista_valores = bar_valores()

    # Create figure and assign axis objects
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.bar(lista_meses, lista_valores, color=colors, width=0.9)

    # Create a list to collect the plt.patches data
    c = 0

    # Set individual bar labels using the above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
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

    canva = FigureCanvasTkAgg(figura, frameCenter)
    canva.get_tk_widget().place(x=10, y=70)


grafico_bar()


# ==============================
# Function for total summary
# ==============================
def resumo():
    valor = bar_valores()

    l_linha = Label(frameCenter, text="", width=215, height=1, anchor=NW, font=('arial 1'), bg='#545454')
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameCenter, text="Total Renda Mensal      ".upper(), height=1, anchor=NW, font=('Verdana 12'),
                      bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=35)
    l_sumario = Label(frameCenter, text='R$ {:,.2f}'.format(valor[0]), height=1, anchor=NW, font=('arial 17 '), bg=co1,
                      fg='#545454')
    l_sumario.place(x=306, y=70)

    l_linha = Label(frameCenter, text="", width=215, height=1, anchor=NW, font=('arial 1'), bg='#545454')
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameCenter, text="Total Despesas Mensais".upper(), height=1, anchor=NW, font=('Verdana 12'),
                      bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=115)
    l_sumario = Label(frameCenter, text='R$ {:,.2f}'.format(valor[1]), height=1, anchor=NW, font=('arial 17 '), bg=co1,
                      fg='#545454')
    l_sumario.place(x=306, y=150)

    l_linha = Label(frameCenter, text="", width=215, height=1, anchor=NW, font=('arial 1 '), bg='#545454')
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameCenter, text="Total Saldo da Caixa    ".upper(), height=1, anchor=NW, font=('Verdana 12'),
                      bg=co1, fg='#83a9e6')
    l_sumario.place(x=306, y=190)
    l_sumario = Label(frameCenter, text='R$ {:,.2f}'.format(valor[2]), height=1, anchor=NW, font=('arial 17 '), bg=co1,
                      fg='#545454')
    l_sumario.place(x=306, y=220)


resumo()


# ==============================
# Function for pie chart
# ==============================
def grafico_pie():
    # Create figure and assign axis objects
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]

    # Only "explode" the 2nd slice (i.e. 'Hogs')
    explode = [0.05 for _ in lista_categorias]
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors, shadow=True,
           startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_right)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


grafico_pie()

# ==============================
# Creating frames for tables
# ==============================
frame_renda = Frame(frameBottom, width=300, height=250, bg=co1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBottom, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_configuracao = Frame(frameBottom, width=220, height=250, bg=co1)
frame_configuracao.grid(row=0, column=2, padx=5)

# ==============================
# Monthly income table
# ==============================
l_income = Label(frameCenter, text="Tabela Receitas e Despesas", height=1, anchor=NW, font='Verdana 12', bg=co1,
                 fg=co4)
l_income.place(x=5, y=309)


# ==============================
# Function to show income
# ==============================
def mostrar_renda():
    # Creating a treeview with dual scrollbars
    tabela_head = ['#Id', 'Categoria', 'Data', 'Quantia']
    lista_itens = tabela()
    global tree
    tree = ttk.Treeview(frame_renda, selectmode="extended", columns=tabela_head, show="headings")

    # Vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    # tree setting and positing
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    hd = ["center", "center", "center", "center"]
    h = [30, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


mostrar_renda()

# ==============================
# Expense settings
# ==============================
l_descricao = Label(frame_operacoes, text="Insira novas despesas", height=1, anchor=NW, relief="flat",
                    font='Verdana 10 bold', bg=co1, fg=co4)
l_descricao.place(x=10, y=10)

l_descricao = Label(frame_operacoes, text="Categoria", height=1, anchor=NW, relief="flat", font='Ivy 10', bg=co1,
                    fg=co4)
l_descricao.place(x=10, y=40)

# Getting categories
categorias_funcao = ver_categorias()
categorias = [i[1] for i in categorias_funcao]

combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10, font=('Ivy 10'))
combo_categoria_despesas['values'] = categorias
combo_categoria_despesas.place(x=110, y=41)

l_cal_despesas = Label(frame_operacoes, text="Data", height=1, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_cal_despesas.place(x=10, y=70)

e_cal_despesas = DateEntry(frame_operacoes, width=12, background='darkblue', foreground='white', borderwidth=2,
                           year=2020)
e_cal_despesas.place(x=110, y=71)

l_valor_despesas = Label(frame_operacoes, text="Quantia Total", height=1, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes, width=14, justify='left', relief=SOLID)
e_valor_despesas.place(x=110, y=101)

# Insert button
img_add_despesas = Image.open("images/icons/icon-add.png")
img_add_despesas = img_add_despesas.resize((17, 17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes, command=inserir_gastos_main, image=img_add_despesas, compound=LEFT,
                                anchor=NW, text=" Add".upper(), width=80, overrelief=RIDGE, font='Ivy 7 bold',
                                bg=co1, fg=co0)
botao_inserir_despesas.place(x=110, y=131)

# ==============================
# Delete operation
# ==============================
l_n_categoria = Label(frame_operacoes, text="Delete action", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4)
l_n_categoria.place(x=10, y=190)

# Delete Button
img_delete = Image.open("images/icons/icon-delete.png")
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frame_operacoes, command=deletar_dados, image=img_delete, compound=LEFT, anchor=NW,
                       text="   Delete".upper(), width=80, overrelief=RIDGE, font='Ivy 7 bold', bg=co1, fg=co0)
botao_deletar.place(x=110, y=190)

# ==============================
# Income settings
# ==============================
l_descricao = Label(frame_configuracao, text="Enter new income", height=1, anchor=NW, relief="flat",
                    font='Verdana 10 bold', bg=co1, fg=co4)
l_descricao.place(x=10, y=10)

l_cal_receitas = Label(frame_configuracao, text="Date", height=1, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_cal_receitas.place(x=10, y=40)
e_cal_receitas = DateEntry(frame_configuracao, width=12, background='darkblue', foreground='white', borderwidth=2,
                           year=2020)
e_cal_receitas.place(x=110, y=41)

l_valor_receitas = Label(frame_configuracao, text="Total Amount", height=1, anchor=NW, font='Ivy 10', bg=co1,
                         fg=co4)
l_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao, width=14, justify='left', relief="solid")
e_valor_receitas.place(x=110, y=71)

# Insert Button
img_add_receitas = Image.open("images/icons/icon-add.png")
img_add_receitas = img_add_receitas.resize((17, 17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
botao_inserir_receitas = Button(frame_configuracao, command=inserir_receitas_main, image=img_add_receitas,
                                compound=LEFT, anchor=NW, text=" Add".upper(), width=80, overrelief=RIDGE,
                                font=('ivy 7 bold'), bg=co1, fg=co0)
botao_inserir_receitas.place(x=110, y=111)

# ==============================
# New Category operation
# ==============================
l_n_categoria = Label(frame_configuracao, text="Category", height=1, anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4)
l_n_categoria.place(x=10, y=160)
e_n_categoria = Entry(frame_configuracao, width=14, justify='left', relief="solid")
e_n_categoria.place(x=110, y=160)

# Insert Button
img_add_categoria = Image.open("images/icons/icon-add.png")
img_add_categoria = img_add_categoria.resize((17, 17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_categoria = Button(frame_configuracao, command=inserir_categoria_main, image=img_add_categoria,
                                 compound=LEFT, anchor=NW, text=" Add".upper(), width=80, overrelief=RIDGE,
                                 font=('ivy 7 bold'), bg=co1, fg=co0)
botao_inserir_categoria.place(x=110, y=190)

# ==============================
#  Main window
# ==============================
janela.mainloop()
