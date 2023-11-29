import telebot
from datetime import timedelta, datetime

API_TOKEN = '6867574423:AAGTo72Ey78pSyvxiwaP5lxM2RJfYfrywao'

bot = telebot.TeleBot(API_TOKEN)


      

def calc_message(a):
            global result
            diff = 0
            for item in range (len(a)-1):
                diff = diff + (a[item+1] - a[item])
            pace = -(diff/(item+1))
            nowDate = datetime.now()
            expire = timedelta(a[-1]//pace)
            targetDate = nowDate + expire
            targetDateRes = str(targetDate.strftime("%d %B %Y (%A)"))
            pace = str(round(pace, 1))
            result = "The queue pace is " + pace + ". You will be received at the Embassy " + targetDateRes
            return result


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello! I’ll help you find out the speed of visitor flow at the Russian Embassy in Yerevan!')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def send_calc(message):
    def data_convert(a):
        global lsTemp
        lsTemp = []
        local = ""
        for char in a:
              if char == " " or char == "  " or char ==",":
                    lsTemp.append(int(local))
                    local = ""
              else:
                    local += char
        return lsTemp
    

    data_convert(message.text)
    calc_message(lsTemp)

    message.text = result
    bot.reply_to(message, message.text)

bot.infinity_polling()