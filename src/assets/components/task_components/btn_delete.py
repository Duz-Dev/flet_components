import flet as ft

from ..styles import Colors, FontSize

btn = ft.Container(
    content=ft.ElevatedButton(
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.with_opacity(1, Colors.color_primary),
            ft.ControlState.HOVERED: ft.Colors.with_opacity(0.7, "red"),
        },
        color=ft.Colors.WHITE,
        content=ft.Text(
            "Delete Task", size=FontSize.h3_size, weight=ft.FontWeight.W_600
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            padding=ft.padding.symmetric(20, 30),
        ),
    ),
    border=ft.border.all(2, "red"),
    border_radius=5,
)

# btn.content.on_click = lambda e: print("pa")
