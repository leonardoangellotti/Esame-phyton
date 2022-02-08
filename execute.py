
from esame import CSVTimeSeriesFile, compute_avg_monthly_difference, ExamException

#----------programma-----------

time_series_file = CSVTimeSeriesFile("data err.csv")

time_series = time_series_file.get_data()

print(time_series)

lista_media = compute_avg_monthly_difference(time_series, "1949", "1960").diff()

print(lista_media)