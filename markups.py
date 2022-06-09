from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

# Главное меню
btnRandom = KeyboardButton('Получить Время')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)


# other menu
btnInfo = KeyboardButton('Информация')
btnMoney = KeyboardButton('Курс Валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney,
                                                          btnMain)
