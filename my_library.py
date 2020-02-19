import json


class JSON:

    @staticmethod
    def add_json(fp, values: dict):
        with open(fp, 'r') as jayson:
            before = jayson.read()
            before = before[:before.rfind("}")]
        print(before)
        with open(fp, 'w') as jayson:
            jayson.write(before)
            for name, value in values.items():
                jayson.write(f', "{name}": "{value}"')
            jayson.write("}")

    @staticmethod
    def read_json(fp, return_type=dict):
        with open(fp, 'r') as file:

            if return_type is dict:
                value = json.load(file)

            elif return_type is str:
                value = file.read()

            else:
                raise (TypeError, "return_type, should be dict or str (or some value i haven't thought yet)")

        return value
