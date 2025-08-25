def check_even_odd(n_list=[0]):
    for n in n_list:
        if n % 2 == 0:
            print(f"{n} is Even")
        else:
            print(f"{n} is Odd")

check_even_odd([1, 2, 3, 4, 5])  


def check_even_odd(n=0):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
print(check_even_odd())    
print(check_even_odd(7))    
print(check_even_odd(12))   




def count_vowels(text, vowels="aeiou"):
    text = text.lower()  
    found_vowels = []    

    for char in text:
        if char in vowels:
            found_vowels.append(char)

    return len(found_vowels)
print(count_vowels("Python is fun"))     
print(count_vowels("HELLO world"))       
print(count_vowels("Why?"))             




def count_even(numbers):
    even_count = 0  

    for num in numbers:
        if num % 2 == 0: 
            even_count += 1

    return even_count
print(count_even([1, 2, 3, 4, 6]))  
print(count_even([7, 9, 13]))       
print(count_even([2, 4, 6, 8]))     




def triangle_area(base, height):
    area = 0.5 * base * height
    return area
print(triangle_area(10, 5))  
print(triangle_area(6, 3))    
print(triangle_area(0, 10))  



def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif 6 <= len(password) <= 10:
        return "Medium"
    else:
       
