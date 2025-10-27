from pathlib import Path

#ruta_base = Path.home()

ruta = Path(Path.home(),Path("Curso Python", "Día 6", "practicas_path.py"))

print(ruta)
print(ruta.stem)