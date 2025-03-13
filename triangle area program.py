print("Please enter the measure of two seperate angles of either equilateral,right angle or an isoceleces triangle:")
angle1 = int(input())
angle2 = int(input())
angle3 = 180 - (angle1 + angle2)

if (angle1 == angle2 == angle3):
    print ("this is a equilateral triangle and the measure of the third angle =",angle3)
elif (angle1 == angle2 < angle3):
    print ("this a isoceleces triangle and the measure of the third angle = ",angle3)
elif (angle1 == angle3 < angle2):
    print ("this a isoceleces triangle and the measure of the third angle = ", angle3)
elif  (angle2 == angle1 < angle3):
    print ("this a isoceleces triangle and the measure of the third angle = ", angle3)
elif (angle2 == angle3 < angle1):
    print ("this a isoceleces triangle and the measure of the third angle = ", angle3)
elif (angle3 == angle1 < angle2):
    print("this a isoceleces triangle and the measure of the third angle = ", angle3)
elif (angle3 == angle2 < angle1):
    print("this a isoceleces triangle and the measure of the third angle = ", angle3)
elif (angle1 == 90):
    print("this a right angle triangle and the measure of the third angle = ", angle3)
elif(angle2 == 90):
    print("this a right angle triangle and the measure of the third angle = ", angle3)
else:
    print("this a right angle triangle and the measure of the third angle = ", angle3)

