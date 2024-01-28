import requests
import config


def create_order(order_body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=order_body)


def get_order(order_track):
    return requests.get(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                        params=order_track)
