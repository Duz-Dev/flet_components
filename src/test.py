import flet as ft
import assets.components.task_components as tc


def main(page: ft.Page):

    tabs = ft.Tabs(
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="base",
                content=tc.Base(),
            ),
            ft.Tab(
                text="Tab 2",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Tab 3",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
        ],
        expand=1,
    )

    page.add(tabs)


ft.app(target=main, assets_dir="assert")
