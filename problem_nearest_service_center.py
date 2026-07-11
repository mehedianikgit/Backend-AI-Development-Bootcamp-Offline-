import math
ax = 1
ay = 2
bx = 8
by = 7
cx = 2
cy = 8
px = 6
py = 5

x = int(input("Emergency distance X:"))
y = int(input("Emergency distance y:"))



a = dis_from_a = math.sqrt((ax-x)**2 + (ay-y)**2)
b = dis_from_b = math.sqrt((bx-x)**2 + (by-y)**2)
c = dis_from_c = math.sqrt((cx-x)**2 + (cy-y)**2)
p = dis_from_p = math.sqrt((px-x)**2 + (py-y)**2)


print("Distance From A:",dis_from_a)
print("Distance From b:",dis_from_b)
print("Distance From c:",dis_from_c)
print("Distance From p:",dis_from_p)

if a<b and a<c and a<p:
    print("A is the nearest From You") 

    if b<c and b<p:
        print("B is the 2nd nearest frpm you")
        if c<p:
            print("C is the 3rd Nearest from you")
            print("P is the 4th Nearest from you")
        else:
            print("C is the 4th Nearest from you")
            print("P is the 3rd Nearest from you")

    elif c<b and c<p:
        print("c is the 2nd nearest from you")
        if b<p:
            print("b is the 3rd Nearest from you")
            print("P is the 4th Nearest from you")
        else:
            print("b is the 4th Nearest from you")
            print("P is the 3rd Nearest from you")

    else:
        print("P is the 2nd nearest from you")
        if b<c:
            print("b is the 3rd Nearest from you")
            print("c is the 4th Nearest from you")
        else:
            print("b is the 4th Nearest from you")
            print("c is the 3rd Nearest from you")


elif b<a and b<c and b<p:
    print("B is the nearest From You") 

    if a<c and a<p:
        print("a is the 2nd nearest from you")
        if c<p:
            print("C is the 3rd Nearest from you")
            print("P is the 4th Nearest from you")
        else:
            print("C is the 4th Nearest from you")
            print("P is the 3rd Nearest from you")

    elif c<a and c<p:
        print("c is the 2nd nearest from you")
        if a<p:
            print("a is the 3rd Nearest from you")
            print("P is the 4th Nearest from you")
        else:
            print("a is the 4th Nearest from you")
            print("P is the 3rd Nearest from you")

    else:
        print("P is the 2nd nearest from you")
        if b<c:
            print("b is the 3rd Nearest from you")
            print("c is the 4th Nearest from you")
        else:
            print("b is the 4th Nearest from you")
            print("c is the 3rd Nearest from you")



elif c<a and c<b and c<p:
    print("c is the nearest From You") 

    if b<a and b<p:
        print("b is the 2nd nearest from you")
        if a<p:
            print("a is the 3rd Nearest from you")
            print("P is the 4th Nearest from you")
        else:
            print("P is the 3rd Nearest from you")
            print("a is the 4th Nearest from you")

    elif a<b and a<p:
        print("a is the 2nd nearest from you")
        if b<p:
            print("b is the 3rd Nearest from you")
            print("P is the 4th Nearest from you")
        else:
            print("P is the 3rd Nearest from you")
            print("b is the 4th Nearest from you")

    else:
        print("P is the 2nd nearest from you")
        if b<a:
            print("b is the 3rd Nearest from you")
            print("a is the 4th Nearest from you")
        else:
            print("a is the 3rd Nearest from you")
            print("b is the 4th Nearest from you")



else:
    print("p is the nearest From You") 

    if b<c and b<a:
        print("b is the 2nd nearest from you")
        if c<a:
            print("C is the 3rd Nearest from you")
            print("a is the 4th Nearest from you")
        else:
            print("C is the 4th Nearest from you")
            print("a is the 3rd Nearest from you")

    elif c<b and c<a:
        print("c is the 2nd nearest from you")
        if b<a:
            print("b is the 3rd Nearest from you")
            print("a is the 4th Nearest from you")
        else:
            print("b is the 4th Nearest from you")
            print("a is the 3rd Nearest from you")

    else:
        print("a is the 2nd nearest from you")
        if b<c:
            print("b is the 3rd Nearest from you")
            print("c is the 4th Nearest from you")
        else:
            print("b is the 4th Nearest from you")
            print("c is the 3rd Nearest from you")