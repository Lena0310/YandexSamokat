import configuration

import requests

import data


# Фукнция создает заказ.
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH,
                         json=body,
                         headers=data.headers)

#Функция возвращает данные заказа по треку заказа
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH,
                        params={"t":track},
                        headers=data.headers)