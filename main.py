# - * - coding: utf- 8 - * -
import telebot

from telebot import types
token = "1486678518:AAH_wUsktSkX4CMVNOd9CRAyMUBVYadAUSw"
bot = telebot.TeleBot(token)
# img = open("123.jpg", "rb")
# bot.send_photo(chat_id=call.message.chat.id, photo=img)
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=1)
    first_button = types.InlineKeyboardButton(text="Москва", callback_data="first")
    halffirst_button = types.InlineKeyboardButton(text="Москвовская область", callback_data="halffirst")
    second_button = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="second")
    thrird_button = types.InlineKeyboardButton(text="Ростов-На-Дону", callback_data="third")
    fourth_button = types.InlineKeyboardButton(text="Екатеринбург", callback_data="fourth")
    five_button = types.InlineKeyboardButton(text="Новосибирск", callback_data="five")
    six_button = types.InlineKeyboardButton(text="Челябинск", callback_data="six")
    seven_button = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="seven")
    keyboardmain.add(first_button,halffirst_button,second_button,thrird_button,fourth_button,five_button,six_button,seven_button)
    bot.send_message(message.chat.id, "Выберите город:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":

        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="Москва", callback_data="first")
        halffirst_button =types.InlineKeyboardButton(text="Москвовская область", callback_data="halffirst")
        second_button = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="second")
        thrird_button = types.InlineKeyboardButton(text="Ростов-На-Дону", callback_data="third")
        fourth_button = types.InlineKeyboardButton(text="Екатеринбург", callback_data="fourth")
        five_button = types.InlineKeyboardButton(text="Новосибирск", callback_data="five")
        six_button = types.InlineKeyboardButton(text="Челябинск", callback_data="six")
        seven_button = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="seven")
        keyboardmain.add(first_button,halffirst_button,second_button,thrird_button,fourth_button,five_button,six_button,seven_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите город",reply_markup=keyboardmain)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Войковский", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="Дмитровский", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="Бибирево", callback_data="3")
        rele4 = types.InlineKeyboardButton(text="Медведково", callback_data="4")
        rele5 = types.InlineKeyboardButton(text="Измайлово", callback_data="5")
        rele6 = types.InlineKeyboardButton(text="Новогиреево", callback_data="6")
        rele7 = types.InlineKeyboardButton(text="Сокольники", callback_data="7")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3,rele4,rele5,rele6,rele7, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Москва.Выберите район",reply_markup=keyboard)

    elif call.data == "halffirst":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Балашиха", callback_data="half1")
        rele2 = types.InlineKeyboardButton(text="Долгопрудный", callback_data="half2")
        rele3 = types.InlineKeyboardButton(text="Королёв", callback_data="half3")
        rele4 = types.InlineKeyboardButton(text="Красногорск", callback_data="half4")
        rele5 = types.InlineKeyboardButton(text="Люберцы", callback_data="half5")
        rele6 = types.InlineKeyboardButton(text="Мытищи", callback_data="half6")
        rele7 = types.InlineKeyboardButton(text="Подольск", callback_data="half7")
        rele8 = types.InlineKeyboardButton(text="Химки", callback_data="half8")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3,rele4,rele5,rele6,rele7,rele8,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Москвовская область.Выберите район",reply_markup=keyboard)

    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Пушкинский", callback_data="Piter1")
        rele2 = types.InlineKeyboardButton(text="Колпинский", callback_data="Piter2")
        rele3 = types.InlineKeyboardButton(text="Красногвардейский", callback_data="Piter3")
        rele4 = types.InlineKeyboardButton(text="Курортный", callback_data="Piter4")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1,rele2,rele3,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Спб.Выберите Район:",reply_markup=keyboard)
    elif call.data == "third":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Железнодорожный", callback_data="Rostov1")
        rele2 = types.InlineKeyboardButton(text="Некрасовский", callback_data="Rostov2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1,rele2,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="РОСТОВ.Выберите Район:",
                              reply_markup=keyboard)
    elif call.data == "fourth":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Орджоникидзевский ", callback_data="ekb1")
        rele2 = types.InlineKeyboardButton(text="Чкаловский", callback_data="ekb2")
        rele3 = types.InlineKeyboardButton(text="Октябрьский ", callback_data="ekb3")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Екб.Выберите Район:",
                              reply_markup=keyboard)
    elif call.data == "five":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Советский ", callback_data="nvsb1")
        rele2 = types.InlineKeyboardButton(text="Первомайский", callback_data="nvsb2")
        rele3 = types.InlineKeyboardButton(text="Ленинский", callback_data="nvsb3")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, rele3, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Новосибирск.Выберите Район:",
                              reply_markup=keyboard)
    elif call.data == "six":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Металлургический ", callback_data="clb1")
        rele2 = types.InlineKeyboardButton(text="Тракторозаводский", callback_data="clb2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Челябинск.Выберите Район:",
                              reply_markup=keyboard)
    elif call.data == "seven":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Автозаводский", callback_data="novgorod1")
        rele2 = types.InlineKeyboardButton(text="Сормовский", callback_data="novgorod2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, rele2, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Нижний Новгород.Выберите Район:",
                              reply_markup=keyboard)


    elif call.data == "1" or call.data == "4" or call.data=="half3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб." , callback_data="prop200")
        rele3 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="first")
        keyboard.add(rele1, rele2, rele3,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "prop100":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитропропен 100грамм", callback_data="payprop100")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитропропен 100грамм.К оплате 9500 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "prop200":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитропропен 200грамм", callback_data="payprop200")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитропропен 200грамм.К оплате 17500 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "etil1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитроэтилен 1литр", callback_data="payetil1")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитроэтилен 1литр.К оплате 11000 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "etil2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитроэтилен 2литра", callback_data="payetil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитроэтилен 2литр.К оплате 18000 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "payprop100":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="prop100")
        # img = open("123.jpg", "rb")
        # bot.send_photo(chat_id=call.message.chat.id, photo=img)
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали товар: \n Нитропропен 200 грамм \n К оплате: 17500 рублей \n Bitcoin кошелёк:\n 1H6DRNV7RwoEgLBaEGehzPEwxtZQTh626G \n После оплаты нажмите кнопку 'Обновить' ",
                              reply_markup=keyboard)
    elif call.data == "payprop200":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="prop200")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали товар: \n Нитропропен 200 грамм \n К оплате: 17500 рублей \n Bitcoin кошелёк:\n 1H6DRNV7RwoEgLBaEGehzPEwxtZQTh626G \n После оплаты нажмите кнопку 'Обновить' ",
                              reply_markup=keyboard)
    elif call.data == "payetil1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="etil1")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитроэтилен 1литр.К оплате 11000 рублей.Переведите на кошелек:32173128dsad8sa.Через 10 минут после оплаты нажмите кнопку обновить",
                              reply_markup=keyboard)
    elif call.data == "payetil2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="etil2")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитроэтилен 2литр.К оплате 18000 рублей.Переведите на кошелек:32173128dsad8sa.Через 10 минут после оплаты нажмите кнопку обновить",
                              reply_markup=keyboard)
    elif call.data == "refresh":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ожидайте,Платёж обрабатывается..",
                              reply_markup=keyboard)
    elif call.data == "2" or call.data =="6":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 500гр - 30500руб." , callback_data="prop500")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="first")
        keyboard.add(rele1, rele2,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "prop500":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитропропен 500гр-30500руб.", callback_data="payprop500")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитропропен 500грамм.К оплате 30500 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "payprop500":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="prop500")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали товар: \n Нитропропен 500 грамм \n К оплате: 30500 рублей \n Bitcoin кошелёк: \n1H6DRNV7RwoEgLBaEGehzPEwxtZQTh626G \n После оплаты нажмите кнопку 'Обновить' ",
                              reply_markup=keyboard)
    elif call.data == "5" or call.data=="half6":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб." , callback_data="prop200")
        rele3 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="first")
        keyboard.add(rele2, rele3,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "3" or call.data == "7" :
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб. ", callback_data="prop200")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 1000гр - 49500руб.", callback_data="prop1000")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 1литр -11000руб.", callback_data="etil1")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="first")
        keyboard.add(rele1, rele2, rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "prop1000":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитропропен 1000гр-49500руб.", callback_data="payprop1000")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="first")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитропропен 1100грамм.К оплате 49500 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "payprop1000":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="prop100")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали товар: \n Нитропропен 200 грамм \n К оплате: 49500 рублей \n Bitcoin кошелёк: \n 1H6DRNV7RwoEgLBaEGehzPEwxtZQTh626G \n После оплаты нажмите кнопку 'Обновить' ",
                              reply_markup=keyboard)
    elif call.data == "etil3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Оплатить Нитроэтилен 3литра-2700руб.", callback_data="payetil3")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитроэтилен 3литра.К оплате 27000 рублей.Товар зарезервирован на 40 минут,спустя 40 минут бронь пропадет!",
                              reply_markup=keyboard)
    elif call.data == "payetil3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Обновить статус", callback_data="refresh")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="etil3")
        keyboard.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выбран товар:Нитроэтилен 3литра.К оплате 27000 рублей.Переведите на кошелек:32173128dsad8sa.Через 10 минут после оплаты нажмите кнопку обновить",
                              reply_markup=keyboard)
    elif call.data == "half1" or call.data =="half3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 500гр - 30500руб." , callback_data="prop500")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="halffirst")
        keyboard.add(rele1, rele2,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "half2" or call.data=="half4":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб." , callback_data="prop200")
        rele3 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="halffirst")
        keyboard.add(rele2, rele3,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "half5" or call.data == "half8":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб. ", callback_data="prop200")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 1литр -11000руб.", callback_data="etil1")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="halffirst")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "half6":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="halffirst")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "half7":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="halffirst")
        keyboard.add(rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "Piter1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб." , callback_data="prop200")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 3литра -27000руб.", callback_data="etil3")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="second")
        keyboard.add(rele2, rele3,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "Piter2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб.", callback_data="prop200")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="second")
        keyboard.add(rele2, rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "Piter3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб.", callback_data="prop200")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="second")
        keyboard.add(rele2, rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "Rostov1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб.", callback_data="prop200")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        rele5 = types.InlineKeyboardButton(text="Нитроэтилен 3литра -27000руб.", callback_data="etil3")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="third")
        keyboard.add(rele1, rele3, rele5, rele2, rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "Rostov2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="third")
        keyboard.add(rele1, rele3,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "ekb1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литра -18000руб.", callback_data="etil2")

        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="fourth")
        keyboard.add(rele1, rele3,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "ekb2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб.", callback_data="prop200")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="fourth")
        keyboard.add(rele1, rele3,rele2,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "ekb3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="fourth")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "nvsb1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="five")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)

    elif call.data == "nvsb2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб.", callback_data="prop200")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="five")
        keyboard.add(rele1, rele3,rele2,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "nvsb3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб. ", callback_data="prop200")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="five")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "clb1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="six")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "clb2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитроэтилен 1литр - 11000руб.", callback_data="etil1")
        rele3 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб.", callback_data="prop100")
        rele2 = types.InlineKeyboardButton(text="Нитропропен 200гр - 17500руб.", callback_data="prop200")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="six")
        keyboard.add(rele1, rele3,rele2,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)
    elif call.data == "novgorod1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="seven")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите Товар:",
                              reply_markup=keyboard)

    elif call.data == "novgorod2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Нитропропен 100гр - 9500руб. ", callback_data="prop100")
        rele4 = types.InlineKeyboardButton(text="Нитроэтилен 2литр -18000руб.", callback_data="etil2")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="seven")
        keyboard.add(rele1,rele4, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Район выбран.Выберите товар:",
                              reply_markup=keyboard)
if __name__ == "__main__":
    bot.polling(none_stop=True)