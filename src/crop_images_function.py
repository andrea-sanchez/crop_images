from PIL import Image
import os

archivos_tu_ciencia = os.listdir("Tu_Ciencia")
carpetas = [elemento for elemento in archivos_tu_ciencia if os.path.isdir(elemento) and not elemento.startswith(".")]
fotos = []
basurita = [".ipynb", ".pdf", ".pptx", ".ppt", ".py", ".md", ".git"]

for base_path, dirs, files in os.walk("."):
    #base_path = os.path.join(path[0], *path[1:][0])
    for file in files:
        if not file.startswith(".") and not os.path.splitext(file)[1] in basurita:
            fotos.append(os.path.join(base_path, file))

for file in fotos:
    img = Image.open(file)
    ancho, alto = img.size
    nuevo_alto = alto * 4 / 6
    origen_y = (alto - nuevo_alto) / 2
    extremo_y = nuevo_alto + origen_y
    box = (0, origen_y, ancho, extremo_y)
    area = img.crop(box)
    #name = os.path.splitext(img)
    area.save(file, 'jpeg')
