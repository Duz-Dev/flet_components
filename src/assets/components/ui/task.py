import flet as ft
import assets.components as fc
import assets.components.task_components as tc


class Task(tc.Base):
    """
    modal experimental que contiene todos los controles personalizados del modulo task.

    Args:
        title (str): Titulo a colocar por encima del modal.
        on_close (OptionalEventCallable): evento que se ejecuta cuando le das click al boton superior derecho (x).
    """

    def __init__(self, title: str = None, on_close: ft.OptionalEventCallable = None):
        self.title = title
        # Componentes
        self.TextArea = tc.TextArea(widht=None, expand=True, height=200)
        self.SubTaskList = tc.SubTaskList(expand=1)
        self.TitleInput = tc.TitleInput()
        self.Date = tc.Date(date="10 - 05 - 2025", template="fecha:")
        self.State = tc.State()
        self.ProgressBar = tc.ProgressBar(value=0)
        self.BtnDelete = tc.BtnDelete(text="Eliminar")

        self.on_close = on_close

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
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[self.BtnDelete],
            ),
        ]

        super().__init__(
            padding=30,
            title=self.title,
            height=600,
            width=530,
            controls=self.controls,
            close_function=self.on_close,
        )
