
mess = "AAAAABBBBBCDDDDDEEEEE"

def RLE(somestr): #Функция RLE RESULLT: 5A5B1C5D5E
    final = ""
    counter=1
    j=0
    for i in somestr:
            
        if  somestr[j]==somestr[j+1]:
            counter+=1
        else:
            final+=str(counter)+somestr[j]
            counter=1
            
        j+=1
        if j+1 == len(somestr):
            final+=str(counter)+somestr[j]
            return final
print(RLE(mess))

mess_res = RLE(mess) #5A5B1C5D5E

mess_res = "5A5B1C5D5E"

def res_RLE(somestr):
    final_str = ""
    index = 0

    for i in somestr:
        if i.isdigit():
            final_str+=somestr[index+1]
        index+=1
    return final_str
            

res_RLE(mess_res)
