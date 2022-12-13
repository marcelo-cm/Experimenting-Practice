guestlist = {"Raisa": ["pizza", "cookies", 3], "Susan": ["salad", 2], "Jia": ["ice cream", 0],
             "Val": ["cake", 21], "Brian": [ "pasta", "cheese", "crackers", 2], "Chandra": ["burgers", "buns", 31]}

def thisisajoke(guestlist):
    for guest in guestlist:
        items = guestlist[guest][:-1]
        guests = guestlist[guest][-1]
        items_string = ''
        for i in range(len(items)):
            if i != len(items)-1:
                items_string += items[i] + ", "
            else:
                if i == 0:
                    items_string += items[i]
                else:
                    items_string += "and " + items[i]
        print("{} is bringing {}.".format(guest, items_string))

thisisajoke(guestlist)