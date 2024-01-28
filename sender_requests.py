import requests
import config
import data


def create_order(create_order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=data.create_order_body)


def get_order(order_track):
    return requests.get(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                        params=order_track)
