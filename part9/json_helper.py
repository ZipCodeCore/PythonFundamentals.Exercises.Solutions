import json
import os
import pickle
from typing import Dict


def read_json(file_path: str) -> Dict:
    with open(file_path) as f:
        json_input = json.load(f)
    return json_input


def read_all_json_files(json_root):
    for root, _, files in os.walk(json_root):
        result = []
        for f in files:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(json_root, f))
                result.append(json_content)
    return result


def write_pickle(file_path: str, data: Dict):
    with open(file_path, "wb") as handler:
        pickle.dump(data, handler)


def load_pickle(file_path):
    with open(file_path, 'rb') as handler:
        data = pickle.load(handler)
    return data


if __name__ == "__main__":

    # Part 2 Proof

    content = read_all_json_files('./data/marvel')
    print(content)

    write_pickle("marvel.pickle", content)
    marvel_content = load_pickle("marvel.pickle")
    print(marvel_content)

