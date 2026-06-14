listl= input("Enter first list (comma-separated):").split(",")
list2= input("Enter second list (comma-separated):").split(",")
list1= [x.strip() for x in listl]
list2= [x.strip()for x in list2]
def has_common (list1l, list2):
    return any (item in list2 for item in list1)
print("First list:",listl)
print("Second list:", list2)
print("Common element exist:", has_common (listl, list2))
