from typing import Text
import telebot
from telebot import types
import sqlite3
#from telegram import ParseMode

from prettytable import PrettyTable
from tabulate import tabulate

#from telegram import ParseMode
from telegram.constants import ParseMode
#from telegram.constants import ParseMode
#from telegram.ext import Updater
#from telegram.ext import CommandHandler 

bot = telebot.TeleBot('5058346875:AAFCcTGUCnZ0BKUjpwxq1keCeokgX4JF-uE')

#joined_file = open("joined.txt", 'w') #если файл не создан, создаем его
#joined_file.close()

#joined_file = open("joined.txt")
#joined_users = set() #set работает лучше массива, т.к в set нельзя добавить 2 одинаковых id
#for i in joined_file:
#    joined_users.add(i.strip())
#joined_file.close()

entered_class = ''

#@bot.message_handler(commands=['start'])
#def start(message):
#    #if not str(message.chat.id) in joined_users:
#    #    joined_file = open("joined.txt", "a")
#    #    joined_file.write(str(message.chat.id)+'\n')
#    #    joined_users.add(message.chat.id)
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    db = sqlite3.connect('database.sqlite3')
#    sql = db.cursor()
#    date = sql.execute("SELECT date FROM substitutions")
#    number_of_date = []
#    for i in date:
#        number_of_date.append(i[0])
#    number_of_date = list(set(number_of_date))
#    btn1 = types.KeyboardButton(f"📑 Замещение")#на " + ' '.join(number_of_date))
#    markup.add(btn1)
#    bot.send_message(message.chat.id, text = '✏️Привет, Чтобы узнать расписание, напиши свой класс.', reply_markup=markup)

@bot.message_handler(commands=['start'])#commands=['']) #добавляем id участника бота в файл
def start(message):
    #if not str(message.chat.id) in joined_users:
    #    joined_file = open("joined.txt", "a")
    #    joined_file.write(str(message.chat.id)+'\n')
    #    joined_users.add(message.chat.id)
    db = sqlite3.connect('database.sqlite3')
    sql = db.cursor()  
    #на " + ' '.join(number_of_date))
    
      
    
                        #date = sql.execute("SELECT date FROM substitutions")
                        #number_of_date = []
                        #for i in date:
                        #    number_of_date.append(i[0])
                        #number_of_date = list(set(number_of_date))

    bot.send_message(message.chat.id, text='''✏️Привет, Бот предоставляет информацию о расписании. Напиши /help, чтобы узнать команды.''', reply_markup=markup)
        
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='Напиши свой класс (например 6-1), а затем нажми на день недели, который тебе нужен.', reply_markup=markup)


#@bot.message_handler(commands=['announce'])
#def announce(message):
#    announcement = message.text[message.text.find(' ')+1::]
#    if "gimnazpass271" in announcement:
#        text = announcement[(announcement.find("-text")+6):announcement.find(" -img")]
#        image_url = announcement[announcement.find("-img")+5::]
#        for user in joined_users:
#            bot.send_message(user, text)
#            bot.send_photo(chat_id=joined_users, photo=image_url)

#@bot.callback_query_handler(func = lambda call: True)
#def answer(call):
#    markup_reply = types.ReplyKeyboardMarkup(resuze_keyboard = True)
#    item_id = types.KeyboardButton('Замещение')
#
#    markup_reply.add(item_id)
#    bot.send_message()


@bot.message_handler(content_types=['text'])#commands=['announce']
def get_text(message):
    global entered_class
    
    #print(entered_class)

    db = sqlite3.connect('database.sqlite3')
    sql = db.cursor()
    t_users = sql.execute("SELECT userid FROM users").fetchall()
    users = []
    if t_users != None:
        for i in t_users:
            users.append(i[0])
    #print(users)
    if users == None or str(message.chat.id) not in users:
        sql.execute("INSERT INTO users VALUES (?)", (message.chat.id,))
        db.commit()
    date = sql.execute("SELECT date FROM substitutions")
    request_classes = sql.execute("SELECT class FROM timetable")

    classes = []
    for i in request_classes:
        classes.append(i[0])
    classes = list(set(classes))
    #print(classes)
    number_of_date = []
    for i in date:
        number_of_date.append(i[0])
    number_of_date = list(set(number_of_date))
    #if(message.text == f"📑 Замещение"):#на" + ' '.join(number_of_date)):
    #    
