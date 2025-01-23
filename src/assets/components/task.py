import flet as ft
from .styles import Colors, FontSize
import assets.components.task_components as tc


task = tc.Base(
    padding=30,
    controls=[
        tc.TitleInput(),
        ft.Row(
            [
                tc.Date(date="10 - 05 - 2025"),
                tc.State(),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        tc.TextArea(),
    ],
    close_function=lambda e: print("close"),
)
