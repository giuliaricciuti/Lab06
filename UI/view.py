import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddAnni = ft.Dropdown(label="anno", width=200)
        self._controller.fillddAnno()

        self.ddBrand = ft.Dropdown(label="brand", width=200)
        self._controller.fillddBrand()

        self.ddRetailer = ft.Dropdown(label="retailer", width=200)
        self._controller.fillddRetailer()

        # button for the "hello" reply
        row1 = ft.Row([self.ddAnni, self.ddBrand, self.ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)

        self.btn_topVendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handle_topVendite)
        self.btn_analizzaVendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handle_analizzaVendite)
        row2 = ft.Row([self.btn_topVendite, self.btn_analizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
