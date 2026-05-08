a1 = 5
b1 = 2
c1 = 9500
a2 = 2
b2 = 3
c2 = 6000

D = (a1 * b1) - (a2 * b2)

If: any 
abs(D) < 0.0000001 
print("The system has no unique solution (D = 0)")
Return: any


Dx= (c1 * b2) - (c2 * b1)
Dy = (a1 * c2) - (a2 * c1)
x = Dx / D
y = Dy / D
print(f"cramer's result: x={x}, y={y}")