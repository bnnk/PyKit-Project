mintubhishi='''import turtle
t=turtle.pen()
turtle.clearscreen()
mini=input("TC,UI Or OBS")
if mini.upper()== "OBS":
    turtle.fillcolor('cyan')
    turtle.begin_fill()
    for x in range(1, 9):
        turtle.forward(100)
        turtle.left(225)
    turtle.end_fill()
elif mini.upper()== "UI":
    turtle.fillcolor('red')
    turtle.begin_fill()
    for x in range(1,20):
        turtle.forward(100)
        turtle.left(95)
    turtle.end_fill()
elif mini.upper()== "TC":
    for ink in ["yellow", "red", "orange","blue"]:
     turtle.begin_fill()
     turtle.color(ink)
     turtle.forward(50)
     turtle.left(90)
     turtle.end_fill()'''
milla=input('Execute?')
if milla.lower()== 'yes':
    print('TC = Square \
    UI = Flower \
    OBS = Rectangular Star')
    exec(mintubhishi)
    tin=input('TO Copy,Enter Code: ')
    if tin== '23GA67&':
     print('Copy the code from here.')
     print(mintubhishi)
     tin=input('Subscribe To bnnk @ github')
     test_function=open("/home/pi/Desktop/licence.txt")
     print(dir(test_function))
     text_begin=test_function.read()
     print(text_begin)
else:
    import sys
    sys.exit(0)

test_function=open("/home/pi/Desktop/licence.txt")
print(dir(test_function))
text_begin=test_function.read()
print(text_begin)
















    
