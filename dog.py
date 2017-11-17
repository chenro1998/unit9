# Kevin Chen
# 11/16/17
# This file set a class call dog and keep tricks in list


class Dog:
    def __init__(self, name):
        """
        This program set the name of dog and create a trick list for dog
        :param name:none
        """
        self.name = name
        self.trick_list = []

    def get_name(self):
        """
        This program can set the name of dog
        :return: name
        """
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        """
        This program can let dog play trick "sit"
        :return: none
        """
        print(self.name, "sits")
        self.trick_list.append("sit")

    def laydown(self):
        """
        This program can let dog play trick "laydown"
        :return: none
        """
        print(self.name, "lays down")
        self.trick_list.append("laydown")

    def sleep(self):
        """
        This program can let dog play trick "sleep"
        :return: none
        """
        print(self.name, "sleep imedialtely")
        self.trick_list.append("sleep")
