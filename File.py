#with open("demo.txt", mode='w') as file:
#    file.write("My name is Qudus Adeshina \n")
 #   file.write("I am trying to open a python file \n")
  #  file.write("Let's see how i can help you \n")

with open("demo.txt", mode='r') as file:
    #print(f'{"FIRST":<10}{"SECOND":<10}{"THIRD":>10}')
    for record in file:
        first,second,*third = record.split()

        print(f'{first:<10}{second:<10}{third}')
