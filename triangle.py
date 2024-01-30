#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:13:46 2024

@author: harshakuppala
"""
import unittest
def classify_triangle(a,b,c):
    e=a*a
    f=b*b
    g=c*c
    if (a<b+c and b<c+a and c<a+b):
      if ((e==f+g)or (f==e+g)or (g==e+f)):
          return "right triangle"
      elif (a==b==c):
          return "equilateral triangle"
      elif ((a==b and b!=c) or (b==c and a!=c) or (a==c and a!=b)):
          return "isosceles triangle"
      else :
          return "scalene triangle"
    else:
        return "error! the given sides doesn't make a triangle"
  

          
a=float(input("enter side a "))
b=float(input("enter side b "))
c=float(input("enter side c "))    
x=classify_triangle(a, b, c)
print(x)
class TestTriangleClassification(unittest.TestCase):

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "right triangle")

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(6, 6, 6), "equilateral triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(3, 5, 5), "isosceles triangle")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(5, 4, 6), "scalene triangle")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 5, 8), "error! the given sides doesn't make a triangle")

if __name__ == '__main__':
    unittest.main()

        
