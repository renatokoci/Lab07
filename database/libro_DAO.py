from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_all_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return []
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT DISTINCT genere FROM libro"
        lista_generi = []
        try:
            cursor.execute(query)
            for row in cursor.fetchall():
                lista_generi.append(row["genere"])
        except Exception as e:
            print(f"Errore DAO: {e}")
            return []
        finally:
            cursor.close()
            cnx.close()
        return lista_generi

    def get_libri_filtrati(self,id_biblioteca,genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return []
        cursor = cnx.cursor(dictionary=True)
        query = ("SELECT * FROM libro WHERE id_biblioteca = COALESCE(%s, id_biblioteca) "
                 f"AND genere = COALESCE (%s,genere)")
        lista_libri = []
        try:
            cursor.execute(query, (id_biblioteca, genere))
            for row in cursor.fetchall():
                libro = Libro(
                    row["id"],
                    row["titolo"],
                    row["autore"],
                    row["genere"],
                    row["anno_pubblicazione"],
                    row["id_biblioteca"]
                )
                lista_libri.append(libro)
        except Exception as e:
            print(f"Errore query filtri: {e}")
            return []
        finally:
            cursor.close()
            cnx.close()
        return lista_libri
