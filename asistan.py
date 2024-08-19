import tkinter as tk
import speech_recognition as sr
import webbrowser
import pyttsx3

def ses_komut_al():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            komut = r.recognize_google(audio, language="tr-TR")
            print(f"Komut: {komut}")
            return komut.lower()
        except sr.UnknownValueError:
            print("Ne dediğinizi anlayamadım.")
            return ""
        except sr.RequestError:
            print("Ses tanıma servisine ulaşılamıyor.")
            return ""

def google_arama_yap(aranacak):
    url = f"https://www.google.com/search?q={aranacak}"
    webbrowser.open(url)
    print("Google'da arama yapılıyor...")

def sesli_geri_bildirim(mesaj):
    engine.say(mesaj)
    engine.runAndWait()

def butona_basildi():
    komut = ses_komut_al()
    label.config(text=f"Algılanan: {komut}")
    if "ara" in komut:
        aranacak = komut.replace("ara", "").strip()
        google_arama_yap(aranacak)
        sesli_geri_bildirim("Google'da arama yapılıyor.")
    elif "çıkış" in komut:
        sesli_geri_bildirim("Görüşmek üzere.")
        root.destroy()

engine = pyttsx3.init()

#Buton
root = tk.Tk()
root.title("Sesli Komut Asistanı")
root.geometry("600x400")

label = tk.Label(root, text="Komutlar burada görünecek", font=("Arial", 14))
label.pack(pady=20)

buton = tk.Button(root, text="Komut ver", command=butona_basildi, width=30, height=5, bg="blue", fg="white")
buton.pack(pady=20)

root.mainloop()
