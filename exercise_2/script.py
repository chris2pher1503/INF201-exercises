#task 0: takes names defined in dictionary with name and a roll numbr and adds a count for each round.
import random as rd

rollers = {"Sarah": 0, 
         "Titus": 0, 
         "Hannah": 0
         } 

def roll(name: str, rollers: dict[str, int]) -> None: 
    rollers[name] += rd.randint(1,6)

for i in range(4):
    for name in rollers:
         roll(name, rollers)
#checking the result and the winner
sorted_rollers = sorted(rollers.items(), key=lambda x: x[1], reverse=True)
print(rollers)
print("The winner is: ", sorted_rollers[0][0], " with a score of: ", sorted_rollers[0][1])




#task 1: 
def count_votes(file_name: str, num_parties: int= None): 
    parties ={}
    eligible_voters = 0

    with open("2021-09-14_party distribution_1_st_2021.csv", "r") as file:
        lines = file.readlines()
        lines = lines[1:]
        for line in lines: 
            line = line.strip().split(";")
            district = line[1]
            party_code= line[6]
            number_of_votes = line[12]
            eligible_voters += int(number_of_votes)
            
            if party_code in parties: 
                parties[party_code] += int(number_of_votes)
                
            else:
                parties[party_code] = int(number_of_votes)
        for party in parties:
            print(f"{party} has {parties[party]} votes")


        
    sorted_parties = sorted(parties.items(), key=lambda x: x[1], reverse=True)

    print (f"{'party':<20}{'votes':<20}{'percentage':<20}")
    print ("="*60)
    for i, party in enumerate(sorted_parties):
        percentage = party[1]/eligible_voters *100
        mark = "*" if percentage >= 4 else ""
        print(f"{party[0]:<20}{party[1]:<20}{percentage:<19.2f}{mark}")
        if num_parties and i + 1 == num_parties:
            break 
    print ("="*60)
    print(f"Total number of voters: {eligible_voters}") 
    print ("="*60)
    
count_votes("2021-09-14_party distribution_1_st_2021.csv", 3)
count_votes("2021-09-14_party distribution_1_st_2021.csv", 7)
count_votes("2021-09-14_party distribution_1_st_2021.csv")
    
    
        
#task 2 og 3:
chars = ["2", "$", "å", "€", "a"]
def ascii_checker(chars: list[str]) -> None:
    for char in chars:
        print(f"Character: '{char}'")
        
        if ord(char) < 128:
            binary = format(ord(char), '08b')
            print(f"- ASCII representation: {binary}")
        else:
            print("- Not in ASCII range")
        
        utf8_bytes = char.encode('utf-8')
        utf8_rep = ' '.join(format(byte, '08b') for byte in utf8_bytes)
        print(f"- UTF-8: {utf8_rep} ({len(utf8_bytes)} bytes)")


ascii_checker(chars)




