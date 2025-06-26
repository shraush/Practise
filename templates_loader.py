from tinydb import TinyDB
from validator import detect_type

def load_templates():
    db = TinyDB("db.json")
    return db.all()

def match_template(templates, request_data):
    for tpl in templates:
        name = tpl.get("name")
        required_fields = {k: v for k, v in tpl.items() if k != "name"}

        if all(
            field in request_data and detect_type(request_data[field]) == field_type
            for field, field_type in required_fields.items()
        ):
            return name
    return None

