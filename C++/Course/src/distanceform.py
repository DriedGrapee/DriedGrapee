import numpy
def distance_form():
    x1 = int(input('x1: \n'))
    y1 = int(input('y1: \n'))
    x2 = int(input('x2: \n'))
    y2 = int(input('y2: \n'))
    step1 = (x1 - x2)**2
    step2 = (y1 - y2)**2
    step3 = step1 + step2
    step4 = numpy.sqrt(step3)
    return step4
print(distance_form())