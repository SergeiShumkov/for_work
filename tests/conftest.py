import pytest
import requests

from my_data import login, password
from configuration import SERVICE_URL


# scope - ограничивает количество выполнений фикстур "function"(default), ``"class"``, ``"module"``, ``"package"`` or ``"session"
# autouse - если True, то фикстура будет выполнятся для всех тестов, даже если она не указана в тесте
@pytest.fixture #(autouse=True) 
def get_settings():
    response = requests.get(url=SERVICE_URL, auth=(f"{login}", f"{password}"))
    return response