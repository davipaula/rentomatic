from collections import Mapping


class InvalidRequestObject:
    def __init__(self) -> None:
        self.errors = []

    def add_error(self, parameter, message) -> None:
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self):
        return False


class ValidRequestObject:
    @classmethod
    def from_dict(cls, dictionary):
        raise NotImplementedError

    def __bool__(self):
        return True


class RoomListRequestObject(ValidRequestObject):
    VALID_KEY_FILTERS = {"code__eq", "price__eq", "price__lt", "price__gt"}

    def __init__(self, filters=None, errors=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, dictionary):
        filters = dictionary["filters"] if "filters" in dictionary else None

        validation_errors = cls.get_validation_errors(filters)

        if validation_errors.has_errors():
            return validation_errors

        return cls(filters)

    @classmethod
    def get_validation_errors(cls, filters) -> InvalidRequestObject:
        invalid_request = InvalidRequestObject()

        if filters is None:
            return invalid_request

        if not isinstance(filters, Mapping):
            invalid_request.add_error("filters", "Is not iterable")

            return invalid_request

        invalid_keys = set(filters.keys()) - cls.VALID_KEY_FILTERS

        for key in invalid_keys:
            invalid_request.add_error("filters", f"Key {key} is not valid")

        return invalid_request
