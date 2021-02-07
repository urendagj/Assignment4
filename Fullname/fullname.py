#Function to create a full-name

def fullname(first,last):
    if len(first) <= 0 or len(last) <= 0:
        raise Exception("Name is invalid")
    else:
        return str(first) + " " + str(last)

#print(fullname("Jacob","Urenda"))