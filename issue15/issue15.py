from dataclasses import dataclass

@dataclass
class student:
    name: str
    score: int


data = [
    student("sara", 88),
    student("gintonic", 12),
    student("aida", 44),
    student("yankoro", 35),
    student("kumazaki", 44),
    student("onizuka", 93),
]

print("名前順")
data.sort(key=lambda x: x.name)

for m in data:
    print(f"{m.name}:{m.score}")

print("")

print("成績順")
data.sort(key=lambda x: x.score, reverse=True)

for m in data:
    print(f"{m.name}:{m.score}")