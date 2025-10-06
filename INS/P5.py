from random import randint

P = 23; G = 9
print(f"Value of P is: {P}")
print(f"Value of G is: {G}")

Alice = 4
Bob = 6
print(f"\nSecret number for Alice is: {Alice}")
print(f"Secret number for Bob is: {Bob}")

x = int(pow(G, Alice, P))
y = int(pow(G, Bob, P))

key_Alice = int(pow(y, Alice, P))
key_Bob = int(pow(x, Bob, P))

print(f"\nSecret key for Alice is: {key_Alice}")
print(f"Secret key for Bob is: {key_Bob}")
