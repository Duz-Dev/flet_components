import flet as ft
from ..styles import Colors, FontSize

text_const = ft.Text(
    value="Fecha:",
    size=FontSize.normal_font_size,
    weight=ft.FontWeight.W_600
    
)

text_date = ft.Text(
    value="DD - MM - YYYY",
    size=FontSize.normal_font_size,
    weight=ft.FontWeight.W_600
)

date = ft.Container(
    content=ft.Row(
        controls=[text_const,text_date]
    ),
)