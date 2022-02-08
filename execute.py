
from esame import CSVTimeSeriesFile, compute_avg_monthly_difference

#----------programma-----------

time_series_file = CSVTimeSeriesFile("data.csv")

time_series = time_series_file.get_data()

print(time_series)

lista_media = compute_avg_monthly_difference(time_series, "1949", "1951").diff()

print(lista_media)