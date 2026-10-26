print("determinador de tipo de triangulo por sus lados (equilatero isosceles y escaleno) pasame tus lados de los triangulos")
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
print("perfecto ahora paso a hacerlo")
#if basico con buscar los lados sabes hacerlo
if lado1 == lado2 == lado3:
    print("tu triangulo es un equilatero")
elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
    print("es isosceles")
else:
    print("es escaleno")
input()

