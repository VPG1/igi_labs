import os
import re


class Container:
    user_containers = {}
    current_user_name = ""

    def __init__(self):
        self.current_user_name = None

    def __init__(self, user_name):
        self.current_user_name = user_name

    def add(self, add_list):
        for i in range(0, len(add_list)):
            try:
                add_list[i] = str(int(add_list[i]))
            except:
                pass

        if self.user_containers.get(self.current_user_name) is None:
            self.user_containers[self.current_user_name] = set(add_list)
        else:
            self.user_containers[self.current_user_name] = self.user_containers[self.current_user_name].union(
                set(add_list))

    def remove(self, key):
        try:
            key = str(int(key))
        except:
            pass

        self.user_containers[self.current_user_name].remove(key)

    def find(self, key_list) :
        result_list = []

        for i in range(0, len(key_list)) :
            try :
                key_list[i] = str(int(key_list[i]))
            except :
                pass

        for key in key_list :
            if(key in self.user_containers[self.current_user_name]) :
                result_list.append(key)

        if(len(result_list) == 0) :
            print("Not found")
        else :
            print(' '.join(result_list))

    def list(self) :
        if(self.user_containers.get(self.current_user_name) == None) :
            print("Dont have elements")
        else :
            print(', '.join(self.user_containers[self.current_user_name]))