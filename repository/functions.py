import unidecode

def archive_camel(class_name):
    class_name = class_name.replace(' ', '_')
    class_name = class_name.lower()
    class_name = unidecode.unidecode(class_name)
    return class_name

def set_entity_name(class_name):
    class_name = unidecode.unidecode(class_name)
    class_name = class_name.title()
    class_name = class_name.replace(' ', '')
    return class_name

def create_class(class_name, list):
    archive_name = archive_camel(class_name)
    entity_name = set_entity_name(class_name)

    constructor = f'    def __init__(self, {list}):'
    constructor = unidecode.unidecode(constructor)
    characters = "[]'"
    for i in range(0, len(characters)):
        constructor = constructor.replace(characters[i], "")

    try:
        with open(f'{archive_name}.py', 'w') as archive:
            archive.write(f'class {entity_name}():\n'
                          f'{constructor}\n')

            for i in range(len(list)):
                attribute = unidecode.unidecode(list[i])
                attribute = attribute.replace(' ', '')
                archive.write(f'        self.__{attribute} = {attribute}\n')
            for i in range(len(list)):
                attribute = unidecode.unidecode(list[i])
                archive.write(f'\n'
                              f'    @property\n'
                              f'    def {attribute}(self):\n'
                              f'        return self.__{attribute}\n'
                              f'\n'
                              f'    @{attribute}.setter\n'
                              f'    def {attribute}(self, {attribute}):\n'
                              f'        self.__{attribute} = {attribute}\n'
                             )
            archive.write(f'\n')
            archive.write(f'### BUILDING LIST ###\n')
            archive.write(f'# list = {list}\n')
        print(f'The file \'{archive_name}.py\' was generated successfully.')

    except FileNotFoundError:
        print('File not found.')


def object_creator(class_name, list):
    entity_name = set_entity_name(class_name)
    object_name = (archive_camel(class_name)).lower()
    tmp_list = []

    for i in list:
        tmp_list.append(f'{i}={i}')

    entity = f'{entity_name}({tmp_list})'
    entity = unidecode.unidecode(entity)

    characters = "[]'"
    for i in range(len(characters)):
        entity = entity.replace(characters[i], '')
    entity = f'{object_name} = {entity}'
    return entity

def django_object_creator(class_name, list):
    entity_name = set_entity_name(class_name)
    attributes = []
    for i in list:
        attribute = f'{i} = form_{entity_name.lower()}.cleaned_data[\'{i}\']'
        attributes.append(attribute)
    object = object_creator(class_name, list)
    attributes.append(object)
    return attributes

def api_object_creator(list):
    attributes = []
    for i in list:
        attribute = f'{i} = i[\'{i}\']'
        attributes.append(attribute)
    return attributes

