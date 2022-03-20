class SignUp:

    def __init__(self, first_name, last_name, phone, email, password, acc_type):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.acc_type = acc_type

    def login(self):
        return self.email

    def acc_password(self):
        return self.password


user1 = SignUp('Jane', 'Black', '+1-202-555-0140', 'qaauto22@mail.ru', 'Qa2022++', 'customer')
user2 = SignUp('Ann', 'Smith', '+1202-555-0563', 'eliz_96@mail.ru', '123abc+', 'customer')





