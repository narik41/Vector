import math 

class Vector : 

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = coordinates
            self.dimension   = len(self.coordinates)
        except ValueError:
            raise ValueError("The coordinates must be non empty")
        except TypeError:
            raise ValueError("The coordinates must be an iterable")
        
    
    def __str__(self):
        return "Vector: {}".format(self.coordinates)
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        """
            Vector addition is the operation of adding the twor vectors together into a vector sum

            args : 
                v - A vector class 
            return :
                a new vector 
        """
        add_value = [x+y for x,y in zip(self.coordinates, v.coordinates)]

        return Vector(add_value)

    def subtract(self, v):
        """
            Vector subtraction is the operation of subtracting the two vectors together into a verctor 

            args :  
                v- A vector class
            
            return :
                a new vector 
        """
        sub_value = [x-y for x,y in zip(self.coordinates, v.coordinates)]

        return Vector(sub_value)

    def scale(self, k):
        """ 
            Use to scale a vector by a k

            args : 
                k - int 
            return 
                new Vector 
        """
        scale_value = [ k * x for x in (self.coordinates)]

        return Vector(scale_value)

    def magnitude(self):
        """ 
            Magnitude of vector is a length of v from the origin.To find the magnitude of a vector 
            from its components, we take the square root of the sum of the components' squares 

            return :
                float
        """
        return math.sqrt(sum([x**2 for x in self.coordinates ]))

    
    def normalized(self):
        """ 
            Normalization consists of dividing every entry in a vector  by its magnitude to 
            create a vector of length 1 known as the unit vector

            return : 
                new Vector 
        """
        try:
            magnitude = self.magnitude()

            return Vector([x/magnitude for x in self.coordinates])

        except ZeroDivisionError:
            raise Exception("Cannot normalize  the zero vector") 

    def dot(self, v):

        """ 
            Adds the products of corresponding components and it gives a scalar

            args : 
                -v - Vector
            return : 
                float
        """

        return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])

    def angle(self, v, in_degree=False):
        """ 
            Find the angle between the two vectors

            args : 
                v - Vector 
                in_degree - bool 
            
            return  : 
                float 
        """
        u1 = self.normalized()
        u2 = v.normalized()

        k = u1.dot(u2)

        angle_in_radians = math.acos(k)
        if in_degree :
            angle_in_degree = 180/math.pi * angle_in_radians
            return angle_in_degree 
        
        return angle_in_radians

    def is_orthogonal(self, v):
        """
            Check if two vector are orthogonal or not 

            args : 
                v - vector 
            return :
                bool 
        """
        u1 = self.dot(v)

        return (u1 == 0 )

    def is_parallel(self, v):
        pass 

    def orthogonal_to(self, v):
        projection_vector = self.projection(v)

        return self.subtract(projection_vector)

    def projection(self, v):
        """ 
            The vector that v creates in the direction of w 

            args : 
                v - Vector
            return 
                Vector 
        """
        uv = v.normalized()

        dot = self.dot(uv)
       
        return Vector([x*dot for x in uv.coordinates])
