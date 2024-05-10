import requests
import configuration
import data


def post_new_orders():
    url = configuration.URL_SERVICE + configuration.CREATE_NEW_ORDERS
    body = data.new_orders
    headers = data.headers
    return requests.post(url, json=body, headers=headers)


def get_orders_track():
    url = configuration.URL_SERVICE + configuration.READ_ORDERS_TRACK
    new_body = data.orders_track.copy()
    print(new_body)
    headers = data.headers.copy()
    return requests.get(url, params=new_body, headers=headers)
