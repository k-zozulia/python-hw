def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    current_cat = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(current_cat)
                except ValueError:
                    print(f"Invalid line {line}")
                    continue

        return cats_info
    
    except FileNotFoundError:
        print("File not found")
        return []
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
