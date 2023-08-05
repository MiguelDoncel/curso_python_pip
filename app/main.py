import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv("data.csv")
  data = list(filter(lambda item: item["Continent"] == "South America",data))
  countries, percentage = utils.world_population(data)

  charts.generate_pie_chart(countries,percentage)
  country = input("Type country: ")
  result = utils.population_by_country(data,country)
  if len(result) > 0:
    country = result[0]
    years, population = utils.get_population(data,country)
    charts.generate_bar_chart(country['Country/Territory'], years,population)

if __name__ == "__main__":    #Esto es correr esta línea desde la terminal como script
  run()