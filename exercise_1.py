


# task1: input name and print out welcome message
name=input("Enter your name: ")
greeting="welcome to INF201, "+name+"!"
print(greeting)
    
#task2: takes input from task one and adds a frame around it
print("*" * (len(greeting)+4))
print("*", greeting, "*")
print("*" * (len(greeting)+4))
    
#task3: takes 1-10 and squares them and to the third power
dash="-"*26
print(dash)
print(f"{'Number':>8} {'Square':>8} {'Cube':>8}")
print(dash)
for i in range(1,11):
    print(f"{i:>8} {i**2:>8} {i**3:>8}")
print(dash)


#task4: reading csv file and sorting on districts and printing out a alphabetical sorted list of population
district_population = {}

with open('/Users/torbjorntorsken/Desktop/INF201/Exercises/csv_files/norway_municipalities_2017.csv','r') as file:
    lines = file.readlines()
    lines=lines[1:]
    for line in lines:
        line = line.strip().split(",")
        district = line[1]
        population = int(line[2])
        
        if district in district_population:
            district_population[district]+=population
        else:
            district_population[district]=population
            
            
#the     
sorted_alphabetical = sorted(district_population.items())
sorted_amount = sorted(district_population.items(), key=lambda x: x[1], reverse=True)
print("sorting by alphabetical district:")
print(f"{'District':<30} {'Population':<30}")
print("-"*41)
for district, population in sorted_alphabetical:
    print(f"{district:<30} {population:<30}")
print("-"*41)
print("sorting by population:")
print(f"{'District':<30} {'Population':<30}")
print("-"*41)
for district, population in sorted_amount:
    print(f"{district:<30} {population:<30}")

            



#task5: plot the data using pandas in a bar chart. 
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('/Users/torbjorntorsken/Desktop/INF201/Exercises/csv_files/norway_municipalities_2017.csv')
district_population = df.groupby('District')['Population'].sum()

district_population.plot(kind='bar')
plt.title("Population in districts in Norway")
plt.ylabel("Population")
plt.xlabel("District")
plt.show()
print(df)

        
        
