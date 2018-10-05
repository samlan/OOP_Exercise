from user import User

class Admin(User):
    def __init__(self,name,email,password):
        super(Admin,self).__init__(name,email,password)
    def delete(self):
        return "this is an admin delete message for "+self.name