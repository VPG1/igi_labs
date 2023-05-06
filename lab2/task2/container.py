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

    def find(self, key_list):
        result_list = []

        for i in range(0, len(key_list)):
            try:
                key_list[i] = str(int(key_list[i]))
            except:
                pass

        for key in key_list:
            if key in self.user_containers[self.current_user_name]:
                result_list.append(key)

        if len(result_list) == 0:
            print("Not found")
        else:
            print(' '.join(result_list))

    def list(self):
        if self.user_containers.get(self.current_user_name) is None:
            print("Dont have elements")
        else:
            print(', '.join(self.user_containers[self.current_user_name]))

    def save(self, path=os.path.join(os.path.dirname(__file__), "data.txt")):
        try:
            file = open(path, "w")
        except:
            print("file not exist")
            return

        for username, value in self.user_containers.items():
            file.write(username + " : " + ' '.join(value) + "\n")

        file.close()

    def load(self, path=os.path.join(os.path.dirname(__file__), "data.txt")):
        try:
            file = open(path, "r")
        except:
            print("file not exist")
            return

        for user in file.readlines():
            if user.split(" ")[0] == self.current_user_name:
                add_list = user.replace("\n", "").split(" ")[2::]
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

        file.close()

    def switch(self, new_user_name):
        self.current_user_name = new_user_name

    def grep(self, regex) :
        result_list = []

        for value in self.user_containers[self.current_user_name] :
            if re.match(regex, value) is not None:
                result_list.append(value)

        print(" ".join(result_list))