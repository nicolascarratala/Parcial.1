class Member():
    
    def __init__(self, _name = '', _surname = '', _age = '', _phone = ''):
        self._name = _name
        self._surname = _surname
        self._age = _age
        self._phone = _phone
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
        print(self.phone)

