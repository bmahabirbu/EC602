#Copyright 2022 Brian Mahabir bmahabir@bu.edu
#import math

def divisorsum(x):
    message = ""
    div_counter = 0
    for i in range(1,x+1):
        if x % i == 0 and i != x:
            message += str(i)+"+"
            div_counter += i
        if i == x:
                #remove last + sign
                message = message[:-1]
                message += " = "+str(div_counter)
    return message

def convertbase(str_num, base, new_base):
    #convert from any base to base 10
    digits = []
    b10_result = 0
    result = ""
    if base == 10:
        b10_result = int(str_num)
    else:
        #split string get each digits ascii value
        for e in str_num:
            char_conv = ord(e)-ord("0")
            #error check for peace of mind
            if char_conv >= base:
                print("string doesnt match base!")
                return 0
            digits.append(char_conv)
        #expand each coeff and convert to base 10 rep
        counter = 1
        for dig in digits:
            b10_result += dig*(base**(len(digits)-counter))
            counter += 1
        if new_base == 10:
            return str(b10_result)
    #convert from base 10 to new base
    while b10_result > 0:
        b10_result, r = divmod(b10_result, new_base)
        if r < 10:
            result += str(r)
        else:
            result += chr(r+ord("0")) #convert to ascii 
    result = result[::-1]  
    return result

def convert_10_to_base(b10_num, base):
    base_result = []
    if base == 10:
        return str(b10_num)
    else:
        while b10_num > 0:
            b10_num, r = divmod(b10_num, base)
            #if remainder is bigger than 10 create list instead of string
            base_result.append(r)
        base_result = base_result[::-1]
        return base_result

def heavy(y, base):
    base_result = y
    sq_result = 0
    loop_tracker=set()
    
    while(True):
        base_result = convert_10_to_base(base_result, base)
        sq_result = 0
        for dig in base_result:
            sq_result += int(dig)**2
        base_result = sq_result
        if sq_result == 1:
            print("True")
            return True
        elif sq_result in loop_tracker:
            print("False")
            return False
        loop_tracker.add(sq_result)