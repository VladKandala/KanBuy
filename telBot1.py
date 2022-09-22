import telebot
import mysql.connector
from telebot import types


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234567890ggvladGG",
    port="3306",
    database="tel_bot"
)
cursor = db.cursor()
#ОТОБРАЖАЕНИЕ АЙФОНОВ Х
def defX(message):
    if message.text == '💰От дорогих к дешевым⬇':
        markup_inline = types.InlineKeyboardMarkup()
        
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дорогих
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone X' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone X' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X' ORDER BY ssulka_zena DESC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
            #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://i.citrus.ua/imgcache/size_800/uploads/shop/8/3/839a9742d5dcd127f96982c50a2a7f75.jpg', reply_markup=markup_inline)
    elif message.text == '💰От дешевых к дорогим⬆':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дешевых
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone X' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone X' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X' ORDER BY ssulka_zena ASC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
            #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://i.citrus.ua/imgcache/size_800/uploads/shop/8/3/839a9742d5dcd127f96982c50a2a7f75.jpg', reply_markup=markup_inline)

#ОТОБРАЖАЕНИЕ АЙФОНОВ 11
def def11(message):
    if message.text == '💰От дорогих к дешевым⬇':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дорогих
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone 11' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone 11' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone 11' ORDER BY ssulka_zena DESC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
           #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://cdn.comfy.ua/media/catalog/product/cache/4/image/600x/9df78eab33525d08d6e5fb8d27136e95/a/p/apple_iphone_11_64gb_black_0_3.jpg', reply_markup=markup_inline)
    elif message.text == '💰От дешевых к дорогим⬆':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дешевых
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone 11' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone 11' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone 11' ORDER BY ssulka_zena ASC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
            #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://cdn.comfy.ua/media/catalog/product/cache/4/image/600x/9df78eab33525d08d6e5fb8d27136e95/a/p/apple_iphone_11_64gb_black_0_3.jpg', reply_markup=markup_inline)

#ОТОБРАЖАЕНИЕ АЙФОНОВ ХR
def defXR(message):
    if message.text == '💰От дорогих к дешевым⬇':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дорогих
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XR' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XR' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone XR' ORDER BY ssulka_zena DESC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
            #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://i.allo.ua/media/catalog/product/cache/1/image/600x600/9df78eab33525d08d6e5fb8d27136e95/a/p/apple-iphone-xr-128gb-black-mry92-3.1000x1000_.jpg', reply_markup=markup_inline)
    elif message.text == '💰От дешевых к дорогим⬆':
        markup_inline = types.InlineKeyboardMarkup()
         #--------------------------------------------------------------------------------------------
        #Отображение стоимости дешевых
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XR' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XR' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone XR' ORDER BY ssulka_zena ASC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
           #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://i.allo.ua/media/catalog/product/cache/1/image/600x600/9df78eab33525d08d6e5fb8d27136e95/a/p/apple-iphone-xr-128gb-black-mry92-3.1000x1000_.jpg', reply_markup=markup_inline)

#ОТОБРАЖАЕНИЕ АЙФОНОВ ХS
def defXS(message):
    if message.text == '💰От дорогих к дешевым⬇':
        markup_inline = types.InlineKeyboardMarkup()
        
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дорогих
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone XS' ORDER BY ssulka_zena DESC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
            #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://i.citrus.ua/imgcache/size_800/uploads/shop/3/c/3ca7aabff2212d386690746e4f259df9.jpg', reply_markup=markup_inline)
    elif message.text == '💰От дешевых к дорогим⬆':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дешевых
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone XS' ORDER BY ssulka_zena ASC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
            #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://i.citrus.ua/imgcache/size_800/uploads/shop/3/c/3ca7aabff2212d386690746e4f259df9.jpg', reply_markup=markup_inline)


