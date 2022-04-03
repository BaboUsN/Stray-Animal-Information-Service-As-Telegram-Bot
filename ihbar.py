import variables as v
import process as pr
import datetime
import json
import AddChecker
import Sorgu
import Adjuster


class Ihbar:
    tarih = None
    kisiIsmi = None
    kisiTelefon = None
    adress = None
    tarihVeYer = None
    konu = None
    alinisTarihi = None
    uygulama = None
    operasyon = None
    degerlendirme = None
    ozelisaret = None
    kimlikNum = None
    baglanti = None

    def __init__(self, mydict):
        self.tarih = mydict.get("tarih")
        self.kisiIsmi = mydict.get("kisiIsmi")
        self.kisiTelefon = mydict.get("kisiTelefon")
        self.adress = mydict.get("adress")
        self.tarihVeYer = mydict.get("tarihVeYer")
        self.konu = mydict.get("konu")
        self.alinisTarihi = mydict.get("alinisTarihi")
        self.uygulama = mydict.get("uygulama")
        self.operasyon = mydict.get("operasyon")
        self.degerlendirme = mydict.get("degerlendirme")
        self.ozelisaret = mydict.get("ozelisaret")
        self.kimlikNum = mydict.get("kimlikNum")
        self.baglanti = mydict.get("baglanti")


def replace_ihbar(newData):
    try:
        if(newData.keys() == 0):
            print(f'Replacement Error in {newData}')
            return "Burağa Bildir!! - Replacement Error!"
    except:
        print(f'Replacement Error in {newData}')
        return "Burağa Bildir!! - Replacement Error!"

    data = json.dumps(newData)
    file = open(
        f"./asset/ihbarlar/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def add_ihbar(newData):
    mydate = datetime.datetime.now()
    nowDay = mydate.strftime("%x").split("/")
    mydate = str(mydate)
    newData["tarih"] = mydate
    newData["kimlikNum"] = pr.getKimlikNo("I")
    if(not (newData["baglanti"] == "yok")):
        Adjuster.ihbarBagla(
            {"ihbarKimlik": newData["kimlikNum"], "hayvanKimlik": newData["baglanti"]})
    v.ihbarObjList.append(Ihbar(newData))  # obj olusutur
    data = json.dumps(newData)
    file = open(
        f"./asset/ihbarlar/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def orderOfAddihbar(text, update):
    v.changeableID = str(update.message.chat_id)
    if(v.changeableID != v.AnimaladdList[0]):
        return pr.penderTime()
    if(text == "iptal"):
        pr.cleartolists()
        v.wait = "default"
        return "İptal Edildi"

    newData = v.ihbarEkleData
    keys = newData.keys()
    for i in keys:
        if(newData[i] == None) and v.firstChecker == True:
            if(i == "baglanti"):
                if(text == "yok"):
                    pass
                else:
                    if(Adjuster.isThereChecker("hayvanKimlik", text)):
                        pass
                    else:

                        return "Geçersiz Hayvan Kimliği\n" + "Hayvan Kayıtlı değilse 'yok' yaz" + Sorgu.getAnimals()
            newData[i] = text
            break
    for i in keys:
        if(newData[i] == None):
            v.firstChecker = True
            return f"🐶{i.upper()}🐶 Bilgisini Girin: "
    v.wait = "default"
    add_ihbar(newData)
    pr.cleartolists()
    return "👍"
