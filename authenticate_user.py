#from ..helpers.validation_helpers import *

from helpers.validation_helpers import *
from helpers.db_handler import *

from helpers.file_handler import *

import helpers.validation_helpers as helpers; 

def Register():
    user_info = validate_user_registration_info()
    insert_user(user_info)


#Register()

def Login():
    user_login_info = helpers.validate_user_login_info()
    user_info = search_user(user_login_info)
    msg = f'voala {user_info[0]["name"] } !' if user_info else "wrong credentials "
    print(msg)
Login()

