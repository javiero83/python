from fastapi import FastAPI, HTTPException
import os

from pydantic import BaseModel

print("Running from: ",os.getcwd())

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"mensaje": "Hola Javier! Tu primera API en Python esta funcionando 🥳"}
#
# @app.get("/saludo/{nombre}")
# def read_item(nombre:str):
#     return {"saludo": f"Hola, {nombre}, bienvenido a tu API con FastAPI 👍"}

#Modelo de datos para un juguete
class Juguete(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool = True

#base de datos en memoria
juguetes = [
    {"id":1, "nombre":"Robot", "precio":150.0,"disponible":True},
    {"id":2, "nombre":"Pelota", "precio":50.0,"disponible":True},
]

#GET -> ver todos los juguetes
@app.get("/juguetes")
def obtener_juguetes():
    return juguetes

#GET -> ver juguete por ID
@app.get("/juguetes/{juguete_id}")
def obtener_juguete(juguete_id:int):
    for j in juguetes:
        #print("Comparando con:", j["id"])
        if j["id"] == juguete_id:
            return j
    raise HTTPException(status_code=404, detail='Juguete no encontrado')

#POST -> agregar un nuevo juguete
@app.post("/juguetes")
def agregar_juguete(juguete:Juguete):
    #verifica si existe el id
    for j in juguetes:
        if j["id"] == juguete.id:
            raise HTTPException(status_code=404, detail="El ID ya existe")
    juguetes.append(juguete.model_dump())
    return {"mensaje":"Juguete agregado correctamente", "juguete": juguete}