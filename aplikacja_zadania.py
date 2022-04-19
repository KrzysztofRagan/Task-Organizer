from curses.ascii import isdigit
from dataclasses import replace
from tkinter import E


user_choice = -1

#def show_tasks():
task_index = 0
file = open("Zadania.txt", "r")
# js = json.loads(file.read())
# print(js)



while user_choice != 5:
  print("1. Pokaz zadania")
  print("2. Dodaj zadanie")
  print("3. Usun zadanie")
  print("4. Zapisz zadanie")
  print("5. Wyjdz")

  user_choice = int(input("Wybierz liczbe: "))
  

  if user_choice == 1 :
    file = open("Zadania.txt", "r")
    for line in file.readlines():
      print('\n')
      print(line)

  elif user_choice == 2:
    zadanie = str(input("wpisz zadanie: "))
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
  #elif user_choice == 3:
    #file = open("Zadanie.txt")


















    