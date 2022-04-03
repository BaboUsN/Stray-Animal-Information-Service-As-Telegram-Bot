import json
from typing import cast
from os import execlp, remove
import datetime
import variables as v


def checker(update):
    file = open("./asset/users.json", "r+", encoding="UTF-8")
    data = json.load(file)
    id = str(update.message.chat_id)
    isThere = False
    for x in data:
        if x["user_id"] == id:
            isThere = True
    if isThere == False:
        add_User(id, (update.message.chat.first_name),
                 (update.message.chat.last_name), data)
    for i in data:
        if id in i["user_id"]:
            if i["verify"] == True:
                file.close()
                return True
    file.close()
    return False


def add_User(id, first, last, data):
    newdata = {"user_id": id, "verify": False,
               "first_name": first, "last_name": last, "try": 3, "card-balance": 50, "card-cost": 2.25}
    data.append(newdata)
    data = json.dumps(data)
    file = open("./asset/users.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


# def back_up():
#     mydate = datetime.datetime.now()
#     nowDay = mydate.strftime("%x").split("/")
#     data = get_Cost(32131)
#     data = json.dumps(data)
#     costList = open(
#         f"./backups/{nowDay[1]}-{nowDay[0]}-{nowDay[2]}.json", "w+", encoding="UTF-8")
#     costList.write(data)
#     costList.close()
#     return "Burak, Başarılı işlem!"


def getIhbarNo():
    file = open("./asset/ihbarno.txt", "r+")
    num = file.readline()
    file.close()
    num2 = int(num) + 1
    file = open("./asset/ihbarno.txt", "r+")
    file.write(str(num2))
    file.close()
    return int(num)


# def ihbarAra(num):
#     data = get_Cost(3123)
#     for i in data:
#         if(i["ihbarNo"]) == num:
#             # print(i)
#             text = f"""
# 🧸İhbar Numarası = {i["ihbarNo"]}

# 🧸Bildirimin Tarihi Ve Yeri ➡️ {i["tarihVeYer"]}
# 🧸Bildirimin Konusu ➡️ {i["konu"]}
# 🧸Değerlendirme ➡️ {i["degerlendirme"]}

# 🧸Hayvanın Alınış Tarihi ➡️ {i["alinisTarihi"]}
# 🧸Hayvanın Küpe Kodu ➡️ {i["kupeNo"]}
# 🧸Hayvanın Türü ➡️ {i["tur"]}
# 🧸Hayvanın Irkı ➡️ {i["irk"]}
# 🧸Hayvanın Yaşı ➡️ {i["yas"]}
# 🧸Hayvanın Rengi ➡️ {i["renk"]}
# 🧸Hayvanın Cinsiyeti ➡️ {i["cinsiyet"]}
# 🧸Hayvanın Özel İşareti ➡️ {i["ozelisaret"]}


# 🧸Uygulamalar ➡️  {i["uygulama"]}
# 🧸Operasyonlar ➡️  {i["operasyon"]}

# 🧸Bildirenin İsmi ➡️ {i["ismi"]}
# 🧸Bildirenin Telefonu ➡️ {i["telefon"]}
# 🧸Bildirenin Adresi ➡️ {i["adress"]}

#             """
#             return text
#     return "🐶Geçersiz İhbarNo🐶"

def get_pwd():
    file = open("./asset/pwd.txt", "r+", encoding="UTF-8")
    pwd = file.read()
    file.close()
    return pwd


def get_Users():
    file = open("./asset/users.json", "r+", encoding="UTF-8")
    data = json.load(file)
    file.close()
    return data


def replace_User(data):
    data = json.dumps(data)
    file = open("./asset/users.json", "w+", encoding="UTF-8")
    file.write(data)
    file.close()


def get_time():
    dt = datetime.datetime.today()
    seconds = dt.timestamp()
    return seconds


def get_CurrentTime():
    mydate = datetime.datetime.now()
    nowDay2 = mydate.strftime("%c")
    return nowDay2


def getYear():
    data = get_CurrentTime()
    data = data.split(" ")
    return data[5]


def penderTime():
    if(len(v.pender) == 0):
        v.pender.append(get_time())
        return "😸Lütfen 60 saniye bekle😸"
    elif (len(v.pender) == 1):
        v.pender.append(get_time())
        if (v.pender[1]-v.pender[0] >= 60):
            cleartolists()
            v.wait = "default"
            return "😇Devam edebiliriz😇"
        else:
            v.pender.pop()
            return "😋Daha 60 saniye dolmadı😋"


def cleartolists():
    v.pender.clear()
    v.wait = "default"
    v.IhbaraddList.clear()
    v.ihbarAraId.clear()
    v.IhbaruygulamaEkleArr.clear()
    v.AnimaladdList.clear()
    v.firstChecker = False
    v.ihbarEkleData = v.ihbarEkleTemp.copy()
    v.HayvanEkleData = v.HayvanEkleTemp.copy()
    v.AdjusterData = v.AdjusterTemp.copy()
    v.ihbarEkleData = v.ihbarEkleTemp.copy()


def getKimlikNo(harf):
    file = open("./asset/kimlikno.txt", "r+")
    num = file.readline()
    file.close()
    num2 = int(num) + 1
    file = open("./asset/kimlikno.txt", "r+")
    file.write(str(num2))
    file.close()
    return f"{harf}{num}"


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
