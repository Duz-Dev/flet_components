import flet as ft
from ..styles import Colors, FontSize


class Date(ft.Container):
    def __init__(self, date: str = "DD - MM - YYYY"):
        super().__init__()
        self.date = date
        self.text_const = ft.Text(
            value="Fecha:", size=FontSize.normal_font_size, weight=ft.FontWeight.W_600
        )
        self.text_date = ft.Text(
            value=date,
            size=FontSize.normal_font_size,
            weight=ft.FontWeight.W_600,
        )
        self.content = ft.Row(controls=[self.text_const, self.text_date])
