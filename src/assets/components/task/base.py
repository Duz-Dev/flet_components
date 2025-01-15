import flet as ft
from ..styles import Colors

content = [] #?Contenido de la base

    
#?Medidas de la base
content_width = 600
content_height = 800    

task = ft.Container(
    content=
        ft.Column(
            controls=[
                #!contenido superior (title and button exit (x))
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(value="task",size=32,weight=ft.FontWeight.BOLD),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE_SHARP,
                                icon_size=30,
                                icon_color=ft.Colors.WHITE
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    bgcolor=Colors.color_secundary,
                    border_radius=ft.border_radius.only(top_left=10, top_right=10),
                    padding=ft.padding.only(left=10,right=10, top=5, bottom=5),
                    width=content_width,
                    border=ft.border.only(
                        left=ft.border.BorderSide(3, Colors.color_C),
                        right=ft.border.BorderSide(3, Colors.color_C),
                        top=ft.border.BorderSide(3, Colors.color_C)
                    )
                ),
                #!contenido inferior (contenido principal)
                ft.Container(
                    bgcolor=Colors.color_secundary,
                    expand=1,
                    border=ft.border.all(3, Colors.color_C),
                    border_radius=ft.border_radius.only(bottom_left=10,bottom_right=10),
                    width=content_width,
                    height=content_height,
                    padding=20,
                    content=ft.Column(
                        controls=content
                    )
                )
            ],
            expand=1,
            spacing=0
        ), 
        expand=1
    
)