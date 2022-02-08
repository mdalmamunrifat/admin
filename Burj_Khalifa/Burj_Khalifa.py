print("Program for Burj Khalifa Pattern")

print("=========================================================")

n = int(input("Please enter row number: "))

def startPrintingFunction(total, row):
    for raw in range(total):
        for new in range(total-row):
            print("  ", end="")
        for coloum in range(1, 2*row):
            print("*", end=" ")
        print()
for num in range(1, n):
    startPrintingFunction(n, num)
print("End Now")
    


