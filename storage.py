def load_expenses(filename):
    expenses=[]
    next_id=1

    try:
        with open(filename,"r") as f:
            for line in f:
                line=line.strip()
                if line=="":
                    continue

                parts=line.split("|")
                if len(parts)!=5:
                    continue

                id_str, date, category, amount_str, note=parts

                try:
                    id_val=int(id_str)
                    amount_val=float(amount_str)
                except ValueError:
                    continue

                
                expense={
                        "id":id_val,
                        "date":date,
                        "category":category,
                        "amount":amount_val,
                        "note":note                    
                }
                expenses.append(expense)
                    

        if expenses: #determinig next id if expenses are loaded
            max_id=max(e["id"] for e in expenses)
            next_id = max_id + 1

    except FileNotFoundError: #if file doesnt exist return empty list
        return[], 1

    return expenses, next_id

def save_expenses(filename, expense_list):
    with open(filename, "w")as f:
        for e in expense_list:
            line = f'{e["id"]}|{e["date"]}|{e["category"]}|{e["amount"]}|{e["note"]}\n'
            f.write(line)    

