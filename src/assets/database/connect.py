import psycopg2 as p2


def open_conn():
    """Abre la conexión a la base de datos."""
    try:
        conn = p2.connect(
            user="postgres", password="admin", port="5432", database="manager_task"
        )
        return conn
    except p2.Error as e:
        print("Error al conectar a la base de datos:", e)
    except UnicodeDecodeError as e:
        print("Error al codificar los parametros de conexion a la DB:", e)
    except Exception as e:
        print("Ocurrio un error inesperado", e)


def execute_curs(sentencia: str, params=None) -> list[tuple] | None:
    """
    Ejecuta una sentencia SQL.

    - Si es una consulta de lectura (SELECT), devuelve los resultados.
    - Si es de escritura (INSERT, UPDATE, DELETE), ejecuta la operación.

    Parámetros:
        sentencia (str): La sentencia SQL a ejecutar.
        params (tuple): Parámetros opcionales para la consulta.
    Retorno:
        list: Resultados de la consulta (si es SELECT).
        None: En caso de que no haya resultados o sea una operación de escritura.
    """
    try:
        conn = open_conn()
        if conn is None:
            raise Exception("No existe conexion con la base de datos.")
        with conn.cursor() as curs:
            curs.execute(sentencia, params)

            # Determinar si es una consulta de lectura
            if sentencia.strip().upper().startswith("SELECT"):
                return curs.fetchall()  # Devuelve los resultados
            else:
                conn.commit()
                return None
    except p2.Error as e:
        print("Error al ejecutar la sentencia:", e)
        return None
    except Exception as e:
        print("Ocurrio un error:", e)
    finally:
        if conn:
            conn.close()
