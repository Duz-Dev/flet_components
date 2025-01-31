import flet as ft

from ..styles import Colors, FontSize


class BtnDelete(ft.Container):
    def __init__(
        self,
        text: str = None,
        click=None,
        bgcolor: ft.Colors = "#23272a",
        bgcolor_hover: ft.Colors = ft.Colors.with_opacity(0.7, "red"),
        padding: ft.PaddingValue = ft.padding.symmetric(20, 30),
        widht: int = None,
        height: int = None,
        border: ft.border = ft.border.all(2, "red"),
        border_radius: ft.border_radius = 5,
    ):
        super().__init__()
        self.__text = text
        self.bgcolor = bgcolor
        self.bgcolor_hover = bgcolor_hover
        self.__padding = padding
        self.width = widht
        self.height = height
        self.__on_click = click
        if not text:
            self.__text = " "

        self.content = ft.ElevatedButton(
            bgcolor={
                ft.ControlState.DEFAULT: self.bgcolor,
                ft.ControlState.HOVERED: self.bgcolor_hover,
            },
            color=ft.Colors.WHITE,
            content=ft.Text(
                value=self.__text, size=FontSize.h3_size, weight=ft.FontWeight.W_600
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
                padding=self.__padding,
            ),
            on_click=self.__on_click,
            height=self.height,
            width=self.width,
        )
        self.border = border
        self.border_radius = border_radius

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
        self.content.content.value = self.__text

    @property
    def click(self):
        return self.__on_click

    @click.setter
    def click(self, on_click):
        self.__on_click = on_click
        self.content.on_click = self.__on_click
