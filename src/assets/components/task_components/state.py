import flet as ft
from ..styles import Colors, FontSize


def state_colors(state):
    match state:
        case 1:
            cicle_status.border = ft.border.all(2.25, Colors.color_state_init)
        case 2:
            cicle_status.border = ft.border.all(2.25, Colors.color_state_progress)
        case 3:
            cicle_status.border = ft.border.all(2.25, Colors.color_state_finish)
    cicle_status.update()


cicle_status = ft.Container(
    bgcolor=Colors.color_C,
    border_radius=50,
    width=15,
    height=15,
    border=ft.border.all(2.25, ft.Colors.WHITE),
)


state = ft.Container(
    content=ft.Row(
        controls=[
            ft.Text(
                value="State",
                size=FontSize.normal_font_size,
                weight=ft.FontWeight.W_600,
            ),
            cicle_status,
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
)

# Recuerda que la barra de progreso avanza en base a la cantidad de checklist = true


progress_bar = ft.ProgressBar(value=0, bgcolor=Colors.color_C)


def state_progress(n_sub_task: int, complete_sub_task: int):
    """Cambia el color y el progreso en base a la cantidad de subtareas / cantidad de sub_tareas completadas.

    Args:
        n_sub_task (int): cantidad de sub_tareas
        complete_sub_task (int): cantidad de sub_tareas completadas
    """
    res = complete_sub_task / n_sub_task
    progress_bar.value = res
    if 0 > res < 0.9:
        progress_bar.color = Colors.color_state_progress
    if res == 1:
        progress_bar.color = Colors.color_state_finish
    progress_bar.update()
