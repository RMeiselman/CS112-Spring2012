def greeter(name):
    name = str(name)
    name = name.lower()
    print "hello,", name

greeter("Enter text")

def box(w,h):
    if type(w) != int or type(h) != int or w < 1 or h < 1:
        print "Error: Invalid Dimensions"
        return
    
    if w == 1:
        top = "+"
        sides = "|"
    else:
        top = "+" + "-"*(w-2) + "+"
        sides = "|" + " "*(w-2) + "|"
    
    print top
    for i in range (h-2):
        print sides
    if h >=2:
        print top


print box(5,5)


