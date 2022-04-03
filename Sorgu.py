import variables as v
import process as pr


def isTextEmpty(text, match):
    if(text == match):
        return "Veri Bulunamadı :("
    else:
        return text


def cinsiyet(bool):
    if(bool):
        return "Dişi"
    else:
        return "Erkek"


def getKısır():
    dataList = v.hayvanObjList
    match = "🌈Kimlik Numara 🌈 Hayvan Tür 🌈 İsim 🌈 Irk 🌈 Küpe NO 🌈 Cinsiyet\n"
    returnText = match[:]
    for i in dataList:
        if(i.kisir == True):
            returnText += f"🐰{i.kimlikNum} ➡️ {i.hayvanTuru} ➡️ {i.ismi} ➡️ {i.irk} ➡️ {i.kupeNo} ➡️ {cinsiyet(i.cinsiyet)}\n\n"
    return isTextEmpty(returnText, match)


def getSahipli():
    dataList = v.hayvanObjList
    match = "🌈Kimlik Numara 🌈 Hayvan Tür 🌈 İsim 🌈 Irk 🌈 Küpe NO 🌈 Cinsiyet\n"
    returnText = match[:]
    for i in dataList:
        if(i.SahiplikDurumu == True):
            returnText += f"🐰{i.kimlikNum} ➡️ {i.hayvanTuru} ➡️ {i.ismi} ➡️ {i.irk} ➡️ {i.kupeNo} ➡️ {cinsiyet(i.cinsiyet)}\n\n"
    return isTextEmpty(returnText, match)


def getSahipliBekleme():
    dataList = v.hayvanObjList
    match = "🌈Kimlik Numara 🌈 Hayvan Tür 🌈 İsim 🌈 Irk 🌈 Küpe NO 🌈 Cinsiyet\n"
    returnText = match[:]
    for i in dataList:
        if(i.SahiplilikBekleme == True):
            returnText += f"🐰{i.kimlikNum} ➡️ {i.hayvanTuru} ➡️ {i.ismi} ➡️ {i.irk} ➡️ {i.kupeNo} ➡️ {cinsiyet(i.cinsiyet)}\n\n"
    return isTextEmpty(returnText, match)


def getTedavisiBitmis():
    dataList = v.hayvanObjList
    match = "🌈Kimlik Numara 🌈 Hayvan Tür 🌈 İsim 🌈 Irk 🌈 Küpe NO 🌈 Cinsiyet\n"
    returnText = match[:]
    for i in dataList:
        if(i.tedavisiDevam == True):
            returnText += f"🐰{i.kimlikNum} ➡️ {i.hayvanTuru} ➡️ {i.ismi} ➡️ {i.irk} ➡️ {i.kupeNo} ➡️ {cinsiyet(i.cinsiyet)}\n\n"
    return isTextEmpty(returnText, match)


def getGeciciYuvadaBekleyen():
    dataList = v.hayvanObjList
    match = "🌈Kimlik Numara 🌈 Sahiplik Durumu 🌈 Hayvan Tür 🌈 İsim 🌈 Irk 🌈 Küpe NO 🌈 Cinsiyet\n"
    returnText = match[:]
    for i in dataList:
        if(len(i.GeciciYuva) != 0):
            returnText += f"🐰{i.kimlikNum} ➡️ {i.SahiplikDurumu} ➡️ {i.hayvanTuru} ➡️ {i.ismi} ➡️ {i.irk} ➡️ {i.kupeNo} ➡️ {cinsiyet(i.cinsiyet)}\n\n"
    return isTextEmpty(returnText, match)


def getihbars():
    dataList = v.ihbarObjList
    match = "🌈Kimlik Numara 🌈 Konu 🌈 Tarih Ve Yer 🌈 Kişi İsmi\n"
    returnText = match[:]
    for i in dataList:
        returnText += f"🐰{i.kimlikNum} ➡️ {i.konu} ➡️ {i.tarihVeYer} ➡️ {i.kisiIsmi}\n\n"
    return isTextEmpty(returnText, match)


def getAnimals():
    dataList = v.hayvanObjList
    match = "🌈Kimlik Numara 🌈Hayvan Tür 🌈 İsim 🌈 Irk 🌈 Küpe NO 🌈 Cinsiyet\n"
    returnText = match[:]
    for i in dataList:
        returnText += f"🐰{i.kimlikNum} ➡️ {i.hayvanTuru} ➡️ {i.ismi} ➡️ {i.irk} ➡️ {i.kupeNo} ➡️ {(cinsiyet(i.cinsiyet))}\n\n"
    return isTextEmpty(returnText, match)


def getHumans():
    dataList = v.humanObjList
    match = "🌈Kimlik Numara 🌈 İsim 🌈 Telefon 🌈 Okul,İş\n"
    returnText = match[:]
    for i in dataList:
        returnText += f"🐰{i.kimlikNum} ➡️ {i.ismi} ➡️ {i.telefon} ➡️ {i.okulIs}\n\n"
    return isTextEmpty(returnText, match)


def isThereHuman(kimlikNum):
    dataList = v.humanObjList
    for i in dataList:
        if(i.kimlikNum == kimlikNum):
            return True
    return False


def isThereHayvan(kimlikNum):
    dataList = v.hayvanObjList
    for i in dataList:
        if(i.kimlikNum == kimlikNum):
            return True
    return False


def isThereihbar(kimlikNum):
    dataList = v.ihbarObjList
    for i in dataList:
        if(i.kimlikNum == kimlikNum):
            return True
    return False
