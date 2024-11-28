bagalar=[]
M1 = int(input("M1="))
M2 = int(input("M2="))
Ex = int(input("Ex="))
y=0
z=0
while True:
    x = input("Baga engiz: eger baga bitse stop dep jaz: )")
    if x=="stop":
        print(bagalar)
        print("y=", y)
        print("arm=", arm)
        print("korytyndy_baga=", korytyndy_baga)
        break
    y = y+int(x)
    z = z+1
    bagalar.append(int(x))
    arm=y/z
    R1 = arm * 0.6 + M1 * 0.2 + M2 * 0.2
    korytyndy_baga = (R1 + Ex) / 2
    print(bagalar)
    print("y=",y)
    print("arm=",arm)
    print("korytyndy_baga=",korytyndy_baga)
