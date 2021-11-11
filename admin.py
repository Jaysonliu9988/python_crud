import json
_DATA_PATH_ = ''

# This function repeatedly prompts for input until an integer is entered.
def input_int(prompt):
    while True:
        target = input(prompt)
        try:
            return int(target)
        except:
            print('Need to enter an integer.')
            continue

def input_something(prompt):
    while True:
        char_target = input(prompt).strip()
        if not char_target:
            print('Enter a valid string, which cannot be composed of blank keys and tabs.')
        else:
            return char_target

def save_data():
    with open(_DATA_PATH_, 'w') as w:
        w.write(json.dumps())

print('Welcome to the Fast-Food Quiz Admin Program.')

try:
    with open(_DATA_PATH_, 'r') as f:
        data = json.loads(f.read())
except:
    data = []

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    # Convert input to lowercase to make choice selection case-insensitive.
    choice = input('> ').lower()
    if choice == 'a':
        name = input_something(prompt='Enter name of fast-food item:')
        energy = input_int(prompt='Enter energy in kilojoules:')
        fat = input_int(prompt='Enter fat in grams:')
        protein = input_int(prompt='Enter protein grams:')
        carbohydrates = input_int(prompt='Enter carbohydrates in grams:')
        sugars = input_int(prompt='Enter sugars in grams:')
        sodium = input_int(prompt='Enter sodium in milligrams:')

    elif choice == 'l':
    # List the current fast-food items.
    # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print('There are no items saved.')
            pass
        print('List of items:')
        for i in list(enumerate(data)):
            print('{0}) {1}'.format(i[0]+1, i[1]['name']))

    elif choice == 's':
        # Search the current fast-food items.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        search_result = []
        if not data:
            print('No items saved')
            continue
        search_target = input_something(prompt='Enter search term:')
        for i in data:
            if search_target.lower() in i['name'].lower():
                search_result.append(i['name'])
        if not search_result:
            print('No results found')
            continue
        print('Search results:')
        for s in range(len(search_result)):
            print('{0}) {1}'.format(s + 1, search_result[s]))
        pass

    elif choice == 'v':
        # View a fast-food item.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        last_view_target = input_int(prompt='Need to enter an integer:')
        if last_view_target <= 0:
            print('Index number shown to by users start from 1')
            continue
        try:
            for keys, vaules in data[last_view_target - 1].items():
                if keys == 'energy':
                    d = 'kilojoules'
                elif keys == 'name':
                    d = ''
                elif keys == 'sodium':
                    d = 'milligram'
                else:
                    d = 'grams'
                print("{0}:{1} {2}".format(keys.capitalize(), vaules, d))
        except IndexError:
            print('Invalid index number')
        pass

    elif choice == 'v':
        # View a fast-food item.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        last_view_target = input_int(prompt='Need to enter an integer:')
        if last_view_target <= 0:
            print('Index number shown to by users start from 1')
            continue
        try:
            for keys, vaules in data[last_view_target - 1].items():
                if keys == 'energy':
                    d = 'kilojoules'
                elif keys == 'name':
                    d = ''
                elif keys == 'sodium':
                    d = 'milligram'
                else:
                    d = 'grams'
                print("{0}:{1} {2}".format(keys.capitalize(), vaules, d))
        except IndexError:
            print('Invalid index number')
        pass