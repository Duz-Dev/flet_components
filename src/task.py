import flet as ft
import assets.components as fc
import assets.components.task_components as tc


def main(page: ft.Page) -> None:
    page.bgcolor = fc.styles.Colors.color_primary
    page.scroll = True
    text_area = tc.TextArea(
        expand=True,
        height=200,
    )
    sub_list = tc.SubTaskList(expand=1)

    task = tc.Base(
        padding=30,
        title="task",
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
            ft.Row([text_area]),
            sub_list,
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    tc.BtnDelete(text="Eliminar", on_click=lambda e: print("Eliminar"))
                ],
            ),
        ],
        # close_function=lambda e: page.window.close(),
        close_function=lambda e: page.close(mdl),
        height=500,
        width=560,
    )

    mdl = ft.AlertDialog(
        content=ft.Row(
            controls=[task], height=600
        ),  # Curisamente es mejor usar row para delimitar el alto de la tarea, de lo contrario se expande toda la pantalla la tarea.
        content_padding=ft.padding.all(0),
        inset_padding=None,
    )

    page.add(
        ft.FilledButton(
            text="prueba",
            on_click=lambda e: print(
                text_area.get_text(),
                sub_list.count_sub_tasks(),
            ),
        ),
        ft.FilledButton(text="abrir task", on_click=lambda e: page.open(mdl)),
    )


ft.app(target=main, assets_dir="assets")
