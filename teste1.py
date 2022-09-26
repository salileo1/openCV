import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def showImage(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)

    return img


def main():
    obj_img = cv.imread("photos/cat.jpg")
    altura, largura, canais_cor = obj_img.shape
    print("Dimensões da imagem: ", str(largura), "X", str(altura))
    print("Canais de cor: ", canais_cor)

    for y in range(0, altura):
        for x in range(0, largura):
            
            azul, verde, vermelho = getColor(obj_img, x, y)
            obj_img = setColor(obj_img, x, y, verde, azul, vermelho)

            #azul = obj_img.item(y, x, 0)
            #verde = obj_img.item(y, x, 1)
            #vermelho = obj_img.item(y, x, 2)
            
            #deixar imagem toda em vermelho 
            # itemset para zerar azul e verde nos pixels
            #obj_img.itemset((y, x, 0), 0)
            #obj_img.itemset((y, x, 1), 0)

            #mostrar pixel por pixel 
            # print("[" + str(x) + "," + str(y) + "]" + str(obj_img[y][x]))
            # input()
    
    #criar ROI
    roi_img = obj_img[196:196 + 60, 499: 499 + 60]
    #colar ROI na imagem original
    obj_img[161 : 161 + roi_img.shape[0], 450 : 450 + roi_img.shape[1]] = roi_img
    showImage(obj_img)
    #roi_img.shape[altura, largura] = busca do recorte
    
    #cv.imwrite("cat_modificado.png", obj_img)
    #showImage(roi_img)
    #showImage(obj_img)

main()

