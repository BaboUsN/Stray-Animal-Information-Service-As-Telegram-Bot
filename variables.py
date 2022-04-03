import json
import process as pr
import datetime


def getIhbarNo():
    file = open("./asset/ihbarno.txt", "r+")
    num = file.readline()
    file.close()
    num2 = int(num) + 1
    file = open("./asset/ihbarno.txt", "r+")
    file.write(str(num2))
    file.close()
    return int(num)


def getKimlikNo(tip):
    now = datetime.datetime.now()
    text = f"{tip}{now.year}{getIhbarNo()}"
    return text


pender = []
wait = "default"
IhbaraddList = []
firstChecker = False
ihbarAraId = []
IhbaruygulamaEkleArr = []
AnimaladdList = []
changeableID = ""

hayvanBoolean = ["kisir", "tasma", "SahiplikDurumu",
                 "kampusHayvani", "cinsiyet", "tedavisiDevam", "SahiplilikBekleme"]
humanBoolean = ["kisir", "tasma", "SahiplikDurumu"]

humanObjList = []
hayvanObjList = []
ihbarObjList = []
ihbarBagla = []

ihbarUsers = ["Private Info", "Private Info"]
ihbarEkleTemp = {
    "tarih": "None",
    "kisiIsmi": None,
    "kisiTelefon": None,
    "adress": None,
    "tarihVeYer": None,
    "konu": None,
    "alinisTarihi": None,
    "uygulama": None,
    "operasyon": None,
    "degerlendirme": None,
    "ozelisaret": None,
    "kimlikNum": 24242,
    "baglanti": None}

ihbarEkleData = ihbarEkleTemp.copy()


HayvanEkleTemp = {
    "tarih": "None",
    "kimlikNum": "None",
    "hayvanTuru": None,
    "ismi": None,
    "neredenGeldi": None,
    "kampusHayvani": None,
    "irk": None,
    "tur": None,
    "renk": None,
    "yas": None,
    "kupeNo": None,
    "cinsiyet": None,
    "canaYakin": None,
    "saglikProblem": None,
    "karakter": None,
    "kilo": None,
    "operasyon": [
        None
    ],
    "kisir": None,
    "tasma": None,
    "yasadigiBolge": None,
    "ilgilenenKisi": None,
    "ilgilenenTel": None,
    "SahiplikDurumu": None,
    "SahiplilikBekleme": None,
    "sahibi": "None",
    "tedavisiDevam": None,
    "GeciciYuva": [],
    "ihbarlari": []
}
# HayvanEkleTemp = {"tarih": "None", "ismi": None, "neredenGeldi": None, "kimlikNum": getKimlikNo("A"),
#                   "tur": None, "irk": None, "renk": None, "yas": None, "kupeNo": None,
#                   "cinsiyet": None, "canaYakin": None, "saglikProblem": None,
#                   "karakter": None, "kilo": None,
#                   "operasyon": [None], "kisir": [None], "ihbarNo":
#                   getIhbarNo(), "tasma": None, "yasadigiBolge": None,
#                   "ilgilenenKisi": None, "ilgilenenTel": None, "SahiplikDurumu": None}
HayvanEkleData = HayvanEkleTemp.copy()
HumanEkleTemp = {"ismi": None,
                 "kimlikNum": 3232,
                 "telefon": None,
                 "yakininTel": None,
                 "evAdresi": None,
                 "ePosta": None,
                 "okulIs": None,
                 "okulIsAdres": None,
                 "okulIsTelefon": None,
                 "referansIsim": None,
                 "referansTelefon": None}
HumanEkleData = HumanEkleTemp.copy()
AdjusterTemp = {
    "ihbarKimlik": None,
    "text": None,
    "hayvanKimlik": None,
    "humanKimlik": None,
    "zaman": None,
    "ara": None
}
AdjusterData = AdjusterTemp.copy()

# tasma section


# class Tasma:
#     tasma1 = None
#     tasma2 = None
#     tasma3 = None
#     tasma4 = None
#     tasma5 = None
#     tasma6 = None
#     tasma7 = None
#     tasma8 = None
#     tasma9 = None
#     tasma10 = None

#     def __init__(self, mydict):
#         self.tasma1 = mydict.get("tasma1")
#         self.tasma2 = mydict.get("tasma2")
#         self.tasma3 = mydict.get("tasma3")
#         self.tasma4 = mydict.get("tasma4")
#         self.tasma5 = mydict.get("tasma5")
#         self.tasma6 = mydict.get("tasma6")
#         self.tasma7 = mydict.get("tasma7")
#         self.tasma8 = mydict.get("tasma8")
#         self.tasma9 = mydict.get("tasma9")
#         self.tasma10 = mydict.get("tasma10")


# def get_tasmaData():
#     costList = open(
#         "./asset/tasma.json", "r+", encoding="UTF-8")
#     data = json.load(costList)
#     costList.close()
#     return data


# tasmaObj = Tasma(get_tasmaData)
