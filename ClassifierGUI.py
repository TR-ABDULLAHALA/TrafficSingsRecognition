#Kütüphanleri içe aktarma
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

#Eğitilmiş modeli yükleme
from keras.models import load_model
model = load_model('traffic_classifier.h5')

#Trafik işaretlerini etiketlemek için bir sözlük oluşturma
classes = { 1: 'Hız sınırı (20 km/s)',
2: 'Hız sınırı (30 km/s)',
3: 'Hız sınırı (50 km/s)',
4: 'Hız sınırı (60 km/s)',
5: 'Hız sınırı (70 km/s)',
6: 'Hız sınırı (80 km/s)',
7: 'Hız sınırı sonu (80 km/s)',
8: 'Hız sınırı (100 km/s)',
9: 'Hız sınırı (120 km/s)',
10: 'Geçilmemesi gereken bölge',
11: '3.5 ton üzerinde araçların geçiş yapması yasak',
12: 'Kavşakta yol verme',
13: 'Öncelikli yol',
14: 'Yol Ver',
15: 'Dur',
16: 'Trafik yasağı',
17: '3.5 ton üzerinde araçların girişi yasak',
18: 'Giriş yasak',
19: 'Genel dikkat',
20: 'Sola tehlikeli viraj',
21: 'Sağa tehlikeli viraj',
22: 'Çift viraj',
23: 'Yol bozuk',
24: 'Kaygan yol',
25: 'Sağa daralan yol',
26: 'Yol çalışması',
27: 'Trafik lambaları',
28: 'Yaya geçidi',
29: 'Çocuk geçidi',
30: 'Bisiklet geçidi',
31: 'Buz/kar uyarısı',
32: 'Yabani hayvan geçişi',
33: 'Hız sınırı ve geçme kısıtlaması sonu',
34: 'Sağa dönüş',
35: 'Sola dönüş',
36: 'Sadece ileri',
37: 'Doğru veya sağa',
38: 'Doğru veya sola',
39: 'Sağa dön',
40: 'Sola dön',
41: 'Dönel kavşak zorunlu',
42: 'Geçmenin yasaklandığı bölgenin sonu',
43: '3.5 ton üzerinde araçların geçiş yasağının sonu' }
# GUI'yi başlatma
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

# Etiket için bir alan oluşturma
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))

# Resim için bir alan oluşturma
sign_image = Label(top)
# Verilen dosya yolu üzerinde sınıflandırma yapma fonksiyonu
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred_probabilities = model.predict(image)
    pred = numpy.argmax(pred_probabilities, axis=1)[0]
    sign = classes[pred+1]
    print(sign)

    # Etiketi güncelleme
    label.configure(foreground='#011638', text=sign)
#Fotoğrafı sınıflandır butonunu gösterme fonksiyonu
def show_classify_button(file_path):
    classify_b=Button(top,text="Fotoğrafı Sınıflandır",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
#Resim yükleme fonksiyonu
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
#Fotoğraf Yüklemek için  buton oluşturma oluşturma
upload=Button(top,text="Fotoğraf Yükle",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)

#Resim ve etiket alanlarını düzenleme
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)

#Başlık etiketini oluşturma
heading = Label(top, text="Know Your Traffic Sign",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()

#GUI'yi çalıştırma
top.mainloop()