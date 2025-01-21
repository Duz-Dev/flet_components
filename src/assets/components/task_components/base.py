import flet as ft
from ..styles import Colors


class Base(ft.Container):
    def __init__(self, controls=[], padding=None):
        self.controls = controls
        super().__init__()  # Llama a el constructor de la clase ft.Container, de esta forma puedo acceder y manipular sus elementos.
        self.content_width = 600
        self.content_height = 800
        self.__padding = padding
        self.content = ft.Column(
            controls=[
                # Contenido superior (título y botón de cerrar)
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(value="task", size=32, weight=ft.FontWeight.BOLD),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE_SHARP,
                                icon_size=30,
                                icon_color=ft.Colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    bgcolor=Colors.color_secundary,
                    border_radius=ft.border_radius.only(top_left=10, top_right=10),
                    padding=ft.padding.only(left=10, right=10, top=5, bottom=5),
                    width=self.content_width,
                    border=ft.border.only(
                        left=ft.border.BorderSide(3, Colors.color_C),
                        right=ft.border.BorderSide(3, Colors.color_C),
                        top=ft.border.BorderSide(3, Colors.color_C),
                    ),
                ),
                # Contenido inferior (contenido principal)
                ft.Container(
                    bgcolor=Colors.color_secundary,
                    expand=1,
                    border=ft.border.all(3, Colors.color_C),
                    border_radius=ft.border_radius.only(
                        bottom_left=10,
                        bottom_right=10,
                    ),
                    width=self.content_width,
                    height=self.content_height,
                    padding=self.__padding,
                    content=ft.Column(controls),
                ),
            ],
            expand=1,
            spacing=0,
        )
