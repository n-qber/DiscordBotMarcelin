import json


class JSON:

    @staticmethod
    def write_json(fp, values: dict):
        with open(fp, "w") as file:
            file.write(json.dumps(values))

    @staticmethod
    def add_json(fp, values: dict):
        before_values = JSON.read_json(fp)
        for key, value in values.items():
            before_values[key] = value
        JSON.write_json(fp, before_values)

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
