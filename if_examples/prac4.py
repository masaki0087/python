n = int(input("得点を入力してください:"))

if 0 <= n <= 100:
    if n >= 90:
        print("成績:A", end=' ')
    elif n >= 80:
        print("成績:B", end=' ')
    elif n >= 70:
        print("成績:C", end=' ')
    elif n >= 60:
        print("成績:D", end=' ')
    else:
        print("成績:F", end=' ')
    
    if n >= 60:
        print("合格")
    else:
        print("不合格")

else:
    print("範囲外の値です")