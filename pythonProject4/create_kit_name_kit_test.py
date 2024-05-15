import data
import sender_stand_request


# тест на создание заказа, сохранение номера заказа и проверка статуса ответа
def test_get_order_by_track():
    response_order = sender_stand_request.post_new_orders(data.new_orders)
    track = {"t": response_order.json()["track"]}
    response_order_by_track = sender_stand_request.get_orders_track(track)
    assert response_order_by_track.status_code == 200