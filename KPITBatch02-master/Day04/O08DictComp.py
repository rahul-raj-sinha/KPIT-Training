
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")
print("Sachin:", players['sachin'])

print("Sachin :", sum(players['sachin']))
print("-" * 60)

scores = {k: sum(v) for k, v in players.items()}
print(scores)
print("-" * 60)

scores = [player for player in players.keys()]
print(scores)
print("-" * 60)

scores = [score for score in players.values()]
print(scores)
print("-" * 60)

avg_score = {name: (lambda scr: sum(scr) / len(scr))(score)
                for name, score in players.items()}
print(f"Average Score :{avg_score}")
print("-" * 60)

def avgScr(scr):
    return sum(scr) / len(scr)

avg_score = {name: avgScr(score) for name, score in players.items()}
print(f"average score :{avg_score}")
print("-" * 60)

basic = [{x: (lambda par: "Mr." + par) ("Sachin {}".format(x))}
         for x in range(1, 6)]
print(basic)
print("-" * 60)

scores = [scr for scr in players.values()]
print(f"scores :{scores}")
print("-" * 60)

scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")
print("-" * 60)

scores = {k: [scr for scr in score if scr > 200]
          for k, score in players.items()}
print(f"scores :{scores}")