x = "Flop"

def FlipFlop(x):
    return "Flip" if x == "Flop" else "Flop"

for _ in range(10):
    print(x := FlipFlop(x))