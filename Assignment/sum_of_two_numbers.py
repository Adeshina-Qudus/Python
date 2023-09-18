while True:
    first_number = int(input("ENTER FIRST NUMBER : "))
    second_number = int(input("ENTER SECOND NUMBER : "))
    sum = first_number + second_number
    print(sum)
    print()
    terminate = int(input("""
    DO YOU WISH TO PERFORM THIS OPERATION AGAIN ? 
                                            
                                            YOU WANT TO CONTINUE ? 
                                                      PRESS 
                                                       [1]
                                            YOU WANT TO TERMINATE ?  
                                                      PRESS
                                                       [-2]   
                                                         """))
    if terminate == 1:
        continue
    if terminate == -2:
        break

