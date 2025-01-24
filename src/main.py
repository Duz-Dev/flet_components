import flet as ft
import assets.components as fc
import assets.components.task_components as tc


def main(page: ft.Page) -> None:
    page.bgcolor = fc.styles.Colors.color_primary
    page.scroll = True
    text_area = tc.TextArea(text="asd")
    sub_list = tc.SubTaskList()

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
            ft.Row(
                [ft.Container(content=tc.ProgressBar(value=0), width=67)],
                alignment=ft.MainAxisAlignment.END,
            ),
            text_area,
            sub_list,
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    tc.BtnDelete(text="Eliminar", on_click=lambda e: print("Eliminar"))
                ],
            ),
        ],
        close_function=lambda e: page.window.close(),
        height=850,
    )
    page.add(task)
    page.add(
        ft.FilledButton(
            text="prueba",
            on_click=lambda e: print(
                text_area.get_text(),
                sub_list.count_sub_tasks(),
            ),
        )
    )


ft.app(target=main, assets_dir="assets")
