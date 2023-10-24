print("Welcome to Pixel Art Generator⭐")
row_1 = "  ⬜  "
row_2 = " ⬜ ⬜ "
row_3 = "⬜   ⬜"

print(row_1)
print(row_2)
print(row_3)

#name = input("Enter your name : ")
#print("Hello", name)

print("Please enter a number to put a pixel. ")
#row_1_position is a  variable name 
row_1_position = input("Enter number between 1 and 5 for row 1:")
row_1_position = int(row_1_position)

while row_1_position < 1 or row_1_position >5:
  row_1_position = input("Enter number between 1 and 5 for row 1:")
  row_1_position = int(row_1_position)
    
row_2_position = input("Enter number between 1 and 5 for row 2:")
row_2_position = int(row_2_position)

row_3_position = input("Enter number between 1 and 5 for row 3:")
row_3_position = int(row_3_position)

row = ''
for i in range(1,6):
    if i == row_1_position:
       row = row + ('⬜')
    else:
       row = row + (' ')
    # print(i,row,'*')
print(row)

row = ''
for i in range(1,6):
    if i == row_2_position:
       row = row + ('⬜')
    else:
       row = row + (' ')
    # print(i,row,'*')
print(row)

row = ''
for i in range(1,6):
    if i == row_3_position:
       row = row + ('⬜')
    else:
       row = row + (' ')
    # print(i,row,'*')
print(row)
