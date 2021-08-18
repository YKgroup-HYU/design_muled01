
# Enter your Python code here
import pya
import math

# 1. mesa
# 2. ITO
# 3. SiO2
# 4. Metal
# 9. Active Layer
# 32. ISO
# 33. Cell size
#

# Preferences
default_unit = 1.0e-6   # 1 um
target_unit = 1.0e-9    # 1 nm
unit = target_unit/default_unit
angle_point = 0.1       # degree
pi = 3.141592           # pi

layout = pya.Layout()
top = layout.create_cell("TOP")
w_wgs = [0.45, 0.5, 0.7]

def Poly_rectangle(x_c, y_c, width1, width2, height1, height2,f):
  global layout
  Layout = layout.layer(f,0)
  x_c, y_c = x_c / unit, y_c / unit
  width1, height1 = width1 / unit, height1 / unit
  width2, height2 = width2 / unit, height2 / unit
  
  points = [0,0,0,0]
  points[0] = pya.Point(round(x_c - width1/2.0), round(y_c - height1/2.0))
  points[1] = pya.Point(round(x_c + width1/2.0), round(y_c - height2/2.0))
  points[2] = pya.Point(round(x_c + width2/2.0), round(y_c + height2/2.0))
  points[3] = pya.Point(round(x_c - width2/2.0), round(y_c + height1/2.0))
  obj = pya.Polygon(points)
  
  junsu= top.shapes(Layout).insert(obj)
  return junsu
  
def Poly_rectangle_hole(x_c, y_c, width1, width2, height1, height2,x_c_1, y_c_1, width1_1, width2_1, height1_1, height2_1,f):
  global layout
  Layout = layout.layer(f,0)
  x_c, y_c = x_c / unit, y_c / unit
  width1, height1 = width1 / unit, height1 / unit
  width2, height2 = width2 / unit, height2 / unit
  
  points = [0,0,0,0]
  points[0] = pya.Point(round(x_c - width1/2.0), round(y_c - height1/2.0))
  points[1] = pya.Point(round(x_c + width1/2.0), round(y_c - height2/2.0))
  points[2] = pya.Point(round(x_c + width2/2.0), round(y_c + height2/2.0))
  points[3] = pya.Point(round(x_c - width2/2.0), round(y_c + height1/2.0))
  x_c_1, y_c_1 = x_c_1 / unit, y_c_1 / unit
  width1_1, height1_1 = width1_1 / unit, height1_1 / unit
  width2_1, height2_1 = width2_1 / unit, height2_1 / unit
  
  points_1= [0,0,0,0]
  points_1[0] = pya.Point(round(x_c_1 - width1_1/2.0), round(y_c_1 - height1_1/2.0))
  points_1[1] = pya.Point(round(x_c_1 + width1_1/2.0), round(y_c_1 - height2_1/2.0))
  points_1[2] = pya.Point(round(x_c_1 + width2_1/2.0), round(y_c_1 + height2_1/2.0))
  points_1[3] = pya.Point(round(x_c_1 - width2_1/2.0), round(y_c_1 + height1_1/2.0))
  obj = pya.Polygon(points)
  obj.insert_hole(points_1)
  junsu= top.shapes(Layout).insert(obj)
  return junsu
  
def Box_create(x,y,w,h,f):
    global layout, top
    Layout = layout.layer(f,0)
    x, y,w, h = x / unit, y / unit, w / unit, h / unit
    box = pya.Box(x,y,w+x,h+y)
    box_create = top.shapes(Layout).insert(box)
    return box_create
    
def Poly_donut(x_c, y_c, r1, r2, degree, rotation,f):
  global layout
  Layout = layout.layer(f,0)
  x_c, y_c = x_c / unit, y_c / unit
  r1, r2 = r1 / unit, r2 / unit
    
  n_point = degree / angle_point + 1
  radian_step = 2.0*pi*(degree/360) / (n_point - 1)
  radian_offset = 2.0*pi*(rotation/360)
  points1 = [pya.Point(round(r1 * math.cos(i * radian_step + radian_offset) + x_c), round(r1 * math.sin(i * radian_step + radian_offset) + y_c)) for i in range(int(n_point))]
  points2 = [pya.Point(round(r2 * math.cos(i * radian_step + radian_offset) + x_c), round(r2 * math.sin(i * radian_step + radian_offset) + y_c)) for i in range(int(n_point))]
  
  if degree != 360:
    points1.append(pya.Point(x_c, y_c))
    points2.append(pya.Point(x_c, y_c))    
  
  obj = pya.Polygon(points1)
  
  
  if r2:
    obj.insert_hole(points2)
  
  circle= top.shapes(Layout).insert(obj)
  return circle

def Unit_circle(x_c, y_c, r1, r2, degree, rotation, f):
  global layout
  Layout = layout.layer(f,0)
  x_c, y_c = x_c / unit, y_c / unit
  r1, r2 = r1 / unit, r2 / unit
    
  n_point = degree / angle_point + 1
  radian_step = 2.0*pi*(degree/360) / (n_point - 1)
  radian_offset = 2.0*pi*(rotation/360)
  points1 = [pya.Point(round(r1 * math.cos(i * radian_step + radian_offset) + x_c), round(r1 * math.sin(i * radian_step + radian_offset) + y_c)) for i in range(int(n_point))]
  points2 = [pya.Point(round(r2 * math.cos(i * radian_step + radian_offset) + x_c), round(r2 * math.sin(i * radian_step + radian_offset) + y_c)) for i in range(int(n_point))]
  points1[0] = pya.Point(round(r2 * math.cos(1 * radian_step + radian_offset) + x_c), round(r2 * math.sin(1 * radian_step + radian_offset) + y_c))
  points1[1] = pya.Point(round(r2 * math.cos(1 * radian_step + radian_offset) + x_c)+(r1-r2)/math.cos(radian_offset), round(r2 * math.sin(1 * radian_step + radian_offset) + y_c))
  points2[0] = pya.Point(round(r2 * math.cos(1 * radian_step + radian_offset) + x_c), round(r2 * math.sin(1 * radian_step + radian_offset) + y_c))
  if degree != 360:
    points1.append(pya.Point(round(r2 * math.cos((int(n_point)-1) * radian_step + radian_offset) + x_c)+(r1-r2)/math.cos(radian_offset), round(r2 * math.sin((int(n_point)-1) * radian_step + radian_offset) + y_c)))
    points1.append(pya.Point(round(r2 * math.cos((int(n_point)-1) * radian_step + radian_offset) + x_c), round(r2 * math.sin((int(n_point)-1) * radian_step + radian_offset) + y_c)))
    points2.append(pya.Point(round(r2 * math.cos((int(n_point)-1) * radian_step + radian_offset) + x_c), round(r2 * math.sin((int(n_point)-1) * radian_step + radian_offset) + y_c)))    
  
  obj = pya.Polygon(points1)
  
  
  if r2:
    obj.insert_hole(points2)
    
  unit_circle = top.shapes(Layout).insert(obj)
  return unit_circle

#Poly_rectangle_hole(0,0,7850,7850,8000,8000,0,0,7840,7840,7990,7990,100)
Box_create(-7830/2,-7980/2,7830,7980,77)
Box_create(-7830/2,3480-10,7830,1,77)
Box_create(-7830/2,-3480+10,7830,1,77)
Box_create(-7830/2,1750-10,7830,1,77)
Box_create(0,1750,1,-5250,77)


for v in range(16):
  for i in range(6):
    j = i*630+135-3915
    a = v * -320+1650
    Box_create(j,-150+a,100,100,4)
    Box_create(150+j,-200+a,200,200,32)
    Box_create(400+j,-150+a,100,100,4)
    Box_create(100+j,-105+a,70,10,4)
    
