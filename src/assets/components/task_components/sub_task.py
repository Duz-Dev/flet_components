import flet as ft
import time
from ..styles import Colors


class SubTaskList(ft.Column):
    def __init__(self):
        super().__init__(expand=1)
        self.subtasks_list: list[ft.ListTile] = []  # Lista de subtareas
        self.list_view = ft.ListView(expand=1, spacing=4)
        self.add_item = self._create_add_item()
        self.list_view.controls.append(self.add_item)
        self.controls = [self.list_view]

    def _create_add_item(self):
        """Crea el botón de añadir nueva subtarea."""
        return ft.ListTile(
            title=ft.Text("Añadir sub tarea"),
            leading=ft.Container(
                content=ft.Icon(
                    name=ft.Icons.ADD,
                    color=ft.Colors.with_opacity(0.4, ft.Colors.WHITE),
                ),
                padding=ft.padding.only(left=2.1),
            ),
            bgcolor=Colors.color_secundary,
            text_color=ft.Colors.with_opacity(0.4, ft.Colors.WHITE),
            on_click=self.builder_sub_task,
        )

    def builder_sub_task(self, e: ft.ControlEvent):
        """Crea una nueva subtarea y la añade a la lista."""
        sub_task = self._create_sub_task()
        self.subtasks_list.append(sub_task)
        self.update_list_view()
        sub_task.title.focus()

    def _create_sub_task(self):
        """Crea una subtarea individual con su lógica de eventos."""

        def delete_sub_task(e):
            """Elimina una subtarea con animación."""
            sub_task.bgcolor = ft.Colors.RED
            sub_task.offset = ft.transform.Offset(-2, 0)
            sub_task.update()
            time.sleep(0.55)  # Duración de la animación
            self.subtasks_list.remove(sub_task)
            self.update_list_view()

        def change_title_sub_task(e):
            """Intercambia entre texto estático y editable."""
            if isinstance(sub_task.title, ft.TextField):
                if not sub_task.title.value:
                    sub_task.title = ft.Container(
                        content=ft.Text(
                            value=f"New Sub Task {len(self.subtasks_list)}",
                        ),
                        on_click=change_title_sub_task,
                    )
                else:
                    sub_task.title = ft.Container(
                        content=ft.Text(
                            value=sub_task.title.value,
                        ),
                        on_click=change_title_sub_task,
                    )
            else:
                sub_task.title = ft.TextField(
                    value=sub_task.title.content.value,
                    border_color=Colors.color_state_progress,
                    on_blur=change_title_sub_task,
                )
                sub_task.update()
                sub_task.title.focus()
            sub_task.update()

        sub_task = ft.ListTile(
            title=ft.TextField(
                border_color=Colors.color_state_progress,
                on_blur=change_title_sub_task,
            ),
            leading=ft.Container(
                content=ft.Checkbox(
                    scale=1.1,
                    check_color=ft.Colors.WHITE,
                    fill_color={
                        ft.ControlState.SELECTED: Colors.color_state_progress,
                    },
                ),
            ),
            bgcolor=Colors.color_secundary,
            text_color=ft.Colors.WHITE,
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(
                400, curve=ft.AnimationCurve.EASE_IN_BACK
            ),
            on_long_press=delete_sub_task,
        )
        return sub_task

    def update_list_view(self):
        """Actualiza el control ListView para reflejar los cambios."""
        self.list_view.controls.clear()
        self.list_view.controls.extend(self.subtasks_list)
        self.list_view.controls.append(self.add_item)
        self.list_view.update()

    def count_sub_tasks(self) -> tuple[int, int]:
        """Cuenta subtareas totales y completadas."""
        num = len(self.subtasks_list)
        is_true = sum(1 for i in self.subtasks_list if i.leading.content.value)
        return num, is_true
