import utils
import charts
import read_csv

def run():
    data = read_csv.read_csv('./app2/best-countries-to-live-in-2024.csv')
    regiones = utils.region(data)
    
    print("Selecciona una de las siguientes regiones para saber cual es el mejor pais para vivir en 2024:")
    for i, region in enumerate(regiones, start=1):
        print(f"{i}. {region}")

    seleccion = int(input("=> "))
    
    if 1 <= seleccion <= len(regiones):
        region = regiones[seleccion - 1]
        result = utils.worldHappiness2022(data, region)
        
        if len(result[0]) > 0:
            labels, values = result
            charts.generate_bar_chart(labels, values)

        print(result)
    else:
        print("Selección no válida.")

if __name__ == '__main__':
    run()