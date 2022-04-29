from curses.ascii import isdigit
import os


user_choice = -1

while user_choice != 4:
  print("1. Show tasks")
  print("2. Add task")
  print("3. Delete task")
  print("4. Close program")

  user_choice = int(input("Choose action: "))
  

  if user_choice == 1:
    filesize = os.path.getsize('Zadania.txt')
    with open("Zadania.txt", "r") as f:
      if filesize != 0:  
        for line in f.readlines():
          print('\n')
          print(line)
      else:
        print('There is no tasks in file!')     


  elif user_choice == 2:
    zadanie = str(input("Write task to save: "))
    file = open("Zadania.txt", "r+")
    if len(file.readlines()) > 0:
      file = open("Zadania.txt", "r+")
      count = 1
      for line in file:
          if line != "\n":
              count += 1
      last_line = line
      file.write('\n')
      file.write('{} {}'.format(count, zadanie))
    else:
      file.write('1 {}'.format(zadanie))
    file.close()


  elif user_choice == 3:
    correct_line_num = 1
    with open("Zadania.txt", "r") as f:
      lines = f.readlines()
      f.close()
    with open("Zadania.txt", "w") as f:
      del_number = input("Write number of task to delete: ")
      if len(lines) > 0:
        for line in lines:
            if not line.startswith(str(del_number)):
              for i in line:
                if line[0].isdigit():
                  i = line.replace(line[0], str(correct_line_num))
              correct_line_num += 1
              f.write(i)
              
          
        print('Task number {} deleted succesfully!'.format(del_number))
      else:
        print('There is no task to delete!')
    # with open("zadania.txt", "r") as input:
    #   with open("temp.txt", "w") as output:
    #     for line in input:
    #       if not line.strip('\n').startswith(str(del_number)):
    #         output.write(line)
    # os.replace('temp.txt', 'Zadania.txt')  
    # input.close()
    # output.close()




















    