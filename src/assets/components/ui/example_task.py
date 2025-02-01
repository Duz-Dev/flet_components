import flet as ft
import assets.components as fc
import assets.components.ui.task as task  # importa una extension del control tc.Base el cual cuenta con todos los demas controles del modulo task_components.


def main(page: ft.Page) -> None:
    page.bgcolor = fc.styles.Colors.color_primary
    page.scroll = True

    t = task.Task("title", on_close=lambda e: print("hola mundo"))
    t.TitleInput.text = "Lorem"
    t.TitleInput.value = True
    t.TextArea.text = """
## Tables

|Syntax                                 |Result                               |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
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