#ОТОБРАЖАЕНИЕ АЙФОНОВ ХS_MAX
def defXS_MAX(message):
    if message.text == '💰От дорогих к дешевым⬇':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дорогих
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS Max' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS Max' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone XS Max' ORDER BY ssulka_zena DESC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
           #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://www.ipeople.in.ua/files/products/839784.800x600w.jpeg', reply_markup=markup_inline)
    elif message.text == '💰От дешевых к дорогим⬆':
        markup_inline = types.InlineKeyboardMarkup()
        #--------------------------------------------------------------------------------------------
        #Отображение стоимости дешевых
        bot.send_message(message.chat.id, "Стоимость от:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS Max' ORDER BY ssulka_zena ASC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        
        bot.send_message(message.chat.id, "Стоимость до:")
            
        cursor.execute("SELECT ssulka_zena FROM site where product_name='Iphone XS Max' ORDER BY ssulka_zena DESC limit 1")
        myresult = cursor.fetchall()
        for x in myresult:
            bot.send_message(message.chat.id, x)
        #-------------------------------------------------------------------------------------------------------
        
        cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone XS Max' ORDER BY ssulka_zena ASC")
        myresult = cursor.fetchall()
        for x in myresult:
            s = str(x)
            s = s[2:len(s) - 3]
           #Добавить кругом
            result_str = ""
            for i in range(0, len(s)):
                 if i > 7:
                    if s[i] != '/':
                        result_str = result_str + s[i]
                    else:
                        break
                    #-------------------------------------
            markup_inline.add(types.InlineKeyboardButton(text=result_str, url=s))
        bot.send_photo(message.chat.id, 'https://www.ipeople.in.ua/files/products/839784.800x600w.jpeg', reply_markup=markup_inline)



#2113973109:AAHpjnDYmcP1Mi6sc8krjU5I
TOKEN = "2113973109:AAHpjnmcP1DgMi6sc8IcjU5I"
bot = telebot.TeleBot(TOKEN)




#@bot.message_handler(commands=['Iphone_X'])
#def get_user_info1(message):
   # cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X'")
    #myresult = cursor.fetchall()

   # for x in myresult:
   #  bot.send_message(message.from_user.id, text=x)
    # print(x)
#cursor.close()

#НАЧАЛО БОТА
@bot.message_handler(commands=['start'])
def get_user_info(message):
    bot.reply_to(message, "🤖KanBuy - простой и быстрый способ\n сравнения цифровой техники:🤖\n"+"💎 Apple 💎\n"
                                                                                        "💎 Samsung 💎")
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Apple', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Samsung', callback_data='no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, '☄Выберите компанию:☄',
                 reply_markup=markup_inline
                 )

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('📱Iphone')
        item_username = types.KeyboardButton('📷Ipad')
        back = types.KeyboardButton('В главное меню')

        markup_reply.add(item_id, item_username, back)
        bot.send_message(call.message.chat.id, 'Выберите категорию: ',
                         reply_markup= markup_reply
                         )
        bot.answer_callback_query(callback_query_id=call.id)
    elif call.data == 'no':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=False)
        bot.send_message(call.message.chat.id, '⚙В разработке⌛',
                         reply_markup=markup_reply
                         )
        bot.answer_callback_query(callback_query_id=call.id)



