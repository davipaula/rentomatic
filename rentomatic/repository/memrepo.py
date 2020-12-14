from typing import Dict, List, Tuple, Union

from rentomatic.domain import room as r


class MemRepo:
    def __init__(self, room_dicts):
        self.rooms = self.get_rooms(room_dicts)

    def list(self, filters: Dict[str, Union[str, int]] = None) -> List[Dict]:
        if filters is None:
            return self.rooms

        filtered_rooms = self.rooms.copy()
        for filter_, value in filters.items():
            field, condition = self.get_field_and_condition(filter_)

            filtered_rooms = [
                room
                for room in filtered_rooms
                if room.__getattribute__(field).__getattribute__(condition)(value)
            ]

        return filtered_rooms

    @staticmethod
    def get_rooms(room_dicts: Dict) -> List[Dict]:
        return [r.Room.from_dict(room) for room in room_dicts]

    @staticmethod
    def get_field_and_condition(filter_: str) -> Tuple[str, str]:
        field, condition = filter_.split("__")

        return field, f"__{condition}__"
