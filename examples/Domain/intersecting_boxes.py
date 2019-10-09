import SVMTK as svm


if __name__ == "__main__":
    
 
   surf1 = svm.Surface()
   surf2 = svm.Surface() 
   surf3 = svm.Surface() 
  
   surf4 = svm.Surface()
   surf4.make_cube(-2,-2,-2,2,2,2)

   surf1.make_cube(-2,-2,-2,0,2,2) 

   surf2.make_cube(0,-2,-2,2,2,2)

   surf3.make_cube(-1,-1,-1,1,1,1)

   maker = svm.Domain([surf1,surf2,surf3])

   maker.add_sharp_border_edges(surf4,90)
   maker.add_sharp_border_edges(surf3,90)
   maker.set_borders()



   maker.create_mesh(64)

   maker.save("boxes.mesh")
