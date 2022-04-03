import variables as v
import process as pr
import datetime
import json
import AddChecker
import Sorgu as S


class Hayvan:
    tarih = None
    kimlikNum = None
    hayvanTuru: None
    ismi = None
    neredenGeldi = None
    kampusHayvani = None
    irk = None
    tur = None
    renk = None
    yas = None
    kupeNo = None
    cinsiyet = None
    canaYakin = None
    saglikProblem = None
    karakter = None
    kilo = None
    operasyon = None
    kisir = None
    tasma = None
    yasadigiBolge = None
    ilgilenenKisi = None
    ilgilenenTel = None
    SahiplikDurumu = None
    sahibi = None
    tedavisiDevam = None
    GeciciYuva = None
    ihbarlari = []
    SahiplilikBekleme = None

    def __init__(self, mydict):
        self.tarih = mydict.get("tarih")
        self.kimlikNum = mydict.get("kimlikNum")
        self.hayvanTuru = mydict.get("hayvanTuru")
        self.ismi = mydict.get("ismi")
        self.neredenGeldi = mydict.get("neredenGeldi")
        self.kampusHayvani = mydict.get("kampusHayvani")
        self.irk = mydict.get("irk")
        self.tur = mydict.get("tur")
        self.renk = mydict.get("renk")
        self.yas = mydict.get("yas")
        self.kupeNo = mydict.get("kupeNo")
        self.cinsiyet = mydict.get("cinsiyet")
        self.canaYakin = mydict.get("canaYakin")
        self.saglikProblem = mydict.get("saglikProblem")
        self.karakter = mydict.get("karakter")
        self.kilo = mydict.get("kilo")
        self.operasyon = mydict.get("operasyon")
        self.kisir = mydict.get("kisir")
        self.SahiplilikBekleme = mydict.get("SahiplilikBekleme")
        self.tasma = mydict.get("tasma")
        self.yasadigiBolge = mydict.get("yasadigiBolge")
        self.ilgilenenKisi = mydict.get("ilgilenenKisi")
        self.ilgilenenTel = mydict.get("ilgilenenTel")
        self.SahiplikDurumu = mydict.get("SahiplikDurumu")
        self.sahibi = mydict.get("sahibi")
        self.tedavisiDevam = mydict.get("tedavisiDevam")
        self.GeciciYuva = mydict.get("GeciciYuva")
        self.ihbarlari = mydict.get("ihbarlari")


def del_AnimalList():
    pass
#     data = get_AnimalList()
#     delItem = data.pop()
#     data = json.dumps(data)
#     file = open(
#         "./asset/HayvanList.json", "w+", encoding="UTF-8")
#     file.write(data)
#     file.close()
#     return "🐶Silindi!🐶"


def animalTypeFilter(typee):
    if(typee == "kopek" or typee == "köpek"):
        return "D"
    elif(typee == "kedi"):
        return "C"
    elif(typee == "kus" or typee == "kuş"):
        return "B"
    else:
        return "N"


def replace_Hayvan(newData):
    try:
        if(newData.keys() == 0):
            print(f'Replacement Error in {newData}')
            return "Burağa Bildir!! - Replacement Error!"
    except:
        print(f'Replacement Error in {newData}')
        return "Burağa Bildir!! - Replacement Error!"

    data = json.dumps(newData)
    file = open(
        f"./asset/Hayvanlar/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def add_Hayvan(newData):
    mydate = datetime.datetime.now()
    nowDay = mydate.strftime("%x").split("/")
    mydate = str(mydate)
    newData["tarih"] = mydate
    newData["kimlikNum"] = pr.getKimlikNo(
        animalTypeFilter(newData["hayvanTuru"]))
    v.hayvanObjList.append(Hayvan(newData))  # obj olusutur
    data = json.dumps(newData)
    file = open(
        f"./asset/Hayvanlar/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def orderOfAddAnimal(text, update):
    v.changeableID = str(update.message.chat_id)
    if(v.changeableID != v.AnimaladdList[0]):
        return pr.penderTime()
    if(text == "iptal"):
        pr.cleartolists()
        v.wait = "default"
        return "İptal Edildi"

    newData = v.HayvanEkleData
    keys = newData.keys()
    for i in keys:
        if(newData[i] == None) and v.firstChecker == True:
            if(i in v.hayvanBoolean):
                if(text == "evet" or text == "hayır"):
                    newData[i] = AddChecker.HayvanCheck.trueFalse(text)
                    break
                else:
                    return "Cevap evet veya hayır şekline olmalı"
            else:
                newData[i] = text
                break
    for i in keys:
        if(newData[i] == None):
            v.firstChecker = True
            return f"🐶{i.upper()}🐶 Bilgisini Girin: "
    v.wait = "default"
    add_Hayvan(newData)
    pr.cleartolists()
    return "👍"

# def get_AnimalList():
#     try:
#         costList = open(
#             "./asset/HayvanList.json", "r+", encoding="UTF-8")
#     except:
#         costList = open(
#             "./asset/HayvanList.json", "w+", encoding="UTF-8")
#         preData = []
#         preData = json.dumps(preData)
#         costList.write(preData)
#         costList.close()
#         costList = open(
#             "./asset/HayvanList.json", "r+", encoding="UTF-8")
#     data = json.load(costList)
#     costList.close()
#     return data
