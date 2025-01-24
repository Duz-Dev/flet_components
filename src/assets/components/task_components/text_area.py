import flet as ft
from ..styles import Colors, FontSize


class TextArea(ft.Row):
    def __init__(
        self, text: str = "", height: int = 400, widht: int = 400, expand=False
    ):
        super().__init__(expand=1)
        self.text_content: str = text
        self.__height = height
        self.__width = widht
        self.__expand = expand
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value="Escribe una nota...",
                    size=FontSize.normal_font_size,
                    color=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
        )

        self.container = ft.Container(
            bgcolor=Colors.color_C,
            expand=self.__expand,
            content=self.content,
            width=self.__width,
            height=self.__height,
            on_hover=self.on_hover,
            # border = ft.border.all(3, ft.Colors.WHITE),
            border_radius=5,
            border=ft.border.all(1, ft.Colors.with_opacity(0.6, ft.Colors.WHITE)),
            on_click=self.on_click,
            padding=10,
        )

        self.container_input = ft.TextField(
            # bgcolor=Colors.color_A,
            expand=True,
            multiline=True,
            text_size=FontSize.normal_font_size,
            border="none",
            # on_focus=prueba
            on_blur=self.view_markdown,
        )

        self.controls = [self.container]

    def view_markdown(self, e, text=None):
        if not text:
            text = self.container_input.value

        container_markdown = ft.Markdown(
            value=text,
            extension_set="gitHubWeb",
            code_theme="atom-one-dark",
            code_style_sheet=ft.TextStyle(font_family="Roboto Mono"),
            expand=1,
        )

        # Agregar scroll al contenido
        scrollable_content = ft.Column(
            controls=[container_markdown],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        self.container.content = scrollable_content
        self.container.update()

    def on_click(self, e):
        self.container.content = self.container_input
        self.container.update()
        self.container_input.focus()

    def on_hover(self, e):

        if (
            e.data == "true"  # Hover activo
            and not self.container_input.value  # No hay texto en el input
            and not self.text_content  # No hay texto en componente por defecto
        ):
            self.container.border = ft.border.all(1, ft.Colors.WHITE)
            self.container.content = self.content
            self.content.controls[0].color = ft.Colors.WHITE
            self.content.update()
        else:  # Hover desactivado

            self.container.border = ft.border.all(
                1, ft.Colors.with_opacity(0.6, ft.Colors.WHITE)
            )
            if not self.container_input.value:  # se salio del foco y no exite texto
                self.container.content = self.content
                self.content.controls[0].color = ft.Colors.with_opacity(
                    0.6, ft.Colors.WHITE
                )
                self.load_text()

        self.container.update()

    def load_text(self):
        if self.text_content:
            text = self.text_content
            self.view_markdown(None, text)

    def did_mount(self):
        # Metodo especial de flet. Se ejecuta despues de que el componente se renderiza.
        self.load_text()

    def get_text(self) -> str | None:
        """
        ### Get text
        Devuelve el texto del componente TextArea.

        Returns:
        - str: Texto del componente TextArea.
        Si el componente cuenta con un texto por defecto, este se retornara si no se ha modificado el contenido del componente.
        """
        if self.container_input.value:
            return self.container_input.value
        elif self.text_content:
            return self.text_content
        else:
            return None


# text_area = TextArea()


# text_area = ft.Row(controls=[container])


# def maint(page: ft.Page):
#     page.bgcolor = Colors.color_primary
#     text_area = TextArea(text="asd")
#     page.add(text_area)


# ft.app(target=maint, assets_dir="assets")
