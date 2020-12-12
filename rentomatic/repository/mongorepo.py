from collections import defaultdict

import pymongo

from rentomatic.domain.room import Room


class MongoRepo:
    def __init__(self, connection_data):
        client = pymongo.MongoClient(
            host=connection_data["host"],
            username=connection_data["user"],
            password=connection_data["password"],
            authSource="admin",
        )

        self.db = client[connection_data["dbname"]]

    def list(self, filters=None):
        collection = self.db.rooms

        if filters is None:
            result = collection.find()
        else:
            mongo_filter = defaultdict(dict)

            for filter_, value in filters.items():
                field, condition = self.get_field_and_condition(filter_)

                if field == "price":
                    value = int(value)

                mongo_filter[field].update({condition: value})

            result = collection.find(mongo_filter)

        return [Room.from_dict(room) for room in result]

    @staticmethod
    def get_field_and_condition(filter_):
        field, condition = filter_.split("__")

        return field, f"${condition}"
