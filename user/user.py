


class User(object):
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    def getUserFirstName(self):
        return self.name.split(' ')[0]
    def getUserLastName(self):
        return self.name.split(' ')[1]
    def update(self,user):
        pass
    def delete(self):
        print "This is a delete message"