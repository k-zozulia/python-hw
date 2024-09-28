def total_salary(path):
    total_salary = 0
    counter = 0

    try:
        with open(path, "r", encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    total_salary += int(salary)
                    counter += 1

                except ValueError:
                    print(f"Invalid line {line}")
                    continue
        
        if counter == 0:
            return (0, 0)
        return (total_salary, total_salary / counter)
    
    except FileNotFoundError:
        print("File not found")
        return (0, 0)
    
    except Exception as e:
        print(f"Error ocurred: {e}")
        return (0, 0)
    
    