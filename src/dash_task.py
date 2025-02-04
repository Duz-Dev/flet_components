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
    page.scroll = "AUTO"

    # ?Captura de la tarea buscar
    id_input = tc.TitleInput(placeHolder="Ingresa el id de la tarea a buscar")

    def buscar_tarea(e):
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

        if not id_input.text.isdigit():
            banner.content.value = (
                "Aviso. En dato ingresado no es valido, intenta de nuevo."
            )
            open_banner()
        else:
            id = int(id_input.text)
            datos = db.read(id)
            if datos:
                load_task(*datos)
            else:
                open_banner()

    modal_TK = ft.AlertDialog(actions_padding=0)

    def open_modal(element):
        modal_TK.actions = [element]
        page.open(modal_TK)

    def close_modal(e=None):
        page.close(modal_TK)

    TK = task.Task(on_close=close_modal)

    def update_task(e=None):
        # e.control.data Este dato es el que me trae la informacion del TK.BtnDelete.meta
        id = int(e.control.data)
        title = TK.TitleInput.text
        text = TK.TextArea.text
        state = "progress"

        db.update(id=id, title=title, text=text, state=state)

    def actualizar_tarea(e=None):
        update_task(e)
        close_modal()

    # ?Mostar los datos de las tareas mediante un TK
    def load_task(id, title, date, text, state, subtask):
        TK.title = "Tarea"
        TK.TitleInput.text = title
        TK.TextArea.text = text
        TK.Date.date = date
        TK.Date.template = "Date:"
        TK.BtnDelete.text = "save"
        TK.BtnDelete.meta = id
        TK.BtnDelete.click = actualizar_tarea
        open_modal(TK)

    # ?Crear una tarea desde cero para añadirla a base de datos
    def crear_tarea(e):
        TK = task.Task(on_close=close_modal)

        def create_TK(e):
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

        TK.title = "Nueva Tarea"
        TK.BtnDelete.text = "Añadir tarea"
        TK.Date.text_date = ""
        TK.BtnDelete.click = create_TK

        open_modal(TK)

    def all_task(e=None):  # funcion experimental
        tasks = db.read()
        for t in tasks:
            TK = task.Task()
            TK.title = "Tarea"
            TK.TitleInput.text = t[1]
            TK.TextArea.text = t[3]
            TK.Date.date = t[2]
            TK.Date.template = "Date:"
            TK.BtnDelete.text = "save"
            TK.BtnDelete.click = actualizar_tarea
            page.add(TK)

    # ? Botones de buscar y Añadir tarea nueva
    btn_search = tc.BtnDelete("Buscar", click=buscar_tarea)
    btn_add = tc.BtnDelete("añadir", click=crear_tarea)
    btn_all = tc.BtnDelete("All", click=all_task)

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
