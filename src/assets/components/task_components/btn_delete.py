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
        meta=None,
    ):
        """

        meta = data
        """
        super().__init__()
        self.__text = text
        self.bgcolor = bgcolor
        self.bgcolor_hover = bgcolor_hover
        self.__padding = padding
        self.width = widht
        self.height = height
        self.__click = click
        self.__meta = meta
        self.border = border
        self.border_radius = border_radius

        self.__btn = ft.ElevatedButton(
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
            on_click=self.__click,
            height=self.height,
            width=self.width,
            data=self.__meta,
        )
        self.content = self.__btn

        if not text:
            self.__text = " "

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
        self.content.content.value = self.__text

    @property
    def click(self):
        return self.__click

    @click.setter
    def click(self, click):
        self.__click = click
        self.__btn.on_click = self.__click

    @property
    def meta(self):
        self.__meta = self.__btn.data
        return self.__meta

    @meta.setter
    def meta(self, meta):
        self.__meta = meta
        self.__btn.data = self.__meta
