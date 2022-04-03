from threading import local
import process as pr
import variables as v
import ihbar as ihbar
import Hayvan
import Human
import Adjuster
import Sorgu


def sample_response(input_text, update):
    id = str(update.message.chat_id)
    user_message = str(input_text).lower()
    users_data = pr.get_Users()
    print(f"{pr.get_CurrentTime()} | {str(update.message.chat_id)} | {update.message.chat.first_name} -> {user_message}")
    for i in users_data:
        if (i["user_id"] == id):
            if (i["try"] == 0):
                return ""

    if user_message == ("parola"):
        v.wait = "pwd"
        v.changeableID = id
        return f"👿👿Parola Girin:👿👿"

    if pr.checker(update) == False:
        return "😱Botu Kullanmak İçin Yetkiniz Bulunmamakta😱"

    if user_message == ("merhaba"):
        return f"Merhaba {update.message.chat.first_name}😁"

    if user_message == ("help"):
        return helpMsj(update.message.chat.first_name)

    if user_message == ("backup") and id == "Private Info":
        return pr.back_up()

    if user_message == ("kullanıcılar") and id == "Private Info":
        users = pr.get_Users()
        preText = ""
        for i in users:
            preText = preText + "\n" + i["user_id"] + \
                "--" + i["first_name"] + "--" + str(i["verify"])
        return preText

    if user_message == ("ara"):
        v.AnimaladdList.append(id)
        v.changeableID = id
        v.wait = "ara"
        return Adjuster.orderOfAdjuster(input_text, update, ["ara"], Adjuster.ara)

    # Sorgu Section
    try:
        if user_message == ("hayvanyazdır"):
            return Sorgu.getAnimals()
        if user_message == ("insanyazdır"):
            return Sorgu.getHumans()
        if user_message == ("ihbaryazdır"):
            return Sorgu.getihbars()
        if user_message == ("yazdırsahipli"):
            return Sorgu.getSahipli()
        if user_message == ("yazdırsahiplibekleme"):
            return Sorgu.getSahipliBekleme()
        if user_message == ("yazdırtedavisibitmis"):
            return Sorgu.getTedavisiBitmis()
        if user_message == ("yazdırgeciciyuvadabekleyen"):
            return Sorgu.getGeciciYuvadaBekleyen()
        if user_message == ("yazdırkisir"):
            return Sorgu.getKısır()
    except Exception:
        print("Sorgu Hatası -> ", Exception.__cause__)

    # IHBAR SECTİON

    if(id in v.ihbarUsers):
        if user_message == ("hayvanekle"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "hayvanekle"
            return Hayvan.orderOfAddAnimal(input_text, update)

        if user_message == ("insanekle"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "insanekle"
            return Human.orderOfAddHuman(input_text, update)

        if user_message == ("ihbarekle"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "ihbarekle"
            return ihbar.orderOfAddihbar(input_text, update)

        if user_message == ("ihbaruygulamaekle"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "ihbarUygulamaEkle"
            return Adjuster.orderOfAdjuster(input_text, update, ["ihbarKimlik", "text"], Adjuster.ihbarUygulamaEkle)

        if user_message == ("ihbaroperasyonekle"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "ihbaroperasyonEkle"
            return Adjuster.orderOfAdjuster(input_text, update, ["ihbarKimlik", "text"], Adjuster.ihbaroperasyonEkle)

    # ----------------------------------
        if user_message == ("tedavibitir"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "tedaviBitir"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik"], Adjuster.tedaviBitir)

        if user_message == ("tedavibaslat"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "tedaviBaslat"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik"], Adjuster.tedaviBaslat)

        if user_message == ("sahiplikbeklemebaslat"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "sahiplikBeklemeBaslat"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik"], Adjuster.sahiplikBeklemeBaslat)

        if user_message == ("sahiplikbeklemebitir"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "sahiplikBeklemeBitir"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik"], Adjuster.sahiplikBeklemeBitir)

        if user_message == ("Sahiplikdurumutrue"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "SahiplikDurumuTrue"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik"], Adjuster.SahiplikDurumuTrue)

        if user_message == ("sahiplendir"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "sahiplendir"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik", "humanKimlik"], Adjuster.sahiplendir)

        if user_message == ("itemsil"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "itemsil"
            return Adjuster.orderOfAdjuster(input_text, update, ["ara"], Adjuster.deleteItem)

        if user_message == ("addgeciciyuva"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "addGeciciYuva"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik", "humanKimlik"], Adjuster.addGeciciYuva)
        if user_message == ("ihbarbagla"):
            v.AnimaladdList.append(id)
            v.changeableID = id
            v.wait = "ihbarBagla"
            return Adjuster.orderOfAdjuster(input_text, update, ["hayvanKimlik", "ihbarKimlik"], Adjuster.ihbarBagla)
    return "🙄Anlayamadım🙄\n😇İstersen help yazarak komutlarıma ulaşabilirsin😇"


def pwd_Checker(text):
    tryed = 3
    pwd = pr.get_pwd()
    users = pr.get_Users()
    for i in users:
        if v.changeableID == i["user_id"]:
            tryed = int(i["try"])
    if (tryed <= 0):
        v.wait = "default"
        return "☠️Hakkınız Bitmiştir.☠️"
    if(pwd == text):
        for i in users:
            if v.changeableID == i["user_id"]:
                i["verify"] = True
                pr.replace_User(users)
                v.wait = "default"
                return "😸Giriş Başarılı😸"
    for i in users:
        if v.changeableID == i["user_id"]:
            i["try"] = i["try"] - 1
            pr.replace_User(users)
    return f"⚠️Başarısız giriş- {tryed} Hakkınız Kaldı⚠️"


def helpMsj(userName):
    msj = f"""
✌️Selamlar {userName}🤩

💡ara ➡️ komutuyla istediğin tipten her şeyi Kimlik Numarasına göre arayabilirsin

➡️ Eğer hatalı bir işlem yaparsan işlem anında 'iptal' yazarak işlemi sonlandırabilirsin

🖶 ihbaryazdır ➡️ komutuyla İhbar listesini yazdırabilirsin

🖶 hayvanyazdır ➡️ komutuyla Hayvan listesini yazdırabilirsin

🖶 insanyazdır ➡️ komutuyla İnsan listesini yazdırabilirsin


🖨️ yazdırsahipli ➡️ komutuyla Sahipli Hayvanları yazdırabilirsin
 
🖨️ yazdırsahiplibekleme ➡️ komutuyla Sahiplenmeyi bekleyen hayvanları yazdırabilirsin
 
🖨️ yazdırtedavisibitmis ➡️ komutuyla Tedavisi bitmiş hayvanları yazdırabilirsin
 
🖨️ yazdırgeciciyuvadabekleyen ➡️ komutuyla Geçici yuvada bekleyen hayvanları yazdırabilirsin
 
🖨️ yazdırkisir ➡️ komutuyla Kısırlaştırılmış hayvanları yazdırabilirsin



⛏️tedavibaslat ➡️ komutuyla hayvanın tedavisini başlatabilirsin

⛏️tedavibitir ➡️ komutuyla hayvanın tedavisini bitirebilirsin

⛏️sahiplikbeklemebaslat ➡️ komutuyla hayvanın sahiplik için beklemesini başlatabilirsin

⛏️sahiplikbeklemebitir ➡️ komutuyla hayvanın sahiplik için beklemesini bitirebilirsin

⛏️Sahiplikdurumutrue ➡️ komutuyla hayvanın sahiplendirildiğini gösterebilirsin

⛏️sahiplendir ➡️ komutuyla hayvanı bir insana sahiplendirebilirsin

⛏️itemsil ➡️ komutuyla kimlik numarasına göre item silebilirsin

⛏️addgeciciyuva ➡️ komutuyla hayvana geçici yuva ekleyebilirsin

⛏️ihbarbagla ➡️ komutuyla hayvana ihbar bağlayabilirsin
        """
    return msj
