import requests
import telebot
from telebot import types
from user_agent import generate_user_agent

tok = '1805574903:AAF_WcH4Ytc6iHGQSvcYX2qu3tyHoseKUkc'
bot = telebot.TeleBot(tok)

headers = {
    'HOST': "www.instagram.com",
    'KeepAlive': 'True',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
}

@bot.message_handler(commands=['start', 'back'])
def send_msg(message):
    user = message.chat.first_name
    key = types.InlineKeyboardMarkup(row_width=3)
    st = types.InlineKeyboardButton("اضغط هنا", callback_data='start')
    key.add(st)
    bot.send_message(message.chat.id, f" مرحبا بك  {user} ", reply_markup=key)


#@bot.message_handler(commands=['help', 'Help'])
#def send_msg(message):
    #reb=bot.send_message(message.chat.id, f"للحصول على الايدي ارسل اليوزر ")

def ddd(message):
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={message.text}")
        ree = re.json()
        dat = ree['data']
        bot.send_message(message.chat.id, text=f"تـاريخ انشــاء الحــساب : {dat}\n\n")
        bot.send_message(message.chat.id, text=f" اكـتـب ID حساب اخــر .. \n\n"
                                                   f"او اذا واجهت مشاكل ابــد مـن جـديـد  /back")


@bot.callback_query_handler(func=lambda call: True)
def make(call):
    if call.data == 'start':
        bot.edit_message_text(chat_id=(call.message.chat.id), message_id=(call.message.id),
                              text='ارسال يوزر اي شخص وانتظر ..')

        @bot.message_handler(func=(lambda message: True))
        def send_message(message):
            if message.text:
                url_id = f'https://www.instagram.com/{message.text}/feed/?__a=1'
                req_id = requests.get(url_id, headers=headers).json()
                idd =str(req_id['graphql']['user']['id'])
                re = requests.get(f"https://o7aa.pythonanywhere.com/?id={idd}")
                ree = re.json()
                dat = ree['data']
                bot.send_message(message.chat.id, text=f"تـاريخ انشــاء الحــساب : {dat}\n\n")
                bot.send_message(message.chat.id, text=f" اكـتـب ID حساب اخــر .. \n\n"
                                                       f"او اذا واجهت مشاكل ابــد مـن جـديـد  /back")


bot.polling()
