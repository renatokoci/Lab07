import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        # Aggiungo l'opzione "Nessun filtro" per la biblioteca
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="",text="Nessun filtro"))

        # Stessa cosa per aggiungere "Nessun filtro" alla tendina dei generi
        self._view.dd_genere.options.append(ft.dropdown.Option(key="",text="Nessun filtro"))

        # Chiedo al model la lista di tutte le biblioteche
        lista_biblioteche = self._model.get_biblioteche()

        # Un ciclo for per inserire ogni biblioteca nella sua tendina
        for bib in lista_biblioteche:
            # 'bib' è un oggetto Biblioteca (ha bib.id e bib.nome)
            # Voglio che la key sia bib.id (convertita in stringa) e il testo sia bib.nome
            opzione_bib = ft.dropdown.Option(key=str(bib.id), text=bib.nome)
            self._view.dd_biblioteca.options.append(opzione_bib)

        lista_generi = self._model.get_generi()
        for genere in lista_generi:
            # Qui 'genere' è già una semplice stringa
            # quindi lo usiamo sia per 'key' che per 'text'
            opzione_genere = ft.dropdown.Option(key=genere, text=genere)
            self._view.dd_genere.options.append(opzione_genere)

        self._view.update()

    # CALLBACKS DROPDOWN
    def leggi_biblioteca(self,e):
        valore = e.control.value
        if valore == "": # Significa che ha cliccato "Nessun filtro"
           self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore
    def leggi_genere(self,e):
        valore = e.control.value
        if valore == "":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self,e):
        # Chiedo al model la lista dei libri filtrati passando le due variabili del controller
        lista_libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        # Svuoto i controlli della ListView nella view
        self._view.lista_libri.controls.clear()

        if lista_libri is None or len(lista_libri) == 0:
            self._view.show_alert("Nessun libro trovato")
        else:
            for libro in lista_libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro)))

        self._view.update()
