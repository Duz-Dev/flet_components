import flet as ft 
from ..styles import Colors, FontSize

def state_colors(state):
    match state:
        case 1:
            cicle_status.bgcolor = Colors.color_E
        case 2:
            cicle_status.bgcolor = Colors.color_E
        case 3:
            cicle_status.bgcolor = Colors.color_E
    cicle_status.update()

cicle_status = ft.Container(
    bgcolor=Colors.color_C,
    border_radius=50,
    width=15,
    height=15,
    border=ft.border.all(2.25, ft.Colors.WHITE)
)


state = ft.Container(
    content=ft.Row(
        controls=[
            ft.Text(value="State",size=FontSize.normal_font_size, weight=ft.FontWeight.W_600),
            cicle_status
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
)

state_bar = ft.ProgressBar(value=20)

#TODO: Progress bar del estado pendiente.