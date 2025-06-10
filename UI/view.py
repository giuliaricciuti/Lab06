import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.window_width = 950
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_metodo = None
        self.btn_grafo = None
        self.btn_handle_prodotti = None
        self.lst_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with dropdowns
        self.dd_anno = ft.Dropdown(width=200,
                                   hint_text="anno",
                                   label="Anno",
                                   on_change=self._controller.readDDAnno)

        self.dd_metodo = ft.Dropdown(width=200,
                                   hint_text="Metodo",
                                   label="Metodo")

        self._controller.fillDD()


        self.txtInS = ft.TextField(label="S")

        row2 = ft.Row([self.dd_anno, self.dd_metodo, self.txtInS],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW with buttons
        self.btn_grafo = ft.ElevatedButton(text="Crea Grafo",
                                                 on_click=self._controller.handle_graph)
        self.btn_handle_prodotti = ft.ElevatedButton(text="Analizza vendite",
                                                      on_click=self._controller.handle_prodotti_redditizi)

        row2 = ft.Row([self.btn_grafo, self.btn_handle_prodotti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.lst_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lst_result)
        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

