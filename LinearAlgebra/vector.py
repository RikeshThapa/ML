import operator
import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = self.getMagnitude()
            self.direction = self.getDirection()

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    #Not a big fan of method declaration for functions like theres, but just for the sake of example and ultimate flexibility:

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, s):
        new_coordinates = [x*s for x in self.coordinates]
        return Vector(new_coordinates)

    #I could compress this into one line or something. But I'm not an asshole who enjoys having people
    # spend hours trying to understand my code
    def getMagnitude(self):
        square_vector = [x**2 for x in self.coordinates]
        sum_of_squares = sum(square_vector)
        magnitude = math.sqrt(sum_of_squares)
        return magnitude

    def getDirection(self):
        try:
            unit_vector = [(1/self.magnitude)*x for x in self.coordinates]
            return unit_vector
            #return self.times_scalar(1./self.magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot be normalized magnitude of vector is 0")



def plus(v1, v2):
    #v1 is vector 1 and v2 is vector 2, the order does not matter
    resultantVector = tuple(map(operator.add, v1.coordinates, v2.coordinates))
    return resultantVector

def minus(v1, v2):
    #v1 is initial v2 is deduction, order does matter
    differenceVector = tuple(map(operator.sub, v1.coordinates, v2.coordinates))
    return differenceVector

def scalar(s, v):
    #s is multiplier, v is vector
    scalarresult = []
    for i in range(0, v.dimension):
        scalarresult.append(s*v.coordinates[i])
        i+=1
    return tuple(scalarresult)

def getDotProduct(v1, v2):
    # we do not know the angle between the vectors, so we will be using expanded
    # dot product equation
    dot_product_vector = [x*y for x,y in zip(v1.coordinates, v2.coordinates)]
    return sum(dot_product_vector)

def getAngle(v1, v2, d_or_r="r"):
    try:
        dot_product = getDotProduct(v1, v2)
        product_of_magnitudes = v1.magnitude * v2.magnitude
        if d_or_r=="d":
            return math.degrees(math.acos(dot_product/product_of_magnitudes))
        else:
            return math.acos(dot_product/product_of_magnitudes)
    except ZeroDivisionError:
        raise Exception("One of the vector magnitudes is 0, so no angle exists")




'''Test main function'''
if __name__ == '__main__':
    coordinates1 = (7.35, 0.221, 5.188)
    v1 = Vector(coordinates1)

    coordinates2 = (2.751, 8.259, 3.985)
    v2 = Vector(coordinates2)

    print(getAngle(v1, v2, "d"))
    #print(v1.direction)

    '''coordinates2 = (1.671, -1.012, -0.318)
    v2 = Vector(coordinates2)

    print(scalar(7.41, v2))'''


