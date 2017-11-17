# Kevin Chen
# 11/16/17
# this program set a class called pack and set the leader of pack, and let all of dogs in the list play tricks


import dog


class Pack:
    def __init__(self, member):
        """
        This program will creat dog list and also can turn list to index
        :param member:
        """
        self.leader_index = 0
        self.members = []
        self.members.append(member)

    def get_leader_name(self):
        """
        This program will choose the leader's name
        :return: name
        """
        return self.members[self.leader_index].get_name()

    def add_member(self, dog):
        """
        This program will add member to dog list
        :param dog:
        :return: dog
        """
        if dog not in self.members:
            self.members.append(dog)

    def print_pack(self):
        print(self.members.name)

    def new_leader(self, number):
        """
        This program will set the new leader
        :param number:
        :return: number
        """
        old_leader = self.get_leader_name()
        self.leader_index = number
        leader = self.get_leader_name()
        print(leader, "deposes", old_leader, "as the new leader of the pack")

    def all_sit(self):
        """
        This program will let all dogs in list play trick "sit"
        :return: none
        """
        for x in self.members:
            x.sit()

    def all_print_tricks(self):
        """
        This program will let all dogs in list play any trick that they played before)
        :return: none
        """
        for x in self.members:
            for trick in x.trick_list:
                print(x.get_name(), trick)
