# Новиков Кирилл, 12 когорта — Финальный проект. Инженер по тестированию плюс.
import data
import sender_requests


def test_order_status_200():
    response_order = sender_requests.create_order(data.create_order_body)
    order_test = {"t": response_order.json()["track"]}
    response_test = sender_requests.get_order(order_test)
    assert response_test.status_code == 200
