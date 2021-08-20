<<<<<<< HEAD
# Design_muLED

Design Drawing of Micro LED and Mini LED that consists of 'default cell' and 'test cell'  
* In 'gds' file, 'Cell_Default.gds' and 'Cell_Test.gds' constitute several unit LED chips and 'muled_ver3.0.gds' is made up of aforementioned test cells and default cells. For more informaiton, please check the '210803_미니LED설계_김강석_ver1.2.pptx' in 'doc'


Test Cell             |  Default Cell             |  Wafer_Screen
:-------------------------:|:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/77437180/129997053-f9e654de-1bbc-4ce2-8cb1-46f8e7eea2ab.png)  |  ![](https://user-images.githubusercontent.com/77437180/129997458-826dcd72-1061-4eb5-aa30-8115ce9bccef.png)  |  ![](https://user-images.githubusercontent.com/77437180/129998085-5b37eb1e-f15f-4012-b81a-52f3a0237659.png)
<!-- <br />
<h1>
<p align="Left">
  <img src="https://user-images.githubusercontent.com/77437180/129997053-f9e654de-1bbc-4ce2-8cb1-46f8e7eea2ab.png" alt="Logo" width="400" height="400">
<p align="Center">
  <img src="https://user-images.githubusercontent.com/77437180/129997458-826dcd72-1061-4eb5-aa30-8115ce9bccef.png" alt="Logo" width="400" height="400"> -->


**Installation Options**
---

<h1 align="center">
  <img src="https://user-images.githubusercontent.com/77437180/130005263-54663ac1-e217-4a5e-9df7-0e1fbfc91488.png" width="200" height="200"/><br/>
  KLayout
  </h1>  
  
Overall Design Drawing is made of [`KLayout`](https://www.klayout.de/build.html).  
Download the KLayout Installer files according to your computer specifications. And these Python files are coded based on ['pya'](https://pypi.org/project/pya).  

```
import pya
import math 
```


**Usage**
---

When KLayout is installed, enter to the 'Editor' mode and you can redesign the Drawing using the Klayout tools or coding by the Python and Ruby. Our Design Drawing is made up of the __Python__ and someone who can use the Python is easier to control the Deisgn more accessible

1. If you would like to redesign the gds files, enter the 'Editor' mode and Click the __'File' > 'Open'__ on top of screen bar and load the gds files depending on the route.
2. Through the __'Macros' > 'Macro Development'__, a development enviroment will be shown and move these Python files to the Local 'Python' file.(Check the route of 'Macros' file)
3. In 'Macro Development', redesign the gds files as you want by coding.

**Precautions**
---
* 'Cell_Default.gds' and 'Cell_Test.gds' is made by Python codes while the 'Wafer_screen.gds' is made by KLayout Editor tools, so that you cannot find the python file of 'Wafer_screen.gds' in Macro Development.
* Always check whether the files is saved. And Other Development Environment like 'Pycharm' or 'Visual Studio Code' wouldn't be interconnected

**Contributor**
---
ASDL(Advanced Semiconductor Devices Lab)

   + Professor   
      Younghyun Kim   younghyunkim@hanyang.ac.kr  
      
   + Deisgner    
      Kangseok Kim  ddol410@hanyang.ac.kr   
      SeungMin Park   psm401@hanyang.ac.kr    
      Junsu Song     sb020578@hanyang.ac.kr
=======
# design_muled01
>>>>>>> 7dda7df871672e372b928f51535da1214a02d9d0
