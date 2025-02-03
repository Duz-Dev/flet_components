import dash_task

# import flet as ft
# import assets.components.ui.task as task
# import assets.components.task_components as tc

# key_active = [None]  # Guarda la ultima tecla oprimida


# def main(page: ft.Page):
#     list_TKs = []  # Lista de TK creados
#     modal_tk = ft.AlertDialog(actions_padding=0)  # Modal para mostrar los TK

#     # Captura las tecla oprimida y la guarda en key_active. Posiblemente para extener en un futuro atajos.
#     def keys(e):
#         global key_active
#         key_active[0] = e.key.lower()

#     page.on_keyboard_event = keys

#     def close_modal(e):
#         if key_active[0] == "Escape":
#             page.close(modal_tk)
#         page.close(modal_tk)

#     def create_TK(e):
#         TK = task.Task("Nueva Tarea", on_close=close_modal)  # creo un TK
#         modal_tk.actions = [TK]  # Enlazo el modal con el TK
#         list_TKs.append(TK)  # Guardo el TK
#         page.open(modal_tk)  # Abro el modal en pantalla

#     def load_TK(e):
#         if list_TKs:  # Si existen TK's  en la lista, entonces:
#             ultimo_tk = [list_TKs[-1]]  # cargo el ultimo añadido
#             modal_tk.actions = ultimo_tk  # enlazo al modal el ultimo añadido
#             page.open(modal_tk)  # abro el modal

#     btn_añadir = tc.BtnDelete("nueva tarea", click=create_TK)
#     btn_cargar = tc.BtnDelete("Mostrar tarea", click=load_TK)

#     page.add(btn_añadir, btn_cargar)


# ft.app(target=main, assets_dir="assets")
