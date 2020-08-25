from PIL import Image
from os import listdir, mkdir
from os.path import isfile, join
import numpy as np

# Método auxiliar trocear una imagen en pedazos iguales de una altura y anchura dadas
def crop(path, inp, label, name, height, width, k, page, area):
    im = Image.open(inp)
    lab = Image.open(label)
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            a_lab = lab.crop(box)
            try:
                o = a.crop(area)
                o_lab = a_lab.crop(area)
                # Solo se quieren los trozos que tengan instancias de aves, no los que están vacios, por lo que se toman los que en su pedazo equivalente
                # de imagen de etiquetas tenga al menos un pixel rojo.
                if(len(o_lab.getcolors()) > 1):
                    o.save(join(path, "%s_256x256-%s.png" % (name, k)))
                    o_lab.save(join(path,"%sdots_256x256-%s.png" % (name, k)))
            except:
                pass
            k += 1


def main():
    # Directorio del nuevo dataset de imágenes de 256x256
    path_savesFile = "dataset_imagenes_aves_256x256"
    # Crea el directorio, si ya existe uno con el mismo nombre dará un error
    mkdir(path_savesFile)

    ########################################################################################
    ##### Se generan trozos de 256x256 de las siguientes imágenes en el directorio
    ########################################################################################

    inp = "ECA_Flocks\GSGO\CUT\GSGO_001_C.JPG"
    label = "ECA_Flocks\GSGO\CUT\GSGO_001_Cdots.png"
    filename = "GSGO_001_C"
    crop(path_savesFile, inp, label, filename, 256, 256, 0, 0, (0, 0, 256, 256))

    inp = "ECA_Flocks\GSGO\CUT\GSGO_059_C.JPG"
    label = "ECA_Flocks\GSGO\CUT\GSGO_059_Cdots.png"
    filename = "GSGO_059_C"
    crop(path_savesFile, inp, label, filename, 256, 256, 0, 0, (0, 0, 256, 256))

    inp = "ECA_Flocks\GSGO\CUT\GSGO_008_C.JPG"
    label = "ECA_Flocks\GSGO\CUT\GSGO_008_Cdots.png"
    filename = "GSGO_008_C"
    crop(path_savesFile, inp, label, filename, 256, 256, 0, 0, (0, 0, 256, 256))

    inp = "ECA_Flocks\GSGO\CUT\GSGO_019_C.JPG"
    label = "ECA_Flocks\GSGO\CUT\GSGO_019_Cdots.png"
    filename = "GSGO_019_C"
    crop(path_savesFile, inp, label, filename, 256, 256, 0, 0, (0, 0, 256, 256))

    inp = "ECA_Flocks\GSGO\CUT\GSGO_014_C.JPG"
    label = "ECA_Flocks\GSGO\CUT\GSGO_014_Cdots.png"
    filename = "GSGO_014_C"
    crop(path_savesFile, inp, label, filename, 256, 256, 0, 0, (0, 0, 256, 256))

    inp = "ECA_Flocks\GSGO\CUT\GSGO_018_C.JPG"
    label = "ECA_Flocks\GSGO\CUT\GSGO_018_Cdots.png"
    filename = "GSGO_018_C"
    crop(path_savesFile, inp, label, filename, 256, 256, 0, 0, (0, 0, 256, 256))

    # El camino al directorio del nuevo dataset de 256x256 para producir el archivo .npz
    mypath = "dataset_imagenes_aves_256x256"
    # Lista con los nombres de los archivos de todas las imagenes de aves de el camino escogido (que sean .JPG, de momento no necesito los otros archivos .csv)
    files_GSGO_001_C = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_001_C_" in f))]
    files_GSGO_001_Cdots = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_001_Cdots_" in f))]
    files_GSGO_059_C = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_059_C_" in f))]
    files_GSGO_059_Cdots = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_059_Cdots_" in f))]
    files_GSGO_008_C = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_008_C_" in f))]
    files_GSGO_008_Cdots = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_008_Cdots_" in f))]
    files_GSGO_019_C = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_019_C_" in f))]
    files_GSGO_019_Cdots = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_019_Cdots_" in f))]
    files_GSGO_014_C = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_014_C_" in f))]
    files_GSGO_014_Cdots = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_014_Cdots_" in f))]
    files_GSGO_018_C = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_018_C_" in f))]
    files_GSGO_018_Cdots = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("GSGO_018_Cdots_" in f))]
    # Se ordenan los nombres
    files_GSGO_001_C = sorted(files_GSGO_001_C)
    files_GSGO_001_Cdots = sorted(files_GSGO_001_Cdots)
    files_GSGO_059_C = sorted(files_GSGO_059_C)
    files_GSGO_059_Cdots = sorted(files_GSGO_059_Cdots)
    files_GSGO_008_C = sorted(files_GSGO_008_C)
    files_GSGO_008_Cdots = sorted(files_GSGO_008_Cdots)
    files_GSGO_019_C = sorted(files_GSGO_019_C)
    files_GSGO_019_Cdots = sorted(files_GSGO_019_Cdots)
    files_GSGO_014_C = sorted(files_GSGO_014_C)
    files_GSGO_014_Cdots = sorted(files_GSGO_014_Cdots)
    files_GSGO_018_C = sorted(files_GSGO_018_C)
    files_GSGO_018_Cdots = sorted(files_GSGO_018_Cdots)

    ######################################################################################################
    #### Se eligen las imágenes y etiquetas asociadas que se usarán para entrenamiento y validación
    ######################################################################################################

    trn_lst = np.array(files_GSGO_018_C[0:len(files_GSGO_018_C)-24])
    trn_lst = np.append(trn_lst, files_GSGO_001_C[0:len(files_GSGO_001_C)-47])
    trn_lst = np.append(trn_lst, files_GSGO_059_C[0:len(files_GSGO_059_C)-2])
    trn_lst = np.append(trn_lst, files_GSGO_008_C[0:len(files_GSGO_008_C)-1])
    trn_lst = np.append(trn_lst, files_GSGO_019_C[0:len(files_GSGO_019_C)-8])
    trn_lst = np.append(trn_lst, files_GSGO_014_C[0:len(files_GSGO_014_C)-72])

    trn_lb = np.array(files_GSGO_018_Cdots[0:len(files_GSGO_018_Cdots)-24])
    trn_lb = np.append(trn_lst, files_GSGO_001_Cdots[0:len(files_GSGO_001_Cdots)-47])
    trn_lb = np.append(trn_lst, files_GSGO_059_Cdots[0:len(files_GSGO_059_Cdots)-2])
    trn_lb = np.append(trn_lst, files_GSGO_008_Cdots[0:len(files_GSGO_008_Cdots)-1])
    trn_lb = np.append(trn_lst, files_GSGO_019_Cdots[0:len(files_GSGO_019_Cdots)-8])
    trn_lb = np.append(trn_lst, files_GSGO_014_Cdots[0:len(files_GSGO_014_Cdots)-72])

    val_lst = np.array(files_GSGO_018_C[len(files_GSGO_018_C)-24:len(files_GSGO_018_C)])       
    val_lst = np.array(files_GSGO_001_C[len(files_GSGO_001_C)-47:len(files_GSGO_001_C)])
    val_lst = np.array(files_GSGO_059_C[len(files_GSGO_059_C)-2:len(files_GSGO_059_C)])
    val_lst = np.array(files_GSGO_008_C[len(files_GSGO_008_C)-1:len(files_GSGO_008_C)])
    val_lst = np.array(files_GSGO_019_C[len(files_GSGO_019_C)-8:len(files_GSGO_019_C)])
    val_lst = np.array(files_GSGO_014_C[len(files_GSGO_014_C)-72:len(files_GSGO_014_C)])

    val_lb = np.array(files_GSGO_018_Cdots[len(files_GSGO_018_Cdots)-24:len(files_GSGO_018_Cdots)])
    val_lb = np.array(files_GSGO_001_Cdots[len(files_GSGO_001_Cdots)-47:len(files_GSGO_001_Cdots)])
    val_lb = np.array(files_GSGO_059_Cdots[len(files_GSGO_059_Cdots)-2:len(files_GSGO_059_Cdots)])
    val_lb = np.array(files_GSGO_008_Cdots[len(files_GSGO_008_Cdots)-2:len(files_GSGO_008_Cdots)])
    val_lb = np.array(files_GSGO_019_Cdots[len(files_GSGO_019_Cdots)-8:len(files_GSGO_019_Cdots)])
    val_lb = np.array(files_GSGO_014_Cdots[len(files_GSGO_014_Cdots)-72:len(files_GSGO_014_Cdots)])

    # Guarda los arrays de numpy en un solo archivo .npz
    np.savez("aves.npz", trn_lb=trn_lb, trn_lst=trn_lst, val_lst=val_lst, val_lb=val_lb)


if __name__ == '__main__':
    main()