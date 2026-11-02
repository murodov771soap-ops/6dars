import requests

url = ""
valyuta_kodi = input("Valyuta kodini kiriting: ").upper()
miqdor = float(input("Miqdorni kiriting: "))

response = requests.get(url)
kurslar = response.json()



for item in kurslar:
    if item["Ccy"] == valyuta_kodi:
        kurs = float(item["Rate"])
        valyuta_nomi = item["CcyNm_UZ"]
        jami = miqdor * kurs
        print(f"Valyuta: {valyuta_nomi}")
        print(f"Miqdor: {miqdor} {valyuta_kodi}")
        print(f"1 {valyuta_kodi} kursi: {kurs} so'm")
        print(f"Jami: {jami} so'm")
        break