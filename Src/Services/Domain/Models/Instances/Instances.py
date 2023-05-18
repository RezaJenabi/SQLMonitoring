
class Instances:
    def __init__(self):
        self._serverName = None
        self._serverAuthenticationType = None
        self._password = None
        self._login = None

    @property
    def Login(self):
        return self._login

    @Login.setter
    def Login(self, value):
        self._login = value

    @property
    def Password(self):
        return self._password

    @Password.setter
    def Password(self, value):
        self._password = value

    @property
    def ServerAuthenticationType(self):
        return self._serverAuthenticationType

    @ServerAuthenticationType.setter
    def ServerAuthenticationType(self, value):
        self._serverAuthenticationType = value

    @property
    def ServerName(self):
        return self._serverName

    @ServerName.setter
    def ServerName(self, value):
        self._serverName = value
