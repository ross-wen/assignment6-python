
def main():
    Number = int(userInput())
    deno = -1
    Pi = 0
    for i in range(Number):
        deno = deno + 2
        if i % 2 == 0: #if i is positive
            Pi = Pi + 4/deno
        else:
            Pi = Pi - 4/deno
    print(Pi)
def userInput():
    while True:
        Num = input()
        if Num.isnumeric():
            if int(Num) > 0:
                return Num

main()
