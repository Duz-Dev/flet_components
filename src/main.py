import flet as ft
import assets.components as fc  # estilos globales
import assets.components.task_components as tc  # componentes de task_components

# import task


def main(page: ft.Page):
    # page.add(tc.Base(title="practice"))
    # page.add(
    #     tc.BtnDelete(
    #         text="edit",
    #         on_click=lambda e: print("hola mundo"),
    #     )
    # )
    # page.add(tc.Date("28-12-2002", template="Fecha:"))  # listo
    # progreso = tc.ProgressBar()
    # progreso.state_progress(5, 3)
    # page.add(progreso)
    # page.add(tc.State())
    # sub = tc.SubTaskList()
    # prueba = tc.BtnDelete("prueba", on_click=lambda e: print(sub.count_sub_tasks()))
    # page.add(sub, prueba)
    # Crear una instancia de SubTaskList
    # Crear una instancia de SubTaskList
    sub_task_list = tc.SubTaskList()

    # Añadir subtareas externamente
    sub_task_list.add_subTask("Subtarea 1", True)  # Checkbox marcado
    sub_task_list.add_subTask("Subtarea 2", False)  # Checkbox sin marcar
    page.add(sub_task_list)
    # Añadir subtareas externamente
    # sub_task_list.did_mount("Subtarea 1", True)  # Checkbox marcado
    # sub_task_list.did_mount("Subtarea 2", False)  # Checkbox sin marcar


ft.app(main)
