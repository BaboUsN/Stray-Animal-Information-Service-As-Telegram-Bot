from telegram.ext import *
import Human
import Response as R
import Constant as keys
import os
import variables as v
import ihbar as ihbar
import Hayvan
import Loader
import Adjuster
os.system("pip3 install python-telegram-bot")


print("Bot has Started..")
Loader.start()


def start_comment(update, context):
    update.message.reply_text("Konusmaya baslamak icin bir seyler yaz.")


def help_comment(update, context):
    update.message.reply_text("HELP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def handle_comment(update, context):
    userId = str(update.message.chat_id)
    if(not(userId == "2023547098") and not(userId == "1614543955")):
        if (v.wait) == "pwd":
            text = str(update.message.text).lower()
            response = R.pwd_Checker(text)
            update.message.reply_text(response)
        elif (v.wait) == "ara":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["ara"], Adjuster.ara)
            update.message.reply_text(response)
        else:
            text = str(update.message.text).lower()
            response = R.sample_response(text, update)
            update.message.reply_text(response)
    else:
        if (v.wait) == "default":
            text = str(update.message.text).lower()
            response = R.sample_response(text, update)
            update.message.reply_text(response)
        elif (v.wait) == "hayvanekle":
            text = str(update.message.text).lower()
            response = Hayvan.orderOfAddAnimal(text, update)
            update.message.reply_text(response)
        elif (v.wait) == "insanekle":
            text = str(update.message.text).lower()
            response = Human.orderOfAddHuman(text, update)
            update.message.reply_text(response)
        elif (v.wait) == "ihbarekle":
            text = str(update.message.text).lower()
            response = ihbar.orderOfAddihbar(text, update)
            update.message.reply_text(response)
        elif (v.wait) == "ihbarUygulamaEkle":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["ihbarKimlik", "text", "zaman"], Adjuster.ihbarUygulamaEkle)
            update.message.reply_text(response)
        elif (v.wait) == "ihbaroperasyonEkle":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["ihbarKimlik", "text", "zaman"], Adjuster.ihbaroperasyonEkle)
            update.message.reply_text(response)
        elif (v.wait) == "tedaviBitir":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "zaman"], Adjuster.tedaviBitir)
            update.message.reply_text(response)
        elif (v.wait) == "tedaviBaslat":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "zaman"], Adjuster.tedaviBaslat)
            update.message.reply_text(response)
        elif (v.wait) == "sahiplikBeklemeBaslat":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "zaman"], Adjuster.sahiplikBeklemeBaslat)
            update.message.reply_text(response)
        elif (v.wait) == "sahiplikBeklemeBitir":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "zaman"], Adjuster.sahiplikBeklemeBitir)
            update.message.reply_text(response)
        elif (v.wait) == "SahiplikDurumuTrue":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "zaman"], Adjuster.SahiplikDurumuTrue)
            update.message.reply_text(response)
        elif (v.wait) == "sahiplendir":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "humanKimlik", "zaman"], Adjuster.sahiplendir)
            update.message.reply_text(response)
        elif (v.wait) == "addGeciciYuva":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "humanKimlik", "zaman"], Adjuster.addGeciciYuva)
            update.message.reply_text(response)
        elif (v.wait) == "ihbarBagla":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["hayvanKimlik", "ihbarKimlik", "zaman"], Adjuster.ihbarBagla)
            update.message.reply_text(response)
        elif (v.wait) == "ara":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["ara"], Adjuster.ara)
            update.message.reply_text(response)
        elif (v.wait) == "itemsil":
            text = str(update.message.text).lower()
            response = Adjuster.orderOfAdjuster(
                text, update, ["ara"], Adjuster.deleteItem)
            update.message.reply_text(response)
        # elif (v.wait) == "pwd":
        #     text = str(update.message.text).lower()
        #     response = R.pwd_Checker(text)
        #     update.message.reply_text(response)
        # elif (v.wait) == "cardBal":
        #     text = str(update.message.text).lower()
        #     response = R.card_balance(text, update)
        #     update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    # dp.add_handler(CommandHandler("start", start_comment))
    # dp.add_handler(CommandHandler("help", help_comment))
    dp.add_handler(MessageHandler(Filters.text, handle_comment))
    dp.add_error_handler(error)

    updater.start_polling(2)

    updater.idle()


main()
