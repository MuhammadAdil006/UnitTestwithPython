import contact
class PhoneBook:
    def __init__(self):
        self.contact={}
    def add(self,ph):
        self.contact[ph.name]=ph.number
    def consistentOrNot(self):
        lis=self.contact.values()
        lis2=set(lis)
        if len(lis)!=len(lis2):
            return False
        return True