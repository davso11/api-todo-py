import typing


def toJson(fields_list:  typing.List, results: typing.List):
    column_list = []
    for i in fields_list:
        column_list.append(i[0])

    jsonData_list = []
    for row in results:
        data_dict = {}
        for i in range(len(column_list)):
            data_dict[column_list[i]] = row[i]
        jsonData_list.append(data_dict)

    return jsonData_list
