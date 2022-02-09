
from esame import CSVTimeSeriesFile, compute_avg_monthly_difference

#----------programma-----------

time_series_file = CSVTimeSeriesFile("data missed.csv")

time_series = time_series_file.get_data()

print(time_series)

lista_media = compute_avg_monthly_difference(time_series, "1950", "1952").diff()

print(lista_media)