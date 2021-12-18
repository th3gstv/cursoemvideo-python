#2m of Wall) = 1 ink liter
#Wall = Variable in Liters
#Wall/2
width=float(input("Wall width: "))
height=float(input("Wall heigh: "))
wall=float((width*height))
ink=(wall)/(2)
print("Your wall has {}x{} dimension, being {}m². It will be necessary {} ink liters".format(width,height,wall,ink))
