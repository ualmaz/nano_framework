import re
from helpers import find_form_data

def address(path):
    def wrapper(func):
        def wrap_func(*args, **kwargs):
            request = args[0]
            match_object = re.search(r'(GET)\s\/(\w+)|(POST)\s\/(\w+)', request).groups()
            print(match_object)
            given_path = match_object[1] or match_object[3]
            method = match_object[0] or match_object[2]
            print('given_path: ', given_path)
            print('method: ', method)
            if method == 'POST':
                kwargs['data'] = find_form_data(request)
            if path == given_path:
                func(*args, **kwargs)
            else:
                kwargs['match'] = False
                func(*args, **kwargs)
        return wrap_func
    return wrapper

#{'firstname': 'Mickey', 'lastname': 'Mouse'}
