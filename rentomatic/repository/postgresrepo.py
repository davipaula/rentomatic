from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rentomatic.domain import room
from rentomatic.repository.postgres_objects import Base, Room


class PostgresRepo:
    def __init__(self, connection_data):
        connection_string = f"postgresql+psycopg2://{connection_data['user']}:{connection_data['password']}@{connection_data['host']}/{connection_data['dbname']}"

        self.engine = create_engine(connection_string)
        Base.metadata.bind = self.engine

    def _create_room_objects(self, results):
        return [
            room.Room(
                code=result.code,
                size=result.size,
                price=result.price,
                latitude=result.latitude,
                longitude=result.longitude,
            )
            for result in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        query = session.query(Room)

        # Not a good implementation because it loads all records in memory.
        rooms = self._create_room_objects(query.all())

        if filters is None:
            return rooms

        for filter_, value in filters.items():
            field, condition = self.get_field_and_condition(filter_)

            rooms = [
                _room
                for _room in rooms
                if _room.__getattribute__(field).__getattribute__(condition)(value)
            ]

        return rooms

    @staticmethod
    def get_field_and_condition(filter_):
        field, condition = filter_.split("__")

        return field, f"__{condition}__"

