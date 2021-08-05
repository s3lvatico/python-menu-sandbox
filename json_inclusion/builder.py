import json


def build_structure():
    print('building!')
    menu_master = _read_from_file('json_inclusion/menu-master.json')
    print(menu_master)
    menu_master = _resolve_inclusions(menu_master)
    print(menu_master)


def _resolve_inclusions(item: dict) -> dict:
    if item['item_type'] == 'command':
        return item
    if type(item['items']) == list:
        return item
    item['items'] = _read_from_file(
        'json_inclusion/' + item['items']['include'])
    for subitem in item['items']:
        subitem = _resolve_inclusions(subitem)
    return item


def _read_from_file(file_name):
    ff = open(file_name)
    string_content = ff.read()
    ff.close()
    dict_content = json.loads(string_content)
    return dict_content


if __name__ == "__main__":
    build_structure()
