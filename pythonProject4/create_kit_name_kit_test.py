# Рязанцев Владимир 16 кагорта - Финальный проектю Инженер по тестированию плюс
import data
import sender_stand_request


# тест на создание заказа, сохранение номера заказа и проверка статуса ответа
def test_new_orders():
    sender_stand_request.post_new_orders()
    new_track = sender_stand_request.post_new_orders()
    #копирую ответ запроса на создание заказа
    track = new_track.json()['track']
    #создаю переменную для хранения значения номера заказа
    #заменяю значение номера заказа в параметрах для запроса заказа по номеру
    data.orders_track['t'] = track
    #Проверяю, что код ответа равен 201
    assert new_track.status_code == 201


def test_orders_track():
    sender_stand_request.get_orders_track()
    order_response = sender_stand_request.get_orders_track()
    assert order_response.status_code == 200
