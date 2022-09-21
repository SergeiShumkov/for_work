import requests
from my_data import login, password

from configuration import SERVICE_URL
# from src.schemas.post import POST_SCHEMA_1, POST_SCHEMA_2
from src.baseclasses.response import Response
from src.pydantic_schema.post import Post


def test_getting_posts():
    r = requests.get(url=SERVICE_URL, auth=(f"{login}", f"{password}"))
    response = Response(r)

    # response.validate(POST_SCHEMA_2)
    response.validate(Post)
    response.assert_status_code([401, 200])
    
    
    

    