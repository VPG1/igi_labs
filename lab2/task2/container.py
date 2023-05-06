import os
import re


class Container:
    user_containers = {}
    current_user_name = ""

    def __init__(self):
        self.current_user_name = None

    def __init__(self, user_name):
        self.current_user_name = user_name