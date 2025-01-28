import flet as ft
import assets.components as fc  # estilos globales
import assets.components.task_components as tc  # componentes de task_components

import task


def main(page: ft.Page):
    page.add(tc.Base(title="practice"))
    page.add(
        tc.BtnDelete(
            text="edit",
            on_click=lambda e: print("hola mundo"),
        )
    )
    page.add(tc.Date("28-12-2002", template="Fecha:"))  # listo
    progreso = tc.ProgressBar()
    progreso.state_progress(5, 3)
    page.add(progreso)
    state = tc.State()
    state1 = tc.State()
    state1.state_colors(1)
    state2 = tc.State()
    state2.state_colors(2)
    state3 = tc.State()
    state3.state_colors(3)
    page.add(state, state1, state2, state3)
    sub = tc.SubTaskList()
    prueba = tc.BtnDelete("prueba", on_click=lambda e: print(sub.count_subTask()))
    page.add(sub, prueba)
    item = tc.TextArea(
        text="""
## Images


![Test image](https://picsum.photos/200/300)

## Tables

|Syntax                                 |Result                               |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
|`**bold 1**`                           |**bold 1**                           |
|`__bold 2__`                           |__bold 2__                           |
|`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
|`***italic bold 1***`                  |***italic bold 1***                  |
|`___italic bold 2___`                  |___italic bold 2___                  |
|`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
|`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|
                       
""",
        expand=1,
        height=None,
    )
    page.add(item)
    title = tc.TitleInput(text="prueba", value=True, placeHolder="lol")
    page.add(title)


ft.app(main)
