from user import User

class NormalUser(User):
    def __init__(self,name,email,password):
        super(NormalUser,self).__init__(name,email,password)
    def delete(self):
        return "this is a normal user delete message for "+self.name