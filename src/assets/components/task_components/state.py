import flet as ft
from ..styles import Colors, FontSize


class State(ft.Container):
    def __init__(self):
        super().__init__()
        self.cicle_status = ft.Container(
            bgcolor=Colors.color_C,
            border_radius=50,
            width=15,
            height=15,
            border=ft.border.all(2.25, ft.Colors.WHITE),
        )
        self.content = ft.Row(
            controls=[
                ft.Text(
                    value="State",
                    size=FontSize.normal_font_size,
                    weight=ft.FontWeight.W_600,
                ),
                self.cicle_status,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def state_colors(self, state=None):
        match state:
            case 1:
                self.cicle_status.border = ft.border.all(2.25, Colors.color_state_init)
            case 2:
                self.cicle_status.border = ft.border.all(
                    2.25, Colors.color_state_progress
                )
            case 3:
                self.cicle_status.border = ft.border.all(
                    2.25, Colors.color_state_finish
                )
            case _:
                self.cicle_status.border = ft.border.all(2.25, ft.Colors.WHITE)


# Recuerda que la barra de progreso avanza en base a la cantidad de checklist = true
class ProgressBar(ft.ProgressBar):
    def __init__(self):
        super().__init__(value=0, bgcolor=Colors.color_C)

    def state_progress(self, n_sub_task: int = None, complete_sub_task: int = None):
        """Cambia el color y el progreso en base a la cantidad de subtareas / cantidad de sub_tareas completadas.

        Args:
            n_sub_task (int): cantidad de sub_tareas
            complete_sub_task (int): cantidad de sub_tareas completadas
        """
        if n_sub_task == None and complete_sub_task == None:
            print("Error: n_sub_task and complete_sub_task are required")
        res = complete_sub_task / n_sub_task
        self.value = res
        if 0 > res < 0.9:
            self.color = Colors.color_state_progress
        if res == 1:
            self.color = Colors.color_state_finish
