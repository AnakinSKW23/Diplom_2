class Urls:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE = 'api/auth/register'
    LOG_IN = 'api/auth/login'
    UPDATE_USER = 'api/auth/user'
    CREATE_ORDER = 'api/orders'
    GET_ORDER = 'api/orders'
    DELETE_USER = 'api/auth/user'

class ServerAnswers:
    registrated_user = 'User already exists'
    empty_any_fields = 'Email, password and name are required fields'
    unautorized_user = 'email or password are incorrect'
    no_token = 'You should be authorised'
    no_ingredient = 'Ingredient ids must be provided'
    without_autorization = 'You should be authorised'

class Ingredients:
    SAUSE_SPICY_X = '61c0c5a71d1f82001bdaaa72'
    BUN_R2_D3 = '61c0c5a71d1f82001bdaaa6d'
    BUN_SHAO_KAN = '61c0c3a2221d1f81101bdaaa6d'
