from rentomatic.request_objects.room_list_request_object import InvalidRequestObject


class ResponseSuccess:
    SUCCESS = 200

    def __init__(self, value=None):
        self.type = 200
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"

    ERRORS = [PARAMETERS_ERROR, RESOURCE_ERROR, SYSTEM_ERROR]

    def __init__(self, response_type, response_message):
        self.type = response_type

        if isinstance(response_message, Exception):
            self.message = f"Exception: {str(response_message)}"
        else:
            self.message = response_message

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request: InvalidRequestObject):
        request_errors = [
            f"{error['parameter']}: {error['message']}"
            for error in invalid_request.errors
        ]

        return cls.build_parameters_error("\n".join(request_errors))

    @classmethod
    def build_resource_error(cls, error):
        return cls(cls.RESOURCE_ERROR, error)

    @classmethod
    def build_parameters_error(cls, error):
        return cls(cls.PARAMETERS_ERROR, error)

    @classmethod
    def build_system_error(cls, error):
        return cls(cls.SYSTEM_ERROR, error)
