#task 0: 
"""
with open("input.txt", "r") as file: 
    lines = file.readlines()
    lines = lines[1:]
    for line in lines: 
        
        words = line.strip().split()
        for word in words:  
            splitted = word.split("@")
            if len(splitted) < 2:
                #print("Invalid email")
                continue
            else: 
                name = splitted[0]
                institution = splitted[1].split(".")[0]
                domain = splitted[1].split(".")[1]
                print(f"{name} from {institution}.{domain}") 
"""
import re

def process_emails(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  
        
        email_pattern = r'([\w.-]+)@([\w-]+)\.([\w.]+)'
        
        for line in lines:
            matches = re.findall(email_pattern, line)
            for match in matches:
                name, institution, domain = match
                print(f"{name} from {institution}.{domain}")

process_emails("input.txt")

                
                
                
                
                
            
#task 1: 
"""
text = 'Ali and Per are friends.
Kari and Joe know each other.
James has known Peter since school days.'


print("Friendships:".center(23))
for line in text.split("\n"):
    words = line.split()
    print("-"*23)
    first_name = words[0]
    words = words[1:]
    for word in words: 
        if word[0].isupper(): 
            print(f"{first_name:>10} - {word:<10}")
print("-"*23)

"""




text = """Ali and Per are friends.
Kari and Joe know each other.
James has known Peter since school days."""

pattern = re.compile(r"([A-Z][a-z]+) .* ([A-Z][a-z]+)")
print("Friendships".center(23))
print("-" * 23)
for line in text.split("\n"):
    match = pattern.match(line)
    if match:
        first_name, second_name = match.groups()
        print(f"{first_name:>10} - {second_name:<10}")

print("-" * 23)

    
#task 2:
"""
def validate_password(password: str) -> bool: 
    if not re.match(r'[I-Z]', password[0]): 
        return "Invalid password: "+password
    if not (4 <= len(password) <= 5):
        return "Invalid password: "+password
    if not password[-1].isdigit():
        return "Invalid password: "+password
    if not re.search(r'\w', password):
        return "Invalid password: "+password
    if password.startswith(" ") or password.endswith(" "):
        return "Invalid password: "+password
    return "Valid password: "+password


print(validate_password('J1234'))  
print(validate_password('I_ab5'))  
print(validate_password('Z9_w4')) 
print(validate_password('A1234'))
print(validate_password('J12345')) 
print(validate_password('I__'))  
"""



def validate_password(password: str) -> str:
    if re.fullmatch(r'[I-Z]\w{2,3}\d', password) and not (password.startswith(" ") or password.endswith(" ")):
        return "Valid password: " + password
    else:
        return "Invalid password: " + password

print(validate_password('J1234'))
print(validate_password('I_ab5')) 
print(validate_password('Z9_w4'))  
print(validate_password('A1234')) 
print(validate_password('J12345'))
print(validate_password('I__'))



#task 3: 
from pathlib import Path
     
def find_imports_in_file(file_path):
    with open(file_path, "r") as file:
        imports = []
        from_imports = []

        for line in file:
            import_match = re.match(r'import (\w+)', line)
            if import_match:
                imports.append(import_match.group(1))

            from_import_match = re.match(r'from (\w+) import (\w+)', line)
            if from_import_match:
                from_imports.append(from_import_match.group(2))

        return imports + from_imports

def find_all_imports():
    py_files = Path().glob("*.py")
    
    for py_file in py_files:
        imports = find_imports_in_file(py_file)
        if imports:
            print(f"{py_file}: {imports}")

find_all_imports()