class InvalidResponseCode(BaseException):
    def __init__(self, code, message="Response Code is not successful (200)") -> None:
        self.code = code
        self.message = message
        super().__init__(self.message)
    
class EmptyContent(BaseException):
    def __init__(self, message="Content is empty") -> None:
        self.message = message
        super().__init__(self.message)

class MatchNotFound(BaseException):
    def __init__(self, message="Match for Response Content had not been found") -> None:
        self.message = message
        super().__init__(self.message)

class NotProvidedParameter(BaseException):
    def __init__(self, parameter_name='ParameterName', message=" is not provided!") -> None:
        self.parameter_name = parameter_name
        self.message = self.parameter_name + message
        super().__init__(self.message)
        
class PaginatedParseMarkerNotFound(BaseException):
    def __init__(self, path=None, message="Marker for Paginated Parsing had not been found") -> None:
        self.path = path
        self.message = message
        self.message += " by the path: {}".format(self.path)
        super().__init__(self.message)