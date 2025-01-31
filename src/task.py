import flet as ft
import assets.components as fc
import assets.components.task_components as tc


class Task(tc.Base):
    def __init__(self, title: str = None, on_click: ft.OptionalEventCallable = None):
        self.title = title
        # Componentes
        self.TextArea = tc.TextArea(widht=None, expand=True, height=200)
        self.SubTaskList = tc.SubTaskList(expand=1)
        self.TitleInput = tc.TitleInput()
        self.Date = tc.Date(date="10 - 05 - 2025", template="fecha:")
        self.State = tc.State()
        self.ProgressBar = tc.ProgressBar(value=0)
        self.BtnDelete = tc.BtnDelete(text="Eliminar")

        self.__on_click = on_click

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
            close_function=self.__on_click,
        )
