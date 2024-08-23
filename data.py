# Заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON.
headers = {
    "Content-Type": "application/json"
}

# Поля для создания заказа
order_body = {
    "firstName": "Naruto", #Имя заказчика
    "lastName": "Uchiha", #Фамилия заказчика
    "address": "Konoha, 142 apt.", #Адрес заказчика
    "metroStation": 4, #Ближайшая к заказчику станция метро
    "phone": "+7 800 355 35 35", #Телефон заказчика
    "rentTime": 5, #Количество дней аренды
    "deliveryDate": "2020-06-06", #Дата доставки
    "comment": "Saske, come back to Konoha", #Комментарий от заказчика
    "color": [ #Предпочитаемые цвета
        "BLACK"
    ]
}

