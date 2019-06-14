# importing numpy for matrix operations
import numpy

transition_matrix = numpy.array([[0.6, 0.4, 0, 0], [0, 0.1, 0.7, 0.2], [0, 0.2, 0.5, 0.3], [0.2, 0.2, 0.1, 0.5]])

zero_state = numpy.array([[0.25, 0.25, 0.25, 0.25]])

print(transition_matrix)

acumulated = zero_state

for iter in range(10):
    for iter_2 in range(iter):
        acumulated = numpy.dot(acumulated,transition_matrix)
    print("-------------------")
    print(acumulated)