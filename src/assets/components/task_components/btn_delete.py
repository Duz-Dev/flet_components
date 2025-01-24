import flet as ft

from ..styles import Colors, FontSize


class BtnDelete(ft.Container):
    def __init__(self, text: str = None, on_click=None):
        super().__init__()
        self.text = text
        if not text:
            self.text = " "
        self.content = ft.ElevatedButton(
            bgcolor={
                ft.ControlState.DEFAULT: ft.Colors.with_opacity(
                    1, Colors.color_primary
                ),
                ft.ControlState.HOVERED: ft.Colors.with_opacity(0.7, "red"),
            },
            color=ft.Colors.WHITE,
            content=ft.Text(
                value=self.text, size=FontSize.h3_size, weight=ft.FontWeight.W_600
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
                padding=ft.padding.symmetric(20, 30),
            ),
            on_click=on_click,
        )
        self.border = ft.border.all(2, "red")
        self.border_radius = 5
