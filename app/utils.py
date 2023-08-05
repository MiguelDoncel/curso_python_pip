def population_by_country(data, country):
  result = list(filter(lambda item: item["Country/Territory"] == country, data))
  return result

def get_population(dict,country):
  keys = []
  values = []
  for i in country.keys():
    keys.append(i)
  for n in country.values():
    values.append(n)
  
  year = 0
  years = []
  population = []
  while year < len(keys):
    years.append(keys[year + 5].replace(" Population", ""))
    year += 1
    if year == 8:
      break
  
  
  popul = 0
  while popul < len(values):
    population.append(int(values[popul + 5]))
    popul += 1
    if popul == 8:
      break
  
  return years,population

def world_population(data):
  countries = []
  percentages = []
  for elements in data:
    countries.append(elements["Country/Territory"])
    percentages.append(elements["World Population Percentage"])
  
  return countries, percentages


