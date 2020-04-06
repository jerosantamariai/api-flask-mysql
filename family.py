from random import randint

class Family:

    def __init__(self, last_name):
        self._last_name = last_name
        self._members = []
        # self._name = ""
        self._age = 0
        self._lucky_number = []
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId() 
        member["last_name"] = self._last_name
        # member["_age"] = self._age
        # member["_lucky_number"] = self._lucky_number
        self._members.append(member)
        return member

    def delete_member(self, id):
        # member["id"] = self._get_member()
        pass

    def update_member(self, id, member):
        # member["id"] = self._get_member()
        pass

    def get_member(self, id):
        member = list(filter(lambda member: member if member["id"] == id else None, self._members)) #filtre member y me de el member segun id si exite
        return member

    def get_all_members(self):
        return self._members


        # MEMBERS[
        #     MEMBER1{
        #         id:
        #         last name:
        #         name:
        #         age:
        #         lucky_number
        #     },
        #     MEMBER2{
        #         id:
        #         last name:
        #         name:
        #         age:
        #         lucky_number
        #     },
        #     MEMBER3{
        #         id:
        #         last name:
        #         name:
        #         age:
        #         lucky_number
        #     }
        # ]
