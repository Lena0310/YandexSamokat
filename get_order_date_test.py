import data
import sender_stand_request


def test_get_order_data_by_order_track_get_success_response():
    track_response = sender_stand_request.create_order(data.order_body)
    track = track_response.json()["track"]
    order_response = sender_stand_request.get_order(track)
    assert order_response.status_code == 200
