

with open('salary_file.txt', 'w') as fh:
    fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\nNatalia Siladi,6000")

def total_salary(path):  
    try:      
        with open(path, 'r') as fh:
            lines = [el.strip() for el in fh.readlines()]
            number_of_developers = 0
            total_salary = 0
            for line in lines:
        
                new_line = line.split(",")
                total_salary = total_salary + int(new_line[1])
                number_of_developers = number_of_developers + 1
        
            average_salary = total_salary / number_of_developers
            result = (total_salary, int(average_salary) )
            return result
    except FileNotFoundError:
        print("File not found") 
        return []   
    except IndexError:
        print("Error processing file. Please check the file format.")
        return []
    except Exception as e:
        print("An unexpected error occurred:", e)
    
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")    

    