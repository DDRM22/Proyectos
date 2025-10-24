
# Parametros por defecto

# Entrenamiento o ejecucion ---------------------------------------- 

bool_entrenamiento_por_defecto = True # Si es True, estamos entrenando el modelo. Si es False, estamos evaluando datos nuevos con el modelo ya entrenado.

def get_entrenamiento_sufix(bool_entrenamiento):
    if bool_entrenamiento:
        entrenamiento_sufix = ""
    else:
        entrenamiento_sufix = "_evaluacion"
    return entrenamiento_sufix

# Indicamos las rutas de los datos
import os

# Carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Rutas absolutas
RUTA_DATOS_INPUT = os.path.join(BASE_DIR, "data", "input")
RUTA_DATOS_PROD = os.path.join(BASE_DIR, "data", "production")
RUTA_DATOS_PROCESADOS = os.path.join(BASE_DIR, "data", "processed")
RUTA_DATOS_PROCESADOS_PROD = os.path.join(BASE_DIR, "data", "processed_prod")
RUTA_DATOS_OUTPUT = os.path.join(BASE_DIR, "data", "output")
RUTA_DATOS_OUTPUT_PROD = os.path.join(BASE_DIR, "data", "output_prod")
RUTA_MODELOS = os.path.join(BASE_DIR, "models")

# Definimos las rutas de entrada y salida de datos en funcion del modo
def get_ruta_input(bool_entrenamiento: bool):
    return os.path.join(BASE_DIR, "data", "input") if bool_entrenamiento else RUTA_DATOS_PROD

def get_ruta_output(bool_entrenamiento: bool):
    return os.path.join(BASE_DIR, "data", "output") if bool_entrenamiento else RUTA_DATOS_OUTPUT_PROD

def get_ruta_modelos(bool_entrenamiento: bool): # Solo para evaluación
    return os.path.join(BASE_DIR, "data", "models") if bool_entrenamiento else RUTA_MODELOS

def get_ruta_processed(bool_entrenamiento: bool):
    return os.path.join(BASE_DIR, "data", "processed") if bool_entrenamiento else RUTA_DATOS_PROCESADOS_PROD