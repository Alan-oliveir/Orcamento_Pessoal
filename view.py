import sys
import sqlite3 as lite
from datetime import datetime

# importing pandas
import pandas as pd

# Criando conexão
con = lite.connect('dados.db')


# Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)


# Inserir receitas
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


# Inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


# Deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)


# Deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)


# Ver Categorias
def ver_categorias():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Receitas
def ver_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Gastos
def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista


def bar_valores():
    # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receitas_total = sum(receitas_lista)

    # Despesas Total ------------------------
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)

    # Despesas Total ------------------------
    saldo_total = receitas_total - gastos_total

    return [receitas_total, gastos_total, saldo_total]


def percentagem_valor():
    # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receitas_total = sum(receitas_lista)

    # Despesas Total ------------------------
    despesas = ver_gastos()
    despesas_lista = []

    for i in despesas:
        despesas_lista.append(i[3])

    despesas_total = sum(despesas_lista)

    # Despesas Total ------------------------
    if receitas_total != 0:
        total = (100 - ((receitas_total - despesas_total) / receitas_total) * 100)
    else:
        total = 0

    return [total]


def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns=['id', 'Categoria', 'Data', 'Valor'])

    # Get the sum of the durations per month
    dataframe = dataframe.groupby('Categoria')['Valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return ([lista_categorias, lista_quantias])