import json
import os
import pickle


def read_json(file_path):
    json_input = None
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


def write_pickle(file_path, data):
    with open("output.pickle", "wb") as handler:
        pickle.dump(data, handler)


def load_pickle(file_path):
    with open(file_path, 'rb') as handler:
        data = pickle.load(handler)
    return data


if __name__ == '__main__':
    # file_path = os.path.join('./', 'data', 'mario.json')
    # json = read_json(file_path)
    # print(json)

    # file_path = os.path.join('./', 'data')
    # result = read_all_json_files(file_path)
    # write_pickle("output.pickle", result)
    # print(result)

    # file_path = os.path.join('output.pickle')
    # data = load_pickle(file_path)
    # print(data)
