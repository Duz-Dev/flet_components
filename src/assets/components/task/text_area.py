import flet as ft 
from ..styles import Colors, FontSize

content = ft.Column(
    controls=[
        ft.Text(
            value="Escribe una nota...",
            size=FontSize.normal_font_size,
            color=ft.Colors.with_opacity(.6, ft.Colors.WHITE)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

def on_hover(e):
    if e.data == "true" and not container_input.value:  # Hover activo
        container.border = ft.border.all(1, ft.Colors.WHITE)
        container.content = content
        content.controls[0].color = ft.Colors.WHITE
        content.update()
    else:  # Hover desactivado
        
        container.border = ft.border.all(1, ft.Colors.with_opacity(.6, ft.Colors.WHITE))
        if not container_input.value:
            print("se salio del foco y no exite texto")
            container.content = content
            content.controls[0].color = ft.Colors.with_opacity(.6, ft.Colors.WHITE)
    container.update()
    
def view_markdown(e):
    container_markdown = ft.Markdown(
        value=container_input.value,
        extension_set="gitHubWeb",
        code_theme="atom-one-dark",
        code_style_sheet=ft.TextStyle(font_family="Roboto Mono"),
        expand=1,
    )
    
    # Agregar scroll al contenido
    scrollable_content = ft.Column(
        controls=[container_markdown],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    
    container.content  = scrollable_content
    container.update()

container_input = ft.TextField(
    # bgcolor=Colors.color_A,
    expand=True,
    multiline=True,
    text_size=FontSize.normal_font_size,
    border= "none",
    # on_focus=prueba
    on_blur=view_markdown
)
    
    
def on_click(e):
    # text_area.controls[0] = container_input
    # text_area.update()
    container.content = container_input
    container.update()
    container_input.focus()
    

container = ft.Container(
        bgcolor=Colors.color_C,
        expand=True,
        content=content,
        height=470,
        on_hover=on_hover,
        # border = ft.border.all(3, ft.Colors.WHITE),
        border_radius=5,
        border = ft.border.all(1, ft.Colors.with_opacity(.6, ft.Colors.WHITE)),
        on_click=on_click,
        padding=10,
)




text_area = ft.Row(
    controls=[
        container
    ]
)