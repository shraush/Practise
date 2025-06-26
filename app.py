import argparse
from templates_loader import load_templates, match_template
from validator import detect_type

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("get_tpl", help="Команда получения шаблона")
    known_args, unknown_args = parser.parse_known_args()

    data = {}
    for arg in unknown_args:
        if arg.startswith("--") and "=" in arg:
            key, value = arg[2:].split("=", 1)
            data[key] = value
    return data

def main():
    request_data = parse_args()
    templates = load_templates()
    matched = match_template(templates, request_data)

    if matched:
        print(matched)
    else:
        result = {k: detect_type(v) for k, v in request_data.items()}
        print(result)

if __name__ == "__main__":
    main()