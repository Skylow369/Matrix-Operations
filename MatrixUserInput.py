from MatrixClass import Matrix


def solvesys():
    numvars = int(input("# of variables in system: "))
    print("Enter coefficients:")
    coeff = Matrix(None, numvars, numvars)

    print("Enter values/right side of equation:")
    vals = Matrix(None, numvars, 1)

    ans = coeff.inverse() * vals
    ans.printmatrix()
    return


def practice():
    action = input("\nA for Add        S for Subtract"
                   "\nM for Multiply   D for Determinant"
                   "\nI for Inverse"
                   "\nWhat would you like to practice? ").upper()
    difficulty = input("Easy (E), Medium(M), or Hard(H)? ").upper()

# Defaults to medium
    if difficulty == "E":
        difficulty = 2
    elif difficulty == "H":
        difficulty = 4
    else:
        difficulty = 3

    if action == "A":
        print("Add the following matrices:")
        mat1 = []
        mat2 = []

        for row in range(difficulty):
            mat1.append([])
            mat2.append([])
            for column in range(difficulty):
                mat1[row].append(random.randint(1, 9))
                mat2[row].append(random.randint(1, 9))
            print(mat1[row], "  ", mat2[row])
        mat1 = Matrix(mat1)
        mat2 = Matrix(mat2)
        mat3 = mat1 + mat2

        usermat = Matrix(None, difficulty, difficulty)
        if usermat.rows == mat3.rows:
            print("Correct")
        else:
            print("Incorrect")

        print("Answer:")
        mat3.printmatrix()

    if action == "S":
        print("Subtract the following matrices:")
        mat1 = []
        mat2 = []

        for row in range(difficulty):
            mat1.append([])
            mat2.append([])
            for column in range(difficulty):
                mat1[row].append(random.randint(1, 9))
                mat2[row].append(random.randint(1, 9))
            print(mat1[row], "  ", mat2[row])
        mat1 = Matrix(mat1)
        mat2 = Matrix(mat2)
        mat3 = mat1 - mat2

        usermat = Matrix(None, difficulty, difficulty)
        if usermat.rows == mat3.rows:
            print("Correct")
        else:
            print("Incorrect")

        print("Answer:")
        mat3.printmatrix()

    if action == "M":
        print("Multiply the following matrices:")
        mat1 = []
        mat2 = []

        for row in range(difficulty):
            mat1.append([])
            mat2.append([])
            for column in range(difficulty):
                mat1[row].append(random.randint(2, 6))
                mat2[row].append(random.randint(2, 6))
            print(mat1[row], "  ", mat2[row])
        mat1 = Matrix(mat1)
        mat2 = Matrix(mat2)
        mat3 = mat1 * mat2

        usermat = Matrix(None, difficulty, difficulty)
        if usermat.rows == mat3.rows:
            print("Correct")
        else:
            print("Incorrect")

        print("Answer:")
        mat3.printmatrix()

    if action == "D":
        print("Find the determinant of the following matrix:")
        mat1 = []
        for row in range(difficulty):
            mat1.append([])
            for column in range(difficulty):
                mat1[row].append(random.randint(2, 6))
            print(mat1[row])
        mat1 = Matrix(mat1)
        d = mat1.determinant()

        user = int(input("Enter determinant: "))

        if user == d:
            print("Correct")
        else:
            print("Incorrect")

        print("Answer:", d)

    if action == "I":
        print("Find the inverse of the following matrix:")
        mat1 = []
        for row in range(difficulty):
            mat1.append([])
            for column in range(difficulty):
                mat1[row].append(random.randint(2, 6))
            print(mat1[row])
        mat1 = Matrix(mat1)
        mat1 = mat1.inverse()

        usermat = Matrix(None, difficulty, difficulty)
        if usermat.rows == mat1.rows:
            print("Correct")
        else:
            print("Incorrect")

        print("Answer")
        mat1.printmatrix()


def start():
    while True:
        action = input("A for Add           S for Subtract  M for Multiply   SS to Solve System\n"
                       "D for Determinant   I for Inverse   P for Practice   Q to Quit\n"
                       "What would you like to do? ").upper()

        if action == "A":
            print("Matrix 1:")
            mat1 = Matrix()

            print("Matrix 2:")
            mat2 = Matrix()

            if type(mat1 + mat2) == Matrix:
                mat3 = mat1 + mat2
                mat3.printmatrix()

        elif action == "S":
            print("Matrix 1:")
            mat1 = Matrix()

            print("Matrix 2:")
            mat2 = Matrix()

            if type(mat1 - mat2) == Matrix:
                mat3 = mat1 - mat2
                mat3.printmatrix()

        elif action == "M":
            print("Matrix 1:")
            mat1 = Matrix()

            print("Matrix 2:")
            mat2 = Matrix()

            if type(mat1 * mat2) == Matrix:
                mat3 = mat1 * mat2
                mat3.printmatrix()

        elif action == "D":
            print("Matrix:")
            mat1 = Matrix()

            if type(mat1.determinant()) == int:
                print(mat1.determinant())

        elif action == "I":
            print("Matrix:")
            mat1 = Matrix()

            inverse = mat1.inverse()
            inverse.printmatrix()

        elif action == "P":
            practice()

        elif action == "SS":
            solvesys()

        elif action == "Q":
            break

        else:
            print("Enter one of the choices above.\n")


start()
