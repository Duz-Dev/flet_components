# import task

# import test
import flet as ft
import assets.components.task_components as tc


def main(page: ft.Page):
    page.bgcolor = "#32353a"

    code = """
```
text_area = tc.TextArea(text=code, widht=None, expand=1)

    def copiar_texto(e):

        page.set_clipboard(
            text_area.get_text()
        )  # Esta linea es la que se encarga de copiar el texto a el portapapeles.

    btn_clip = tc.BtnDelete("copiar texto", on_click=copiar_texto)
```    
"""
    text_area = tc.TextArea(text=code, widht=None, expand=1)

    def copiar_texto(e):

        page.set_clipboard(
            text_area.get_text().replace("`", "").strip()
        )  # Esta linea es la que se encarga de copiar el texto a el portapapeles.

    btn_clip = tc.BtnDelete("copiar texto", on_click=copiar_texto)

    # page.add(text_area, btn_clip)

    def procesar_markdown_y_componentes(markdown_text):
        # Define un marcador para identificar componentes
        marcador_boton = "{clipBoard}"
        partes = markdown_text.split(marcador_boton)

        # Crea una lista de controles para agregar al diseño
        controles = []
        for i, parte in enumerate(partes):
            controles.append(ft.Markdown(value=parte))
            # Inserta el clipBoard después de cada marcador
            if i < len(partes) - 1:
                controles.append(text_area)
                controles.append(btn_clip)
        return controles

    contenido = """
# Título

Esto es un botón de Flet:
{clipBoard}
Aquí termina el Markdown.
    """
    controles = procesar_markdown_y_componentes(contenido)
    page.add(ft.Column(controls=controles))


ft.app(target=main, assets_dir="assert")
