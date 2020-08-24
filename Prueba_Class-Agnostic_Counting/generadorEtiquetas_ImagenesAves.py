from PIL import Image
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np


def main():
    # El camino a los archivos que quiero utilizar para producir sus etiquetas
    mypath = "ECA_Flocks/GSGO/CUT"
    # Obtengo una lista con los nombres de los archivos de todoas las imagenes de aves de el camino escogido (que sean .JPG,de momento no necesito los otros archivos .csv)
    onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (".JPG" in f))]
    
    # Bucle para procesar cada imagen
    for nombreImgAve in onlyfiles:
        im_aves2 = Image.open(join(mypath, nombreImgAve))
        # Obtengo las dimensiones de la imagen
        width, height = im_aves2.size
        # Genero la imagen en negro que será la imagen de las etiquetas labels, que indicará donde está situado cada ave en la imagen original mediante un pixel de color rojo (255, 0, 0)
        img_label = np.zeros((height, width, 3), dtype = "uint8") # Pongo 3 para que sea RGB
        nombre_sinExtension = nombreImgAve[:-4] # Obtengo el nombre sin la extensión de archivo .JPG
        # Leo el csv asociado a la misma imagen que stoy procesando, que contendrá la posición de todos los pájaros en la imagen
        aves = pd.read_csv(join(mypath, nombre_sinExtension + ".csv"))
        # Bucle para recorrer cada pájaro indicado en el .csv y poner un pixel en la imagen de etiquetas en negro de otro color RGB: rojo (255, 0, 0)
        for i in range(aves.shape[0]):
            img_label[int(round(aves.iloc[i]["Y"])), int(round(aves.iloc[i]["X"]))] = (255, 0, 0)
        
        im = Image.fromarray(img_label) # Convierto la imagen matriz de numpy en algo que pueda guaradr como archivo
        # Guardo la nueva imagen .png con las etiquetas de las aves de la imagen correspondiente original
        im.save(join(mypath, nombre_sinExtension + "dots.png"))



if __name__ == '__main__':
    main()