for y in range(12):
  for t in range(6):
    x = t *630+135-3915+100
    b = y * -320+1650

    #CA-전극크기
    if (y == 0):
      Poly_donut(150+x,-100+b,5,0,360,0,1)  #mesa
      Unit_circle(150+x,-100+b,25,15,300,30+180,4)
      Poly_donut(150+x,-100+b,1,0,180,270,4)
      Box_create(140+x,-100-1+b,10,2,4)
      Box_create(70+x,-100-2.5+b,70,5,4)
      Box_create(173+x,-105+b,127,10,4)
      Poly_donut(150+x,-100+b,3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,23,17,292,34+180,3)   #SiO2
      Poly_donut(150+x,-100+b,2.5,0,360,0,4) #metal
    if (y == 1):
      Poly_donut(150+x,-100+b,10,0,360,0,1)  #mesa
      Unit_circle(150+x,-100+b,30,20,315,22.5+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(178+x,-105+b,122,10,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Poly_donut(150+x,-100+b,7,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,5,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,28,22,308,26+180,3)   #SiO2
      Poly_donut(150+x,-100+b,5,0,360,0,4) #metal
    if (y == 2):
      Poly_donut(150+x,-100+b,20,0,360,0,1) 
      Unit_circle(150+x,-100+b,40,30,331,14.5+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(188+x,-105+b,112,10,4)
      Poly_donut(150+x,-100+b,17,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,15,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,38,32,325.6,17.2+180,3)   #SiO2
      Poly_donut(150+x,-100+b,15,0,360,0,4) #metal
    if (y == 3):
      Poly_donut(150+x,-100+b,30,0,360,0,1) 
      Unit_circle(150+x,-100+b,50,40,338.4,10.8+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(198+x,-105+b,102,10,4)
      Poly_donut(150+x,-100+b,27,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,25,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,48,42,333.8,13.05+180,3)   #SiO2
      Poly_donut(150+x,-100+b,25,0,360,0,4) #metal
    if (y == 4):
      Poly_donut(150+x,-100+b,40,0,360,0,1) 
      Unit_circle(150+x,-100+b,60,50,342.8,8.55+180,4)
      Poly_donut(150++x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(208+x,-105+b,92,10,4)
      Poly_donut(150+x,-100+b,37,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,35,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,58,52,339,10.45+180,3)   #SiO2
      Poly_donut(150+x,-100+b,35,0,360,0,4) #metal
    if (y == 5):
      Poly_donut(150+x,-100+b,50,0,360,0,1) 
      Unit_circle(150+x,-100+b,70,60,345.8,7.05+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(218+x,-105+b,82,10,4)
      Poly_donut(150+x,-100+b,47,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,45,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,68,62,342.6,8.65+180,3)   #SiO2
      Poly_donut(150+x,-100+b,45,0,360,0,4) #metal
      
    #CB-광량
    if (y == 6):
      Poly_donut(150+x,-100+b,5,0,360,0,1)  #mesa
      Unit_circle(150+x,-100+b,25,15,300,30+180,4)
      Poly_donut(150+x,-100+b,1,0,180,270,4)
      Box_create(140+x,-100-1+b,10,2,4)
      Box_create(70+x,-100-2.5+b,70,5,4)
      Box_create(173+x,-105+b,127,10,4)
      Poly_donut(150+x,-100+b,3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,23,17,292,34+180,3)   #SiO2
      Poly_donut(150+x,-100+b,2.5,0,360,0,4) #metal
    if (y == 7):
      r = 10
      Poly_donut(150+x,-100+b,r,0,360,0,1) 
      Unit_circle(150+x,-100+b,30,20,315,22.5+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(178+x,-105+b,122,10,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Poly_donut(150+x,-100+b,r-3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,(r-3)/2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,28,22,308,26+180,3)   #SiO2
      Poly_donut(150+x,-100+b,(r-3)/2+2,0,360,0,4) #metal
    if (y == 8):
      r = 20
      Poly_donut(150+x,-100+b,r,0,360,0,1) 
      Unit_circle(150+x,-100+b,40,30,331,14.5+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(188+x,-105+b,112,10,4)
      Poly_donut(150+x,-100+b,r-3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,(r-3)/2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,38,32,325.6,17.2+180,3)   #SiO2
      Poly_donut(150+x,-100+b,(r-3)/2+2,0,360,0,4) #metal
    if (y == 9):
      r = 30
      Poly_donut(150+x,-100+b,r,0,360,0,1) 
      Unit_circle(150+x,-100+b,50,40,338.4,10.8+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(198+x,-105+b,102,10,4)
      Poly_donut(150+x,-100+b,r-3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,(r-3)/2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,48,42,333.8,13.05+180,3)   #SiO2
      Poly_donut(150+x,-100+b,(r-3)/2+2,0,360,0,4) #metal
    if (y == 10):
      r = 40
      Poly_donut(150+x,-100+b,r,0,360,0,1) 
      Unit_circle(150+x,-100+b,60,50,342.8,8.55+180,4)
      Poly_donut(150++x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(208+x,-105+b,92,10,4)
      Poly_donut(150+x,-100+b,r-3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,(r-3)/2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,58,52,339,10.45+180,3)   #SiO2
      Poly_donut(150+x,-100+b,(r-3)/2+2,0,360,0,4) #metal
    if (y == 11):
      r = 50
      Poly_donut(150+x,-100+b,r,0,360,0,1) 
      Unit_circle(150+x,-100+b,70,60,345.8,7.05+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(218+x,-105+b,82,10,4)
      Poly_donut(150+x,-100+b,r-3,0,360,0,2)  #ITO
      Poly_donut(150+x,-100+b,(r-3)/2,0,360,0,3)  #SiO2
      Unit_circle(150+x,-100+b,68,62,342.6,8.65+180,3)   #SiO2
      Poly_donut(150+x,-100+b,(r-3)/2+2,0,360,0,4) #metal

for y in [12,13,14,15]:
  for t in range(6):
    x = t *630+135-3915+100
    b = y * -320+1650
    if (y == 12) or (y == 14):
      Poly_donut(150+x,-100+b,50,0,360,0,1) 
      Unit_circle(150+x,-100+b,70,60,345.8,7.05+180,4)
      Poly_donut(150+x,-100+b,2.5,0,180,270,4)
      Box_create(70+x,-100-2.5+b,80,5,4)
      Box_create(218+x,-105+b,82,10,4)
      Poly_donut(150+x,-100+b,47,0,360,0,2)  #ITO
      Unit_circle(150+x,-100+b,68,62,342.6,8.65+180,3)   #SiO2
      Poly_donut(150+x,-100+b,45,0,360,0,4) #metal
      if (t == 0):
        Poly_donut(150+x,-100+b,2.5,0,360,0,3)  #SiO2
      if (t == 1):
        Poly_donut(150+x,-100+b,5,0,360,0,3)  #SiO2
      if (t == 2):
        Poly_donut(150+x,-100+b,10,0,360,0,3)  #SiO2
      if (t == 3):
        Poly_donut(150+x,-100+b,20,0,360,0,3)  #SiO2
      if (t == 4):
        Poly_donut(150+x,-100+b,30,0,360,0,3)  #SiO2
      if (t == 5):
        Poly_donut(150+x,-100+b,40,0,360,0,3)  #SiO2
    if (y == 13) or (y == 15):
      if (t == 1) or (t == 2) or (t == 3) or (t == 4) or (t == 5):
        Poly_donut(150+x,-100+b,50,0,360,0,1) 
        Unit_circle(150+x,-100+b,70,60,345.8,7.05+180,4)
        Poly_donut(150+x,-100+b,2.5,0,180,270,4)
        Box_create(70+x,-100-2.5+b,80,5,4)
        Box_create(218+x,-105+b,82,10,4)
        Poly_donut(150+x,-100+b,47,0,360,0,2)  #ITO
        Poly_donut(150+x,-100+b,2,0,360,0,3)  #SiO2
        Unit_circle(150+x,-100+b,68,62,342.6,8.65+180,3)   #SiO2  
      if (t == 1):
        Poly_donut(150+x,-100+b,5,0,360,0,4) #metal
      if (t == 2):
        Poly_donut(150+x,-100+b,10,0,360,0,4) #metal
      if (t == 3):
        Poly_donut(150+x,-100+b,20,0,360,0,4) #metal
      if (t == 4):
        Poly_donut(150+x,-100+b,30,0,360,0,4) #metal
      if (t == 5):
        Poly_donut(150+x,-100+b,40,0,360,0,4) #metal
      if (t == 0):
        Poly_donut(150+x,-100+b,50,0,360,0,1) 
        Unit_circle(150+x,-100+b,70,60,345.8,7.05+180,4)
        Poly_donut(150+x,-100+b,1,0,180,270,4)
        Box_create(140+x,-100-1+b,10,2,4)
        Box_create(70+x,-100-2.5+b,70,5,4)
        Box_create(218+x,-105+b,82,10,4)
        Poly_donut(150+x,-100+b,47,0,360,0,2)  #ITO
        Poly_donut(150+x,-100+b,2,0,360,0,3)  #SiO2
        Unit_circle(150+x,-100+b,68,62,342.6,8.65+180,3)   #SiO2
        Poly_donut(150+x,-100+b,2.5,0,360,0,4) #metal


      
def CTLM(x_c, y_c, width, height, r1, r2, degree, rotation, floor):
  
  global layout  
  Layout = layout.layer(floor,0) 
  x_c, y_c = x_c / unit, y_c / unit  
  width, height = width / unit , height / unit  
  r1, r2 = r1 / unit , r2 /unit  
  pi = 3.141592
  
  angle_point = 0.1
  
   
  
  x_c, y_c = x_c, y_c
  
  width, height = width , height
  
  r1, r2 = r1 , r2
  
  n_point = degree / angle_point + 1
  
  radian_step = 2.0*pi*(degree/360) / (n_point - 1)
  
  radian_offset = 2.0*pi*(rotation/360)
  
   
  
  points = [0,0,0,0]
  
  points[0] = pya.Point(round(x_c - width/2.0), round(y_c - height/2.0))
  
  points[1] = pya.Point(round(x_c + width/2.0), round(y_c - height/2.0))
  
  points[2] = pya.Point(round(x_c + width/2.0), round(y_c + height/2.0))
  
  points[3] = pya.Point(round(x_c - width/2.0), round(y_c + height/2.0))
  
  
   
  
  points1 = [pya.Point(round(r1 * math.cos(i * radian_step + radian_offset) + x_c), round(r1 * math.sin(i * radian_step + radian_offset) + y_c)) for i in range(int(n_point))]
  
  points2 = [pya.Point(round(r2 * math.cos(i * radian_step + radian_offset) + x_c), round(r2 * math.sin(i * radian_step + radian_offset) + y_c)) for i in range(int(n_point))]
  
   
  
  if degree != 360:
  
    points1.append(pya.Point(x_c, y_c))
    
    points2.append(pya.Point(x_c, y_c))
    
  obj = pya.Polygon(points)
    
  obj.insert_hole(points1)

 

  if r2:

    obj_2 = pya.Polygon(points2)
    
    ctlm = top.shapes(Layout).insert(obj)
      
    ctlm1 =top.shapes(Layout).insert(obj_2)
    
  return ctlm,ctlm1

def CTLM_n(x,y):
    global CTLM, Box_create
    x,y = x+140, y+140
   
    CTLM(x+0,y+0,220,280,52,50,360,0,4) # Metal
    CTLM(x+220,y+0,220,280,60,50,360,0,4)
    CTLM(x+470,y+0,280,280,70,50,360,0,4)
    CTLM(x+750,y+0,280,280,90,50,360,0,4)
    CTLM(x+1030,y+0,280,280,100,50,360,0,4)

    CTLM(x+0,y+0,210,270,57,45,360,0,3) # SiO2
    CTLM(x+220,y+0,210,270,65,45,360,0,3)
    CTLM(x+470,y+0,270,270,75,45,360,0,3)
    CTLM(x+750,y+0,270,270,95,45,360,0,3)
    CTLM(x+1030,y+0,270,270,105,45,360,0,3)
    Box_create(x+105,y-135,10,270,3)
    Box_create(x+105+220,y-135,10,270,3)
    Box_create(x+105+220+280,y-135,10,270,3)
    Box_create(x+105+220+280+280,y-135,10,270,3)
    
    Box_create(x-130,y-160,1320,320,32) # Iso

def CTLM_p(x,y):
    global CTLM, Box_create
    x,y = x+140, y+140
   
    CTLM(x+0,y+0,220,280,52,50,360,0,4) # Metal
    CTLM(x+220,y+0,220,280,60,50,360,0,4)
    CTLM(x+470,y+0,280,280,70,50,360,0,4)
    CTLM(x+750,y+0,280,280,90,50,360,0,4)
    CTLM(x+1030,y+0,280,280,100,50,360,0,4)

    CTLM(x+0,y+0,210,270,57,45,360,0,3) # SiO2
    CTLM(x+220,y+0,210,270,65,45,360,0,3)
    CTLM(x+470,y+0,270,270,75,45,360,0,3)
    CTLM(x+750,y+0,270,270,95,45,360,0,3)
    CTLM(x+1030,y+0,270,270,105,45,360,0,3)
    Box_create(x+105,y-135,10,270,3)
    Box_create(x+105+220,y-135,10,270,3)
    Box_create(x+105+220+280,y-135,10,270,3)
    Box_create(x+105+220+280+280,y-135,10,270,3)
    
    Box_create(x-135,y-165,1330,330,1) # mesa
    Box_create(x-125,y-155,1310,310,2) # ITO
    Box_create(x-130,y-160,1320,320,32) # Iso


def Align_box(x,y,w,h,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,w,h,s = x / unit, y /unit, w / unit, h / unit, s / unit
    points = [0,0,0,0]
    points[0] = pya.Point(round(x - w/2.0), round(y - h/2.0))
    points[1] = pya.Point(round(x + w/2.0), round(y - h/2.0))
    points[2] = pya.Point(round(x + w/2.0), round(y + h/2.0))
    points[3] = pya.Point(round(x - w/2.0), round(y + h/2.0))


    points1 = [0,0,0,0]
    points1[0] = pya.Point(round(x - (w-s)/2.0), round(y - (h-s)/2.0))
    points1[1] = pya.Point(round(x + (w-s)/2.0), round(y - (h-s)/2.0))
    points1[2] = pya.Point(round(x + (w-s)/2.0), round(y + (h-s)/2.0))
    points1[3] = pya.Point(round(x - (w-s)/2.0), round(y + (h-s)/2.0))
    
    
    obj = pya.Polygon(points)
    obj.insert_hole(points1)
    
    align_box = top.shapes(Layout).insert(obj)
    return align_box


def Align_key_1(x,y,w,h,s,u,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,w,h,s,u = x / unit, y /unit, w / unit, h / unit, s / unit, u / unit
    points = [0,0,0,0]
    points[0] = pya.Point(round(x - w/2.0), round(y - h/2.0))
    points[1] = pya.Point(round(x + w/2.0), round(y - h/2.0))
    points[2] = pya.Point(round(x + w/2.0), round(y + h/2.0))
    points[3] = pya.Point(round(x - w/2.0), round(y + h/2.0))


    points1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x - s), round(y - s*2))
    points1[1] = pya.Point(round(x - s), round(y - s))
    points1[2] = pya.Point(round(x - 2*s), round(y - s))
    points1[3] = pya.Point(round(x - 2*s), round(y + s))
    points1[4] = pya.Point(round(x - s), round(y + s))
    points1[5] = pya.Point(round(x - s), round(y + 2*s))
    points1[6] = pya.Point(round(x + s), round(y + 2*s))
    points1[7] = pya.Point(round(x + s), round(y + s))
    points1[8] = pya.Point(round(x + 2*s), round(y + s))
    points1[9] = pya.Point(round(x + 2*s), round(y - s))
    points1[10] = pya.Point(round(x + s), round(y - s))
    points1[11] = pya.Point(round(x + s), round(y - 2*s))
    
    obj = pya.Polygon(points)
    obj.insert_hole(points1)
    align_box = top.shapes(Layout).insert(obj)
    
    if u != 0:
      points2 = [0,0,0,0,0,0,0,0,0,0,0,0]
      points2[0] = pya.Point(round(x - s + u), round(y - s*2 + u))
      points2[1] = pya.Point(round(x - s + u), round(y - s + u))
      points2[2] = pya.Point(round(x - 2*s + u), round(y - s + u))
      points2[3] = pya.Point(round(x - 2*s + u), round(y + s - u))
      points2[4] = pya.Point(round(x - s + u), round(y + s - u))
      points2[5] = pya.Point(round(x - s + u), round(y + 2*s - u))
      points2[6] = pya.Point(round(x + s - u), round(y + 2*s - u))
      points2[7] = pya.Point(round(x + s - u), round(y + s - u))
      points2[8] = pya.Point(round(x + 2*s - u), round(y + s - u))
      points2[9] = pya.Point(round(x + 2*s - u), round(y - s + u))
      points2[10] = pya.Point(round(x + s - u), round(y - s + u))
      points2[11] = pya.Point(round(x + s - u), round(y - 2*s + u))
      obj_i = pya.Polygon(points2)
      align_key = top.shapes(Layout).insert(obj_i)
      return align_box, align_key
    
    return align_box

def Align_key_2(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    u = 5/unit
    points2 = [0,0,0,0,0,0,0,0,0,0,0,0]
    points2[0] = pya.Point(round(x - s + u), round(y - s*2 + u))
    points2[1] = pya.Point(round(x - s + u), round(y - s + u))
    points2[2] = pya.Point(round(x - 2*s + u), round(y - s + u))
    points2[3] = pya.Point(round(x - 2*s + u), round(y + s - u))
    points2[4] = pya.Point(round(x - s + u), round(y + s - u))
    points2[5] = pya.Point(round(x - s + u), round(y + 2*s - u))
    points2[6] = pya.Point(round(x + s - u), round(y + 2*s - u))
    points2[7] = pya.Point(round(x + s - u), round(y + s - u))
    points2[8] = pya.Point(round(x + 2*s - u), round(y + s - u))
    points2[9] = pya.Point(round(x + 2*s - u), round(y - s + u))
    points2[10] = pya.Point(round(x + s - u), round(y - s + u))
    points2[11] = pya.Point(round(x + s - u), round(y - 2*s + u))
    obj_i = pya.Polygon(points2)
    align_key = top.shapes(Layout).insert(obj_i)
    
    return align_key

def Align_key(x,y):
    global Align_key1, Align_key2, Align_box
    x,y = x+600, y+200
    #<!--- Align_box ---!>
    Align_box(x,y,1200,400,20,32)



    #<!--- ISO ----!>
    Align_key_1(x-500,y+100,70,70,10,5,32) # full

    Align_key_1(x-500,y-100,70,70,10,0,32) # empty
    Align_key_1(x+100,y+100,70,70,10,0,32) 
    Align_key_1(x+100,y-100,70,70,10,0,32)

    Align_key_2(x-400,y+100,10,32) #key  
    Align_key_2(x-300,y+100,10,32)
    Align_key_2(x-200,y+100,10,32)
    Align_key_2(x-100,y+100,10,32)

    #<!--- mesa ---!>
    Align_key_1(x+200,y+100,70,70,10,5,1) # full

    Align_key_1(x-400,y+100,70,70,10,0,1) # empty
    Align_key_1(x-400,y-100,70,70,10,0,1) 
    Align_key_1(x+200,y-100,70,70,10,0,1)

    Align_key_2(x+100,y+100,10,1) #key
    Align_key_2(x+300,y+100,10,1) 
    Align_key_2(x+400,y+100,10,1)
    Align_key_2(x+500,y+100,10,1)
    Align_key_2(x-500,y-100,10,1)

    #<!--- ITO ---!>
    Align_key_1(x-300,y-100,70,70,10,5,2) # full

    Align_key_1(x-300,y+100,70,70,10,0,2) # empty
    Align_key_1(x+300,y+100,70,70,10,0,2) 
    Align_key_1(x+300,y-100,70,70,10,0,2)

    Align_key_2(x-400,y-100,10,2) #key
    Align_key_2(x-200,y-100,10,2)
    Align_key_2(x+100,y-100,10,2)
    Align_key_2(x+200,y-100,10,2)

    #<!--- SiO2 ---!>
    Align_key_1(x+400,y-100,70,70,10,5,3) # full

    Align_key_1(x-200,y+100,70,70,10,0,3) # empty
    Align_key_1(x-200,y-100,70,70,10,0,3) 

    Align_key_2(x+300,y-100,10,3) #key
    Align_key_2(x+500,y-100,10,3)

    #<!--- Metal ---!>
    Align_key_1(x-100,y-100,70,70,10,5,4) # full

    Align_key_1(x-100,y+100,70,70,10,0,4) # empty
    Align_key_1(x+400,y+100,70,70,10,0,4) 
    Align_key_1(x+500,y+100,70,70,10,0,4) 
    Align_key_1(x+500,y-100,70,70,10,0,4) 


def Line_space(x,y):
    global Box_create
    x,y = x+20, y+200 
    # estimate cell's unit
    a = [2,2,2,3,3,3,3,5,5,5,10,10,10,10,20,20,20,30,30]
    b = [2,2,2,3,3,3,5,5,5,5,10,10,10,20,20,20,20,30]


    #<!--- ISO ---!>
    c = x
    d = x+2  
    for i in a:
       Box_create(c,y+0,i,180,32)
       c += i+i    
    for i in b: 
       Box_create(d,y-190,i,180,32)
       d += i+i     

    Box_create(x+600,y-210,400,410,32)
    Box_create(x+1200,y-210,400,410,32)
    Box_create(x+1800,y-210,400,410,32)
    Box_create(x+2400,y-210,400,410,32)
    


    #<!--- mesa ---!>
    e = x+620
    f = x+622  
    for i in a:
       Box_create(e,y,i,180,1)
       e += i+i    
    for i in b: 
        Box_create(f,y-190,i,180,1)
        f += i+i
        
    Box_create(x+-20,y-210,400,410,1)
    Box_create(x+1200,y-210,400,410,1)
    Box_create(x+1800,y-210,400,410,1)
    Box_create(x+2400,y-210,400,410,1)
    
    
    #<!--- ITO ---!>
    e = x+1220
    f = x+1222  
    for i in a:
        Box_create(e,y+0,i,180,2)
        e += i+i    
    for i in b: 
        Box_create(f,y-190,i,180,2)
        f += i+i     
    
    
    
    #<!--- SiO2 ---!>
    g = x+1820
    h = x+1822  
    for i in a:
        Box_create(g,y+0,i,180,3)
        g += i+i    
    for i in b: 
        Box_create(h,y+-190,i,180,3)
        h += i+i
        
    
    #<1--- Metal ---!>
    j = x+2420
    k = x+2422  
    for i in a:
        Box_create(j,y+0,i,180,4)
        j += i+i    
    for i in b: 
        Box_create(k,y-190,i,180,4)
        k += i+i  
    #mLED_Rectangle

def RA_10(x,y):
    global Box_create    
    Box_create(x+0,y+0,10,10,32) #ISO 
    Box_create(x-2,y-2,8,14,1) #mesa
    Box_create(x+1,y+1,4,8,2) #ITO
    Box_create(x+2.5,y+2.5,1,5,3) #SiO2
    Box_create(x+7.5,y+2.5,1,5,3) #SiO2
    Box_create(x+2,y+2,2,6,4) #Metal(p)
    Box_create(x+7,y+2,2,6,4) #Metal(n)
    Box_create(x+7,y+2,148,6,4) #Metal(n)_wire
    Box_create(x+155,y-45,100,100,4) #Metal(n)_pad
    Box_create(x-145,y+2,149,6,4) #Metal(p)_wire    
    Box_create(x-245,y-45,100,100,4) #Metal(p)_pad
    
def RA_20(x,y):
    x,y = x-5,y-5
    Box_create(x+0,y+0,20,20,32) #ISO
    Box_create(x-3,y-3,15,26,1) #mesa    
    Box_create(x+2,y+2,8,16,2) #ITO    
    Box_create(x+4,y+4,4,12,3) #SiO2    
    Box_create(x+15,y+4,2,12,3) #SiO2    
    Box_create(x+3,y+3,6,14,4) #Metal(p)    
    Box_create(x+14,y+3,4,14,4) #Metal(n)    
    Box_create(x+14,y+5,146,10,4) #Metal(n)_wire    
    Box_create(x+160,y-40,100,100,4) #Metal(n)_pad    
    Box_create(x-140,y+5,148,10,4) #Metal(p)_wire    
    Box_create(x-240,y-40,100,100,4) #Metal(p)_pad

def RA_40(x,y):
    x,y = x-15,y-15
    Box_create(x+0,y+0,40,40,32) #ISO   
    Box_create(x-3,y-3,27,46,1) #mesa    
    Box_create(x+2,y+2,20,36,2) #ITO    
    Box_create(x+4,y+4,16,32,3) #SiO2    
    Box_create(x+27,y+4,10,32,3) #SiO2    
    Box_create(x+3,y+3,18,34,4) #Metal(p)    
    Box_create(x+26,y+3,12,34,4) #Metal(n)    
    Box_create(x+32,y+15,138,10,4) #Metal(n)_Wire    
    Box_create(x+170,y-30,100,100,4) #Metal(n)_pad    
    Box_create(x-130,y+15,142,10,4) #Metal(p)_Wire    
    Box_create(x-230,y-30,100,100,4) #Metal(p)_pad    
  

def RA_60(x,y):
    x,y = x-25,y-25
    Box_create(x,y,60,60,32) #ISO
    Box_create(x-3,y-3,39,66,1) #mesa
    Box_create(x+2,2+y,32,56,2) #ITO
    Box_create(4+x,4+y,28,52,3) #SiO2
    Box_create(39+x,4+y,18,52,3) #SiO2
    Box_create(3+x,3+y,30,54,4) #Metal(p)
    Box_create(38+x,3+y,20,54,4) #Metal(n)
    Box_create(48+x,25+y,132,10,4) #Metal(n)_wire
    Box_create(180+x,-20+y,100,100,4) #Metal(n)_pad
    Box_create(-120+x,25+y,138,10,4) #Metal(p)_wire
    Box_create(-220+x,-20+y,100,100,4) #Metal(p)_pad
    
    
def RA_80(x,y):
    x,y = x-35,y-35
    Box_create(x,y,80,80,32) #ISO
    Box_create(x-3,y-3,51,86,1) #mesa
    Box_create(2+x,2+y,44,76,2) #ITO
    Box_create(4+x,4+y,40,72,3) #SiO2
    Box_create(51+x,4+y,26,72,3) #SiO2
    Box_create(3+x,3+y,42,74,4) #Metal(p)
    Box_create(50+x,3+y,28,74,4) #Metal(n)
    Box_create(64+x,35+y,126,10,4) #Metal(n)_wire
    Box_create(190+x,y-10,100,100,4) #Metal(n)_pad
    Box_create(-110+x,35+y,134,10,4) #Metal(p)_wire
    Box_create(-210+x,y-10,100,100,4) #Metal(p)_pad
    
def RA_100(x,y):
    x,y = x-45,y-45
    Box_create(x,y,100,100,32) #ISO
    Box_create(x-3,y-3,63,106,1) #mesa
    Box_create(2+x,2+y,56,96,2) #ITO
    Box_create(4+x,4+y,52,92,3) #SiO2
    Box_create(63+x,4+y,34,92,3) #SiO2  
    Box_create(3+x,3+y,54,94,4) #Metal(p)
    Box_create(62+x,3+y,36,94,4) #Metal(n)
    Box_create(80+x,45+y,120,10,4) #Metal(n)_wire
    Box_create(200+x,y,100,100,4) #Metal(n)_pad
    Box_create(-100+x,45+y,130,10,4) #Metal(p)_wire
    Box_create(-200+x,y,100,100,4) #Metal(p)_pad
    
def RB_10(x,y):
    global Box_create    
    Box_create(x+0,y+0,10,10,32) #ISO 
    Box_create(x-2,y-2,8,14,1) #mesa
    Box_create(x+1,y+1,4,8,2) #ITO
    Box_create(x+2.5,y+2.5,1,5,3) #SiO2
    Box_create(x+7.5,y+2.5,1,5,3) #SiO2
    Box_create(x+2,y+2,2,6,4) #Metal(p)
    Box_create(x+7,y+2,2,6,4) #Metal(n)
    Box_create(x+7,y+2,148,6,4) #Metal(n)_wire
    Box_create(x+155,y-45,100,100,4) #Metal(n)_pad
    Box_create(x-145,y+2,149,6,4) #Metal(p)_wire    
    Box_create(x-245,y-45,100,100,4) #Metal(p)_pad
    
def RB_20(x,y):
    x,y = x-5,y-5
    Box_create(x+0,y+0,20,20,32) #ISO
    Box_create(x-3,y-3,15,26,1) #mesa    
    Box_create(x+2,y+2,8,16,2) #ITO    
    Box_create(x+4,y+6,4,8,3) #SiO2    
    Box_create(x+15,y+6,2,8,3) #SiO2    
    Box_create(x+3,y+5,6,10,4) #Metal(p)    
    Box_create(x+14,y+5,4,10,4) #Metal(n)    
    Box_create(x+14,y+5,146,10,4) #Metal(n)_wire    
    Box_create(x+160,y-40,100,100,4) #Metal(n)_pad    
    Box_create(x-140,y+5,148,10,4) #Metal(p)_wire    
    Box_create(x-240,y-40,100,100,4) #Metal(p)_pad

def RB_40(x,y):
    x,y = x-15,y-15
    Box_create(x+0,y+0,40,40,32) #ISO   
    Box_create(x-3,y-3,27,46,1) #mesa    
    Box_create(x+2,y+2,20,36,2) #ITO    
    Box_create(x+7,y+11,10,18,3) #SiO2    
    Box_create(x+29,y+11,6,18,3) #SiO2    
    Box_create(x+6,y+10,12,20,4) #Metal(p)    
    Box_create(x+28,y+10,8,20,4) #Metal(n)    
    Box_create(x+32,y+15,138,10,4) #Metal(n)_Wire    
    Box_create(x+170,y-30,100,100,4) #Metal(n)_pad    
    Box_create(x-130,y+15,142,10,4) #Metal(p)_Wire    
    Box_create(x-230,y-30,100,100,4) #Metal(p)_pad    
  

def RB_60(x,y):
    x,y = x-25,y-25
    Box_create(x,y,60,60,32) #ISO
    Box_create(x-3,y-3,39,66,1) #mesa
    Box_create(x+2,2+y,32,56,2) #ITO
    Box_create(10+x,16+y,16,28,3) #SiO2
    Box_create(43+x,16+y,10,28,3) #SiO2
    Box_create(9+x,15+y,18,30,4) #Metal(p)
    Box_create(42+x,15+y,12,30,4) #Metal(n)
    Box_create(48+x,25+y,132,10,4) #Metal(n)_wire
    Box_create(180+x,-20+y,100,100,4) #Metal(n)_pad
    Box_create(-120+x,25+y,138,10,4) #Metal(p)_wire
    Box_create(-220+x,-20+y,100,100,4) #Metal(p)_pad
    
    
def RB_80(x,y):
    x,y = x-35,y-35
    Box_create(x,y,80,80,32) #ISO
    Box_create(x-3,y-3,51,86,1) #mesa
    Box_create(2+x,2+y,44,76,2) #ITO
    Box_create(13+x,21+y,22,38,3) #SiO2
    Box_create(57+x,21+y,13,38,3) #SiO2
    Box_create(12+x,20+y,24,40,4) #Metal(p)
    Box_create(56+x,20+y,15,40,4) #Metal(n)
    Box_create(64+x,35+y,126,10,4) #Metal(n)_wire
    Box_create(190+x,y-10,100,100,4) #Metal(n)_pad
    Box_create(-110+x,35+y,134,10,4) #Metal(p)_wire
    Box_create(-210+x,y-10,100,100,4) #Metal(p)_pad
    
def RB_100(x,y):
    x,y = x-45,y-45
    Box_create(x,y,100,100,32) #ISO
    Box_create(x-3,y-3,63,106,1) #mesa
    Box_create(2+x,2+y,56,96,2) #ITO
    Box_create(16+x,26+y,28,48,3) #SiO2
    Box_create(71+x,26+y,18,48,3) #SiO2  
    Box_create(15+x,25+y,30,50,4) #Metal(p)
    Box_create(70+x,25+y,20,50,4) #Metal(n)
    Box_create(80+x,45+y,120,10,4) #Metal(n)_wire
    Box_create(200+x,y,100,100,4) #Metal(n)_pad
    Box_create(-100+x,45+y,130,10,4) #Metal(p)_wire
    Box_create(-200+x,y,100,100,4) #Metal(p)_pad

    
for o in range(12):
  for p in range(6):
    x_1 = p*630+ 375
    y_1 = -o*320+1150+395
    if (o == 0):
      RA_10(x_1,y_1)
    if (o == 1):
      RA_20(x_1,y_1)
    if (o == 2):
      RA_40(x_1,y_1)
    if (o == 3):
      RA_60(x_1,y_1)
    if (o == 4):
      RA_80(x_1,y_1)
    if (o == 5):
      RA_100(x_1,y_1)
    if (o == 6):
      RB_10(x_1,y_1)
    if (o == 7):
      RB_20(x_1,y_1)
    if (o == 8):
      RB_40(x_1,y_1)
    if (o == 9):
      RB_60(x_1,y_1)
    if (o == 10):
      RB_80(x_1,y_1)
    if (o == 11):
      RB_100(x_1,y_1)
      
def TLM_p_process(x,y,w,h,interval_1,interval_2,interval_3, interval_4, interval_5):
  global Box_create, layout, top
      
  Box_create(x,y,(w)*6 + interval_1 + interval_2 + interval_3 + interval_4 + interval_5+20, h+60,32) #ISO 공정 
  Box_create(x+5,y+5,(w)*6 + interval_1 + interval_2 + interval_3 + interval_4 + interval_5+10,h+50,2) # ITO
  Box_create(x-5,y-5,(w)*6 + interval_1 + interval_2 + interval_3 + interval_4 + interval_5+20+10,h+70,1) #mesa(etching)
  Box_create(x+10,y+30,80,100,4) #n-metal_1
  Box_create(x+w+interval_1+10,y+30,80,100,4)#n-metal_2
  Box_create(x+2*w+interval_1+interval_2+10,y+30,80,100,4)#n-metal_3 
  Box_create(x+3*w+interval_1+interval_2+interval_3+10,y+30,80,100,4)#n-metal_4
  Box_create(x+4*w+interval_1+interval_2+interval_3+interval_4+10,y+30,80,100,4)#n-metal_5
  Box_create(x+5*w+interval_1+interval_2+interval_3+interval_4+interval_5+10,y+30,80,100,4)#n-metal_6
  
  Box_create(x+15,y+35,70,90,3) #SiO2
  Box_create(x+w+interval_1+15,y+35,70,90,3)
  Box_create(x+2*w+interval_1+interval_2+15,y+35,70,90,3) 
  Box_create(x+3*w+interval_1+interval_2+interval_3+15,y+35,70,90,3)
  Box_create(x+4*w+interval_1+interval_2+interval_3+interval_4+15,y+35,70,90,3)
  Box_create(x+5*w+interval_1+interval_2+interval_3+interval_4+interval_5+15,y+35,70,90,3)
      
      
def TLM_n_process(x,y,w,h,interval_1,interval_2,interval_3, interval_4, interval_5):
  global Box_create, layout, top
   
  Box_create(x,y,(w)*6 + interval_1 + interval_2 + interval_3 + interval_4 + interval_5+20, h+60,32) #ISO 공정 
  Box_create(x+10,y+30,80,100,4) #n-metal_1
  Box_create(x+w+interval_1+10,y+30,80,100,4)#n-metal_2
  Box_create(x+2*w+interval_1+interval_2+10,y+30,80,100,4)#n-metal_3 
  Box_create(x+3*w+interval_1+interval_2+interval_3+10,y+30,80,100,4)#n-metal_4
  Box_create(x+4*w+interval_1+interval_2+interval_3+interval_4+10,y+30,80,100,4)#n-metal_5
  Box_create(x+5*w+interval_1+interval_2+interval_3+interval_4+interval_5+10,y+30,80,100,4)#n-metal_6
  
  Box_create(x+15,y+35,70,90,3) #SiO2
  Box_create(x+w+interval_1+15,y+35,70,90,3)
  Box_create(x+2*w+interval_1+interval_2+15,y+35,70,90,3) 
  Box_create(x+3*w+interval_1+interval_2+interval_3+15,y+35,70,90,3)
  Box_create(x+4*w+interval_1+interval_2+interval_3+interval_4+15,y+35,70,90,3)
  Box_create(x+5*w+interval_1+interval_2+interval_3+interval_4+interval_5+15,y+35,70,90,3)    

      
for i in range(4):
  z_3,z_4 = 3930-687-40,-410+3500-i*410
  
  #2/2
  TLM_p_process(45+1343+20-46,z_4,80,100,2,5,10,20,50)
  TLM_n_process(45+1927+1333+19-14,z_4,80,100,2,5,10,20,50)

  CTLM_p(45-41,4000-500-280-130-i*410)
  CTLM_n(45+1927+20-30,4000-500-280-130-i*410)

for i in range(4):
  z_3,z_4 = 15-687,-410+3500-i*410
  
  #1/2
  TLM_p_process(-3916+14+1330+18+10,z_4,80,100,2,5,10,20,50)
  TLM_n_process(-3916+14+1330+18+597+18+1320+18+5,z_4,80,100,2,5,10,20,50)

  CTLM_p(-3916+14,4000-500-280-130-i*410)
  CTLM_n(-3916+14+1330+18+10+597+18-15,4000-500-280-130-i*410)
    
Align_key(-4000+300,4000-450)
Align_key(+4000-1500,4000-450)
Align_key(-4000+300,-4000+50)
Align_key(+4000-1500,-4000+50)


Line_space(-1410,4000-450)
Line_space(-1410,-4000+50)


  #병렬 연결 Micro LED 
def circle_3(x_1,y_1):
    x = x_1
    y = y_1
      
    a= Box_create(x-50,y,100,200,4)
    b= Box_create(100+x,y,200,200,32)
    c=Box_create(300+x+50,y,100,200,4)
    
    def circle_position(a,b):
        x_1 = 150+a+x
        y_1 = -100+b+y
        Box_create(130+100+a+x,-105+200+b+y,120-a,10,4)
        Box_create(20+100+x,-100-2.5+200+b+y,80+a,5,4)
        Box_create(100+a+100+x,-100-1+200+b+y,10,2,4)
        Box_create(-50+100+x,-105+200+b+y,70,10,4)
        
    
        Poly_donut(+50+x_1+10,200+y_1,5,0,360,0,1)  #mesa
        Unit_circle(+50+x_1+10,200+y_1,25,15,300,30+180,4)
        Poly_donut(+50+x_1+10,200+y_1,1,0,180,270,4)
        Poly_donut(+50+x_1+10,200+y_1,3,0,360,0,2)  #ITO
        Poly_donut(50+x_1+10,200+y_1,2,0,360,0,3)  #SiO2
        Unit_circle(50+x_1+10,200+y_1,23,17,292,34+180,3)   #SiO2
        Poly_donut(+50+x_1+10,+200+y_1,2.5,0,360,0,4) #metal
    
    d=circle_position(0,0)
    e=circle_position(-50,50)
    f=circle_position(50,-50)
    
    
    return a,b,c,d,e,f
    

def circle_5(x_1,y_1):
    x = x_1
    y = y_1
      
    a= Box_create(x-50,y,100,300,4)
    b= Box_create(100+x,y,300,300,32)
    c=Box_create(400+x+50,y,100,300,4)
    
    def circle_position(a,b):
        x_1 = 150+a+x
        y_1 = -100+b+y
        Box_create(170+100+a+x,-105+250+b+y,180-a,10,4)
        Box_create(20+100+x,-100-2.5+250+b+y,120+a,5,4)
        Box_create(140+a+100+x,-100-1+250+b+y,10,2,4)
        Box_create(-50+100+x,-105+250+b+y,70,10,4)
        
    
        
        Poly_donut(+100+x_1,250+y_1,5,0,360,0,1)  #mesa
        Unit_circle(+100+x_1,250+y_1,25,15,300,30+180,4)
        Poly_donut(+100+x_1,250+y_1,1,0,180,270,4)
        Poly_donut(+100+x_1,250+y_1,3,0,360,0,2)  #ITO
        Poly_donut(100+x_1,250+y_1,2,0,360,0,3)  #SiO2
        Unit_circle(100+x_1,250+y_1,23,17,292,34+180,3)   #SiO2
        Poly_donut(+100+x_1,+250+y_1,2.5,0,360,0,4) #metal
    d=circle_position(0,0)
    e=circle_position(-50,50)
    f=circle_position(50,-50)
    g=circle_position(-100,100)
    h=circle_position(100,-100)
    
    return a,b,c,d,e,f,g,h

 

def circle_10(x_1,y_1):
    x = x_1
    y = y_1
      
    a= Box_create(x-200,y-150,100,600,4)
    b= Box_create(-50+x,y-150,600,600,32)
    c=Box_create(550+x+50,y-150,100,600,4)
    
    def circle_position(a,b):
        x_1 = 150+a+x
        y_1 = -100+b+y
        Box_create(170+100+a+x,-105+250+b+y,180-a+150,10,4)
        Box_create(20-50+x,-100-2.5+250+b+y,120+a+150,5,4)
        Box_create(140+a+100+x,-100-1+250+b+y,10,2,4)
        Box_create(-50+100-150+x,-105+250+b+y,70,10,4)
        
    
        Poly_donut(+100+x_1,250+y_1,5,0,360,0,1)  #mesa
        Unit_circle(+100+x_1,250+y_1,25,15,300,30+180,4)
        Poly_donut(+100+x_1,250+y_1,1,0,180,270,4)
        Poly_donut(+100+x_1,250+y_1,3,0,360,0,2)  #ITO
        Poly_donut(100+x_1,250+y_1,2,0,360,0,3)  #SiO2
        Unit_circle(100+x_1,250+y_1,23,17,292,34+180,3)   #SiO2
        Poly_donut(+100+x_1,+250+y_1,2.5,0,360,0,4) #metal
    
    d=circle_position(-25,25)
    e=circle_position(-75,75)
    f=circle_position(-125,125)
    g=circle_position(-175,175)
    h=circle_position(-225,225)
    i=circle_position(25,-25)
    j=circle_position(125,-125)
    k=circle_position(75,-75)
    l=circle_position(175,-175)
    m=circle_position(225,-225)
    
    return a,b,c,d,e,f,g,h

def circle_3_20(x_1,y_1):
    x = x_1
    y = y_1
      
    a= Box_create(x-50,y,100,200,4)
    b= Box_create(100+x,y,200,200,32)
    c=Box_create(300+x+50,y,100,200,4)
    
    def circle_position(a,b):
        x_1 = 150+a+x
        y_1 = -100+b+y
        r=10
        Box_create(130+100+a+x,-105+200+b+y,120-a,10,4)
        Box_create(20+100+x,-100-2.5+200+b+y,80+a,5,4)
        Box_create(100+a+100+x,-100-1+200+b+y,10,2,4)
        Box_create(-50+100+x,-105+200+b+y,70,10,4)
        
    
        Poly_donut(+50+x_1+10,200+y_1,10,0,360,0,1)  #mesa
        Unit_circle(+50+x_1+10,200+y_1,30,20,300,30+180,4)
        Poly_donut(+50+x_1+10,200+y_1,2.5,0,180,270,4)
        Poly_donut(+50+x_1+10,200+y_1,r-3,0,360,0,2)  #ITO
        Poly_donut(50+x_1+10,200+y_1,(r-3)/2,0,360,0,3)  #SiO2
        Unit_circle(50+x_1+10,200+y_1,28,22,292,34+180,3)   #SiO2
        Poly_donut(+50+x_1+10,+200+y_1,(r-3)/2+2,0,360,0,4) #metal
    
    d=circle_position(0,0)
    e=circle_position(-50,50)
    f=circle_position(50,-50)
    
    
    return a,b,c,d,e,f



def circle_5_20(x_1,y_1):
    x = x_1
    y = y_1
      
    a= Box_create(x-50,y,100,300,4)
    b= Box_create(100+x,y,300,300,32)
    c=Box_create(400+x+50,y,100,300,4)
    
    def circle_position(a,b):
        x_1 = 150+a+x
        y_1 = -100+b+y
        r=10
        Box_create(170+100+a+x,-105+250+b+y,180-a,10,4)
        Box_create(20+100+x,-100-2.5+250+b+y,120+a,5,4)
        Box_create(140+a+100+x,-100-1+250+b+y,10,2,4)
        Box_create(-50+100+x,-105+250+b+y,70,10,4)
        
    
        
        Poly_donut(+100+x_1,250+y_1,10,0,360,0,1)  #mesa
        Unit_circle(+100+x_1,250+y_1,30,20,300,30+180,4)
        Poly_donut(+100+x_1,250+y_1,2.5,0,180,270,4)
        Poly_donut(+100+x_1,250+y_1,r-3,0,360,0,2)  #ITO
        Poly_donut(100+x_1,250+y_1,(r-3)/2,0,360,0,3)  #SiO2
        Unit_circle(100+x_1,250+y_1,28,22,292,34+180,3)   #SiO2
        Poly_donut(+100+x_1,+250+y_1,(r-3)/2+2,0,360,0,4) #metal
    
    
  
    d=circle_position(0,0)
    e=circle_position(-50,50)
    f=circle_position(50,-50)
    g=circle_position(-100,100)
    h=circle_position(100,-100)
    
    return a,b,c,d,e,f,g,h

def circle_10_20(x_1,y_1):
    x = x_1
    y = y_1
      
    a= Box_create(x-200,y-150,100,600,4)
    b= Box_create(-50+x,y-150,600,600,32)
    c=Box_create(550+x+50,y-150,100,600,4)
    
    def circle_position(a,b):
        x_1 = 150+a+x
        y_1 = -100+b+y
        r=10
        Box_create(170+100+a+x,-105+250+b+y,180-a+150,10,4)
        Box_create(20-50+x,-100-2.5+250+b+y,120+a+150+10,5,4)
        Box_create(-50+100-150+x,-105+250+b+y,70,10,4)
        
    
        Poly_donut(+100+x_1,250+y_1,10,0,360,0,1)  #mesa
        Unit_circle(+100+x_1,250+y_1,30,20,300,30+180,4)
        Poly_donut(+100+x_1,250+y_1,2.5,0,180,270,4)
        Poly_donut(+100+x_1,250+y_1,r-3,0,360,0,2)  #ITO
        Poly_donut(100+x_1,250+y_1,(r-3)/2,0,360,0,3)  #SiO2
        Unit_circle(100+x_1,250+y_1,28,22,292,34+180,3)   #SiO2
        Poly_donut(+100+x_1,+250+y_1,(r-3)/2+2,0,360,0,4) #metal
    
    d=circle_position(-25,25)
    e=circle_position(-75,75)
    f=circle_position(-125,125)
    g=circle_position(-175,175)
    h=circle_position(-225,225)
    i=circle_position(25,-25)
    j=circle_position(125,-125)
    k=circle_position(75,-75)
    l=circle_position(175,-175)
    m=circle_position(225,-225)
    
    return a,b,c,d,e,f,g,h  
  
def circles_layout(x_2,y_2):
    circle_5(822+x_2,-2570+y_2)
    circle_10(3077+x_2,-2570+y_2)
    circle_3(187+x_2,-2520+y_2)
    circle_5_20(2192+x_2,-2570+y_2)
    circle_3_20(1557+x_2,-2520+y_2)
    
def circles_layout2(x_3,y_3):
    circle_5(822+x_3,-2570+y_3)
    circle_10_20(3077+x_3,-2570+y_3)
    circle_3(187+x_3,-2520+y_3)
    circle_5_20(2192+x_3,-2570+y_3)
    circle_3_20(1557+x_3,-2520+y_3)

circles_layout(0,0)
circles_layout2(0,-649)

   #name
def name_M(x, y, width1,f):
  global layout
  Layout = layout.layer(f,0)
  x, y = x / unit, y / unit
  width1 = width1 / unit
  height1 = width1
  
  points = [0,0,0,0]
  points[0] = pya.Point(round(x - width1/2.0), round(y - height1/2.0))
  points[1] = pya.Point(round(x + width1/2.0), round(y - height1/2.0))
  points[2] = pya.Point(round(x + width1/2.0), round(y + height1/2.0))
  points[3] = pya.Point(round(x - width1/2.0), round(y + height1/2.0))
  
  
  points_1= [0,0,0,0]
  points_1[0] = pya.Point(round(x - (width1/10.0)*3), round(y + height1/4.0))
  points_1[1] = pya.Point(round(x - (width1/10.0)), round(y+ height1/4.0))
  points_1[2] = pya.Point(round(x - (width1/10.0)), round(y - height1/2.0))
  points_1[3] = pya.Point(round(x - (width1/10.0)*3), round(y - height1/2.0))
  
  points_2= [0,0,0,0]
  points_2[0] = pya.Point(round(x + (width1/10.0)*3), round(y + height1/4.0))
  points_2[1] = pya.Point(round(x + (width1/10.0)), round(y + height1/4.0))
  points_2[2] = pya.Point(round(x + (width1/10.0)), round(y - height1/2.0))
  points_2[3] = pya.Point(round(x + (width1/10.0)*3), round(y - height1/2.0))
  
  obj = pya.Polygon(points)
  obj.insert_hole(points_1)
  obj.insert_hole(points_2)
  M = top.shapes(Layout).insert(obj)
  return M
  
def name_O(x, y, width1,f):
  global layout
  Layout = layout.layer(f,0)
  x, y = x / unit, y / unit
  width1 = width1 / unit
  height1 = width1
  
  points = [0,0,0,0]
  points[0] = pya.Point(round(x - width1/2.0), round(y - height1/2.0))
  points[1] = pya.Point(round(x + width1/2.0), round(y - height1/2.0))
  points[2] = pya.Point(round(x + width1/2.0), round(y + height1/2.0))
  points[3] = pya.Point(round(x - width1/2.0), round(y + height1/2.0))
  
  
  points_1= [0,0,0,0]
  points_1[0] = pya.Point(round(x - width1/4.0), round(y + height1/4.0))
  points_1[1] = pya.Point(round(x + width1/4.0), round(y + height1/4.0))
  points_1[2] = pya.Point(round(x + width1/4.0), round(y - height1/4.0))
  points_1[3] = pya.Point(round(x - width1/4.0), round(y - height1/4.0))
  
  points_2= [0,0,0]
  points_2[0] = pya.Point(round(x + width1/4.0), round(y + height1/2.0))
  points_2[1] = pya.Point(round(x + width1/2.0), round(y + height1/2.0))
  points_2[2] = pya.Point(round(x + width1/2.0), round(y + height1/4.0))
  
  points_3= [0,0,0]
  points_3[0] = pya.Point(round(x + width1/2.0), round(y - height1/4.0))
  points_3[1] = pya.Point(round(x + width1/2.0), round(y - height1/2.0))
  points_3[2] = pya.Point(round(x + width1/4.0), round(y - height1/2.0))
  
  points_4= [0,0,0]
  points_4[0] = pya.Point(round(x - width1/4.0), round(y + height1/2.0))
  points_4[1] = pya.Point(round(x - width1/2.0), round(y + height1/2.0))
  points_4[2] = pya.Point(round(x - width1/2.0), round(y + height1/4.0))
  
  points_5= [0,0,0]
  points_5[0] = pya.Point(round(x - width1/2.0), round(y - height1/4.0))
  points_5[1] = pya.Point(round(x - width1/2.0), round(y - height1/2.0))
  points_5[2] = pya.Point(round(x - width1/4.0), round(y - height1/2.0))
  
  obj = pya.Polygon(points)
  obj.insert_hole(points_1)
  obj.insert_hole(points_2)
  obj.insert_hole(points_3)
  obj.insert_hole(points_4)
  obj.insert_hole(points_5)
  
  O = top.shapes(Layout).insert(obj)
  return O
  
def name_E(x, y, width1,f):
  global layout
  Layout = layout.layer(f,0)
  x, y = x / unit, y / unit
  width1 = width1 / unit
  height1 = width1
  
  points = [0,0,0,0]
  points[0] = pya.Point(round(x - width1/2.0), round(y - height1/2.0))
  points[1] = pya.Point(round(x + width1/2.0), round(y - height1/2.0))
  points[2] = pya.Point(round(x + width1/2.0), round(y + height1/2.0))
  points[3] = pya.Point(round(x - width1/2.0), round(y + height1/2.0))
  
  
  points_1= [0,0,0,0]
  points_1[0] = pya.Point(round(x - width1/4.0), round(y + (height1/10.0)*3))
  points_1[1] = pya.Point(round(x + width1/2.0), round(y + (height1/10.0)*3))
  points_1[2] = pya.Point(round(x + width1/2.0), round(y + height1/10.0))
  points_1[3] = pya.Point(round(x- width1/4.0), round(y + height1/10.0))
  
  points_2= [0,0,0,0]
  points_2[0] = pya.Point(round(x- width1/4.0), round(y - (height1/10.0)))
  points_2[1] = pya.Point(round(x + width1/2.0), round(y - (height1/10.0)))
  points_2[2] = pya.Point(round(x + width1/2.0), round(y - (height1/10.0)*3))
  points_2[3] = pya.Point(round(x- width1/4.0), round(y -(height1/10.0)*3))
  
  obj = pya.Polygon(points)
  obj.insert_hole(points_1)
  obj.insert_hole(points_2)
  E = top.shapes(Layout).insert(obj)
  return E


def name_A(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + 2.5*s/10), round(y))
    points1[2] = pya.Point(round(x +4*s/10), round(y + 4*s/10))
    points1[3] = pya.Point(round(x + 6*s/10), round(y + 4*s/10))
    points1[4] = pya.Point(round(x +7.5*s/10), round(y))
    points1[5] = pya.Point(round(x + s), round(y))
    points1[6] = pya.Point(round(x + 6*s/10), round(y + s))
    points1[7] = pya.Point(round(x + 4*s/10), round(y + s))
    
    
    points = [0,0,0,0]
    points[0] = pya.Point(round(x + 4.4*s/10), round(y + 6*s/10))
    points[1] = pya.Point(round(x + 5.7*s/10), round(y + 6*s/10))
    points[2] = pya.Point(round(x + 5.4*s/10), round(y + 7*s/10))
    points[3] = pya.Point(round(x + 4.7*s/10), round(y + 7*s/10))
    
    
    obj = pya.Polygon(points1)
    obj.insert_hole(points)
    align_box = top.shapes(Layout).insert(obj)

    return align_box

def name_L(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + 4*s/5), round(y))
    points1[2] = pya.Point(round(x + 4*s/5), round(y + s/5))
    points1[3] = pya.Point(round(x + 1*s/5), round(y + s/5))
    points1[4] = pya.Point(round(x + 1*s/5), round(y + s))
    points1[5] = pya.Point(round(x), round(y + s))

    
    obj = pya.Polygon(points1)
    align_box = top.shapes(Layout).insert(obj)

    return align_box


def name_T(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y + s))
    points1[1] = pya.Point(round(x), round(y + 4*s/5))
    points1[2] = pya.Point(round(x + 2*s/5), round(y + 4*s/5))
    points1[3] = pya.Point(round(x + 2*s/5), round(y))
    points1[4] = pya.Point(round(x + 3*s/5), round(y))
    points1[5] = pya.Point(round(x + 3*s/5), round(y + 4*s/5))
    points1[6] = pya.Point(round(x + s), round(y + 4*s/5))
    points1[7] = pya.Point(round(x + s), round(y + s))


    
    obj = pya.Polygon(points1)
    align_box = top.shapes(Layout).insert(obj)

    return align_box
    
def name_I(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + s), round(y))
    points1[2] = pya.Point(round(x + s), round(y + s/5))
    points1[3] = pya.Point(round(x + 3*s/5), round(y + s/5))
    points1[4] = pya.Point(round(x + 3*s/5), round(y + 4*s/5))
    points1[5] = pya.Point(round(x + s), round(y + 4*s/5))
    points1[6] = pya.Point(round(x + s), round(y + s))
    points1[7] = pya.Point(round(x), round(y + s))
    points1[8] = pya.Point(round(x), round(y + 4*s/5))
    points1[9] = pya.Point(round(x + 2*s/5), round(y + 4*s/5))
    points1[10] = pya.Point(round(x + 2*s/5), round(y + s/5))
    points1[11] = pya.Point(round(x), round(y + s/5))


    
    obj = pya.Polygon(points1)
    align_box = top.shapes(Layout).insert(obj)

    return align_box


def name_S(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + s), round(y))
    points1[2] = pya.Point(round(x + s), round(y + 3*s/5))
    points1[3] = pya.Point(round(x + s/5), round(y + 3*s/5))
    points1[4] = pya.Point(round(x + s/5), round(y + 4*s/5))
    points1[5] = pya.Point(round(x + 4*s/5), round(y + 4*s/5))
    points1[6] = pya.Point(round(x + 4*s/5), round(y + 7*s/10))
    points1[7] = pya.Point(round(x + s), round(y + 7*s/10))
    points1[8] = pya.Point(round(x + s), round(y + s))
    points1[9] = pya.Point(round(x), round(y + s))
    points1[10] = pya.Point(round(x), round(y + 2*s/5))
    points1[11] = pya.Point(round(x + 4*s/5), round(y + 2*s/5))
    points1[12] = pya.Point(round(x + 4*s/5), round(y + s/5))
    points1[13] = pya.Point(round(x), round(y + s/5))


    
    obj = pya.Polygon(points1)
    align_box = top.shapes(Layout).insert(obj)

    return align_box  

    
def name_2(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + s), round(y))
    points1[2] = pya.Point(round(x + s), round(y + s/5))
    points1[3] = pya.Point(round(x + s/5), round(y + s/5))
    points1[4] = pya.Point(round(x + s/5), round(y + 2*s/5))
    points1[5] = pya.Point(round(x + s), round(y + 2*s/5))
    points1[6] = pya.Point(round(x + s), round(y + s))
    points1[7] = pya.Point(round(x), round(y + s))
    points1[8] = pya.Point(round(x), round(y + 4*s/5))
    points1[9] = pya.Point(round(x + 4*s/5), round(y + 4*s/5))
    points1[10] = pya.Point(round(x + 4*s/5), round(y + 3*s/5))
    points1[11] = pya.Point(round(x), round(y + 3*s/5))

    
    obj = pya.Polygon(points1)
    align_box = top.shapes(Layout).insert(obj)

    return align_box
  
def name_B(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + 2*s/5), round(y))
    points1[2] = pya.Point(round(x + 3*s/5), round(y + s/6))
    points1[3] = pya.Point(round(x + 3*s/5), round(y + 2*s/6))
    points1[4] = pya.Point(round(x + 2*s/5), round(y + 1*s/2))
    
    points1[5] = pya.Point(round(x + 3*s/5), round(y + 4*s/6))
    points1[6] = pya.Point(round(x + 3*s/5), round(y + 5*s/6))
    points1[7] = pya.Point(round(x +2*s/5), round(y + s))
    points1[8] = pya.Point(round(x), round(y + s))
    points1[9] = pya.Point(round(x), round(y + s/2))
    

    
    points = [0,0,0,0]
    points[0] = pya.Point(round(x + 1.5*s/10), round(y + s/6))
    points[1] = pya.Point(round(x + 3.5*s/10), round(y + s/6))
    points[2] = pya.Point(round(x + 3.5*s/10), round(y + 2*s/6))
    points[3] = pya.Point(round(x + 1.5*s/10), round(y + 2*s/6))
    
    points2 = [0,0,0,0]
    points2[0] = pya.Point(round(x + 1.5*s/10), round(y + 4*s/6))
    points2[1] = pya.Point(round(x + 3.5*s/10), round(y + 4*s/6))
    points2[2] = pya.Point(round(x + 3.5*s/10), round(y + 5*s/6))
    points2[3] = pya.Point(round(x + 1.5*s/10), round(y + 5*s/6))
    
    points3 = [0,0,0,0]
    points3[0] = pya.Point(round(x), round(y + 499*s/1000))
    points3[1] = pya.Point(round(x + 2*s/5), round(y + 499*s/1000))
    points3[2] = pya.Point(round(x + 2*s/5), round(y + 501*s/1000))
    points3[3] = pya.Point(round(x), round(y + 501*s/1000))
    
    obj = pya.Polygon(points1)
    obj.insert_hole(points)
    obj.insert_hole(points2)
    obj.insert_hole(points3)
    align_box = top.shapes(Layout).insert(obj) 

    
def name_N(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + s/5), round(y))
    points1[2] = pya.Point(round(x + s/5), round(y + 4*s/5))
    points1[3] = pya.Point(round(x + 3.7*s/5), round(y))
    points1[4] = pya.Point(round(x + s), round(y))
    points1[5] = pya.Point(round(x + s), round(y + s))
    points1[6] = pya.Point(round(x + 4*s/5), round(y + s))
    points1[7] = pya.Point(round(x + 4*s/5), round(y + s/5))
    points1[8] = pya.Point(round(x + 1.3*s/5), round(y + s))
    points1[9] = pya.Point(round(x), round(y + s))
   
    
    obj = pya.Polygon(points1)
    align_box = top.shapes(Layout).insert(obj)

    return align_box

def name_C(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + s), round(y))
    points1[2] = pya.Point(round(x+s), round(y+s))
    points1[3] = pya.Point(round(x), round(y+s))
   
    
    points = [0,0,0,0]
    points[0] = pya.Point(round(x + 1*s/5), round(y + 1*s/5))
    points[1] = pya.Point(round(x+s), round(y+1*s/5))
    points[2] = pya.Point(round(x+s), round(y+4*s/5))
    points[3] = pya.Point(round(x + 1*s/5), round(y + 4*s/5))
    
    
    obj = pya.Polygon(points1)
    obj.insert_hole(points)
    align_box = top.shapes(Layout).insert(obj)

def name_R(x,y,s,f):
    global layout, top
    Layout = layout.layer(f,0)
    x,y,s = x / unit, y /unit, s / unit
    
    points1 = [0,0,0,0,0,0,0,0,0]
    points1[0] = pya.Point(round(x), round(y))
    points1[1] = pya.Point(round(x + s/5), round(y))
    points1[2] = pya.Point(round(x + s/5), round(y + s/2))
    points1[3] = pya.Point(round(x + 3*s/5), round(y))
    points1[4] = pya.Point(round(x + 4.5*s/5), round(y))
    points1[5] = pya.Point(round(x + 2.5*s/5), round(y + s/2))
    points1[6] = pya.Point(round(x + 4*s/5), round(y + s/2))
    points1[7] = pya.Point(round(x + 4*s/5), round(y + s))
    points1[8] = pya.Point(round(x), round(y + s))
   
    
    points = [0,0,0,0]
    points[0] = pya.Point(round(x + 2*s/10), round(y + 4*s/6))
    points[1] = pya.Point(round(x + 6*s/10), round(y + 4*s/6))
    points[2] = pya.Point(round(x + 6*s/10), round(y + 5*s/6))
    points[3] = pya.Point(round(x + 2*s/10), round(y + 5*s/6))
    
    
    obj = pya.Polygon(points1)
    obj.insert_hole(points)
    align_box = top.shapes(Layout).insert(obj)
    
def name_D(x, y, width1, f):
  global layout
  Layout = layout.layer(f,0)
  x, y = x / unit, y / unit
  width1 = width1 / unit
  height1 = width1
  
  points = [0,0,0,0]
  points[0] = pya.Point(round(x - width1/2.0), round(y - height1/2.0))
  points[1] = pya.Point(round(x + width1/2.0), round(y - height1/2.0))
  points[2] = pya.Point(round(x + width1/2.0), round(y + height1/2.0))
  points[3] = pya.Point(round(x - width1/2.0), round(y + height1/2.0))
  
  
  points_1= [0,0,0,0]
  points_1[0] = pya.Point(round(x - width1/4.0), round(y + height1/4.0))
  points_1[1] = pya.Point(round(x + width1/4.0), round(y + height1/4.0))
  points_1[2] = pya.Point(round(x + width1/4.0), round(y - height1/4.0))
  points_1[3] = pya.Point(round(x - width1/4.0), round(y - height1/4.0))
  
  points_2= [0,0,0]
  points_2[0] = pya.Point(round(x + width1/4.0), round(y + height1/2.0))
  points_2[1] = pya.Point(round(x + width1/2.0), round(y + height1/2.0))
  points_2[2] = pya.Point(round(x + width1/2.0), round(y + height1/4.0))
  
  points_3= [0,0,0]
  points_3[0] = pya.Point(round(x + width1/2.0), round(y - height1/4.0))
  points_3[1] = pya.Point(round(x + width1/2.0), round(y - height1/2.0))
  points_3[2] = pya.Point(round(x + width1/4.0), round(y - height1/2.0))
  
  obj = pya.Polygon(points)
  obj.insert_hole(points_1)
  obj.insert_hole(points_2)
  obj.insert_hole(points_3)
  
  D = top.shapes(Layout).insert(obj)
  return D

  #mLED
def mLED_A(x,y,t):    
    name_M(12.5+x,12.5+y,t/2,4)
    name_L(35+x,0+y,t,4)
    name_E(110+x,25+y,t,4)
    name_D(170+x,25+y,t,4)
    Box_create(205+x,20+y,20,10,4)
    name_A(235+x,0+y,t,4)
    

def mLED_B(x,y,t):    
    name_M(12.5+x,12.5+y,t/2,4)
    name_L(35+x,0+y,t,4)
    name_E(110+x,25+y,t,4)
    name_D(170+x,25+y,t,4)
    Box_create(205+x,20+y,20,10,4)
    name_B(235+x,0+y,t,4)

def mLED_C(x,y,t):    
    name_M(12.5+x,12.5+y,t/2,4)
    name_L(35+x,0+y,t,4)
    name_E(110+x,25+y,t,4)
    name_D(170+x,25+y,t,4)
    Box_create(205+x,20+y,20,10,4)
    name_C(235+x,0+y,t,4)

  #number

def number_0(x,y,s,f):
  global layout, top
  Layout = layout.layer(f,0)
  x,y,s = x / unit, y /unit, s / unit       

  points1 = [0,0,0,0]
  points1[0] = pya.Point(round(x), round(y))
  points1[1] = pya.Point(round(x + 2*s/3), round(y))
  points1[2] = pya.Point(round(x+2*s/3), round(y+s))
  points1[3] = pya.Point(round(x), round(y+s))
   
    
  points = [0,0,0,0]
  points[0] = pya.Point(round(x + 1*s/5), round(y + 1*s/5))
  points[1] = pya.Point(round(x+7*s/15), round(y+1*s/5))
  points[2] = pya.Point(round(x+7*s/15), round(y+4*s/5))
  points[3] = pya.Point(round(x + 1*s/5), round(y + 4*s/5))
    
    
  obj = pya.Polygon(points1)
  obj.insert_hole(points)
  align_box = top.shapes(Layout).insert(obj)

def number_4(x,y,s,f):
  global layout, top
  Layout = layout.layer(f,0)
  x,y,s = x / unit, y /unit, s / unit       

  points1 = [0,0,0,0]
  points1[0] = pya.Point(round(x), round(y))
  points1[1] = pya.Point(round(x + 2*s/3), round(y))
  points1[2] = pya.Point(round(x+2*s/3), round(y+s))
  points1[3] = pya.Point(round(x), round(y+s))
   
    
  points2 = [0,0,0,0]
  points2[0] = pya.Point(round(x), round(y))
  points2[1] = pya.Point(round(x+1*s/3), round(y))
  points2[2] = pya.Point(round(x+1*s/3), round(y+2*s/5))
  points2[3] = pya.Point(round(x), round(y + 2*s/5))
  
  points3 = [0,0,0,0]
  points3[0] = pya.Point(round(x+1*s/2), round(y))
  points3[1] = pya.Point(round(x+2*s/3), round(y))
  points3[2] = pya.Point(round(x+2*s/3), round(y+2*s/5))
  points3[3] = pya.Point(round(x+1*s/2), round(y + 2*s/5))

  points4 = [0,0,0,0]
  points4[0] = pya.Point(round(x+1*s/2), round(y+3*s/5))
  points4[1] = pya.Point(round(x+2*s/3), round(y+3*s/5))
  points4[2] = pya.Point(round(x+2*s/3), round(y+s))
  points4[3] = pya.Point(round(x+1*s/2), round(y+s))
  
  points5 = [0,0,0,0]
  points5[0] = pya.Point(round(x+1*s/6), round(y+3*s/5))
  points5[1] = pya.Point(round(x+1*s/3), round(y+3*s/5))
  points5[2] = pya.Point(round(x+1*s/3), round(y+s))
  points5[3] = pya.Point(round(x+1*s/6), round(y+s))  
    
    
  obj = pya.Polygon(points1)
  obj.insert_hole(points2)
  obj.insert_hole(points3)
  obj.insert_hole(points4)
  obj.insert_hole(points5)
  align_box = top.shapes(Layout).insert(obj) 

def number_6(x,y,s,f):
  global layout, top
  Layout = layout.layer(f,0)
  x,y,s = x / unit, y /unit, s / unit       

  points1 = [0,0,0,0]
  points1[0] = pya.Point(round(x), round(y))
  points1[1] = pya.Point(round(x + 2*s/3), round(y))
  points1[2] = pya.Point(round(x+2*s/3), round(y+s))
  points1[3] = pya.Point(round(x), round(y+s))
   
    
  points2 = [0,0,0,0]
  points2[0] = pya.Point(round(x + 1*s/5), round(y + 3*s/5))
  points2[1] = pya.Point(round(x+2*s/3), round(y+3*s/5))
  points2[2] = pya.Point(round(x+2*s/3), round(y+4*s/5))
  points2[3] = pya.Point(round(x + 1*s/5), round(y + 4*s/5))
  
  points3 = [0,0,0,0]
  points3[0] = pya.Point(round(x+1*s/5), round(y+1*s/5))
  points3[1] = pya.Point(round(x+7*s/15), round(y+1*s/5))
  points3[2] = pya.Point(round(x+7*s/15), round(y+2*s/5))
  points3[3] = pya.Point(round(x+1*s/5), round(y + 2*s/5))
    
    
  obj = pya.Polygon(points1)
  obj.insert_hole(points2)
  obj.insert_hole(points3)
  align_box = top.shapes(Layout).insert(obj)      

def number_8(x,y,s,f):
  global layout, top
  Layout = layout.layer(f,0)
  x,y,s = x / unit, y /unit, s / unit       

  points1 = [0,0,0,0]
  points1[0] = pya.Point(round(x), round(y))
  points1[1] = pya.Point(round(x + 2*s/3), round(y))
  points1[2] = pya.Point(round(x+2*s/3), round(y+s))
  points1[3] = pya.Point(round(x), round(y+s))
   
    
  points2 = [0,0,0,0]
  points2[0] = pya.Point(round(x + 1*s/5), round(y + 3*s/5))
  points2[1] = pya.Point(round(x+7*s/15), round(y+3*s/5))
  points2[2] = pya.Point(round(x+7*s/15), round(y+4*s/5))
  points2[3] = pya.Point(round(x + 1*s/5), round(y + 4*s/5))
  
  points3 = [0,0,0,0]
  points3[0] = pya.Point(round(x+1*s/5), round(y+1*s/5))
  points3[1] = pya.Point(round(x+7*s/15), round(y+1*s/5))
  points3[2] = pya.Point(round(x+7*s/15), round(y+2*s/5))
  points3[3] = pya.Point(round(x+1*s/5), round(y + 2*s/5))
    
    
  obj = pya.Polygon(points1)
  obj.insert_hole(points2)
  obj.insert_hole(points3)
  align_box = top.shapes(Layout).insert(obj)
  
  
  #CA - 지름표시
for i in range(6):
  for j in range(6):
    y_1 = -320*j
    ax = [630,630,630,630]
    
    if j == 0:
      x_1 = ax[1]*i
      Box_create(-3577+x_1,1365+y_1,10,50,4)
      number_0(-3557+x_1,1365+y_1,50,4)
    if j == 1:
      x_1 = ax[0]*i
      name_2(-3577+x_1,1365+y_1,50,4)
      number_0(-3517+x_1,1365+y_1,50,4)
    if j == 2:
      x_1 = ax[2]*i
      number_4(-3568+x_1,1365+y_1,50,4)
      number_0(-3525+x_1,1365+y_1,50,4)
    if j == 3:
      x_1 = ax[2]*i
      number_6(-3568+x_1,1365+y_1,50,4)
      number_0(-3525+x_1,1365+y_1,50,4)
    if j == 4:
      x_1 = ax[2]*i
      number_8(-3568+x_1,1365+y_1,50,4)
      number_0(-3525+x_1,1365+y_1,50,4) 
    if j == 5:
      x_1 = ax[3]*i
      Box_create(-3578+x_1,1365+y_1,10,50,4)
      number_0(-3557+x_1,1365+y_1,50,4)
      number_0(-3514+x_1,1365+y_1,50,4)

  #CB - 지름표시
for i in range(6):
  for j in range(6):
    y_1 = -320*j
    ax = [630,630,630,630]
    
    if j == 0:
      x_1 = ax[1]*i
      Box_create(-3577+x_1,-555+y_1,10,50,4)
      number_0(-3557+x_1,-555+y_1,50,4)
    if j == 1:
      x_1 = ax[0]*i
      name_2(-3577+x_1,-555+y_1,50,4)
      number_0(-3517+x_1,-555+y_1,50,4)
    if j == 2:
      x_1 = ax[2]*i
      number_4(-3568+x_1,-555+y_1,50,4)
      number_0(-3525+x_1,-555+y_1,50,4)
    if j == 3:
      x_1 = ax[2]*i
      number_6(-3568+x_1,-555+y_1,50,4)
      number_0(-3525+x_1,-555+y_1,50,4)
    if j == 4:
      x_1 = ax[2]*i
      number_8(-3568+x_1,-555+y_1,50,4)
      number_0(-3525+x_1,-555+y_1,50,4) 
    if j == 5:
      x_1 = ax[3]*i
      Box_create(-3578+x_1,-555+y_1,10,50,4)
      number_0(-3557+x_1,-555+y_1,50,4)
      number_0(-3514+x_1,-555+y_1,50,4)      


  # RA 길이표시
for i in range(6):
  for j in range(6):
    y_1 = -320*j
    ax = [630,630,630,630]
    
    if j == 0:
      x_1 = ax[1]*i
      Box_create(353+x_1,1365+y_1,10,50,4)
      number_0(373+x_1,1365+y_1,50,4)
    if j == 1:
      x_1 = ax[0]*i
      name_2(333+x_1,1365+y_1,50,4)
      number_0(393+x_1,1365+y_1,50,4)
    if j == 2:
      x_1 = ax[2]*i
      number_4(342+x_1,1365+y_1,50,4)
      number_0(385+x_1,1365+y_1,50,4)
    if j == 3:
      x_1 = ax[2]*i
      number_6(342+x_1,1365+y_1,50,4)
      number_0(385+x_1,1365+y_1,50,4)
    if j == 4:
      x_1 = ax[2]*i
      number_8(342+x_1,1365+y_1,50,4)
      number_0(385+x_1,1365+y_1,50,4) 
    if j == 5:
      x_1 = ax[3]*i
      Box_create(332+x_1,1365+y_1,10,50,4)
      number_0(352+x_1,1365+y_1,50,4)
      number_0(395+x_1,1365+y_1,50,4)

  # RB 길이표시
for i in range(6):
  for j in range(6):
    y_1 = -320*j
    ax = [630,630,630,630]
    
    if j == 0:
      x_1 = ax[1]*i
      Box_create(353+x_1,-555+y_1,10,50,4)
      number_0(373+x_1,-555+y_1,50,4)
    if j == 1:
      x_1 = ax[0]*i
      name_2(333+x_1,-555+y_1,50,4)
      number_0(393+x_1,-555+y_1,50,4)
    if j == 2:
      x_1 = ax[2]*i
      number_4(342+x_1,-555+y_1,50,4)
      number_0(385+x_1,-555+y_1,50,4)
    if j == 3:
      x_1 = ax[2]*i
      number_6(342+x_1,-555+y_1,50,4)
      number_0(385+x_1,-555+y_1,50,4)
    if j == 4:
      x_1 = ax[2]*i
      number_8(342+x_1,-555+y_1,50,4)
      number_0(385+x_1,-555+y_1,50,4) 
    if j == 5:
      x_1 = ax[3]*i
      Box_create(332+x_1,-555+y_1+50,10,50,4)
      number_0(352+x_1,-555+y_1+50,50,4)
      number_0(395+x_1,-555+y_1+50,50,4)


  #C부분 지름표시
def mLED_C_number(x,y):
  for i in range(4):
    y_1 = -320*i
    #10
    Box_create(x,y+y_1,10,50,4)
    number_0(20+x,y+y_1,50,4)
    #20
    name_2(610+x,y+y_1,50,4)
    number_0(670+x,y+y_1,50,4)
    #40
    number_4(1248+x,y+y_1,50,4)
    number_0(1291+x,y+y_1,50,4)
    #60
    number_6(1878+x,y+y_1,50,4)
    number_0(1921+x,y+y_1,50,4)
    #80
    number_8(2508+x,y+y_1,50,4)
    number_0(2551+x,y+y_1,50,4)         
    #100
    Box_create(3128+x,y+y_1,10,50,4)
    number_0(3148+x,y+y_1,50,4)
    number_0(3191+x,y+y_1,50,4)    

mLED_C_number(-3577,-2475)


name_I(-1300,-3530,50,32)
name_S(-1230,-3530,50,32)
name_O(-1130,-3505,50,32)


name_M(-700,-3500,50,1)
name_E(-620,-3500,50,1)
name_S(-560,-3524,50,1)
name_A(-480,-3524,50,1)

name_I(-70,-3524,50,2)
name_T(10,-3524,50,2)
name_O(110,-3500,50,2)

name_S(510,-3524,50,3)
name_I(590,-3524,50,3)
name_O(690,-3500,50,3)
name_2(730,-3530,20,3)


name_M(1080,-3500,50,4)
name_E(1150,-3500,50,4)
name_T(1200,-3524,50,4)
name_A(1270,-3524,50,4)
name_L(1350,-3524,50,4)

mLED_A(-3880,1670,50)
mLED_A(50,1670,50)
mLED_B(-3880,-250,50)
mLED_B(50,-250,50)
mLED_C(-3880,-2170,50)
###


name_I(-1300,3470,50,32)
name_S(-1230,3470,50,32)
name_O(-1130,3495,50,32)


name_M(-700,3500,50,1)
name_E(-620,3500,50,1)
name_S(-560,3476,50,1)
name_A(-480,3476,50,1)

name_I(-70,3476,50,2)
name_T(10,3476,50,2)
name_O(110,3500,50,2)

name_S(510,3476,50,3)
name_I(590,3476,50,3)
name_O(690,3500,50,3)
name_2(730,3470,20,3)


name_M(1080,3500,50,4)
name_E(1150,3500,50,4)
name_T(1200,3476,50,4)
name_A(1270,3476,50,4)
name_L(1350,3476,50,4)


### ASDL
name_A(1750,-3800,100,32)
name_S(1870,-3800,100,32)
name_D(2040,-3750,100,32)
name_L(2110,-3800,100,32)


### ANRL
name_A(-2110,-3800,100,32)
name_N(-1990,-3800,100,32)
name_R(-1870,-3800,100,32)
name_L(-1750,-3800,100,32)

Box_create(-3915,-3470,7830,6940,3)

layout.write("C:/Users/dream/KLayout/python/lump_gds/overall.gds")