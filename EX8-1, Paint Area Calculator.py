#Write your code below this line 👇
def paint_calc(height,width,cover):
    cans_o_paint = round((height * width) / cover)
    print(f"You'll need {cans_o_paint} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

