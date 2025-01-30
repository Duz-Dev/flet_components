import flet as ft
from io import BytesIO
from PIL import ImageGrab
import base64
import time


def main(page: ft.Page):
    img_control = ft.Image()
    ProgressBar = ft.ProgressBar(value=0, height=20)
    alert = ft.AlertDialog(
        title=ft.Column(
            [
                ft.Text(
                    "No se encontro una imagen en el portapapeles, intenta nuevamente.",
                    text_align="center",
                ),
                ProgressBar,
            ],
            spacing=30,
        )
    )

    def pegar_imagen(e):
        img = ImageGrab.grabclipboard()  # Captura la imagen del portapapeles
        if img:
            buffer = BytesIO()
            img.save(buffer, format="PNG")  # Guarda la imagen en el buffer como PNG
            img_bytes = buffer.getvalue()  # Obtén los datos binarios de la imagen
            base64_img = base64.b64encode(img_bytes).decode("utf-8")
            # Codifica a base64
            img_control.src_base64 = base64_img
            page.add(img_control)
        else:
            page.open(alert)
            count()

    btn = ft.FilledButton("Pegar Imagen", on_click=pegar_imagen)
    page.add(btn)

    def count():
        for i in range(0, 101):
            ProgressBar.value = i * 0.01
            time.sleep(0.02)
            page.update()
        page.close(alert)


ft.app(main, assets_dir="assets")
