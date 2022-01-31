number = input()
number = int(number)
type = input()
result = None
if type == 'k':
    points = input()
    points = int(points)
if type == 'b':
    result = (number * 1024)
    print(result)
if type == 'k':
    result = number / 1024
    print(round(result, points))
    # print("%.pointsf" % result)