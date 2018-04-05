
def wtfj():
    entry = input(); int_list = []; float_list = []
    num_get = 0
    while num_get == 0:
        num = int(entry[1])
        num_get = 1
        return num_get and num
    stop_var = 0
    while stop_var == 0 and num_get == 1:
        listy = input()
        listy = listy.split(' ')
        if len(listy) <= 0:
            stop_var = 1
            return "gheaurh" and stop_var
        else:
            for i in listy:
                if int_list.index(i) < num and float_list.index(i) < num:
                    if i.isdigit():
                        int_list.append(i)
                    else:
                        try:
                            float(i)
                            float_list.append(i)
                        except TypeError:
                            stop_var = 1
                            return "Integers: " + str(int_list) + "Floats: " + str(float_list) and stop_var


'''for i in listy:
        if int_list < num and float_list.index < num:
            if i.isdigit():
                int_list.append(i)
            else:
                try:
                    float(i)
                    float_list.append(i)
                except TypeError:
                    float_list = float_list
    print("p")
 return "Integers: " + str(int_list) + "\nFloats: " + str(float_list)
'''

if __name__ == "__main__":
        main()