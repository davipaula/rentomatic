import json
import uuid

from rentomatic.domain import room as r
from rentomatic.serializers import room_json_serializer as ser


def test_serialize_domain_room():
    code = uuid.uuid4()

    room = r.Room(code, size=200, price=10, longitude=-0.9998975, latitude=51.75436293)

    expected_json = f"""
        {{
            "code": \"{code}\",
            "size": 200,
            "price": 10,
            "longitude": -0.9998975,
            "latitude": 51.75436293
        }}
    """

    json_room = json.dumps(room, cls=ser.RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
