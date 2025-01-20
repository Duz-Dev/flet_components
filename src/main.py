import flet as ft
import assets.components as fc  # flet component
import assets.components.styles as styles


def main(page: ft.Page) -> None:
    page.bgcolor = styles.Colors.color_secundary
    text = ft.Text()
    page.add(fc.ListSubTasks, text)

    # page.add(fc.SubTasks)
    def count_tasks(e):
        cantidad_tareas, cantidad_completadas = fc.count_subtask()
        text.value = f"Cantidad de subtareas: {cantidad_tareas}"
        page.update()

    page.add(ft.FilledButton("submit", on_click=count_tasks))


ft.app(target=main, assets_dir="assets")
