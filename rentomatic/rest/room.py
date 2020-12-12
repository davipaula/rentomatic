import json

from flask import Blueprint, Response, request

from rentomatic.repository import postgresrepo as pr
from rentomatic.serializers import room_json_serializer as ser
from rentomatic.use_cases import room_list_use_case as uc
from rentomatic.request_objects import room_list_request_object as req

blueprint = Blueprint("room", __name__)

connection_data = {
    "dbname": "rentomaticdb",
    "user": "postgres",
    "password": "rentomaticdb",
    "host": "localhost",
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

    repo = pr.PostgresRepo(connection_data)
    use_case = uc.RoomListUseCase(repo)

    result = use_case.execute(room_list_request)
    print(result.value)

    return Response(
        json.dumps(result.value, cls=ser.RoomJsonEncoder),
        mimetype="application/json",
        status=200,
    )
