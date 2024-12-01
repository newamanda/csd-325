#Amanda New
#CSD325-A311
#Module 7.2 Assignment
#Test Cases
#City Functions


def city_country(city, country, population=None, language=None):

    #return string - population and language optional
    city_info = f"{city}, {country}"
    if population is not None:
        city_info += f" - Population: {population}"
    if language is not None:
        city_info += f", Language: {language}"
    return city_info

#test city; first city, includes city, country, population, and language    
first_city = "London"
first_country = "England"
first_population = 9000000
first_language = "English"
first_string = city_country(first_city, first_country, first_population, first_language)
print(first_string)

#second city, includes city and country only
second_city = "Rome"
second_country = "Italy"
second_string = city_country(second_city, second_country)
print(second_string)

#thrid city, includes city, country, and population
third_city = "Sydney"
third_country = "Australia"
third_population = 5000000
third_string = city_country(third_city, third_country, third_population)
print(third_string)

