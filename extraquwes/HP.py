#harmonic progression code for calculating the series 
N = int(input("Enter N: "))
s = 0

for i in range(1, N + 1):
    # Add the required term here
    s = s + 1/i

print(s)

