import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as f:
        data = []
        json_arr = []

        rows = f.read()[:-1].split('\n')

        for row in rows:
            data.append(row.split(','))

        for i in range(1, len(rows)):
            json_arr.append(dict(zip(data[0], data[i])))

    return json_arr

# TODO реализовать конвертер из csv в json
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#Пустая строка