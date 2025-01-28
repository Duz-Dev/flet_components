import flet as ft
from ..styles import Colors, FontSize


class Date(ft.Container):
    """
    Un componente personalizado para mostrar una fecha.

    El componente `Date` combina un texto de plantilla ("Fecha:") con una fecha especificada por el usuario.
    Es ideal para aplicaciones que necesiten mostrar fechas con un formato específico de manera consistente.

    Este componente se construye sobre el control `Container` de Flet y utiliza una fila (`Row`) para alinear el texto de la plantilla y la fecha.

    Ejemplo:

    ```
    import flet as ft

    def main(page: ft.Page):
        date_display = Date(date="25 - 01 - 2025", template="Fecha:")
        page.add(date_display)

    ft.app(target=main)
    ```
    -----

    Observación: Puedes modificar directamente  el control del template o del date haciendo referencia a los Atributos ``text_template`` y ``text_date`` respectivamente.

    -----

    Online docs: (Enlace a documentación personalizada si aplica)
    """

    def __init__(self, date: str = "DD - MM - YYYY", template: str = None):

        super().__init__()
        self.date = date
        self.text_template: ft.Text = ft.Text(
            value=template, size=FontSize.normal_font_size, weight=ft.FontWeight.W_600
        )
        self.text_date = ft.Text(
            value=date,
            size=FontSize.normal_font_size,
            weight=ft.FontWeight.W_600,
        )
        self.content = ft.Row(controls=[self.text_template, self.text_date])
