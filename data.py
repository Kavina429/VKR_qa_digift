import datetime
from dateutil.relativedelta import relativedelta

data_text = "Congratulations, my dear! This gift is for you only!"
data_nominal = "300"
data_name_from = "Victor"
data_lastname_from = "Turbin"
data_mail_from = "v.turbin@gmail.com"
data_phone_from = "+79287415588"
data_name_to = "Natalie"
data_lastname_to = "Kavina"
data_mail_to = "n.kavina@gmail.com"
data_phone_to = "+79137773344"
data_calender = "28.09.2024"
data_assert_1 = 'Ваш подарок уже в пути!'
data_assert_2 = "Подтверждение заказа отправлено по электронной почте v.turbin@gmail.com."

def get_segodnya(): # выбор завтрашней даты в календаре
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow

def get_sevenday(): # выбор даты через 6 дней в календаре
    today = datetime.date.today()
    tosevenday = today + datetime.timedelta(days=7)
    return tosevenday

def get_date_in_three_months(start_date): # получение даты через месяца от выбранной
    return start_date + relativedelta(months=3)

def format_date(date_obj): # преобразование даты в строку/текст
    return date_obj.strftime("%d.%m.%Y")