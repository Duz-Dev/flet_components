import flet as ft
import assets.components.ui.task as task
import assets.components.task_components as tc
from assets.database.tasks import dbTask
from assets.components.styles import FontSize, Colors
import time

db = dbTask()  # creo una instancia de la conexion a la tabla "tasks"


def main(page: ft.Page):
    # ?Estilos de la pagina
    page.padding = 40

    # ?Captura de la tarea buscar
    id_input = tc.TitleInput(placeHolder="Ingresa el id de la tarea a buscar")

    def buscar_tarea(e):
        id = int(id_input.text)
        datos = db.read(id)
        if datos:
            load_task(*datos)
        else:

            def open_banner(e=None):
                page.open(banner)
                for i in range(4):
                    time.sleep(1)
                close_banner()

            def close_banner(e=None):
                page.close(banner)

            banner = ft.Banner(
                bgcolor=ft.Colors.AMBER_100,
                leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER),
                content=ft.Text(
                    "Aviso. Parece que no existe el dato que has buscado en nuestra base de datos.",
                    color=ft.Colors.BLACK,
                ),
                actions=[
                    ft.TextButton(
                        text="Ok",
                        on_click=close_banner,
                        style=ft.ButtonStyle(color=ft.Colors.BLACK),
                    )
                ],
            )
            open_banner()

    modal_TK = ft.AlertDialog(actions_padding=0)

    def open_modal(element):
        modal_TK.actions = [element]
        page.open(modal_TK)

    def close_modal(e=None):
        page.close(modal_TK)

    # ?Mostar los datos de las tareas mediante un TK
    def load_task(id, title, date, text, state, subtask):
        TK = task.Task("Tarea", on_close=close_modal)
        TK.TitleInput.text = title
        TK.TextArea.text = text
        TK.Date.date = date
        TK.Date.template = "Date:"
        TK.BtnDelete.text = "close"
        TK.BtnDelete.click = close_modal
        open_modal(TK)

    # ?Crear una TK desde cero para añadirla a list_TK
    def crear_tarea(e):
        def add(e):
            db.add(
                title=TK.TitleInput.text,
                text=TK.TextArea.text,
                state="progress",
            )
            # print("ID")
            # print(TK.TitleInput.text)
            # print(TK.Date.date)
            # print(TK.TextArea.text)
            # print("progress")
            # print("subtask")
            close_modal()

        TK = task.Task("Nueva Tarea", on_close=close_modal)
        TK.BtnDelete.text = "Añadir tarea"
        TK.Date.text_date = ""
        TK.BtnDelete.click = add

        open_modal(TK)

    # ? Botones de buscar y Añadir tarea nueva
    btn_search = tc.BtnDelete("Buscar", click=buscar_tarea)
    btn_add = tc.BtnDelete("añadir", click=crear_tarea)
    btn_all = tc.BtnDelete("All", click=lambda e: print(db.read()))
    # Añado los elementos principales a la pagina
    page.add(
        id_input,
        ft.Row(
            [btn_search, btn_all, btn_add],
            alignment=ft.MainAxisAlignment.END,
            spacing=30,
        ),
    )


ft.app(target=main, assets_dir="assets")

# TK = task.Task("title", on_close=lambda e: print("hola mundo"))
# TK.TitleInput.text = "Lorem"
# TK.TitleInput.value = True
# TK.TextArea.text = "texto"
# TK.Date.date = "30-01-2025"
# TK.Date.template = "Date:"
# TK.State.state_colors(2)
# TK.ProgressBar.state_progress(2, 1)
# TK.SubTaskList.add_subTask("terminar actividad", False)  # añade una subtarea
# TK.SubTaskList.add_subTask("comprar chettos", True)  # añade una subtarea
# TK.BtnDelete.text = "save"
# TK.BtnDelete.click = lambda e: page.add(ft.Text(value=TK.SubTaskList.count_subTask()))
# page.add(TK)
