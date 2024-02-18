from tkinter import * 

class Library:
    def __init__(self):
        self.dosya_adi = "books.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitapları_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        if not kitaplar:
            return "Kütüphanede kayıtlı kitap yok."
        else:
            kitap_bilgileri = ""
            for kitap in kitaplar:
                kitap_bilgisi = kitap.strip().split(',')
                kitap_bilgileri += f"Başlık: {kitap_bilgisi[0]}\nYazar: {kitap_bilgisi[1]}\n\n"
            return kitap_bilgileri

    def kitap_ekle(self, baslik, yazar, yayin_tarihi, sayfa_sayisi):
        if not all([baslik, yazar, yayin_tarihi, sayfa_sayisi]):
            return "Boş bir kitap eklenemez."
        try:
            int(yayin_tarihi)  
        except ValueError:
            return "Yayın tarihi hatalı bu alan sayı olmalıdır."
        try:
            int(sayfa_sayisi)  
        except ValueError:
            return "Sayfa sayısı hatalı bu alan sayı olmalıdır."
        
        kitap_bilgisi = f"{baslik},{yazar},{yayin_tarihi},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        return "Kitap başarıyla eklendi."

    def kitap_sil(self, baslik):
        self.dosya.seek(0)  
        kitaplar = self.dosya.readlines()
        
        if not kitaplar:  
            return "Kütüphanede kitap yok."

        guncel = [kitap for kitap in kitaplar if not kitap.startswith(baslik)]
        if len(guncel) == len(kitaplar):
            return "Kitap bulunamadı."
        else:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(guncel)
            return "Kitap başarıyla silindi."



    def temizle(self):
        baslik_entry.delete(0, END)
        yazar_entry.delete(0, END)
        yayin_tarihi_entry.delete(0, END)
        sayfa_sayisi_entry.delete(0, END)

        
kütüphane = Library() 

root = Tk()
root.title("Library")
root.geometry("550x550+500+100")

def kitapları_listele():
    kitaplar_metni = kütüphane.kitapları_listele()
    kitaplar_text.delete(1.0, END)  
    kitaplar_text.insert(END, kitaplar_metni)

def kitap_ekle():
    baslik = baslik_entry.get()
    yazar = yazar_entry.get()
    yayin_tarihi = yayin_tarihi_entry.get()
    sayfa_sayisi = sayfa_sayisi_entry.get()
    sonuç = kütüphane.kitap_ekle(baslik, yazar, yayin_tarihi, sayfa_sayisi)
    sonuç_label.config(text=sonuç)
    

def kitap_sil():
    baslik = sil_entry.get()
    if not baslik:  
        sonuç_label.config(text="Silinecek kitabın adını girin.")
    else:
        sonuç = kütüphane.kitap_sil(baslik)
        sonuç_label.config(text=sonuç)

    

def temizle():
    kütüphane.temizle()

#------------------------------------------------------------------------------------------------------#
        
# tk arayüz stil kod alanı 
resim=PhotoImage(file="library.png")

üst_bosluk = Label(root, image=resim)
üst_bosluk.grid(row=0, columnspan=4, padx=10)

baslik_label = Label(root, text="Başlık:")
baslik_label.grid(row=1, column=0, padx=10, pady=10)
baslik_entry = Entry(root)
baslik_entry.grid(row=1, column=1, padx=10, pady=10)

yazar_label = Label(root, text="Yazar:")
yazar_label.grid(row=2, column=0, padx=10, pady=10)
yazar_entry = Entry(root)
yazar_entry.grid(row=2, column=1, padx=10, pady=10)

yayin_tarihi_label = Label(root, text="Yayın Tarihi:")
yayin_tarihi_label.grid(row=3, column=0, padx=10, pady=10)
yayin_tarihi_entry = Entry(root)
yayin_tarihi_entry.grid(row=3, column=1, padx=10, pady=10)

sayfa_sayisi_label = Label(root, text="Sayfa Sayısı:")
sayfa_sayisi_label.grid(row=4, column=0, padx=10, pady=10)
sayfa_sayisi_entry = Entry(root)
sayfa_sayisi_entry.grid(row=4, column=1, padx=10, pady=10)

ekle_button = Button(root, text="Kitap Ekle", command=kitap_ekle, padx=10)
ekle_button.grid(row=5, column=0,  padx=10, pady=10, sticky="WE")   

temizle_button = Button(root, text="Temizle",command=temizle, padx=10)
temizle_button.grid(row=5, column=1, padx=10, pady=10, sticky="WE")


sil_label = Label(root, text="Silinecek Kitap Adı:")
sil_label.grid(row=1, column=2, padx=10, pady=10)
sil_entry = Entry(root)
sil_entry.grid(row=1, column=3, padx=10, pady=10)

sil_button = Button(root, text="Kitap Sil", command=kitap_sil, padx=10)
sil_button.grid(row=2, column=3,columnspan=1,  padx=10, pady=10, sticky="WE")


liste_button = Button(root, text="Kitapları Listele", command=kitapları_listele, padx=10)
liste_button.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky="WE")

cikis = Button(root, text="Çıkış", command=root.destroy, padx=10)
cikis.grid(row=6, column=3,columnspan=1, padx=10, pady=10, sticky="WE")

kitaplar_text = Text(root, height=10, width=60, wrap=WORD) 
kitaplar_text.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

# Dikey scroll 
kitaplar_scroll = Scrollbar(root, orient=VERTICAL, command=kitaplar_text.yview) 
kitaplar_scroll.grid(row=9, column=4, padx=0, pady=10, sticky="NS") 
kitaplar_text.config(yscrollcommand=kitaplar_scroll.set) 

sonuç_label = Label(root, text="")
sonuç_label.grid(row=4, column=2, columnspan=3, padx=10, pady=10)

#------------------------------------------------------------------------------------------------------#

root.mainloop()

