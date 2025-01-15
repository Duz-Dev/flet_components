import flet as ft 
import assets.components as fc #flet component

def main(page: ft.Page) -> None:
    page.add(fc.task)
    
ft.app(target=main, assets_dir="assets")
    
