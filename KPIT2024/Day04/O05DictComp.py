
d1 = [(x,y) for x in range(3) for y in range(3)]
print(f"d1 :{d1}")
print("-" * 60)

d2 = [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(f"d2 :{d2}")
print("-" * 60)

print([x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)])
print("-" * 60)

players = {
    'sachin':[ 300, 250, 350, 390, 400],
    'sehwag':[ 280, 325, 435, 375, 450],
    'rahul':[ 200, 300, 180, 450, 150],
    'sourav':[ 180, 300, 250, 390, 225],
    'laxman':[ 200, 250, 150, 310, 290],
    'yuvraj':[ 150, 185, 220, 275, 320]
}

print(f"players :{players}")

print("-" * 60)
print(players['sachin'])

print("-" * 60)
print("Sum of all runs :", sum(players['sachin']))

print("-" * 60)
plyscr = {k: sum(v) for k,v in players.items()}
print(f"plyscr :{plyscr}")

print("-" * 60)
plyscr = {k: (lambda score: sum(score) / len(score))(v)
              for k, v in players.items()}
print(f"plyscr :{plyscr}")

def avgScr(score):
    return sum(score)/len(score)

print("-" * 60)
plyscr = {k: avgScr(v) for k, v in players.items()}
print(f"plyscr :{plyscr}")

print("-" * 60)
res = [{x: (lambda par: "Mr." + par) ("Sachin {}".format(x))}
       for x in range(1, 6)]

print(f"res: {res}")

print("-" * 60)
res = {(lambda par: par * 10) (k): (lambda par: par * par)(v)
       for k, v in {1:1, 2:2, 3:3, 4:4, 5:5}.items()}
print(f"res :{res}")

print("-" * 60)
plyscr = [ply_scr for ply_scr in players.values()]
print(f"plyscr :{plyscr}")

print("-" * 60)
plyscr = [scr for ply_scr in players.values() for scr in ply_scr]
print(f"plyscr :{plyscr}")

print("-" * 60)
plyscr = [scr for ply_scr in players.values() for scr in ply_scr if scr > 200]
print(f"plyscr :{plyscr}")

print("-" * 60)
plyscr = {name :[scr for scr in score if scr > 200] for name, score in players.items()}
print(f'plyscr :{plyscr}')