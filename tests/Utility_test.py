import unittest
import SVMTK


class Utility_Test(unittest.TestCase):


    def test_convex_hull(self):
        s1 = SVMTK.convex_hull([1,2,3]) 
        self.assertEqual(surface2.num_vertices(),1)  
        tetra_points = [0, 0, 0, 
                                    0, 0, 1, 
                                    0, 1, 1,
                                    1, 1, 1,  ]
        s2 = SVMTK.convex_hull(tetra_points)   
        self.assertEqual(surface2.num_vertices(),4)

    def test_simple_cgal_wrappers(self):
        p3 = SVMTK.Point_3(1.,0,1.0)
        self.assertEqual(p3.x(),1.0) 
        self.assertEqual(p3.y(),0.0) 
        self.assertEqual(p3.z(),1.0) 
        p2 = SVMTK.Point_2(0,1.)
        self.assertEqual(p2.x(),0)
        self.assertEqual(p2.y(),1.0)  
        pl3 = SVMTK.Plane_3(1,2,3,4) 
        self.assertEqual(pl3.a(),1.0)
        self.assertEqual(pl3.b(),2.0)
        self.assertEqual(pl3.c(),3.0)
        self.assertEqual(pl3.d(),4.0)
           
        v3 =  SVMTK.Vector_3(0,1.0,0.0)
        self.assertEqual(v3.x(),0.0) 
        self.assertEqual(v3.y(),1.0) 
        self.assertEqual(v3.z(),0.0) 

        pl3 = SVMTK.Plane_3(p3,v3)
        self.assertEqual(pl3.a(),0.0)
        self.assertEqual(pl3.b(),1.0)
        self.assertEqual(pl3.c(),0.0)
        self.assertEqual(pl3.d(),0.0)


    def test_seperate_close_surfaces(self):
        s1 =SVMTK.Surface()
        s2 =SVMTK.Surface()  
        s3 =SVMTK.Surface()    
        s1.make_cube(1.,0.,1.,2.,1.,2.,1) 
        s2.make_cube(1.,1,1.,2.,2.,2.,1) 
        
        self.assertTrue(SVMTK.separate_close_surfaces(s1,s2))
       

    def test_seperate_close_surfaces_2(self):
        s1 =SVMTK.Surface()
        s2 =SVMTK.Surface()  
        s3 =SVMTK.Surface()    
        s1.make_cube(1.,0.,1.,2.,1.,2.,5) 
        s2.make_cube(1.,1.,1.,2.,2.,2.,5) 
        s3.make_cube(1.2,0.5,1.2,1.8,1.5,1.8,5) 
        self.assertTrue(SVMTK.separate_overlapping_surfaces(s1,s2,s3))
       

    def test_seperate_overlapping_surfaces(self):
        s1 =SVMTK.Surface()
        s2 =SVMTK.Surface()  
        s3 =SVMTK.Surface()    
        s1.make_cube(1.,0.,1.,2.,1.,2.,1) 
        s2.make_cube(1.,1,1.,2.,2.,2.,1) 
        s3.make_cube(1.2,0.5,1.2,1.8,1.5,1.8,1) 
        s1.union(s3) 
        s1.adjust_boundary(-0.01) 
        s2.adjust_boundary(-0.01) 
        self.assertTrue(SVMTK.separate_overlapping_surfaces(s1,s2))


    def test_sperate_overlapping_surface_2(self):
        s1 =SVMTK.Surface()
        s2 =SVMTK.Surface()  
        s3 =SVMTK.Surface()    
        s1.make_cube(1.,0.,1.,2.,1.,2.,5) 
        s2.make_cube(1.,1.,1.,2.,2.,2.,5) 
        s3.make_cube(1.2,0.5,1.2,1.8,1.5,1.8,5) 
        self.assertTrue(SVMTK.separate_overlapping_surfaces(s1,s2,s3)) 



    def test_morphological_surface_union(self):
        s1 =SVMTK.Surface("tests/Data/s1.off")
        s2 =SVMTK.Surface("tests/Data/s2.off")  
        s5  = SVMTK.union_partially_overlapping_surfaces(s1,s2,0.9,0.2,1)
        self.assertTrue(s5.num_faces()>0) 



if __name__ == '__main__':
    unittest.main()







