from datetime import datetime
import csv
import os


def main():
    expenses = []

    if os.path.exists("expenses.csv"):
        with open("expenses.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

    def valid_date_pattern(date_given, date_form="%Y-%m-%d"):
        try: 
            datetime.strptime(date_given, date_form)
            return True
        except:
            return False    
    while True:
        print("Click 1 to Add expense")
        print("Click 2 to View expenses")
        print("Click 3 to View expenses by category")
        print("Click 4 to delete an expense")
        print("Click 5 to Exit")

        try:
            choice = int(input("Your choice: "))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError
        except ValueError:
            print("It must be either 1, 2, 3, 4 or 5!!")
            continue    

        if choice == 1:
            try:
                amount = float(input("Please enter the amount{In your currency}: "))
                category = input("Please enter what category: ").lower().title()
                date = input("Please enter the date forme(year-month-day): ")
                if valid_date_pattern(date):
                    expenses.append({
                        "amount": amount,
                        "category": category,
                        "date": date
                    })
                else:
                    raise ValueError    
            except ValueError:
                print("The amount needs to be a float!!! or date needs to be in the pattern given")   
                continue 
        elif choice == 2:
            if expenses:
                for expense in expenses:
                    print(f"Amount: {expense['amount']} | Category: {expense['category']} | Date: {expense['date']}")

                total = sum(exp["amount"] for exp in expenses)
                print(f"The total: {total}")    
            else:
                print("You must add expenses to view them")    
                continue  
        elif choice == 3:
            if expenses:
                expenses_category = set(exp["category"] for exp in expenses)
                for i ,el in enumerate(expenses_category):
                    category_total = 0
                    for exp in expenses:
                        if exp["category"] == el:
                            category_total += exp["amount"]           
                    print(f"{el}: {category_total}")
                chosen_category = input("Enter the category that you want to view: ").lower().title()
                
                if chosen_category in expenses_category:
                    for exp in expenses:
                        if exp["category"] == chosen_category:
                            print(f"Amount: {exp['amount']} | Category: {exp['category']} | Date: {exp['date']}")  
                else:
                    print("The category chosen needs to be one of the listed ones")
                    continue    
            else:
                print("You must add expenses to view them")    
                continue   
        elif choice == 4:
            if expenses:
                number_av = []   
                for i, exp in enumerate(expenses):
                    print(f"{i + 1}. Amount: {exp['amount']} | Category: {exp['category']} | Date: {exp['date']}")
                    number_av.append(i)
                try:
                    num = int(input("Enter the number of the expense that you want to delete: ")) - 1
                    if num not in number_av:
                        raise ValueError
                except ValueError:
                    print("The value entered need to be an integer and one of the one shown")
                    continue

                expenses.remove(expenses[num])
        else:
            mode = "w"
                
            with open("expenses.csv", mode, newline='') as file:
                fieldnames = ["amount", "category", "date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for exp in expenses:
                    writer.writerow(exp)  

            break         
if __name__ == "__main__":

    main()
