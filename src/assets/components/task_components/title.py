import flet as ft
from ..styles import Colors, FontSize


class TitleInput(ft.Row):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase ft.Row
        self.checkbox = ft.Container(
            content=ft.Checkbox(
                scale=1.5,
                check_color=ft.Colors.WHITE,
                fill_color={
                    ft.ControlState.SELECTED: Colors.color_B,
                },
            )
        )

        self.text_fild = ft.TextField(
            hint_text="Enter New Task",
            border=ft.InputBorder.NONE,
            text_size=FontSize.h2_size,
            text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            hint_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE),
            ),
            content_padding=ft.padding.only(10, 0, 0, 0),
            max_length=80,
            expand=1,
            on_blur=self.text_fild__on_blur,
            on_focus=self.text_fild__on_focus,
            bgcolor=ft.Colors.with_opacity(0.65, Colors.color_primary),
            prefix_icon=ft.Icons.MODE_EDIT_OUTLINE,
        )

        self.controls = [self.checkbox, self.text_fild]
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def text_fild__on_blur(self, e):
        if not self.text_fild.value:
            self.text_fild.bgcolor = ft.Colors.with_opacity(0.65, Colors.color_primary)
            self.text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
        else:
            self.text_fild.bgcolor = ft.Colors.TRANSPARENT
            self.text_fild.prefix_icon = ""
        self.text_fild.border = ft.InputBorder.NONE
        self.text_fild.update()

    def text_fild__on_focus(self, e):
        self.text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
        self.text_fild.border = ft.InputBorder.OUTLINE
        self.text_fild.border_color = Colors.color_B
        self.text_fild.update()
