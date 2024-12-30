import turtle 
import Lsys

      
rules = dict()
commands = dict()
arguments = dict()        
        
#-------------------------------
#
#Кристалл / Crystal  
#
#------------------------------

xstart = -400
ystart = -200
tsize = 1
turtle.penup()
turtle.setposition (xstart,ystart)
turtle.pendown()
turtle.pensize(tsize)
turtle.speed(0)


commands ["A"] = "forward(arguments['A'])"
commands ["+"] = "right(arguments['+'])"
commands ["-"] = "left(arguments['-'])"
commands ["C"] = "color(arguments['C'])"
commands ["D"] = "color(arguments['D'])"

arguments ["A"] = 2
arguments ["+"] = 90
arguments ["-"] = 90
arguments ["C"] =  "red"
arguments ["D"] =  "green"


rules ["A"] = "AA+A++A+A"
rules ["B"] = "C"
#rules ["C"] = "ABC"
#rules ["D"] = "()"


start_string = "A+A+A+A"
iter_number = 4 

L1 = Lsys.Lsystem (arguments,commands,rules,"turtle")
L1.execute_cmd_Lstring (iter_number,start_string)


#--------------------------------------
#
#Кривая Коха / Koch curve
#
#---------------------------------------

xstart = -100
ystart = -200
turtle.penup()
turtle.setposition (xstart,ystart)
turtle.pendown()
tsize = 2
turtle.pensize(tsize)

commands ["A"] = "forward(arguments['A'])"
commands ["+"] = "right(arguments['+'])"
commands ["-"] = "left(arguments['-'])"
commands ["C"] = "color(arguments['C'])"
commands ["D"] = "color(arguments['D'])"



rules ["A"] = "A+A-DA-A+AC"
rules ["B"] = "C"
#rules ["C"] = "ABC"
#rules ["D"] = "()"


start_string = "A"
iter_number = 4   

L1.execute_cmd_Lstring (iter_number,start_string)

    
#--------------------------------------------------------------------
#
#Треугольник Серпинского / Sierpinski triangle
#
#---------------------------------------------------------------------

xstart = -100
ystart = -200
turtle.setposition (xstart,ystart)

rules ["A"] = "B-A-B"
rules ["B"] = "A+B+A"
commands ["B"] = "forward(arguments['A'])"
arguments ["A"] = 5
arguments ["+"] = 60
arguments ["-"] = 60

start_string = "A"
iter_number = 5  

L1.execute_cmd_Lstring (iter_number,start_string)


#---------------------------------------------------------------
#
# Кривая дракона / The Dragon's Curve
#
#----------------------------------------------------------------

xstart =  150
ystart = -200
turtle.penup()
turtle.setposition (xstart,ystart)
turtle.pendown()


rules ["X"] = "X+YF+"
rules ["Y"] = "-FX-Y"
commands ["F"] = "forward(arguments['F'])"
commands ["-"] = "left(arguments['-'])"
commands ["+"] = "right(arguments['+'])"
commands ["X"] = "color(arguments['X'])"
commands ["Y"] = "color(arguments['Y'])"

arguments ["X"] = "red"
arguments ["Y"] = "green"
arguments ["F"] = 5
arguments ["-"] = 90
arguments ["+"] = 90


start_string = "FX"
iter_number = 12  

L1.execute_cmd_Lstring (iter_number,start_string,1)


print ("T H E   E N D")

    

        
        
