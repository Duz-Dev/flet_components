import flet as ft
import assets.components as fc
import task  # prube de una interfaz provicional para modificar el layout de tarea.
import assets.components.task_components as tc


def main(page: ft.Page) -> None:
    page.bgcolor = fc.styles.Colors.color_primary
    page.scroll = True

    t = task.Task("title", on_click=lambda e: print("hola mundo"))
    t.TitleInput.text = "Lorem"
    t.TitleInput.value = True
    t.TextArea.text_content = """
## Table

|Syntax                                 |Result                               |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
    """
    t.Date.date = "30-01-2025"
    t.Date.template = "Date:"
    t.State.state_colors(2)
    t.ProgressBar.state_progress(2, 1)
    t.SubTaskList.add_subTask("terminar actividad", False)  # añade una subtarea
    t.SubTaskList.add_subTask("comprar chettos", True)  # añade una subtarea
    t.BtnDelete.text = "save"
    t.BtnDelete.click = lambda e: page.add(ft.Text(value=t.SubTaskList.count_subTask()))
    page.add(t)


ft.app(target=main, assets_dir="assets")
