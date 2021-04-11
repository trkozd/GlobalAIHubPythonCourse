def swap_list(l):
    """This function takes a list as input and swap the second half of the list with the first half of the list."""
    r = len(l)
    if r % 2 != 0:
        print("Error! List length should be double")
        return None
    else:
        # first half
        l1 = l[:int(r / 2)]
        # --degub--print(l1)

        # second half
        l2 = l[-int(r / 2):]
        # --degub--print(l2)

        # return swapped list
        sl = l2 + l1
        return sl


def print_even_numbers(n):
    """This function takes an integer(n) and prints out all the even numbers from 0 to n."""
    for i in range(n):
        if i % 2 == 0:
            print(i, end=" ")


# ---Part1----
# Prepare input list. (You can chage items.)
l = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
print("input list=", l)
sl = swap_list(l)
print("swapped list:", sl)

# ---Part2----
# Prepare input list. (You can chage items.)
max_try = 3
try_count = 0
valid = False
while not valid:
    try_count += 1
    try:
        print("-----------------")
        n = int(input("Pelase input a single digit integer number:"))
        if n < 10:
            valid = True
        else:
            print("Integer should be 0-9")
    except:
        print("You have did not provide a valid integer")

    if (try_count == max_try):
        break
    elif (not valid):
        print("You have {0} tries left".format(max_try - try_count))

if valid:
    print_even_numbers(n)
else:
    print("You did not provide correct input.")
