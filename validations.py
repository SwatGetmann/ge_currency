from exceptions import *

def validate_request(request):
    if request.status_code != 200:
        raise InvalidResponseCode(request.status_code)

def validate_content(content):
    if content == '':
        raise EmptyContent()

def validate_match(match):
    if match is None:
        raise MatchNotFound()