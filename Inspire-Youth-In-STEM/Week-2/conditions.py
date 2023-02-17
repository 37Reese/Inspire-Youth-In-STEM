age = 24
gender = "male"

if (age < 18):
    print("You are still young")
else:
    print("You should get an ID")

#compound/multiple

if((age > 30) & (gender == 'male')):
    print("You qualify for a loan")
else:
    print("No loan for you")


fav_color = "grey"
age = 22
if(fav_color == 'grey')|(age <= 20):
    print("Happy birthday")
else:
    print("No birthday present for you yet")