@bot.message_handler(content_types=['text'])
def Iphone_1(message):
   if message.chat.type == 'private':
       if message.text == '📱Iphone':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           X = types.KeyboardButton('🧊Iphone X🧊')
           X_s = types.KeyboardButton('⚡Iphone XS⚡')
           X_s_max = types.KeyboardButton('⛓Iphone XS Max⛓')
           X_r = types.KeyboardButton('🪐Iphone XR🪐')
           X_11 = types.KeyboardButton('⭐Iphone 11⭐')
           back = types.KeyboardButton('↪Назад')
           markup_reply.add(X_r, X, X_s,X_s_max, X_11, back)
           bot.send_message(message.chat.id, '🔥IPHONE:🔥', reply_markup=markup_reply)

       elif message.text == '📷Ipad':
            bot.send_message(message.chat.id, '⚙В разработке⌛')

       elif message.text == '↪Назад':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            iphone = types.KeyboardButton('📱Iphone')
            ipad = types.KeyboardButton('📷Ipad')
            back = types.KeyboardButton('В главное меню')
            markup_reply.add(iphone, ipad, back)
            bot.send_message(message.chat.id, '↪Назад', reply_markup=markup_reply)
       elif message.text == '↩Вернуться к моделям':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           X = types.KeyboardButton('🧊Iphone X🧊')
           X_s = types.KeyboardButton('⚡Iphone XS⚡')
           X_s_max = types.KeyboardButton('⛓Iphone XS Max⛓')
           X_r = types.KeyboardButton('🪐Iphone XR🪐')
           X_11 = types.KeyboardButton('⭐Iphone 11⭐')
           back = types.KeyboardButton('↪Назад')
           markup_reply.add(X_r, X, X_s, X_s_max, X_11, back)
           bot.send_message(message.chat.id, '🔥IPHONE:🔥', reply_markup=markup_reply)
       elif message.text == 'В главное меню':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           apple = types.KeyboardButton('💎 Apple 💎')
           samsung = types.KeyboardButton('💎 Samsung 💎')
           markup_reply.add(apple, samsung)
           bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markup_reply)

       elif message.text == '💎 Samsung 💎':
            bot.send_message(message.chat.id, '⚙В разработке⌛')

       elif message.text == '💎 Apple 💎':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           iphone = types.KeyboardButton('📱Iphone')
           ipad = types.KeyboardButton('📷Ipad')
           back = types.KeyboardButton('В главное меню')
           markup_reply.add(iphone, ipad, back)
           bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup_reply)
       elif message.text == '🧊Iphone X🧊':
             markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
             zena_ot = types.KeyboardButton('💰От дорогих к дешевым⬇')
             zena_do = types.KeyboardButton('💰От дешевых к дорогим⬆')
             back = types.KeyboardButton('↩Вернуться к моделям')
             markup_reply.add(zena_ot, zena_do, back)
             bot.send_message(message.chat.id, 'Выберите сортировку цены: ', reply_markup=markup_reply)
             bot.register_next_step_handler(message, defX)

          # if message.text == '💰Цена⬇':
             #  cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X' ORDER BY ssulka_zena DESC")
               #myresult = cursor.fetchall()

              # for x in myresult:
                 #  bot.send_message(message.from_user.id, text=x)
                 #  print(x)
       elif message.text == '⚡Iphone XS⚡':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           zena_ot = types.KeyboardButton('💰От дорогих к дешевым⬇')
           zena_do = types.KeyboardButton('💰От дешевых к дорогим⬆')
           back = types.KeyboardButton('↩Вернуться к моделям')
           markup_reply.add(zena_ot, zena_do, back)
           bot.send_message(message.chat.id, 'Выберите сортировку цены: ', reply_markup=markup_reply)
           bot.register_next_step_handler(message, defXS)
       elif message.text == '🪐Iphone XR🪐':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           zena_ot = types.KeyboardButton('💰От дорогих к дешевым⬇')
           zena_do = types.KeyboardButton('💰От дешевых к дорогим⬆')
           back = types.KeyboardButton('↩Вернуться к моделям')
           markup_reply.add(zena_ot, zena_do, back)
           bot.send_message(message.chat.id, 'Выберите сортировку цены: ', reply_markup=markup_reply)
           bot.register_next_step_handler(message, defXR)
       elif message.text == '⛓Iphone XS Max⛓':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           zena_ot = types.KeyboardButton('💰От дорогих к дешевым⬇')
           zena_do = types.KeyboardButton('💰От дешевых к дорогим⬆')
           back = types.KeyboardButton('↩Вернуться к моделям')
           markup_reply.add(zena_ot, zena_do, back)
           bot.send_message(message.chat.id, 'Выберите сортировку цены: ', reply_markup=markup_reply)
           bot.register_next_step_handler(message, defXS_MAX)
       elif message.text == '⭐Iphone 11⭐':
           markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
           zena_ot = types.KeyboardButton('💰От дорогих к дешевым⬇')
           zena_do = types.KeyboardButton('💰От дешевых к дорогим⬆')
           back = types.KeyboardButton('↩Вернуться к моделям')
           markup_reply.add(zena_ot, zena_do, back)
           bot.send_message(message.chat.id, 'Выберите сортировку цены: ', reply_markup=markup_reply)
           bot.register_next_step_handler(message, def11)
           #elif message.text == '💰Цена⬇':
           #if message.text == 'Iphone X':
           # cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X' ORDER BY ssulka_zena DESC")
           # myresult = cursor.fetchall()

           # for x in myresult:
           #   bot.send_message(message.from_user.id, text=x)
           #    print(x)
           # elif message.text == '💰Цена⬆':
           #if message.text == 'Iphone X':
           # cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X' ORDER BY ssulka_zena ASC")
           # myresult = cursor.fetchall()

           # for x in myresult:
           # bot.send_message(message.from_user.id, text=x)
           # print(x)










bot.polling(none_stop= True)
# elif message.text == 'Ввести минимальную цену:':
          # markup_inline = types.InlineKeyboardMarkup()
          # cursor.execute("SELECT ssulka_ FROM site where product_name='Iphone X'")
           #myresult = cursor.fetchall()
          # for x in myresult:
              # item_yes = types.InlineKeyboardButton(string=x, callback_data='yes')
              # item_no = types.InlineKeyboardButton(string=x, callback_data='no')
              # markup_inline.add(item_yes, item_no)
              # bot.send_message(message.chat.id, '☄Выберите категорию:☄', reply_markup=markup_inline)