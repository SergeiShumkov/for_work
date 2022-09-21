# from jsonschema import validate

# from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json() # response.json()[1].get("name")
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                # print(schema.parse_obj(item))
                schema.parse_obj(item)
                # validate(item, schema)
        else:
            schema.parse_obj(self.response_json)
            # validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self # status_code, GlobalErrorMessages.WRONG_STATUS_CODE
        else:
            assert self.response_status == status_code, self # status_code, GlobalErrorMessages.WRONG_STATUS_CODE
        return self

    def __str__(self): # Этот метод помогает описать представление объекта класса. Помогает отразить или кастомизировать вид объекта в консоли
        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json[:4]}"
