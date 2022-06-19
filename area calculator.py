def calculate_square_area(side: float):
    return side*side

def calculate_rectangle_area(lenght: float, width: float):
    return lenght*width

def calculate_circle_area(radius: float):
    pi=3.14
    return pi*radius*radius

print("""
 ------------
 Area calculator
 ------------
 Select a shape:
 """)

selection = input("select a shape") 
  



if selection == "square":
    side=input("enter the side")
    area=calculate_square_area(float(side))
elif selection == "rectangle":
    lenght=input("enter the lenght")
    width=input("enter the width")
    area=calculate_rectangle_area(float(lenght),float(width))
elif selection == "circle":
    radius=input("entr the rsdius")
    area=calculate_circle_area(float(radius))

else:
    print("invalid selection")

print(area)

