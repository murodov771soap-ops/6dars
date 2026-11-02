from datetime import datetime

def bugungi_sana():
    return datetime.now().date()

def hozirgi_vaqt():
    return datetime.now().time().strftime("%H:%M:%S")

def yili_aniqla(sana):
    return datetime.strptime(sana, "%Y-%m-%d").year