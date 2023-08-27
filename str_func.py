"""
First function
"""


def Up_string(old_string):
    return (str.upper(old_string))


"""
Add second function
"""


def new_up_strig(old_string):
    new_string = ""
    count = 1
    new_string += str.upper(old_string[0])
    while count + 1 <= len(old_string):
        if old_string[count - 1] == " ":
            new_string += str.upper(old_string[count])
        else:
            new_string += old_string[count]
        count += 1
    return new_string


print(new_up_strig("hello world"))
