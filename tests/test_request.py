from configuration import SERVICE_URL
# from src.schemas.post import POST_SCHEMA_1, POST_SCHEMA_2
from src.baseclasses.response import Response
from src.schemas.settings import Settings


# def test_1():
#     resp = requests.get(url=SERVICE_URL, auth=(f"{login}", f"{password}"))
#     print("\n", resp.json()[0].get("value"))
#     # print(resp.__getstate__()) # __getstate__ выводит всю инфоромацию об объекте
#     print(resp.url)
#     # print(resp.headers.get("Set-Cookie"))  # пример отбора информации

def test_getting_settings(get_settings):
    Response(get_settings).assert_status_code(200).validate(Settings)
    # test_object = Response(response)
    # test_object.assert_status_code(200).validate(Settings)
    

def test_another():
    assert 1 == 1
   