#haha yes, funny name.
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    
    new_country["visits"]  = visits

    
    new_country["cities"] = cities_visited 
    
    # for cities in range(num_cities):
    #     cities_visited = input("What city did you visit? ")
    #     new_country["cities"].append(cities_visited)
    # Failed attempt at creativity, come back later once more comfortable, but for now, answer is dirrectly added thru src code.
    travel_log.append(new_country)




add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


