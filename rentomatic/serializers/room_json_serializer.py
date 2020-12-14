import json
from typing import Any, Dict


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Dict:
        try:
            # TODO change to use to_dict function
            to_serialize = {
                "code": str(o.code),
                "size": o.size,
                "price": o.price,
                "longitude": o.longitude,
                "latitude": o.latitude,
            }

            return to_serialize
        except AttributeError:
            return super().default(o)
