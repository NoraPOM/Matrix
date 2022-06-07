# print a matrix

def print_matrix(matrix):

    for row in matrix:

        temp = "["

        for item in row:

            temp+= str(item) + ","

        print(temp[:-1]+"]")

       


def create_matrix(size):

    matrix = []

    for i in range(size):

        row = []

        for j in range(size):

            if j == i:
            
                row.append(1)
        
            else:
    
                row.append(0)

        matrix.append(row)           

    print_matrix(matrix)

   

def main():

    size = input("Ingrese el numero: ")

    create_matrix(int(size))



if __name__ == "__main__":

    main()
