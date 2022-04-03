import json
import Hayvan
import Human
import ihbar
import variables as v
import os


def getFileList(path):
    files = [f for f in os.listdir(path)]
    return files


def get_AnimalItem(i):
    costList = open(
        f"./asset/Hayvanlar/{i}", "r+", encoding="UTF-8")
    data = json.load(costList)
    costList.close()
    print(data)
    return data


def get_HumanItem(i):
    costList = open(
        f"./asset/Humans/{i}", "r+", encoding="UTF-8")
    data = json.load(costList)
    costList.close()
    print(data)
    return data


def get_ihbarItem(i):
    costList = open(
        f"./asset/ihbarlar/{i}", "r+", encoding="UTF-8")
    data = json.load(costList)
    costList.close()
    print(data)
    return data


def animalLoader():
    fileList = getFileList('./asset/Hayvanlar')
    try:
        for i in fileList:
            nw = get_AnimalItem(i)
            # print(nw)
            v.hayvanObjList.append(Hayvan.Hayvan(nw))
        text = f"Hayvan Ön Yükleme BASARILI - Yüklenen Hayvan Sayısı = {len(v.hayvanObjList)}"
        # print(text)
        return text
    except:
        print("Hayvan Ön Yükleme Hatası")
        quit()


def humanLoader():
    fileList = getFileList('./asset/Humans')
    try:
        for i in fileList:
            nw = get_HumanItem(i)
            # print(nw)
            v.humanObjList.append(Human.Human(nw))
        text = f"Human Ön Yükleme BASARILI - Yüklenen Human Sayısı = {len(v.humanObjList)}"
        # print(text)
        return text
    except:
        print("Human Ön Yükleme Hatası")
        quit()


def ihbarLoader():
    fileList = getFileList('./asset/ihbarlar')
    try:
        for i in fileList:
            nw = get_ihbarItem(i)
            # print(nw)
            v.ihbarObjList.append(ihbar.Ihbar(nw))
        text = f"İhbar Ön Yükleme BASARILI - Yüklenen İhbar Sayısı = {len(v.ihbarObjList)}"
        # print(text)
        return text
    except:
        print("İhbar Ön Yükleme Hatası")
        quit()


def start():
    a = animalLoader()
    h = humanLoader()
    i = ihbarLoader()
    print(a)
    print(h)
    print(i)

# def start():
#     try:
#         for i in hayvanData:
#             v.hayvanObjList.append(Hayvan.Hayvan(i))
#         print("Hayvan Liste Yüklemesi Başarılı")
#     except:
#         print("Hayvan Listesi Yüklenemedi!")
#     try:
#         humanData = Human.get_HumanList()
#         for i in humanData:
#             v.humanObjList.append(Human.Human(i))
#         print("Human Liste Yüklemesi Başarılı")
#     except:
#         print("Human Listesi Yüklenemedi!")
