import mariadb
import sys

db_user = "CHANGE_ME"
db_password = "CHANGE_ME"
db_host = "CHANGE_ME"
db_port = int("CHANGE_ME")
db_name = "CHANGE_ME"

try:
    
    conn = mariadb.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )
except mariadb.Error as e:
    print(f"Erro ao conectar ao MariaDB: {e}")
    sys.exit(1)


cursor = conn.cursor()

minha_tabela = "CHANGE_ME"

try:
    cursor.execute(f"INSERT INTO {minha_tabela} (nome, idade) VALUES (?, ?)", ("Alice", 30))
    conn.commit()
    print("Registro inserido com sucesso!")
except mariadb.Error as e:
    print(f"Erro ao inserir registro: {e}")

cursor.execute(f"SELECT nome, idade FROM {minha_tabela} WHERE idade > ?", (25,))
for nome, idade in cursor:
    print(f"Nome: {nome}, Idade: {idade}")

try:
    cursor.execute(f"UPDATE {minha_tabela} SET idade = ? WHERE nome = ?", (35, "Alice"))
    conn.commit()
    print("Registro atualizado com sucesso!")
except mariadb.Error as e:
    print(f"Erro ao atualizar registro: {e}")

try:
    cursor.execute(f"DELETE FROM {minha_tabela} WHERE nome = ?", ("Alice",))
    conn.commit()
    print("Registro excluído com sucesso!")
except mariadb.Error as e:
    print(f"Erro ao excluir registro: {e}")

conn.close()
