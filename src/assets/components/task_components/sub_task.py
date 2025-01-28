import flet as ft
import time
from ..styles import Colors


class SubTaskList(ft.Column):
    """
    Una lista personalizada de subtareas con soporte para agregar, eliminar y actualizar tareas.

    `SubTaskList` permite gestionar una lista interactiva de subtareas, proporcionando funcionalidades
    para añadir nuevas subtareas, actualizar su estado y eliminarlas tanto desde la interfaz gráfica
    como programáticamente.

    Ejemplo:

    ```python
    import flet as ft
    from this.modulo import SubTaskList

    def main(page: ft.Page):
        task_list = SubTaskList(expand=True)
        page.add(task_list)

        # Agregar subtareas desde código
        task_list.add_subTask("Subtarea 1", is_completed=False)
        task_list.add_subTask("Subtarea 2", is_completed=True)

        # Contar subtareas totales y completadas
        total, completadas = task_list.count_subTask()
        print(f"Total: {total}, Completadas: {completadas}")

    ft.app(target=main)
    ```

    -----

    Online docs: (Enlace a documentación personalizada si aplica)
    """

    def __init__(
        self, text_add: str = "add", text_subTask: str = "New Sub Task", expand=None
    ):

        super().__init__()
        """
        Inicializa una instancia de `SubTaskList`.

        Args:
            text_add (str): Texto que se mostrará en el botón para añadir subtareas.
            text_subTask (str): Texto por defecto para una nueva subtarea.
            expand (bool, opcional): Define si el componente expandirá su tamaño.
        """
        self.expand = expand
        self.subtasks_list: list[ft.ListTile] = []  # Lista de subtareas
        self.list_view = ft.ListView(expand=1, spacing=4)
        self.text_add = text_add
        self.text_subTask = text_subTask
        self.add_item = self._create_add_item(self.text_add)
        self.list_view.controls.append(self.add_item)
        self.controls = [self.list_view]
        self.pending_subtasks = []  # Cola temporal de subtareas externas

    def _create_add_item(self, text: str):
        """
        Crea el botón para añadir nuevas subtareas.

        Args:
            text (str): Texto que se mostrará en el botón.

        Returns:
            ft.ListTile: Botón configurado como una lista interactiva.
        """
        return ft.ListTile(
            title=ft.Text(value=text),
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

    def builder_sub_task(self, e: ft.ControlEvent = None):
        """
        Evento que crea y agrega una nueva subtarea a la lista cuando se presiona el botón de añadir.
        """
        sub_task = self._create_sub_task()
        self.subtasks_list.append(sub_task)
        self.update_list_view()
        sub_task.title.focus()

    def _create_sub_task(
        self, title: str = "new task", is_completed: bool = False, external=False
    ):
        """
        Crea un objeto de subtarea configurado.

        Args:
            title (str): Título de la subtarea.
            is_completed (bool): Estado inicial de la subtarea (completada o no).
            external (bool): Define si la subtarea proviene de una fuente externa.

        Returns:
            ft.ListTile: Subtarea configurada.
        """

        def delete_sub_task(e):
            """
            Elimina la subtarea tras una animación de retroceso.
            """
            sub_task.bgcolor = ft.Colors.RED
            sub_task.offset = ft.transform.Offset(-2, 0)
            sub_task.update()
            time.sleep(0.55)  # Duración de la animación
            self.subtasks_list.remove(sub_task)
            self.update_list_view()

        def change_title_sub_task(e):
            """
            Cambia el título de la subtarea entre un `Text` y un `TextField`.
            """
            if isinstance(sub_task.title, ft.TextField):
                if not sub_task.title.value:
                    sub_task.title = ft.Container(
                        content=ft.Text(
                            value=self.text_subTask,
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

        if external:
            content_title = ft.Container(
                content=ft.Text(value=title),
                on_click=change_title_sub_task,
            )
        else:
            content_title = ft.TextField(
                border_color=Colors.color_state_progress,
                on_blur=change_title_sub_task,
            )

        sub_task = ft.ListTile(
            title=content_title,
            leading=ft.Container(
                content=ft.Checkbox(
                    scale=1.1,
                    check_color=ft.Colors.WHITE,
                    fill_color={
                        ft.ControlState.SELECTED: Colors.color_state_progress,
                    },
                    value=is_completed,
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
        """
        Actualiza la vista de la lista con las subtareas actuales.
        """
        self.list_view.controls.clear()
        self.list_view.controls.extend(self.subtasks_list)
        self.list_view.controls.append(self.add_item)
        self.list_view.update()

    def count_subTask(self) -> tuple[int, int]:
        """
        Cuenta el número total de subtareas y las completadas.

        Returns:
            tuple[int, int]: Una tupla que contiene el total de subtareas y el número de subtareas completadas.

        Observación:
            - Este método itera sobre `subtasks_list` para calcular cuántas subtareas están marcadas como completadas.
            - Optimizable en listas muy grandes si se usan mecanismos alternativos para llevar un conteo.
        """
        num = len(self.subtasks_list)
        is_true = sum(1 for i in self.subtasks_list if i.leading.content.value)
        return num, is_true

    def add_subTask(self, title: str, is_completed: bool):
        """
        Añade una subtarea desde una fuente externa.

        Args:
            title (str): Título de la subtarea.
            is_completed (bool): Define si la subtarea debe añadirse como completada.

        Observación:
            - Si el componente no está montado, almacena la subtarea en una cola temporal (`pending_subtasks`).
            - Esto asegura que subtareas externas se integren tras el montaje con `did_mount()`.
        """
        if not hasattr(self, "page") or not self.page:
            self.pending_subtasks.append((title, is_completed))
        else:
            sub_task = self._create_sub_task(
                title=title, is_completed=is_completed, external=True
            )
            self.subtasks_list.append(sub_task)
            self.update_list_view()

    def did_mount(self):
        """
        Procesa las subtareas pendientes tras montar el control en la página.
        """
        for title, is_completed in self.pending_subtasks:
            self.add_subTask(title, is_completed)
        self.pending_subtasks.clear()
