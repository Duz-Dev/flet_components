import flet as ft 
from ..styles import Colors, FontSize

content = ft.Column(
    controls=[
        ft.Text(
            value="Escribe una nota...",
            size=FontSize.normal_font_size,
            color=ft.Colors.with_opacity(.6, ft.Colors.WHITE)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

def on_hover(e):
    if e.data == "true":  # Hover activo
        container.border = ft.border.all(1, ft.Colors.WHITE)
        content.controls[0].color = ft.Colors.WHITE
    else:  # Hover desactivado
        container.border = ft.border.all(1, ft.Colors.with_opacity(.6, ft.Colors.WHITE))
        content.controls[0].color = ft.Colors.with_opacity(.6, ft.Colors.WHITE)
    content.update()
    container.update()
    
container = ft.Container(
        bgcolor=Colors.color_C,
        expand=True,
        content=content,
        height=250,
        on_hover=on_hover,
        # border = ft.border.all(3, ft.Colors.WHITE),
        border_radius=5,
        border = ft.border.all(1, ft.Colors.with_opacity(.6, ft.Colors.WHITE))
)

text_area = ft.Row(
    controls=[
        container
    ]
)