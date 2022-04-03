from cmath import exp
import datetime
import json
import os
import ihbar
import Hayvan
import Sorgu
import Human
import variables as v
import Loader
import process as pr
# __dict__


def replace_tasma(newData):
    try:
        if(newData.keys() == 0):
            print(f'Replacement Error in {newData}')
            return "Burağa Bildir!! - Replacement Error!"
    except:
        print(f'Replacement Error in {newData}')
        return "Burağa Bildir!! - Replacement Error!"

    data = json.dumps(newData)
    # print(data)
    file = open(
        f"./asset/tasma.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


# def tasmaDevret(dic):
#     tasma = dic.get("tasma")
#     text = dic.get("text")
#     if(tasma in v.tasmaObj.__dict__.keys()):

#     for i in hayvanList:
#         if(i.kimlikNum.lower() == hayvanKimlik.lower()):
#             i.SahiplikDurumu = True
#             Hayvan.replace_Hayvan(i.__dict__)
#             return "😁İşlem Başlarılı😁"


def tedaviBitir(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.tedavisiDevam = False
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def tedaviBaslat(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.tedavisiDevam = True
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def sahiplikBeklemeBaslat(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.SahiplilikBekleme = True
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def sahiplikBeklemeBitir(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.SahiplilikBekleme = False
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def SahiplikDurumuTrue(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.SahiplikDurumu = True
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def SahiplikDurumuFalse(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.SahiplikDurumu = False
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def ihbarUygulamaEkle(dic):
    ihbarKimlik = dic.get("ihbarKimlik")
    text = dic.get("text")
    ihbarList = v.ihbarObjList
    for i in ihbarList:
        if(i.kimlikNum.lower() == ihbarKimlik.lower()):
            try:

                if(isinstance(i.uygulama, str)):
                    newList = [i.uygulama]
                    i.uygulama = newList
                    i.uygulama.append(text)
                else:
                    i.uygulama.append(text)
                ihbar.replace_ihbar(i.__dict__)
            except:
                pass
            return "😁İşlem Başlarılı😁"


def ihbaroperasyonEkle(dic):
    ihbarKimlik = dic.get("ihbarKimlik")
    text = dic.get("text")
    ihbarList = v.ihbarObjList
    for i in ihbarList:
        if(i.kimlikNum.lower() == ihbarKimlik.lower()):
            if(isinstance(i.operasyon, str)):
                newList = [i.operasyon]
                i.operasyon = newList
                i.operasyon.append(text)
            else:
                i.operasyon.append(text)
            ihbar.replace_ihbar(i.__dict__)
            return "😁İşlem Başlarılı😁"


def ihbarBagla(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    ihbarKimlik = dic.get("ihbarKimlik")
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.ihbarlari.append(ihbarKimlik)
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def replace_deleted(newData):
    try:
        if(newData.keys() == 0):
            print(f'Replacement Error in {newData}')
            return "Burağa Bildir!! - Replacement Error!"
    except:
        print(f'Replacement Error in {newData}')
        return "Burağa Bildir!! - Replacement Error!"

    data = json.dumps(newData)
    file = open(
        f"./asset/deleted/{newData['kimlikNum']}.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def deleteItem(dic):
    araWord = dic.get("ara")
    firstLetter = araWord[0]
    if(firstLetter.lower() in ["d", "c", "b", "n"]):
        hayvanList = v.hayvanObjList
        for i in hayvanList:
            if(i.kimlikNum.lower() == araWord.lower()):
                replace_deleted(i.__dict__)
                v.hayvanObjList.remove(i)
        path = f"./asset/Hayvanlar/{araWord}.json"
        os.remove(path)
        return f"No:{araWord} - Hayvan Silindi"
    elif(firstLetter.lower() in ["i"]):
        ihbarList = v.ihbarObjList
        for i in ihbarList:
            if(i.kimlikNum.lower() == araWord.lower()):
                replace_deleted(i.__dict__)
                v.ihbarObjList.remove(i)
        path = f"./asset/ihbarlar/{araWord}.json"
        os.remove(path)
        return f"No:{araWord} - İhbar Silindi"
    elif(firstLetter.lower() in ["h"]):
        humanList = v.humanObjList
        for i in humanList:
            if(i.kimlikNum.lower() == araWord.lower()):
                replace_deleted(i.__dict__)
                v.humanObjList.remove(i)
        path = f"./asset/Humans/{araWord}.json"
        os.remove(path)
        return f"No:{araWord} - Human Silindi"
    return "Hata ! - Burağa Bildir! (Error About Deleter)"


def ara(dic):
    araWord = dic.get("ara")
    hayvanList = v.hayvanObjList
    humanList = v.humanObjList
    ihbarList = v.ihbarObjList
    text = ""
    for i in ihbarList:
        if(i.kimlikNum.lower() == araWord.lower()):
            data = i.__dict__
            keys = data.keys()
            for x in keys:
                text += f"{x} => {data[x]}\n"
            return text
    for i in hayvanList:
        if(i.kimlikNum.lower() == araWord.lower()):
            data = i.__dict__
            keys = data.keys()
            for x in data:
                text += f"{x} => {data[x]}\n"
            return text
    for i in humanList:
        if(i.kimlikNum.lower() == araWord.lower()):
            data = i.__dict__
            keys = data.keys()
            for x in keys:
                text += f"{x} => {data[x]}\n"
            return text
    return "🥸🥸Geçersiz🥸 Bilgi🥸"


def addGeciciYuva(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    humanKimlik = dic.get("humanKimlik")
    zaman = dic.get("zaman")
    hayvanList = v.hayvanObjList
    mydate = datetime.datetime.now()
    nowDay = mydate.strftime("%x").split("/")
    mydate = str(mydate)
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            obj = {"tarih": mydate, "zaman": zaman, "kisi": humanKimlik}
            i.GeciciYuva.append(obj)
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def sahiplendir(dic):
    hayvanKimlik = dic.get("hayvanKimlik")
    humanKimlik = dic.get("humanKimlik")
    SahiplikDurumuTrue()
    hayvanList = v.hayvanObjList
    for i in hayvanList:
        if(i.kimlikNum.lower() == hayvanKimlik.lower()):
            i.sahibi = humanKimlik
            Hayvan.replace_Hayvan(i.__dict__)
            return "😁İşlem Başlarılı😁"


def isThereChecker(typee, data):
    if(typee in ["ihbarKimlik", "hayvanKimlik", "humanKimlik", "ara"]):
        hayvanListe = v.hayvanObjList
        for i in hayvanListe:
            if(i.kimlikNum.lower() == data.lower()):
                return True
        humanList = v.humanObjList
        for i in humanList:
            if(i.kimlikNum.lower() == data.lower()):
                return True
        ihbarList = v.ihbarObjList
        for i in ihbarList:
            if(i.kimlikNum.lower() == data.lower()):
                return True
        return False
    return True


def orderOfAdjuster(text, update, arr, fun):
    v.changeableID = str(update.message.chat_id)
    if(v.changeableID != v.AnimaladdList[0]):
        return pr.penderTime()
    if(text == "iptal"):
        pr.cleartolists()
        v.wait = "default"
        return "😨İptal Edildi😨"

    newData = v.AdjusterData
    for i in arr:
        if(newData[i] == None) and v.firstChecker == True:
            if((isThereChecker(i, text))):
                pass
            else:
                if(i == "hayvanKimlik"):
                    info = Sorgu.getAnimals()
                    return f"🥸Geçersiz🥸 {i}\n" + info
                elif(i == "humanKimlik"):
                    info = Sorgu.getHumans()
                    return f"🥸Geçersiz🥸 {i}\n" + info
                elif(i == "ihbarKimlik"):
                    info = Sorgu.getihbars()
                    return f"🥸Geçersiz🥸 {i}\n" + info
                pr.cleartolists()
                return f"🥸Geçersiz🥸 {i}"
            newData[i] = text
            break
    for i in arr:
        if(newData[i] == None):
            v.firstChecker = True
            return f"🐶{i.upper()}🐶 Bilgisini Girin: "
    try:
        if(arr[0] == "ara"):
            data = fun(newData)
            pr.cleartolists()
            return data
        else:
            fun(newData)
    except:
        pr.cleartolists()
        return "☠️Hata ! - Burağa Bildir! (Error About Adjuster)☠️"
    pr.cleartolists()
    return "😁İşlem Başlarılı😁"
