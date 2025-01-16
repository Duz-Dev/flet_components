import flet as ft
from ..styles import Colors, FontSize

def text_fild__on_blur(e):
    if not text_fild.value:
        text_fild.bgcolor=ft.Colors.with_opacity(0.65, Colors.color_primary)
        text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
    else: 
        text_fild.bgcolor= ft.Colors.TRANSPARENT
        text_fild.prefix_icon = ""
    text_fild.border = ft.InputBorder.NONE

    text_fild.update()

def text_fild__on_focus(e):
    # text_fild.bgcolor = "red"
    text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
    text_fild.border = ft.InputBorder.OUTLINE,
    text_fild.border_color = Colors.color_B
    text_fild.update()
    ...

checkbox = ft.Container(
            content=ft.Checkbox(
                scale=1.5,
                value=True,
                check_color=ft.Colors.WHITE,
               fill_color={
                ft.ControlState.SELECTED: Colors.color_B,
            }
        ))

text_fild = ft.TextField(
            hint_text = "Enter New Task",
            # border=ft.BorderSide(3, "green"),
            border=ft.InputBorder.NONE,
            # border_color=Colors.color_B,
            text_size=FontSize.h2_size,
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
                ),
            hint_style =  ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.with_opacity(0.5, ft.Colors.WHITE)
                ),
            content_padding=ft.padding.only(10, 0,0,0),
            max_length = 80,
            expand=1,
            # filled=True,
            # fill_color={
            #     ft.ControlState.SELECTED: Colors.color_B,
            # }        # focused_bgcolor = "green",
            # focused_border_color="green"
           on_blur=text_fild__on_blur,
           on_focus=text_fild__on_focus,
           bgcolor=ft.Colors.with_opacity(0.65, Colors.color_primary),
           prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
        )


title_input = ft.Row(
    controls=[checkbox, text_fild],
    vertical_alignment=ft.CrossAxisAlignment.CENTER,
)