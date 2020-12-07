from rentomatic.domain import room as r


class MemRepo:
    def __init__(self, room_dicts):
        self.room_dicts = room_dicts

    def list(self):
        return [r.Room.from_dict(room) for room in self.room_dicts]
