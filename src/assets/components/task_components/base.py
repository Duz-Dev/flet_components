import flet as ft
from ..styles import Colors


class Base(ft.Container):
    """
    Un componente base personalizado que actúa como un contenedor flexible y estilizado,
    compuesto por una cabecera con un título y un botón para cerrar, junto con un área de contenido principal.

    Este componente es útil para crear ventanas modales, paneles de información o secciones con un encabezado.

    Atributos:
        controls (list[ft.Control]): Lista de controles que se colocarán en el contenido principal del componente.
        title (str): Título que se mostrará en la cabecera del componente.
        padding (ft.PaddingValue): Espaciado interno del área de contenido principal.
        close_function (callable): Función que se ejecutará al presionar el botón de cerrar.
        width (int): Ancho del componente principal en píxeles. Por defecto, 600.
        height (int): Altura del área de contenido principal en píxeles. Por defecto, 100.
        expand (bool): Define si el área de contenido principal se expandirá para ocupar el espacio disponible.

    Ejemplo:
        ```python
        import flet as ft
        from mymodule import Base

        def close_handler(e):
            print("Ventana cerrada.")

        def main(page: ft.Page):
            base_component = Base(
                title="Mi Ventana",
                controls=[
                    ft.Text("Este es el contenido principal."),
                ],
                close_function=close_handler,
                width=500,
                height=200,
                padding=ft.padding.all(20),
            )
            page.add(base_component)

        ft.app(target=main)
        ```
    """

    def __init__(
        self,
        controls: list[ft.Control] = [],
        title: str = None,
        padding: ft.PaddingValue = None,
        close_function=None,
        width: int = 600,
        height: int = 100,
        expand: bool = None,
    ):

        self.controls = controls
        super().__init__()  # Inicializa la clase padre `ft.Container`.
        """
        Inicializa un componente `Base`.

        Args:
            controls (list[ft.Control], opcional): Controles que se mostrarán en el área principal.
                                                   Por defecto, lista vacía.
            title (str, opcional): Título que aparece en la cabecera. Por defecto, `None`.
            padding (ft.PaddingValue, opcional): Espaciado interno del contenido principal. Por defecto, `None`.
            close_function (callable, opcional): Función que se ejecuta al presionar el botón de cerrar. Por defecto, `None`.
            width (int, opcional): Ancho del componente. Por defecto, 600.
            height (int, opcional): Altura del contenido principal. Por defecto, 100.
            expand (bool, opcional): Indica si el contenido principal debe expandirse. Por defecto, `None`.
        """
        self.content_width = width
        self.content_height = height
        self.__padding = padding
        self.close = close_function
        self.title = title
        self.expand = expand

        # Configuración del contenido principal
        self.content = ft.Column(
            controls=[
                # Contenedor superior (cabecera con título y botón de cerrar)
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(value=title, size=32, weight=ft.FontWeight.BOLD),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE_SHARP,
                                icon_size=30,
                                icon_color=ft.Colors.WHITE,
                                on_click=self.close,
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
                # Contenedor inferior (contenido principal)
                ft.Container(
                    bgcolor=Colors.color_secundary,
                    expand=self.expand,
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
            spacing=0,
        )
