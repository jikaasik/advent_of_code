import os 

def get_input(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        return f.read()

txt = get_input("input_demo.txt")
print(txt)