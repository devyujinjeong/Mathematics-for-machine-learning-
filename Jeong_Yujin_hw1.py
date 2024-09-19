import numpy as np

# problem 1
# (a)
print("#pro1-(a):",1.32+45.32)

#(b)
print("#pro1-(b):",32.12+np.sqrt(2)-12/12)

# problem 2
a = 3.4
b = 32
c = np.sqrt(pow(a,2)+pow(b,2))
print("#pro2-1:",a/c)
print("#pro2-2:",a+b-a*c+(a+b**2)*(a-c**2))

# problem 3
x = 25
print("#pro3:",x)

# problem 4
# (a)
c_area = 6*pow(12,2)
s_r = np.sqrt(c_area/(4*np.pi))
print("#pro4-(a):",s_r)

# (b)
c_volumn = 12**3
v_r = (c_volumn * 3/(4*np.pi))**(1/3)
print("#pro4-(b):",v_r)

# problem 5
d1 = np.pi*18/180
d2 = np.pi*45/180

result1 = np.tan(4*d1)
result2 = (4*np.tan(d1) - 4*(np.tan(d1)**3))/(1 - 6*np.tan(d1)**2+np.tan(d1)**4)
dif1= result1-result2
print("#pro5-1:",dif1)

result3 = np.tan(4*d2)
result4 =(4*np.tan(d2) - 4*np.tan(d2)**3)/(1 - 6*np.tan(d2)**2+np.tan(d2)**4)
dif2= result3-result4
print("#pro5-2:",dif2)

# problem 6
x1 = 3; y1 = 4;
x2 = 5; y2 = 9;
print("#pro6:",np.sqrt((x1-x2)**2+(y1-y2)**2))

# problem 7
# (a)
print("#pro7-(a):",5000*pow((1+0.085/1),17*1))

# (b)
print("#pro7-(b):",5000*pow((1+0.085/12),17*12))

# problem 8
R1=12 ; R2=9.5 ; R3=16 ; R4=6.5;
a1=R1+R4 ; a2=R4+R3 ; a3=R1+R3 ;
b1=R1+R2 ; b2=R2+R3 ; b3=a3 ;

cosA=(a2**2+a3**2-a1**2)/(2*a2*a3) ;
sinA=np.sin(np.acos(cosA)) ;

cosB=(b2**2+b3**2-b1**2)/(2*b2*b3) ;
sinB=np.sin(np.acos(cosB)) ;
x1=sinA*a2 ; x2=sinB*b2 ; distance=x1+x2 ;
print("#pro8:",distance)

# problem 9
answer = (83*np.cos(3*np.pi/7))/np.sqrt((1-0.32)+(3-np.sqrt(0.34))**2)
print("#pro9:",answer)

# problem 10
tan36 = np.tan(36*np.pi/180) 
tan42 = np.tan(42*np.pi/180) 
d = (1500*tan36*tan42)/(tan36+tan42)
print("#pro10:",d,"m")