import json

from flask import Blueprint, Response, request

from rentomatic.repository import memrepo as mr
from rentomatic.serializers import room_json_serializer as ser
from rentomatic.use_cases import room_list_use_case as uc
from rentomatic.request_objects import room_list_request_object as req

blueprint = Blueprint("room", __name__)

room1 = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "size": 215,
    "price": 39,
    "longitude": -0.09998975,
    "latitude": 51.75436293,
}
room2 = {
    "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
    "size": 405,
    "price": 66,
    "longitude": 0.18228006,
    "latitude": 51.74640997,
}
room3 = {
    "code": "913694c6-435a-4366-ba0d-da5334a611b2",
    "size": 56,
    "price": 60,
    "longitude": 0.27891577,
    "latitude": 51.45994069,
}


@blueprint.route("/rooms", methods=["GET"])
def room():
    request_filters = request.args

    filters = dict()
    for request_filter in request_filters.items():
        condition = request_filter[0].replace("filter_", "")
        value = request_filter[1]

        filters[condition] = value

    room_list_request = req.RoomListRequestObject.from_dict({"filters": filters})

    repo = mr.MemRepo([room1, room2, room3])
    use_case = uc.RoomListUseCase(repo)

    result = use_case.execute(room_list_request)

    return Response(
        json.dumps(result.value, cls=ser.RoomJsonEncoder),
        mimetype="application/json",
        status=200,
    )
