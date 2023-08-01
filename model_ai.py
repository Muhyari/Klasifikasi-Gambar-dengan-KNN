from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from PIL import Image
import os

kotak = []
lingkaran = []
segitiga = []
satu = []

def data_set():
    global kotak, lingkaran, segitiga, satu
    # data gambar kotak
    for data in os.listdir("Klasifikasi Gambar/foto/kotak/"):
        kotak_image = Image.open("Klasifikasi Gambar/foto/kotak/" + data)
        kotak_image = np.array(kotak_image)
        kotak_image = kotak_image.flatten()
        kotak.append(kotak_image)
        
    # data gambar lingkaran
    for data in os.listdir("Klasifikasi Gambar/foto/lingkaran/"):
        lingkaran_image = Image.open("Klasifikasi Gambar/foto/lingkaran/" + data)
        lingkaran_image = np.array(lingkaran_image)
        lingkaran_image = lingkaran_image.flatten()
        lingkaran.append(lingkaran_image)
        
    # data gambar segitiga
    for data in os.listdir("Klasifikasi Gambar/foto/segitiga/"):
        segitiga_image = Image.open("Klasifikasi Gambar/foto/segitiga/" + data)
        segitiga_image = np.array(segitiga_image)
        segitiga_image = segitiga_image.flatten()
        segitiga.append(segitiga_image)
        
    # data gambar satu
    for data in os.listdir("Klasifikasi Gambar/foto/satu/"):
        satu_image = Image.open("Klasifikasi Gambar/foto/satu/" + data)
        satu_image = np.array(satu_image)
        satu_image = satu_image.flatten()
        satu.append(satu_image)
    return kotak, lingkaran, segitiga, satu
        
        
def image_model():
    model = KNeighborsClassifier(n_neighbors=5)
    print("LOAD DATA SET".center(30,"="))
    kotak, lingkaran, segitiga, satu = data_set()
    print("LOAD MODEL".center(30, "="))
    y_kotak = np.ones(len(kotak)) * 4
    y_lingkaran = np.zeros(len(lingkaran))
    y_segitiga = np.ones(len(segitiga)) * 3
    y_satu = np.ones(len(satu))
    
    x = kotak+lingkaran+segitiga+satu
    y = np.concatenate([y_kotak,y_lingkaran,y_segitiga,y_satu])
    model.fit(x,y) # type: ignore
    return model