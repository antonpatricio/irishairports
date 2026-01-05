import pandas as pd
import csv

df = pd.read_csv('AirportData.csv')

new = df.drop(['STATISTIC', 'UNIT', 'TLIST(M1)', 'Statistic Label', 'C02935V03550'], axis=1)
new['Airport'] = new['Airport'].str.upper()
new['Month'] = new['Month'].str.upper()

counter = 0

'''for row in new['Airport']: # For Taking Out The Total Passengers From All Airports Rows / File Name: OnlyAirports
    counter = counter + 1
    if row == 'ALL MAIN AIRPORTS':
        counter = counter-1
        new = new.drop(new.index[counter])'''

for row in new['Airport']: # For Taking Out All Aiports Except 1
    counter = counter + 1
    if row == 'ALL MAIN AIRPORTS' or row == 'DUBLIN' or row == 'CORK' or row == 'SHANNON' or row == 'KNOCK': # Put All Airport Values You Want To Take Out
        counter = counter-1
        new = new.drop(new.index[counter])

new = new.rename(columns = {"Month":"Date"})
new = new.rename(columns = {"VALUE":"Passengers"})

print(new)

df = pd.DataFrame(new)
csv_file_path = 'KerryAirport.csv' # Change name of file depending on the data being cleaned
df.to_csv(csv_file_path, index=False)