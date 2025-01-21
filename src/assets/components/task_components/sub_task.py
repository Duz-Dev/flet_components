import flet as ft  # Importa flet
import time
from ..styles import (
    Colors,
)  # Importa estilos globales(paleta de colores)

subtasks_list: list[ft.ListTile] = (
    []
)  # Contendra cada una de las subtareas [item] creadas


def builder_sub_task(e: ft.ControlEvent):
    """
    ### builder sub_task
    Gestiona el comportamiento de las subtarea [sub_task].
    - Crea un sub_task(list_title) y lo añade a la lista de sub-tareas [subtasks_list]
    - Cambia el comportamento del texto [sub_task.title] que contiene la subtarea en base diferentes estados.
    - Elimina la tarea de la lista de tareas, junto con una animacion :D

    Args:
        e (ft.ControlEvent): argumento que introduce flet por defecto caundo la funcion es llamado por algun evento.
    variables:
    sub_task: Contiene el item que sera añadido a la `subtasks_list`
    """

    def delete_sub_task(e):
        """
        ### Delete sub_task
        Elimina la tarea seleccionada al dejar precionado sobre alguno de los elementos de la lista. Añadiendo un toque con una animacion especial :D
        """
        sub_task.bgcolor = ft.Colors.RED
        sub_task.offset = ft.transform.Offset(-2, 0)
        sub_task.update()
        time.sleep(
            0.55
        )  # La duracion de espera es igual a lo que dura la animacion de la sub_tarea
        subtasks_list.remove(sub_task)
        update_listView_SubTasks()

    def ChangeTitle_sub_task(e):
        """
        ### Change Title sub_task
        Cambia el texto de la sub tarea [sub_task.title] en base a el estado que se espera. Con estado me refiero a los comportamientos posibles que se pueden llevar para editar el texto de la tarea, intercambiando entre un control de entrada de texto [TextFild] y un contenedor [Container] que contiene un texto [Text].

        Args:
            e (_type_): Parametro obligatorio cuando se es llamada la funcion desde un evento.
        """
        if isinstance(sub_task.title, ft.TextField):
            if not sub_task.title.value:
                sub_task.title = ft.Container(
                    content=ft.Text(
                        value=f"New Sub Task {len(subtasks_list)}",
                    ),
                    on_click=ChangeTitle_sub_task,
                )
            else:
                sub_task.title = ft.Container(
                    content=ft.Text(
                        value=sub_task.title.value,
                    ),
                    on_click=ChangeTitle_sub_task,
                )  # ?titulo de la sub-tarea
        else:  # Si no es un textFild, entonces es el ft.Container
            sub_task.title = ft.TextField(
                value=sub_task.title.content.value,
                border_color=Colors.color_state_progress,
                on_blur=ChangeTitle_sub_task,
            )
            sub_task.update()
            sub_task.title.focus()
        sub_task.update()

    # >>> SUB TAREA [sub_task]<<<

    sub_task = ft.ListTile(
        # texto de la tarea
        title=ft.TextField(
            border_color=Colors.color_state_progress,
            on_blur=ChangeTitle_sub_task,
        ),
        # Checkbox de la tarea
        leading=ft.Container(
            content=ft.Checkbox(
                scale=1.1,
                check_color=ft.Colors.WHITE,
                fill_color={
                    ft.ControlState.SELECTED: Colors.color_state_progress,
                },
                # on_change=count_sub_task,
            ),
        ),
        # Estilos y animaciones de la sub tarea
        bgcolor=Colors.color_secundary,
        text_color=ft.Colors.WHITE,
        offset=ft.transform.Offset(0, 0),
        animate_offset=ft.animation.Animation(
            400, curve=ft.AnimationCurve.EASE_IN_BACK
        ),
        on_long_press=delete_sub_task,
        # data=,  # meta data para utilizar mas adelante
    )
    # Añado la sub tarea a la lista de sub tareas
    subtasks_list.append(sub_task)
    # llamo a la funcion que actualiza el control para visualizar las sub-tareas
    update_listView_SubTasks()
    # indico que quiero  que haga focus sobre el texto (en este caso seria un textFild) namas cargada la tarea en el visualizador [listView_subtasks]
    sub_task.title.focus()


def update_listView_SubTasks():
    """
    ### Update
    Limpia el view, lo "extiende" añadiendole un la lista, añade al final el [add_item] y actualiza el control.
    """
    listView_subtasks.controls.clear()
    listView_subtasks.controls.extend(
        subtasks_list
    )  # ya que append esta pensado para adjuntar un solo elemento, extend es util en este caso ya que nos permite adjuntar una lista(iterable).
    listView_subtasks.controls.append(add_item)
    listView_subtasks.update()
    # count_sub_task()


def count_sub_task(e=None) -> tuple[int, int]:
    """
    ### Count sub_tasks
    Hace un conteo de:
    - Cantidad de sub-tareas actuales
    - Total de sub-tareas terminadas (check = true)

    args:

    e (ft.ControlEvent): argumento necesario si la funcion es llamada por un evento.

    return:

    num: Cantidad de sub-tareas
    is_true: cantidad de sub-tareas terminadas
    """
    num = len(subtasks_list)
    is_true = 0
    for i in subtasks_list:
        if i.leading.content.value:
            is_true += 1
    # print(f"Existen en total {num} sub-tareas y solo {is_true} estan completas")
    return num, is_true


# ?Control que contendra la lista de [subtasks_list]
listView_subtasks = ft.ListView(
    expand=1,
    spacing=4,
)  # Sin el expand=true, no se va conportar con el efecto de scroll

# ?Control que sera el responsable de añadir una nueva tarea
add_item = ft.ListTile(
    title=ft.Text(
        "Añadir sub tarea",
    ),
    leading=ft.Container(
        content=ft.Icon(
            name=ft.Icons.ADD, color=ft.Colors.with_opacity(0.4, ft.Colors.WHITE)
        ),
        padding=ft.padding.only(left=2.1),
    ),
    bgcolor=Colors.color_secundary,
    text_color=ft.Colors.with_opacity(0.4, ft.Colors.WHITE),
    on_click=builder_sub_task,
)

#!Por defecto, el ListView tendra de momento el [add_item]
listView_subtasks.controls.append(add_item)
