import numpy as np
import pandas as pd
import matplotlib.pyplot as pyp

def count_of_laptops(dataframe):
    count = dataframe["Company"].value_counts()
    pyp.figure(figsize=[9,7])
    pyp.bar(dataframe["Company"].unique(),count,color="green")
    pyp.title("Company's count of laptops")
    pyp.ylabel("Count")
    pyp.xlabel("Companies")
    pyp.xticks(rotation=45)
    pyp.show()

def price_per_companies(dataframe):
    avg_price = dataframe.groupby("Company")["Price (Euro)"].mean().values
    companies = np.sort(dataframe["Company"].unique())
    pyp.figure(figsize=[9,7])
    pyp.bar(companies,avg_price,color="skyblue")
    pyp.title("Companies v/s Avg prices")
    pyp.ylabel("Avg Prices")
    pyp.xlabel("Companies")
    pyp.xticks(rotation=45)
    pyp.show()
    
def ramsize_laps(dataframe):
    ram_sizes = dataframe['RAM (GB)']
    ram_counts = ram_sizes.value_counts()
    pyp.figure(figsize=(10, 6))
    ram_counts.plot(kind='bar')
    pyp.title('Count of Laptops by RAM Size')
    pyp.xlabel('RAM Size (GB)')
    pyp.ylabel('Count')
    pyp.show()
    
def ask_menu(dataframe):
    while(True):
        print('''
---------------------------------------------------------
    1.Price per companies
    2.Count of laptops
    3.Count of Laptops by RAM Size
---------------------------------------------------------
            ''')
        choice = int(input("Enter your choice (1/2/3) : "))
        if(choice==1):
            price_per_companies(dataframe)
        elif(choice==2):
            count_of_laptops(dataframe)
        elif(choice==3):
            ramsize_laps(dataframe)
        print("-----------------------------------------------------")
        ask = (input("Do you still want to continue(y/n) : "))
        if(ask=='n' or ask=="N"):
            break
        elif(ask=='y' or ask=="Y"):
            pass
        else:
            print("INVALID CHOICE --------------")
            

def main():
    df = pd.read_csv("lp_rice.csv")
    ask_menu(df)


main()