import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddRetalierValue = None

    def fillddAnno(self):
        for a in self._model.getAllAnni():
            self._view.ddAnni.options.append(
                ft.dropdown.Option(a)
            )

    def fillddBrand(self):
        for b in self._model.getAllBrand():
            self._view.ddBrand.options.append(
                ft.dropdown.Option(b)
            )

    def fillddRetailer(self):
        for r in self._model.getAllRetailer():
            self._view.ddRetailer.options.append(
                ft.dropdown.Option(key=r.Retailer_code,
                                   text=r.Retailer_name,
                                   data=r,
                                   on_click=self.readRetalier)
            )

    def readRetalier(self, e):
        self._ddRetalierValue = e.control.data


    def handle_topVendite(self, e):
        self._view.txt_result.controls.clear()
        top = []
        anno = self._view.ddAnni.value
        brand = self._view.ddBrand.value
        retailer = self._ddRetalierValue
        # if anno is None or anno == "":
        #     self._view.create_alert("Inserire l'anno")
        #     return
        # if brand is None or brand == "":
        #     self._view.create_alert("Inserire il brand")
        #     return
        # if retailer is None:
        #     self._view.create_alert("Inserire il retailer")
        #     return
        top = self._model.handle_topVendite(anno, brand, retailer)
        self._view.txt_result.controls.append(ft.Text(f"Classifica vendite"))
        for t in top:
            self._view.txt_result.controls.append(ft.Text(f"{t}"))
        self._view.update_page()

    def handle_analizzaVendite(self, e):
        self._view.txt_result.controls.clear()
        res = []
        anno = self._view.ddAnni.value
        brand = self._view.ddBrand.value
        retailer = self._ddRetalierValue
        res = self._model.handle_analizzaVendite(anno, brand, retailer)
        self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite"))
        self._view.txt_result.controls.append(ft.Text(f"""
        Giro d'affari: {res[0]}
        Numero vendite: {res[1]}
        Numero retailers coinvolti: {res[2]}
        Numero prodotti coinvolti: {res[3]}
        """))
        self._view.update_page()
