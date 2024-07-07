point = int(input("得点を入力してください:"))

if point >= 90:
    print("成績:A")
elif point >= 80:
    print("成績:B")
elif point >= 70:
    print("成績:C")
elif point >= 60:
    print("成績:D")
else:
    print("成績:F")