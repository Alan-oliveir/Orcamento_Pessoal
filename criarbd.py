# Importando o SQLite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabelas com IF NOT EXISTS para evitar erro se as tabelas já existirem
with con:
    cur = con.cursor()
    # Criando tabela Categoria
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    """)

    # Criando tabela Receitas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Receitas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            adicionado_em DATE,
            valor DECIMAL
        )
    """)

    # Criando tabela de Gastos
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Gastos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            retirado_em DATE,
            valor DECIMAL
        )
    """)

