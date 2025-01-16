import flet as ft 
import assets.components as fc #flet component
import assets.components.styles as styles


def main(page: ft.Page) -> None:
    page.bgcolor = styles.Colors.color_secundary
    # page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH  # Asegura el 100% del ancho
    page.add(fc.text_area)

    
ft.app(target=main, assets_dir="assets")
    
