import telebot
import smtplib, ssl
import re
from telebot import types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
# 5946631163:AAFbTKU5UYKudelCo0K51AG3-URNqgU23n8 -new bot

bot = telebot.TeleBot('6392355149:AAHM3pGdr4lN1PXkmFGrgwFkBwRWPWCKlKQ')
port = 465  # For SSL
password = 'hphgdkfxshbfefpi'
chatID = -943952027 # rfu_bot id 5776904173 myself 449714355 bot - 1001689526561 self = 5733204941
#mail_to = "rfumarxist@tutanota.com" #were to send e-mail
mail_to = "Laborconsultation@proton.me" #were to send e-mail

@bot.message_handler(commands = ['start'])
def start(message):
    resp = open('./files/hello.txt','r',encoding='utf-8')
    #bot.send_message(message.chat.id,resp)
    #btn = types.InlineKeyboardMarkup()
    #btn.add(types.InlineKeyboardButton("Отримати юридичну консультацію", callback_data='consult'))
    #btn.add(types.InlineKeyboardButton("Поділитись листом про порушення трудових прав на підприємстві", callback_data='mail_1'))
    #btn.add(types.InlineKeyboardButton("Розповісти про недобросовісного роботодавця", callback_data='mail_2'))
    #btn.add(types.InlineKeyboardButton("Хочу почати боротьбу. З чого почати?", callback_data='info_1'))
    #btn.add(types.InlineKeyboardButton("Допомога", callback_data='help'))
    #btn.add(types.InlineKeyboardButton("Медіа-ресурси РФУ", callback_data='links'))
    bot.send_message(message.chat.id,resp, parse_mode='html')


@bot.message_handler()
def share(message):
    #bot.send_message(message.chat.id,message.reply_to_message.text if message.reply_to_message != None else "empty" )
    if re.search("^Сообщение от.*:\n[0-9]+.*",message.reply_to_message.text if message.reply_to_message != None else "empty") != None:
        msg = message.reply_to_message.text.split(":\n")
        reply_to_id = re.findall('[0-9]+', msg[1])[0]
        print("replyer id"+reply_to_id)
        bot.send_message(reply_to_id,message.text, parse_mode='html')
    #bot.send_message(message.chat.id,message.reply_to_message)
    #bot.reply_to(message.chat.id,message)
    elif re.search("^Ответ от РФУ:.*",message.text) != None:
        text = message.text.split(":")
        bot.send_message(text[1],text[2], parse_mode='html')
        bot.reply_to()
    else:
        if message.chat.id != chatID:
            bot.send_message(message.chat.id,'<b>Дякуємо! Наші юристи скоро дадуть відповідь</b>', parse_mode='html')
            bot.send_message(chatID,"Сообщение от @"+ message.from_user.username + ":\n"+ str(message.from_user.id)+":\n" + message.text, parse_mode='html')



#@bot.callback_query_handler(func=lambda call: True)
#def callback_inline(call):
#    try:
#        if call.message:
#            if call.data == 'mail_1':
#                #bot.send_message(call.message.chat.id,"Почта нарушение прав: \n Надішліть повідомлення у відповідь на це для зв\'язку через пошту")
#                bot.send_message(call.message.chat.id,"Порушення прав:\n Надішліть повідомлення у відповідь на це для зв\'язку через телеграм бот або надішліть файл")
#            elif call.data == 'mail_2':
                #bot.send_message(call.message.chat.id,"Почта работодатель: \n Надішліть повідомлення у відповідь на це для зв\'язку через пошту")
