from rentomatic.request_objects.room_list_request_object import RoomListRequestObject
from rentomatic.response_objects import response_objects as res


class RoomListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request: RoomListRequestObject):
        if not request:
            return res.ResponseFailure.build_from_invalid_request_object(request)

        try:
            rooms = self.repo.list(filters=request.filters)

            return res.ResponseSuccess([room.to_dict() for room in rooms])
        except Exception as err:
            return res.ResponseFailure.build_system_error(err)

