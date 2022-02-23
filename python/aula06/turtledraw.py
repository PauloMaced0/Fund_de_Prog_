import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

with open('drawing.txt', 'r') as instructions_file:
    file = instructions_file.readlines()
    for eich_command in file:
        eich_command = eich_command.strip()
        if eich_command == 'UP':
            t.up()
        elif eich_command == 'DOWN':
            t.down()
        else:
            coordinate = eich_command.split()
            t.goto(int(coordinate[0]),int(coordinate[1]))

turtle.Screen().exitonclick()



