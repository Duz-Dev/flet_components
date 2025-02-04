from assets.components.task_components.btn_delete import BtnDelete, ft
from assets.components.styles import Colors


class BtnFlex(BtnDelete):
    def __init__(
        self,
        text="",
        bgcolor=Colors.color_primary,
        border=ft.border.all(2, color=Colors.color_C),
        bgcolor_hover=Colors.color_secundary,
        padding: ft.PaddingValue = ft.padding.symmetric(20, 30),
        width: int = None,
        height: int = None,
        meta=None,
        click=None,
    ):
        super().__init__(
            padding=padding,
            bgcolor_hover=bgcolor_hover,
            bgcolor=bgcolor,
            border=border,
            widht=width,
            height=height,
            meta=meta,
            text=text,
            click=click,
        )
