
class Keys:

    def __init__(self):

        self._app_key = """ secret app key here """
        self._public_key = """ reCAPTCHA public key """
        self._secret_key = """ reCAPTCHA secret key """

    def get_app_key(self):

        return self._app_key

    def get_private_key(self):

        return self._secret_key

    def get_public_key(self):

        return self._public_key

class AccessCode:

    def __init__(self):

        self.__access_code = """ your access code """

    def get_access_code(self):

        return self.__access_code

class Names(dict):

    def __init__(self):

        self.names = {
            "name1" : """ parental-unit name 1 """,
            "name2" : """ parental-unit name 2 """
        }

        super().__init__(self.names)
