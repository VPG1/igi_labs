import os

file = open(os.path.join(os.path.dirname(__file__), "data.txt"), "r")
text = file.readline()