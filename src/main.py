import flet as ft
import assets.components as fc
import assets.components.task_components as tc


def main(page: ft.Page) -> None:
    page.bgcolor = fc.styles.Colors.color_primary
    text_area = tc.TextArea(text="asd")
    task = tc.Base(
        padding=30,
        controls=[
            tc.TitleInput(),
            ft.Row(
                [
                    tc.Date(date="10 - 05 - 2025"),
                    tc.State(),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            text_area,
        ],
        close_function=lambda e: page.window.close(),
    )
    page.add(task)
    page.add(
        ft.FilledButton(text="prueba", on_click=lambda e: print(text_area.get_text()))
    )


ft.app(target=main, assets_dir="assets")
