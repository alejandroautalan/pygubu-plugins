import json
from pygubu.utils.datatrans import DataTransformer


class IntOrJsonList(DataTransformer):
    def transform(self, value: str, default=None):
        val = self.default_value if default is None else default
        try:
            val = int(value)
        except ValueError:
            try:
                json_list = json.loads(value)
                if isinstance(json_list, list):
                    val = json_list
                else:
                    val = self.on_error_default
            except json.JSONDecodeError:
                val = self.on_error_default
        return val
