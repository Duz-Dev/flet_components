import flet as ft
from ..styles import Colors, FontSize


class TitleInput(ft.Row):
    """
    Un componente personalizado que combina un cuadro de texto (`TextField`) y una casilla de verificación (`Checkbox`).

    Este componente está diseñado para representar una tarea editable con un estado de completado opcional.
    La casilla de verificación indica si la tarea está completada, y el cuadro de texto permite modificar
    el título de la tarea. Además, incluye estilos personalizados para una mejor apariencia.

    Atributos:
        text (str): El texto inicial del cuadro de texto (opcional).
        value (bool): El estado inicial de la casilla de verificación (opcional).
        placeHolder (str): Texto de fondo que da contexto del input. (opcional)

    Ejemplo:
        ```python
        import flet as ft
        from mymodule import TitleInput

        def main(page: ft.Page):
            task = TitleInput(text="Mi Tarea", value=True, placeHolder="Example")
            page.add(task)
            print(task.value) #salida: "Mi Tarea"

        ft.app(target=main)
        ```
    """

    def __init__(
        self, text: str = "", value: bool = False, placeHolder="Enter New Task"
    ):

        self.__text = text
        self.__value = value
        self.placeHolder = placeHolder
        super().__init__()  # Llama al constructor de la clase ft.Row
        """
        Inicializa el componente `TitleInput`.

        Args:
            text (str, opcional): El texto inicial del cuadro de texto. Por defecto, está vacío.
            value (bool, opcional): El estado inicial de la casilla de verificación. 
                                    Por defecto, es `False` (no completada).
        """
        # Casilla de verificación personalizada
        self.checkbox = ft.Container(
            content=ft.Checkbox(
                scale=1.5,
                check_color=ft.Colors.WHITE,
                fill_color={
                    ft.ControlState.SELECTED: Colors.color_B,
                },
            )
        )

        # Campo de texto con estilos personalizados
        self.text_fild = ft.TextField(
            hint_text=self.placeHolder,
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
        )

        # Ajusta los valores iniciales según los argumentos proporcionados
        if self.__value:
            self.checkbox.content.value = True
        if self.__text:
            self.text_fild.value = self.__text
        else:
            self.text_fild.bgcolor = ft.Colors.with_opacity(0.65, Colors.color_primary)
            self.text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
        self.value = self.text_fild.value

        self.controls = [self.checkbox, self.text_fild]  # Componentes del control
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

    def text_fild__on_blur(self, e):
        """
        Manejador del evento `on_blur` del cuadro de texto.

        Este método ajusta el estilo visual del cuadro de texto cuando pierde el foco.
        Si el cuadro de texto está vacío, se aplica un fondo y un ícono predeterminado.
        """
        if not self.text_fild.value:
            self.text_fild.bgcolor = ft.Colors.with_opacity(0.65, Colors.color_primary)
            self.text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
        else:
            self.text_fild.bgcolor = ft.Colors.TRANSPARENT
            self.text_fild.prefix_icon = ""
        self.text_fild.border = ft.InputBorder.NONE
        self.text_fild.update()

    def text_fild__on_focus(self, e):
        """
        Manejador del evento `on_focus` del cuadro de texto.

        Este método ajusta el estilo visual del cuadro de texto cuando obtiene el foco.
        Se agrega un borde de resaltado y un ícono de edición.
        """
        self.text_fild.prefix_icon = ft.Icons.MODE_EDIT_OUTLINE
        self.text_fild.border = ft.InputBorder.OUTLINE
        self.text_fild.border_color = Colors.color_B
        self.text_fild.update()
