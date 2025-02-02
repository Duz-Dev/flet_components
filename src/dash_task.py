import flet as ft
import assets.components.ui.task as task
import assets.components.task_components as tc
from assets.database.tasks import dbTask


def main(page: ft.Page):
    db = dbTask()

    id_input = tc.TitleInput(placeHolder="Ingresa el id de la tarea a buscar")

    def buscar_tarea(e):
        print(id_input.text, id_input.value)

    button = tc.BtnDelete("Buscar", click=buscar_tarea)
    page.add(id_input, button)


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
# TK.BtnDelete.click = lambda e: page.add(
#     ft.Text(value=TK.SubTaskList.count_subTask())
# )
# page.add(TK)
