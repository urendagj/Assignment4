#function to calclulate the volume of a cube
def cubevolume(edge):
    if edge <= 0:
        # print("Input must be > 0")
        # return None
        raise Exception("Value must be positive")
    try:
         return edge ** 3
    except TypeError:
        print("Input is not a numeric value")




    


