import pandas as pd

df = pd.read_csv('OnlyAirports.csv')

def peak_value(airport):
    airport_Name = pd.read_csv(f"{airport}Airport.csv")
    peak = 0
    for value in airport_Name['Passengers']:
        if value > peak:
            peak = value
    
    return(peak)

def minimum_value(airport):
    airport_Name = pd.read_csv(f"{airport}Airport.csv")
    minimum = 1000000000000000000000000000
    for value in airport_Name['Passengers']:
        if value < minimum:
            minimum = value
    
    return(minimum)

def mean_calculator(airport):
    airport_Name = pd.read_csv(f"{airport}Airport.csv")
    total = 0
    counter = 0
    for value in airport_Name['Passengers']:
        total = total+value
        counter = counter + 1
    
    mean = total / counter
    mean = round(mean, 0)
    
    return(mean)
        
def median_finder(airport):
    airport_Name = pd.read_csv(f"{airport}Airport.csv")
    value_List = []
    for value in airport_Name['Passengers']:
        value_List.append(value)
    
    value_List = sorted(value_List)
    total = len(value_List)
    
    if total%2 == 0:
        value1 = value_List[total // 2-1]
        value2 = value_List[total // 2]
        median = (value1 + value2) / 2
        median = round(median)
    else:
        median = value_List[total // 2]
        
    return median

def range_finder(airport):
    airport_Name = pd.read_csv(f"{airport}Airport.csv")
    lowest_value = min(airport_Name['Passengers'])
    highest_value = max(airport_Name['Passengers'])
    range_value = highest_value - lowest_value
    
    return range_value

airports = ['Dublin', 'Cork', 'Shannon', 'Knock', 'Kerry']

airportDictionary = {
    "Dublin" : {
        
    },
    "Cork" : {
        
    },
    "Shannon" : {
        
    },
    "Knock" : {
        
    },
    "Kerry" : {
        
    }
}

for name in airports:
    peak = peak_value(name)
    minimum = minimum_value(name)
    mean = float(mean_calculator(name))
    median = median_finder(name)
    range_value = range_finder(name)
    airportDictionary[f"{name}"]["Name"] = f"{name}"
    airportDictionary[f"{name}"]["Peak"] = peak
    airportDictionary[f"{name}"]["Minimum"] = minimum
    airportDictionary[f"{name}"]["Mean"] = mean
    airportDictionary[f"{name}"]["Median"] = median
    airportDictionary[f"{name}"]["Range"] = range_value
    
print(airportDictionary) 