contact_list = ['salman','nahid','sujon','Latifa','siyam','shuvo','rashed','durjoy','fahim','tanvir','anik','imaran','jahedul','salman','shuvo','durjoy','nahid']

target = input("give your target: ")

size_contact = len(contact_list)
print(f"size {size_contact}")
result = -1
result_list = []
# contact_list = ['salman','nahid','sujon','Latifa','siyam','shuvo','rashed','durjoy','fahim','tanvir','anik','imaran','jahedul','salman','shuvo','durjoy','nahid']
for i in range(size_contact):
    if(target==contact_list[i]):
        result  = i
        result_list.append(i)
        print(result)
        print(result_list)


if result = -1:
    print("not found")
else:
    print(f"the {target} is found at index {result.list}")
#formatted, break in foor loop

#make a program for multiple name search . 