import random
def generate_balanced_grid(rows,cols):
    if(rows<3 or cols<3):
        print("Grid must be at least 3*3 to have an inner layer.")
        return
    while True:
        grid=[[random.randint(1,20) for _ in range(cols)] for _ in range(rows)]
        outer_sum=0
        inner_sum=0
        for i in range(rows):
              for j in range(cols):
                  if i==0 or j==0 or j==rows-1 or i==cols-1:
                      outer_sum +=grid[i][j]
                  else:
                      inner_sum+=grid[i][j]
        if outer_sum==inner_sum:
            print("\nBalanced Grid:")
            for row in grid:
                print(row)
            print(f"\nOuter Layer Sum = {outer_sum}")
            print(f"\nInner Layer Sum = {inner_sum}")
            break
rows=int(input("Enter number of rows(minimum3):"))
cols=int(input("Enter number of cols(minimum3):"))
generate_balanced_grid(rows,cols)


