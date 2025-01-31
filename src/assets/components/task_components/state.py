import flet as ft
from ..styles import Colors, FontSize


class State(ft.Container):
    """
    Un componente personalizado para mostrar un estado con un texto descriptivo y un indicador visual circular.

    El componente `State` combina un texto y un círculo de estado, ideal para representar etapas o estados
    de un proceso (como inicialización, en progreso y finalizado). El círculo cambia de color dependiendo del estado.

    Ejemplo:

    ```
    import flet as ft

    def main(page: ft.Page):
        state_display = State(text="En progreso", width=20, height=20, size=16)
        state_display.state_colors(state=2)  # Cambiar a color de estado "En progreso"
        page.add(state_display)

    ft.app(target=main)
    ```
    -----

    Observación: tanto width y height modifican las dimensiones del cirulo, no del control completo en si.

    El Metodo ``state_colors()`` esta limitado a solo 3 opciones y en su defecto no cambiara de color.


    -----
    Online docs: (Enlace a documentación personalizada si aplica)
    """

    def __init__(
        self,
        text: str = "state",
        width: int = 15,
        height: int = 15,
        size: int = FontSize.normal_font_size,
    ):

        super().__init__()
        self.__width = width
        self.__height = height
        self.__text = text
        self.__size = size
        self.cicle_status = ft.Container(
            bgcolor=Colors.color_C,
            border_radius=50,
            width=self.__width,
            height=self.__height,
            border=ft.border.all(2.25, ft.Colors.WHITE),
        )
        self.content = ft.Row(
            controls=[
                ft.Text(
                    value=self.__text,
                    size=size,
                    weight=ft.FontWeight.W_600,
                ),
                self.cicle_status,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def state_colors(self, state=None):
        """
        Cambia el color del indicador de estado según el estado proporcionado.

        Args:
            state (int, opcional): El estado actual del componente. Los valores posibles son:

            - 1: Estado inicial (color definido en `Colors.color_state_init`).

            - 2: Estado en progreso (color definido en `Colors.color_state_progress`).

            - 3: Estado finalizado (color definido en `Colors.color_state_finish`).

            - Otro: Estado predeterminado (blanco).
        """
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
    """
    ProgressBar es una clase personalizada que extiende la barra de progreso de Flet.
    Está diseñada para facilitar el manejo visual del progreso en función de subtareas.

    Atributos:
        value (float): Valor inicial de progreso, por defecto es 0.
        expand (bool): Indica si la barra debe expandirse para ocupar todo el espacio disponible.
        width (int): Ancho de la barra de progreso en píxeles.
        height (int): Altura de la barra de progreso en píxeles.

    Métodos:
        state_progress(n_sub_task: int, complete_sub_task: int):
            Actualiza el progreso y cambia el color de la barra dependiendo del estado de las subtareas.
    """

    def __init__(
        self,
        value: float = 0,
        expand: bool = None,
        width: int = None,
        height: int = None,
    ):
        super().__init__(value=0, bgcolor=Colors.color_C, expand=1)
        self.value = value
        self.width = width
        self.height = height
        self.expand = expand

    def state_progress(self, n_sub_task: int = None, complete_sub_task: int = None):
        """Cambia el color y el progreso en base a la cantidad de subtareas / cantidad de sub_tareas completadas.

        Args:
            n_sub_task (int): cantidad de sub_tareas
            complete_sub_task (int): cantidad de sub_tareas completadas
        """
        if n_sub_task == None and complete_sub_task == None:
            raise Exception("Error: n_sub_task y complete_sub_task son requeridos")
        if n_sub_task < complete_sub_task:
            raise Exception("El valor de <n_sub_task> debe ser mayor.")

        res = complete_sub_task / n_sub_task
        self.value = res
        if 0 < res < 0.5:
            self.color = Colors.color_state_init
        if 0.5 <= res < 0.9:
            self.color = Colors.color_state_progress

        if res == 1:
            self.color = Colors.color_state_finish
