x = int(input("整数xの値を入力してください:"))
y = int(input("整数yの値を入力してください:"))

if x > 0 and y > 0 or x < 0 and y < 0:
    print("点は第1象限か第3象限にあります")
elif x < 0 and y > 0 or x > 0 and y < 0:
    print("点は第2象限か第4象限にあります")
else:
    print("点はx軸もしくはy軸上にあります")