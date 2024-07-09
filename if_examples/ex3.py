a = int(input("aを入力してください:"))
b = int(input("bを入力してください:"))
c = int(input("cを入力してください:"))

if a < b < c:
    print("bはaより大きく、cはbより大きい値です")
elif b < c < a:
    print("cはbより大きく、aはcより大きい値です")
elif c < a < b:
    print("aはcより大きく、bはaより大きい値です")
elif a == b == c:
    print("a,b,c全て等しい値です")
else:
    print("いずれの条件も満たしません")