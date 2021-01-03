def run():
    my_dictionary = { #dictionary is a list instead subindice, have a key.
        'keyOne': 1234,
        'name_of_me': "Ivan Farid", 
        'age': 28,
    }
    print(my_dictionary['keyOne'])
    print(my_dictionary['name_of_me'])
    print(my_dictionary['age'])
    print("\n")
    
    popoluation_country = {
        'Mexico': 131000000,
        'USA': 450000000,
        'Sweden': 11000000,
    }

    for country in popoluation_country.keys(): #we are accesing to the key
        print(country)

    for country in popoluation_country.values(): #We are accesing to value
        print(country)

    for country, population in popoluation_country.items(): #we are accesing to key and value with items
        print(country + " have " + str(population) + " population")

if __name__ == '__main__':
    run()