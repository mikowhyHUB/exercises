def transform(legacy_data):
    data = {}
    for key in legacy_data:
        for value in legacy_data[key]:
            data.update({value.casefold(): key})
    return data


legacy_data = {1: ["A", "E"], 2: ["D", "G"]}
data = {"a": 1, "d": 2, "e": 1, "g": 2}
print(transform(legacy_data))
