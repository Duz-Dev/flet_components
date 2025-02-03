import flet as ft
import assets.components as fc
import assets.components.task_components as tc
from assets.components.styles import Colors


class Task(tc.Base):
    """
    modal experimental que contiene todos los controles personalizados del modulo task.

    Args:
        title (str): Titulo a colocar por encima del modal.
        on_close (OptionalEventCallable): evento que se ejecuta cuando le das click al boton superior derecho (x).
    """

    def __init__(
        self, title: str = None, on_close: ft.OptionalEventCallable = None, data=None
    ):
        self.__data = data
        # Componentes
        self.TextArea = tc.TextArea(widht=None, expand=True, height=200)
        self.SubTaskList = tc.SubTaskList(expand=1)
        self.TitleInput = tc.TitleInput()
        self.Date = tc.Date(template="fecha:")
        self.State = tc.State()
        self.ProgressBar = tc.ProgressBar(value=0)
        self.__BtnDelete = tc.BtnDelete(
            text="Save task",
            bgcolor=Colors.color_primary,
            border=ft.border.all(2, color=Colors.color_C),
            bgcolor_hover=Colors.color_secundary,
            meta=self.__data,
        )

        self.on_close = on_close
        self.__row3 = ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[self.__BtnDelete],
        )

        self.controls = [
            self.TitleInput,
            ft.Row(
                [self.Date, self.State],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Row(
                [ft.Container(content=self.ProgressBar, width=67)],
                alignment=ft.MainAxisAlignment.END,
            ),
            self.TextArea,
            self.SubTaskList,
            self.__row3,
        ]

        super().__init__(
            padding=30,
            height=600,
            width=530,
            controls=self.controls,
            close_function=self.on_close,
        )
        self.title = title

    @property
    def BtnDelete(self):
        self.__BtnDelete = self.__row3.controls[0]
        return self.__BtnDelete

    @BtnDelete.setter
    def BtnDelete(self, BtnDelete):
        self.__BtnDelete = BtnDelete
        self.__row3.controls[0] = self.__BtnDelete

    @property
    def data(self):
        self.__data = self.__BtnDelete.data
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
        self.__BtnDelete.data = self.__data
