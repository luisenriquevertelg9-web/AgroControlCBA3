import json
import os
import csv
import shutil
from datetime import datetime

DATA = "data"
ARCHIVOS = {
    "productos": f"{DATA}/productos.json",
    "lotes": f"{DATA}/lotes.json",
    "movimientos": f"{DATA}/movimientos.json",
    "ventas": f"{DATA}/ventas.json"
}

productos = []
lotes = []
movimientos = []
ventas = []

def cargar_archivo(ruta):
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print(f" No se pudo leer {ruta}. Se iniciará vacío.")
    return []

def guardar_archivo(ruta, datos):
    os.makedirs(DATA, exist_ok=True)
    respaldo = ruta + ".bak"
    if os.path.exists(ruta):
        try:
            shutil.copy2(ruta, respaldo)
        except OSError:
            pass
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_todo():
    global productos, lotes, movimientos, ventas
    productos = cargar_archivo(ARCHIVOS["productos"])
    lotes = cargar_archivo(ARCHIVOS["lotes"])
    movimientos = cargar_archivo(ARCHIVOS["movimientos"])
    ventas = cargar_archivo(ARCHIVOS["ventas"])

def guardar_todo():
    guardar_archivo(ARCHIVOS["productos"], productos)
    guardar_archivo(ARCHIVOS["lotes"], lotes)
    guardar_archivo(ARCHIVOS["movimientos"], movimientos)
    guardar_archivo(ARCHIVOS["ventas"], ventas)

    