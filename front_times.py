# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front;


def front_times(str, n):
    if len(str) < n:
        return str * n
    else:
        return str[:3] * n

    ###################### Another answer ###############################
    # front_len = 3
    # if front_len > len(str):
    #     front_len = len(str)
    # front = str[:front_len]

    # result = ""
    # for i in range(n):
    #     result = result + front
    # return result


print(front_times("Chocolate", 2))  # → 'ChoCho'
print(front_times("Chocolate", 3))  # → 'ChoChoCho'
print(front_times("Abc", 3))  # → 'AbcAbcAbc'

