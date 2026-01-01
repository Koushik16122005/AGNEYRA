#Marks Average Analyzer
marks = list(map(int, input("Enter the marks separated by spaces: ").split()))

def TotalMarks(marks):
  return sum(marks)

def AverageMarks(marks):
  return sum(marks) / len(marks)

def HighestMarks(marks):
  return max(marks)

def LowestMarks(marks):
  return min(marks)

while True:
  print("\n Marks Average Analyzer Menu: \n")
  print("1. Total Marks")
  print("2. Average Marks")
  print("3. Highest Marks")
  print("4. Lowest Marks")
  print("5. Exit")

  choice = int(input("Choose an option (1-5): "))
  match choice:

    case 1:
      print("Total Marks:", TotalMarks(marks))
            
    case 2:
      print("Average Marks:", AverageMarks(marks))

    case 3:
      print("Highest Marks:", HighestMarks(marks))

    case 4:
      print("Lowest Marks:", LowestMarks(marks))

    case 5:
      print("Exiting the program.")
      break
      
    case _:
      print("Invalid choice. Please select a valid option.")
