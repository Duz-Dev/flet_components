import flet as ft


def main(page: ft.Page):
    page.padding = 0  # Normalizar pagina

    box = ft.Container(bgcolor="green", width=100, height=100)
    # page.add(box)

    body = ft.Container(bgcolor="red", expand=1, width=100)
    # El expand indica que el elemento pueda abarcar el 100% del ancho y 100%  del alto del contenedor padre. En el caso del container, si estableces expand = true, puedes sobrescribir el ancho del elemento pero no el alto.

    # page.add(body)

    container = ft.Row(
        controls=[box, box, box, box, box], expand=1
    )  # Row pocisiona los elementos dentro de este en formato horizontal, asi formando una fila. Si colocas espand=true, se expande como normalmente vimos, al 100% del ancho y alto.

    container2 = ft.Row(
        [body]
    )  # En este ejemplo sucede algo curioso. Dado que el contenedor padre ahora es el ft.Row, al no tener medidas definidas, en este caso un alto, el elemento hijo (body), el alto al que es relativo es 0. por ende no se vera nada.
    # page.add(container2)

    container2.height = 200  # Ahora si establecemos un alto veremos que en automatico nuestro elemento hijo se expande.
    # page.add(container2)

    container2.width = 300  # Y no solo eso, si no que dado que el elemento hijo original tiene la propiedad expand, se expande abarcando todo el espacio que tenga el contenedor padre (ft.Row), esto a pesar de que el elemento hijo le pasamos un alto definido. Entonces concluyo que row ignora el pequeño truco que encontre que era el poder sobrescribir el ancho si se tenia ya expand true en dicho elemento hijo.

    # page.add(container2)

    container3 = ft.Row(
        controls=[body], expand=1
    )  # Si le establecemos un expand true, En automatico y sin dudarlo el Row se expande el 100% del espacio que permita el contenedor padre, en este caso la pagina en si.

    # page.add(container3)

    container3.width = 100  # Aun asi el truco de sobrescribir el ancho para tener un alto del 100% funciona.

    # ?Observacion. Mi imagino que nada a la naturaleza y propocito del ft.Row, el truco de sobrescribir el ancho, no funciona para el alto.

    # page.add(container3)

    container4 = ft.Column(
        controls=[box, box, box, box, box]
    )  # Column, alinea los elementos en forma de columna.
    # page.add(container4)

    container5 = ft.Column(
        controls=[body]
    )  # Aqui sucede un efecto cuanto menos curioso. En esta situacion tenemos el mismo detalle que cuando añadimos solo body a el elemento ft.Row, que al no tener medidas definidas, el body no se expandia.
    # page.add(container5)

    container5.expand = 1  # Pero algo extraño sucede y es que ahora si establecemos expand=true, el elemenento padre ya toma un 100% de espacio con referencia a su padre (en este caso page), asi en efecto el elemento hijo que es body, puede expandirse tomando ahora si las medidas de su pádre (container5). Lo extraño es que a diferencia de ft.Row, aqui el truco de mantener el ancho que si le indicamos a body, si funciona.

    # page.add(container5)

    item = ft.Container(
        bgcolor="yellow", expand=1
    )  # Dado que no existen medidas expecificas, y al dotarlo de expand=1, este toma el alto y ancho del contenedor padre, en este caso el page.
    # page.add(item)

    fila = ft.Row(
        controls=[item], height=100
    )  # Si establecemos solo el alto, se expande en 100% en cuanto el ancho.
    # page.add(fila)

    columna = ft.Column(
        controls=[item], height=100
    )  # El mismo fenomeno pasa exactamente con el column.
    # page.add(columna)

    fila2 = ft.Row(controls=[item], width=100)
    # page.add(fila2) #Si solo estableces el ancho, da igual, no apacerece nada. Esto desconozco porque.

    columna2 = ft.Column(controls=[item], width=100)
    # page.add(columna2)

    fila3 = ft.Row(
        controls=[item], expand=1, width=100
    )  # Ahora si establecemos el expand =true, ya sea en el row o en el column, y si definimos el width, el alto si se expande al 100%
    # page.add(fila3)

    columna3 = ft.Column(controls=[item], expand=1, width=100)
    # page.add(columna3)


ft.app(target=main, assets_dir="assets")
