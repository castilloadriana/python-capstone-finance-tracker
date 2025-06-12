# Command-line personal finance tracker that allows users to log expenses,
#  categorize them, and view summaries. 



# prints all categories and their expenses
def view_expenses(data):
    for i in data:
        print(f"Category: {i}")
        for item in data[i]:
            print(f"- {item[0]} : ${item[1]}")
        

#shows the total amount spent per category
def view_summary(data):
    print("Summary:")

    for i in data:
        sum = 0
        for item in data[i]:
            sum+= item[1]
            
        print(f"- {item[0]} : ${sum}")


print("Welcome to the Personal Finance Tracker!")
expenses = {} 
try:
    response= int(input("What would you like to do? 1. Add Expense 2. View All Expenses 3. View Summary 4. Exit > "))

    while (response > 5):
        print("Choose a menu item option from 1-4")
        response= int(input("What would you like to do? 1. Add Expense 2. View All Expenses 3. View Summary 4. Exit > "))

except ValueError:
    print("Invalid input! Please enter a valid number.")

else:

    while response != 4:

        if response == 1:
            repeat= 1 #1= yes repeat, 2= stop
            while repeat == 1:
                description= input("Enter expense description: ")
                category= input("Enter category: ")
                try:
                    amount= float(input("Enter amount: "))        
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                else:
                    if category not in expenses:
                        expenses[category]= [(description, amount)]
                        print("Expense added successfully.")
                    else: 
                        expenses[category].append((description, amount))
                        print("Expense added successfully.")

                    try:
                        repeat= int(input("Would you like to add another item? 1. Yes 2. No "))
                    except ValueError:
                        print("Invalid input! Please enter a valid number.")
        elif response == 2:
            view_expenses(expenses)

        elif response == 3:
            view_summary(expenses)
        
        try:
            response= int(input("What would you like to do? 1. Add Expense 2. View All Expenses 3. View Summary 4. Exit > "))

            while (response > 5):
                print("Choose a menu item option from 1-4")
                response= int(input("What would you like to do? 1. Add Expense 2. View All Expenses 3. View Summary 4. Exit > "))

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    exit()               

finally:
    print("Goodbye.")