from .connect import execute_curs

"""
!La estructura de la tabla "tasks" es:  
| id | title | date | text | state | subtask |

id : Numero que incrementa en automatico
title: titulo de la tarea
text: texto de la tarea
date: Se espera la fecha de la creacion de la tarea.
state: estado de la tarea (tipo de dato str, posiblemente lo gestione como 'init', 'progress', 'finish')
subtask (opcional): almacena un string en forma de: [id,state,title]. En si la idea que pienso es que guarde la informacion en forma de string y que se conviertan en listas ,pero creo que lo mejor sera gestionarlo como un json a futuro.
"""


class dbTask:
    def __init__(self):
        self.__execute = execute_curs

    def read(self, id: int = None) -> tuple:
        """
        Busca una tarea con el `id` ingresado

        Args:
            id (int): Id de el numero a buscar (opcional)
        """
        try:
            if id:
                # Previamente verificamos si existe el id en el campo id:
                consulta = "SELECT EXISTS (SELECT 1 FROM tasks WHERE id = %s)"
                busqueda = self.__execute(consulta, (id,))[0][0]

                if busqueda:  # si se encontro, entonces:
                    consulta = "SELECT * FROM tasks WHERE id = %s"
                    read = self.__execute(consulta, (id,))[0]
                else:
                    raise ValueError(f"el dato '{id}' no existe en el campo id")
            else:
                consulta = "SELECT * FROM tasks"
                read = self.__execute(consulta)
            return read
        except Exception as e:
            print("Error:", e)

    def add(self, title: str, text: str, state: str, subtask: str = None):
        """
        Añade los datos a la tabla

        Args:
            title (str): titulo de la tarea
            text (str): texto/contenido de la tarea
            state (str): estado de la tarea (init/progress/finish)
            subtask (str, optional): las subtareas creadas.
        """
        if subtask:
            consulta = (
                "INSERT INTO tasks(title, text, state, subtask) VALUES(%s, %s, %s, %s)"
            )
            params = (title, text, state, subtask)
        else:
            consulta = "INSERT INTO tasks(title, text, state) VALUES(%s, %s, %s)"
            params = (title, text, state)
        self.__execute(consulta, params)


# task = dbTask()

# data = task.read(1)
# print(data)

# id = data[0]
# title = data[1]
# date = data[2]
# text = data[3]
# state = data[4]
# subtask = data[5]
# print(
#     f"""
# id : {id}
# title : {title}
# text : {text}
# state : {state}
# subtask : {subtask}
# """
# )


# task.add("nueva tarea", "# lorem ipsum \n Texto texto y mas texto", "progress")

# print(task.read(1))


# def last_id():
#     # execute = "SELECT currval('todo_id_seq')"
#     execute = "SELECT MAX(id) FROM todo"
#     read = execute_curs(execute)[0][0]
#     return read


# def exist_id(id):
#     execute = "SELECT EXISTS (SELECT 1 FROM todo WHERE id = %s)"
#     read = execute_curs(execute, (id,))[0][0]
#     return read


# def update_task(id: int, title, content):
#     execute = "UPDATE todo SET title = %s, content = %s WHERE id = %s"
#     execute_curs(execute, (title, content, id))


# def all_tasks():
#     execute = "SELECT * FROM todo ORDER BY id ASC"
#     read = execute_curs(execute)
#     return read
