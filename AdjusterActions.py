import process as pr
import variables as v


def orderOfAdjuster(text, update, arr, fun):
    v.changeableID = str(update.message.chat_id)
    if(v.changeableID != v.AnimaladdList[0]):
        return pr.penderTime()
    if(text == "iptal"):
        pr.cleartolists()
        v.wait = "default"
        return "İptal Edildi"

    newData = v.AdjusterData
    for i in arr:
        if(newData[i] == None) and v.firstChecker == True:
            newData[i] = text

    for i in arr:
        if(newData[i] == None):
            v.firstChecker = True
            return f"🐶{i.upper()}🐶 Bilgisini Girin: "

    v.wait = "default"
    try:
        fun(newData)
    except:
        return "Hata ! - Burağa Bildir!"
    pr.cleartolists()
    return "Başarılı"
