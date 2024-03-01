#s = "this\nis\nline"
#print (s)

#s1= """this
#is
#line"""
#print(s1)

#operator for str
#x=input ("nhap:")
#print("ban co " + x + " con")
#print(f"ban co {x} con")


#name = input("Your name:")
#print(len(name))
#print(name.find("D"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.count("d"))
#print(name.replace("d", "b"))

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:end]

name= "hoang long"

first_name = name[name.find("h"):5]
print(first_name)

last_name = name[name.find("l"):]
print(last_name)

reserve_name = name[::-1]
print(reserve_name)