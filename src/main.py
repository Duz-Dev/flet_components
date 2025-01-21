import flet as ft
import assets.components as fc


def main(page: ft.Page) -> None:
    page.bgcolor = fc.styles.Colors.color_primary
    page.scroll = True
    page.add(fc.task)


ft.app(target=main, assets_dir="assets")