#                bot.send_message(call.message.chat.id,"Роботодавець:\n Надішліть повідомлення у відповідь на це для зв\'язку через телеграм бот або надішліть файл")
                #bot.send_message(call.message.chat.id,"Надішліть повідомлення формату \'Почта работодатель:<Текст повідомлення>\' або \'Работодатель:<Текст повідомлення>\' для зв\'язку через телеграм бот")
 #           elif call.data == 'info_1':
 #               resp = open('./files/info_1.txt','r',newline="",encoding='utf-8')
 #               btn = types.InlineKeyboardMarkup()
 #               btn.add(types.InlineKeyboardButton("Чому не можна вести боротьбу самотужки?",callback_data=forward(call.data)))
 #               btn.add(types.InlineKeyboardButton("На головну",callback_data="main"))
 #               bot.send_message(call.message.chat.id,resp.read(), parse_mode='html',reply_markup=btn)
 #           elif call.data == 'info_2':
 #               resp = open('./files/info_2.txt','r',encoding='utf-8')
 #               btn = types.InlineKeyboardMarkup()
 #               btn.add(types.InlineKeyboardButton("План перемоги",callback_data=forward(call.data)))
 #               btn.add(types.InlineKeyboardButton("Назад",callback_data=back(call.data)))
 #               btn.add(types.InlineKeyboardButton("На головну",callback_data="main"))
 #               bot.send_message(call.message.chat.id,resp.read(), parse_mode='html',reply_markup=btn)
 #           elif call.data == 'info_3':
 #               resp = open('./files/info_3.txt','r',encoding='utf-8')
 #               btn = types.InlineKeyboardMarkup()
 #               btn.add(types.InlineKeyboardButton("Корисні поради",callback_data=forward(call.data)))
 #               btn.add(types.InlineKeyboardButton("Назад",callback_data=back(call.data)))
 #               btn.add(types.InlineKeyboardButton("На головну",callback_data="main"))
 #               bot.send_message(call.message.chat.id,resp.read(), parse_mode='html',reply_markup=btn)
 #           elif call.data == 'info_4':
 #               resp = open('./files/info_4.txt','r',encoding='utf-8')
 #               btn = types.InlineKeyboardMarkup()
 #               btn.add(types.InlineKeyboardButton("Назад",callback_data=back(call.data)))
 #               btn.add(types.InlineKeyboardButton("На головну",callback_data="main"))
 #               bot.send_message(call.message.chat.id,resp.read(), parse_mode='html',reply_markup=btn)
 #           elif call.data == 'help':
 #               btn = types.InlineKeyboardMarkup()
 #               btn.add(types.InlineKeyboardButton("Донат (криптовалюта)", callback_data="help_1"))
 #               btn.add(types.InlineKeyboardButton("Доєднатися до філософського гуртку", callback_data="help_2"))
 #               btn.add(types.InlineKeyboardButton("Доєднатися до проекту", callback_data="help_2"))
 #               btn.add(types.InlineKeyboardButton("На головну",callback_data="main"))
 #               bot.send_message(call.message.chat.id,'Допомога',reply_markup=btn)
 #           elif call.data == 'help_1':
 #               resp = open('./files/help_1.txt','r',encoding='utf-8')
 #               bot.send_message(call.message.chat.id,resp.read(), parse_mode='html')
 #           elif call.data == 'help_2':
 #               resp = open('./files/help_2.txt','r',encoding='utf-8')
 #               bot.send_message(call.message.chat.id,resp.read(), parse_mode='html')
 #           elif call.data == 'links':
 #               btn = types.InlineKeyboardMarkup()
 #               btn.add(types.InlineKeyboardButton("Сайт РФУ", url = "https://rfu.red/"))
 #               btn.add(types.InlineKeyboardButton("Youtube канал", url = "https://www.youtube.com/channel/UC7_PphtW31IZ5f49CqJZXiA/featured"))
 #               btn.add(types.InlineKeyboardButton("Канал в Telegram", url = "https://t.me/RFU_media"))
 #               btn.add(types.InlineKeyboardButton("Сторінка на Facebook", url = "https://www.facebook.com/rfu.media/"))
 #               btn.add(types.InlineKeyboardButton("Аккаунт в Instagram", url = "https://www.instagram.com/rfu_media/"))
 #               btn.add(types.InlineKeyboardButton("Аккаунт в Twitter", url = "https://twitter.com/rfumedia"))
 #               btn.add(types.InlineKeyboardButton("На головну",callback_data="main"))
 #               bot.send_message(call.message.chat.id,'Ознайомитися з ресурсами РФУ',reply_markup=btn)
 #           elif call.data == 'consult':
#              #bot.send_message(call.message.chat.id,"Почта консультация: \n  Опишіть нам вашу проблему у вiдповіді на це повідомлення для зв\'язку через пошту")
#                bot.send_message(call.message.chat.id,"Консультація:\n Опишіть нам вашу проблему у вiдповіді на це повідомлення для зв\'язку через телеграм бот")
#            elif call.data == 'main':
#                start(call.message)
#    except Exception as e:
#        print(repr(e))

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        #chatID = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = './files/received/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,'<b>Дякуємо! З вами зв’яжуться, якщо в нас виникнуть деякі питання</b>', parse_mode='html')
        bot.send_message(chatID,"Сообщение от @"+ message.from_user.username + ":\n"+ str(message.from_user.id)+":\n", parse_mode='html')
        bot.send_document(chatID, open(src, 'rb'))
    except Exception as e:
        bot.reply_to(message, e)

def send_mail(subject,msg):
    context = ssl.create_default_context()
    letter = MIMEMultipart("alternative")
    letter["Subject"] = subject
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sgfdpk.for.bot@gmail.com", password)
        letter.attach(MIMEText(msg, "plain"))
        server.sendmail("sgfdpk.for.bot@gmail", mail_to, letter.as_string())

def forward(data):
    split = data.split("_")
    num = int(split[1]) + 1
    return split[0] + "_" + str(num)

def back(data):
    split = data.split("_")
    num = int(split[1]) - 1
    return split[0] + "_" + str(num)

def main():
    try:
        print("Starting bot")
        bot.polling(non_stop=True)
    except Exception as e:
        print("Bot failed with Error\n" + repr(e))
        bot.stop_polling()
        sleep(3)
        print("Trying to restart")
        main()
main()
#bot.polling(non_stop=True)
