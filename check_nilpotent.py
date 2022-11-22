def create_matrix():
    dimension = int(input("Please enter matrix dimension: "))
    if dimension == 1:
        print('Matrix of dimension 1 is just a number')
        return -1
    else:
        initial = np.zeros((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                value = int(input(f"Enter the value for [{i}][{j}]: "))
                initial[i][j] = value
        return initial

def check_nilpotent_iterative():
    """ Sam's homemade solution """
    index = 1
    zero_count = 0
    starting = to_check = create_matrix() # setting starting for a static variable for later, to check will change
    dim = to_check.ndim

    # this for loop multiplies the matrix with each iteration
    for i in range(dim):
        result = to_check
        # these nested for loops iterate through the whole matrix
        for j in range(dim):
            for k in range(dim):
                if result[j][k] == 0:
                    zero_count += 1
                    if zero_count == dim * dim:
                        print(f'{starting} is nilpotent at degree {index}')
                        return 1
                    else:
                        zero_count = 0
                        pass
                else:
                    pass
        result = np.matmul(to_check, starting)
        index += 1
        to_check = result
        # end of matrix check, loop back and multiply again
    print(f"{starting} is not nilpotent")
    return -1
    
    if __name__ == '__main__':
    check_nilpotent_iterative()
