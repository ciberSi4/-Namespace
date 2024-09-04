# "Пространство имён"

calls : int = 0


def count_calls():
    global calls
    number_of_function_calls : int = calls
    return number_of_function_calls


def string_info (string  : str):
    global calls
    returned_data : tuple = (len(string), string.upper(), string.lower())
    calls += 1
    return returned_data


def is_contains (string : str, list_to_search : list):
    global calls
    bool_ : bool = True
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower():
            bool_ = True
        else:
            bool_ = False

    calls += 1
    the_string_is_present = bool_
    return the_string_is_present


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)