import sqlite3

try:
    conexao = sqlite3.connect("db/innertable.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Usuarios"
                   " INNER JOIN Infos ON Usuarios.id = Infos.idfk;")

    for mostrar in cursor.fetchall():
        nome = mostrar[0]
        sobrenome = mostrar[1]
        endereco = mostrar[2]

        print("\tNOME:", nome, "\n", "\tSOBRENOME:", sobrenome, "\n", "\tENDEREÇO:", endereco, "\n"+"-"*25)

except Exception as e:
    print("ERRO:", e)

finally:
    cursor.close()
    conexao.close()
