
import unittest

def classifyTriangle(a, b, c):

    if a == b == c:
        return ' Equilateral'
    elif a == b or a == c or b == c:
        return ' Isosceles'
    elif a*a + b*b == c*c:
        return ' Right'
    else:
        return ' Scalene'

def runClassifyTriangle(a, b, c):
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c), sep="")


class TestTriangles(unittest.TestCase):
    def testSet1(self):

        self.assertEqual(classifyTriangle(3, 4, 5), ' Right', "3,4,5 should be Right Triangle")
        self.assertEqual(classifyTriangle(2, 4, 6), ' Scalene', "2,4,6 should be Scalene Triangle")
        self.assertEqual(classifyTriangle(4, 4, 4), ' Equilateral', "4,4,4 should be Equilateral Triangle")
        # self.assertEqual(classifyTriangle(3, 3, 3), ' Scalene', "3,3,3 should  be Equilateral Triangle") # Incorrect
        self.assertEqual(classifyTriangle(5, 8, 5), ' Isosceles', "5,8,5 should be Isosceles Triangle")
        self.assertEqual(classifyTriangle(6, 8, 10), ' Right', "6,8,10 should be Right Triangle")
        self.assertEqual(classifyTriangle(12, 16, 20), ' Right', "12,16,20 should be Right Triangle")
        self.assertEqual(classifyTriangle(12, 8, 10), ' Scalene', "12,8,10 should be Scalene Triangle")
        self.assertEqual(classifyTriangle(12, 24, 3), ' Right', "5,8,5 should be Scalene Triangle")  # Incorrect

    def testSet2(self):

        self.assertEqual(classifyTriangle(1, 1, 1), ' Equilateral', '1,1,1 should be Equilateral')
        self.assertEqual(classifyTriangle(10, 15, 30), ' Scalene', '10,15,30 should be Scalene')
        # self.assertEqual(classifyTriangle(2, 8, 5), ' Right', "2,8,5 should be Scalene Triangle") # Incorrect
        self.assertEqual(classifyTriangle(10, 14, 10), ' Isosceles', "10,14,10 should be Isosceles Triangle")
        self.assertEqual(classifyTriangle(40, 40, 40), ' Equilateral', "40,40,40 should be Equilateral Triangle")
        self.assertEqual(classifyTriangle(10, 10, 10), ' Isosceles', '10,10,10 should be Equilateral')  # Incorrect


if __name__ == '__main__':
    runClassifyTriangle(2, 7, 12)
    runClassifyTriangle(8, 8, 8)
    runClassifyTriangle(4, 4, 6)
    runClassifyTriangle(3, 4, 5)

    unittest.main(exit=False)