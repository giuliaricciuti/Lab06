import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._metodo = None

    def handle_graph(self, e):
        self._view.lst_result.controls.clear()
        if self._anno is None or self._metodo is None:
            self._view.lst_result.controls.append(ft.Text("Seleziona un anno e un metodo.", color='red'))
            self._view.update_page()
            return
        soglia=self._view.txtInS.value
        if soglia is None or soglia=="":
            self._view.lst_result.controls.append(ft.Text("Inserisci una soglia.", color='red'))
            self._view.update_page()
            return
        try:
            float(soglia)
        except ValueError:
            self._view.lst_result.controls.append(ft.Text("Inserisci un valore numerico"))
            self._view.update_page()
            return
        self._model.creaGrafo(self._anno, self._metodo.Order_method_code, float(soglia))
        self._view.lst_result.controls.append(ft.Text(f"Grafo creato!\n"
                                                      f"Ci sono {self._model.getNum()[0]} vertici.\n"
                                                      f"Ci sono {self._model.getNum()[1]} archi"))
        self._view.update_page()

    def handle_prodotti_redditizi(self, e):
        self._view.lst_result.controls.append(ft.Text(f"I prodotti più redditizi sono:"))
        for r in self._model.getRedditizi():
            self._view.lst_result.controls.append(
                ft.Text(f"Prodotto {r[0].Product_number}   Archi Entranti={r[1]}  Ricavo={r[0].tot_vendite}"))
        self._view.update_page()

    def fillDD(self):
        for i in range(2015, 2019):
            self._view.dd_anno.options.append(ft.dropdown.Option(
                text=i, key=i
            ))

        metodi = self._model.getMethods()
        for m in metodi:
            self._view.dd_metodo.options.append(ft.dropdown.Option(
                text = m.Order_method_type, data = m, on_click= self.readDDMethod
            ))
        self._view.update_page()

    def readDDAnno(self, e):
        if self._view.dd_anno.value is None:
            self._anno = None
        else:
            self._anno = self._view.dd_anno.value
        print(self._anno)

    def readDDMethod(self, e):
        if e.control.data is None:
            self._metodo = None
        else:
            self._metodo = e.control.data
        print(self._metodo)