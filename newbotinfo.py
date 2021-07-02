import telepot
import time
import requests
from telepot.loop import MessageLoop

n = str
bot = telepot.Bot('1744244474:AAHLZPNxMS_SQXeMwsB-5oY-vvap6zsqXjQ')

def randpas(msg):
    person_id = msg['chat']['id']
    command = msg['text']
    print("command: ", command)
    if command == '/start':
        replay = "اهلا بك, ادخل يوزر الشخص"
        bot.sendMessage(person_id, replay)
    elif command == '/help':
        replay = "ادخل اليوزر بدون علامة(@)\n\n اذ لم تظهر النتائج تأكد من كتابته بالشكل الصحيح`✔ "
        bot.sendMessage(person_id, replay)
    elif command == command:
        user = command
        headers = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
            'Cookie': 'cookie',
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9" }
        try:
            r = requests.Session()
            url_id = f'https://www.instagram.com/{user}/?__a=1'
            ul="https://www.instagram.com/"+user
            req_id = r.get(url_id, headers=headers).json()
            bio = "· · • • • Bio • • • · ·\n\n"+str(req_id['graphql']['user']['biography'])
            url = "· · • • • Website • • • · ·\n\n"+str(req_id['graphql']['user']['external_url'])
            nam = "· · • • • Name • • • · ·\n\n"+str(req_id['graphql']['user']['full_name'])
            idd = "· · • • • Id • • • · ·\n\n"+str(req_id['graphql']['user']['id'])
            isp = "· · • • • الحساب خاص او غير خاص • • • · ·\n\n"+str(req_id['graphql']['user']['is_private'])
            isv = "· · • • • علامة التحقق, الصح الازرق • • • · ·\n\n"+str(req_id['graphql']['user']['is_verified'])
            pro =str(req_id['graphql']['user']['profile_pic_url_hd'])
            empt= "=========#By @ahmed_4a========="

            bot.sendMessage(person_id,empt)
            bot.sendMessage(person_id,ul)
            bot.sendMessage(person_id, nam)
            bot.sendMessage(person_id, idd)
            bot.sendMessage(person_id, isp)
            bot.sendMessage(person_id, isv)
            bot.sendMessage(person_id, bio)
            bot.sendMessage(person_id, url)
            bot.sendPhoto(person_id, pro)
            bot.sendMessage(person_id,empt)

        except TypeError:
            s="no user"
            bot.sendMessage(person_id, s)


MessageLoop(bot, randpas).run_as_thread()
while 1:
    time.sleep(1)
