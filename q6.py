def fileter_value(cost):
    if(cost>350):
        return True
    else:
        return False
price = [230,400,450,350,370]
fileter_value = filter(fileter_value,price)
print(list(fileter_value))