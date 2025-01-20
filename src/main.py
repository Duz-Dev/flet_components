import flet as ft
import assets.components as fc  # flet component
import assets.components.styles as styles


def main(page: ft.Page) -> None:
    page.bgcolor = styles.Colors.color_secundary
    page.add(fc.ButtonDelete)


ft.app(target=main, assets_dir="assets")
