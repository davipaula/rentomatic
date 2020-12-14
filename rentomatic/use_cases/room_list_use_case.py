from typing import Union

from rentomatic.repository.postgresrepo import PostgresRepo
from rentomatic.request_objects.room_list_request_object import (
    InvalidRequestObject,
    RoomListRequestObject,
)
from rentomatic.response_objects import response_objects as res
from rentomatic.response_objects.response_objects import (
    ResponseFailure,
    ResponseSuccess,
)


class RoomListUseCase:
    def __init__(self, repo: PostgresRepo):
        self.repo = repo

    def execute(
        self, request: Union[RoomListRequestObject, InvalidRequestObject]
    ) -> Union[ResponseSuccess, ResponseFailure]:
        if not request:
            return res.ResponseFailure.build_from_invalid_request_object(request)

        try:
            rooms = self.repo.list(filters=request.filters)

            return res.ResponseSuccess(rooms)
        except Exception as err:
            return res.ResponseFailure.build_system_error(err)
