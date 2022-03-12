name = "John"

def change_name(new_name):
    global name
    name = new_name

change_name("Mary")
print(name)


