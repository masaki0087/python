n = int(input("整数値を入力してください:"))

if n > 0:
    print(f"{n}の値は正の数です")
elif n == 0:
    print(f"{n}の値は0です")
else:
    print(f"{n}の値は負の数です")