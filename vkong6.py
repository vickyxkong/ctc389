#Vicky Kong
#Lab 6

names=["Julia","Annie","Marcus","Carlos","Jesmark"]

for i in names:
    print(i)

print("Menu")
print("To add student to list, enter 1")
print("To modify student name, eneter 2")
print("To remove a student from the list, enter 3")

x=int(input("Enter the number:"))

if(x==1):
    newname=input("Enter the student's name you like to add:")
    names.append(newname)

    for i in names:
        print(i)


if(x==2):
    print("0",names[0])
    print("1",names[1])
    print("2",names[2])
    print("3",names[3])
    print("4",names[4])

    modifynum=int(input("Enter the number for the name you would like to modify:"))
    modifyname=input("Enter the name you want to modify to:")
    names[modifynum]=modifyname

    for i in names:
        print(i)


if(x==3):
    print("0",names[0])
    print("1",names[1])
    print("2",names[2])
    print("3",names[3])
    print("4",names[4])

    remove=int(input("Enter the index number for the name you would like to remove:"))

    names.pop(remove)

    for i in names:
        print(i)

