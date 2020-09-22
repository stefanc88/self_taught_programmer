

# personal information stored in Container


personal_information = {"Height":"178", "eye colour":"brown", 
                        "favorite author":"Dostojewski", "favorite colour":"orange"}


n = input ("type in a personal information of me:")
if n in personal_information:
    result = personal_information[n]
    print(result)
else:
    print("Wrong Input")



    
