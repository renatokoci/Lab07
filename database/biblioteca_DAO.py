from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return []
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT * FROM biblioteca"
        lista_biblioteche = []
        try:
            cursor.execute(query)
            for row in cursor.fetchall():
                bib = Biblioteca(row["id"],row["nome"],row["indirizzo"])
                lista_biblioteche.append(bib)
        except Exception as e:
            print(f"Errore DAO biblioteche: {e}")
            return []
        finally:
            cursor.close()
            cnx.close()

        return lista_biblioteche


