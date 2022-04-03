import variables as v
import process as pr
import datetime
import json
import AddChecker


class Human:
    kimlikNum = None
    ismi = None
    telefon = None
    yakininTel = None
    evAdresi = None
    ePosta = None
    okulIs = None
    okulIsAdres = None
    okulIsTelefon = None
    referansIsimSoy = None
    referansTelefon = None

    def __init__(self, myDict):
        self.kimlikNum = myDict.get("kimlikNum")
        self.ismi = myDict.get("ismi")
        self.telefon = myDict.get("telefon")
        self.yakininTel = myDict.get("yakininTel")
        self.evAdresi = myDict.get("evAdresi")
        self.ePosta = myDict.get("ePosta")
        self.okulIs = myDict.get("okulIs")
        self.okulIsAdres = myDict.get("okulIsAdres")
        self.okulIsTelefon = myDict.get("okulIsTelefon")
        self.referansIsimSoy = myDict.get("referansIsimSoy")
        self.referansTelefon = myDict.get("referansTelefon")


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
        f"./asset/Humans/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def add_Human(newData):
    mydate = datetime.datetime.now()
    nowDay = mydate.strftime("%x").split("/")
    mydate = str(mydate)
    newData["tarih"] = mydate
    newData["kimlikNum"] = pr.getKimlikNo("H")
    v.hayvanObjList.append(Human(newData))  # obj olusutur
    data = json.dumps(newData)
    file = open(
        f"./asset/Humans/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()
    print(len(v.humanObjList))


def orderOfAddHuman(text, update):
    v.changeableID = str(update.message.chat_id)
    if(v.changeableID != v.AnimaladdList[0]):
        return pr.penderTime()
    if(text == "iptal"):
        pr.cleartolists()
        v.wait = "default"
        return "İptal Edildi"

    newData = v.HumanEkleData
    keys = newData.keys()
    for i in keys:
        if(newData[i] == None) and v.firstChecker == True:
            if(i in v.humanBoolean):
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
    add_Human(newData)
    pr.cleartolists()
    return "👍"
