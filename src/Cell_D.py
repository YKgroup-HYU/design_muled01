import pya
# Enter your Python code here

# Preferences
default_unit = 1.0e-6   # 1 um
target_unit = 1.0e-9    # 1 nm
unit = target_unit/default_unit    # degree
pi = 3.141592 


layout = pya.Layout()
top = layout.create_cell("TOP")

    
def Box_create(x,y,w,h,f):
    global layout, top
    Layout = layout.layer(f,0)
    x, y = x / unit, y / unit
    w, h = w / unit, h / unit    
    
    box = pya.Box(x,y,w+x,h+y)
    box_create = top.shapes(Layout).insert(box)
    return box_create


for i in range(27):
  p = 290*i-7830/2
  for j in range(57):
    m = 140*j-7980/2
    Box_create(0+p,0+m,290,140,99)  #Unit size 
    Box_create(20+p,20+m,250,100,32) #ISO
    Box_create(10+p, 10+m, 160,120,1) #mesa(n-GaN)
    Box_create(25+p,25+m,140,90,2) #ITO
    Box_create(185+p, 35+m, 70, 70,3) #SiO2
    Box_create(35+p, 35+m, 70, 70,3) #SiO2
    Box_create(30+p,30+m,80,80,4) #Metal(P)
    Box_create(180+p,30+m,80,80,4) #Metal(n) 
    Box_create(0-7830/2,0-7980/2,7830,7980,77) #base Layer
Box_create(0-7830/2,0-7980/2,7830,7980,3)  #SiO2


layout.write("C:/Users/dream/KLayout/python/lump_gds/cell_default.gds")



