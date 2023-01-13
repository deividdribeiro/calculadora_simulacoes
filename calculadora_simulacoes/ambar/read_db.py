import sqlite3

# Caminho para o arquivo sqlite3
path = 'arquivos/faturas_cpfl_paulista.db'

# Cria conexão com banco de dados
conn = sqlite3.connect(path)

# Cria cursor
cursor = conn.cursor()

# Executa consulta
cursor.execute("SELECT uc FROM nome_tabela")

# Armazena resultado da consulta
resultado = cursor.fetchall()

# Itera sobre o resultado
for linha in resultado:
    print(linha)

# Fecha conexão
conn.close()