#
#
#
    #    #columns = ['Дата', 'Номер урока', 'Класс',  'Кто замещает', 'Урок', 'Кабинет']
    #    teachers1 = sql.execute("SELECT teacher1 FROM substitutions")
    #    teachers1_true = []
    #    for i in teachers1:
    #        teachers1_true.append(i[0])
    #    teachers1_true = list(set(teachers1_true))
    #    dates = sql.execute("SELECT date FROM substitutions")
    #    number_of_dates = []
#
    #    for date in dates:
    #        number_of_dates.append(date[0])
    #    number_of_dates = list(set(number_of_dates))
    #    headers=['Дата', '№ урока', 'класс','Кого замещают', 'Кто замещает', 'Предмет', 'Кабинет']
    #    table_subs = PrettyTable(headers)
    #    data = []
    #    for date in number_of_dates:
    #        for j in teachers1_true:
    #            
#
    #            for b in sql.execute(f"""SELECT date, number_of_lesson, class, teacher2, subject, cabinet FROM substitutions WHERE teacher1='{j}' and date='{date}' """):
    #                data.append((b[0],b[1],b[2],j,b[3],b[4],b[5]))
    #                table_subs.add_row([b[0],b[1],b[2],j,b[3],b[4],b[5]])
    #            
    #            
    #            
    #            #print(data)
    #            #tablesubs = PrettyTable(headers)
    #            #bot.send_message(message.chat.id, j)
    #            #bot.send_message(message.chat.id, table)
    #        #tablesubs.add_row()
    #        #date = sql.execute("SELECT date FROM substitutions")
    #        #img = open(f'announce_{date}.png', 'rb')
    #        #bot.send_photo(message.chat.id, text=f'<pre>{tablesubs}</pre>', parse_mode=ParseMode.HTML)     
    #            #print(type(j))
    #            #print(type(table))
    #        #print(tabulate([data[0], data[1], data[2], data[4], data[5], data[6]], headers=['Дата', '№ урока', 'класс', 'Кто замещает', 'Предмет', 'Кабинет']))
    #        #data.append(('','','','','','',''))
    #    table = tabulate(data, headers=['Дата', '№ урока', 'класс',  'Кто замещает', 'Предмет', 'Кабинет'])
    #    bot.send_message(message.chat.id, text=f'<pre>{table_subs}</pre>', parse_mode=ParseMode.HTML)
    if message.text in classes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Суббота")

        markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
        bot.send_message(message.chat.id, text=f'Укажи день недели',reply_markup=markup)
        #img = open(f'{message.text}.png', 'rb')
        #bot.send_photo(message.chat.id, img)

        #week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        week_short = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']
        
        #print(timeTable)
        #for day in range(6):
#
        #    current_request = list(sql.execute(f"SELECT lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7 FROM timetable WHERE class='{message.text}' and day='{week[day]}'").fetchall()[0])
        #    for j in range(7):
        #        if current_request[j] == ' ':
        #            current_request[j] = '---------'
        #    num = 1
        #    for i in current_request:
        #        timeTable.add_row([week_short[day], f'{num}', i])
        #        num += 1
        #    #myTable.add_row(['', '', ''])
        #bot.send_message(message.chat.id, text=f'<pre>{timeTable}</pre>', parse_mode=ParseMode.HTML)
        #print(myTable)
    if entered_class in classes and message.text in ["Понедельник","Вторник", "Среда", "Четверг", "Пятница", "Суббота"]:
        current_request = list(sql.execute(f"SELECT lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7 FROM timetable WHERE class='{entered_class}' and day='{message.text}'").fetchall()[0])
        #print(current_request)
        timeTable = PrettyTable(["№ Урока", f"{message.text}"])#])
        for iter in range(7):
            timeTable.add_row([str(iter+1), f'{current_request[iter]}'])
        bot.send_message(message.chat.id, text=f'<pre>{timeTable}</pre>', parse_mode=ParseMode.HTML)
    elif entered_class not in classes:
        entered_class = message.text
    if message.text not in ["Понедельник","Вторник", "Среда", "Четверг", "Пятница", "Суббота"] and message.text not in classes:
        bot.send_message(message.chat.id, text = 'Неизвестная команда!')
    

bot.polling()
