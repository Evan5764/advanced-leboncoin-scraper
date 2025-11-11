thonimport json

def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)