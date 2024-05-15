import requests
import configuration
import data


def post_new_orders(body):
    url = configuration.URL_SERVICE + configuration.CREATE_NEW_ORDERS
    return requests.post(url, json=body)

def get_orders_track(track):
    url = configuration.URL_SERVICE + configuration.READ_ORDERS_TRACK
    return requests.get(url, params=track)