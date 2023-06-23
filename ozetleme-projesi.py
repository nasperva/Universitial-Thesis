import spacy

nlp = spacy.load("tr_core_news_trf")


with open("dilbilim-terimleri-sozlukcesi.txt", "r", encoding="utf-8") as f:
    terimler = f.read().splitlines()

with open("hedef_metin.txt", "r", encoding="utf-8") as f:
    hedef_metin = f.read()

cümleler = list(nlp(hedef_metin).sents)

hedef_cümleler = []
for terim in terimler:
    for cümle in cümleler:
        if terim in cümle.text.lower():
            hedef_cümleler.append(cümle.text.strip())


özet = " ".join(hedef_cümleler)

max_sözcük_sayisi = 50
sözcükler = özet.split()
if len(sözcükler) > max_sözcük_sayisi:
    özet = " ".join(sözcükler[:max_sözcük_sayisi])

print("Özetlenmiş Metin:")
print(özet)
