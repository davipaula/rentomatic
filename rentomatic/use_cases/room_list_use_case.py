from rentomatic.request_objects.room_list_request_object import RoomListRequestObject
from rentomatic.response_objects import response_objects as res


class RoomListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request: RoomListRequestObject):
        rooms = self.repo.list(filters=request.filters)

        return res.ResponseSuccess(rooms)
