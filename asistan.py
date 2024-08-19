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
engine = pyttsx3.init()

def sesli_geri_bildirim(mesaj):
    engine.say(mesaj)
    engine.runAndWait()

r = sr.Recognizer()
mic = sr.Microphone()
while True:
    komut = ses_komut_al()
    print(f"Algılanan: {komut}")
    if "ara" in komut:
        aranacak = komut.replace("ara", "").strip()
        google_arama_yap(aranacak)
        sesli_geri_bildirim("Google'da arama yapılıyor.")
    elif "çıkış" in komut:
        sesli_geri_bildirim("Görüşmek üzere!")
        break