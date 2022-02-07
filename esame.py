class ExamException(Exception):

    pass

class CSVFile():

    #inizializzo
    def __init__(self, name):

        pass

    #prende data e sales e li mette in una lista
    def get_data(self, start = None, end = None):

        pass

#classe CVS file
class CSVTimeSeriesFile(CSVFile):

    #inizializzo
    def __init__(self, name = "data.csv"):

        self.name = name

        my_file = open(self.name, 'r')

    #prende data e sales e li mette in una lista
    def get_data(self, start = None, end = None):

        #apre il file 
        my_file = open(self.name, 'r')

        lista = []

        #divide gli elementi nel file e li aggiune ad una lista
        for lines in my_file:
            
            line = lines.split(',')

            lista.append(line)
            
        #chiude il file
        my_file.close()

        #stampa lunghezza lista voluta
        print(lista[start:end])
    
        #chiude il file in modalità lettura
        my_file.close()

class compute_avg_monthly_difference():

    def __init__(self, time_series, first_year, last_year):

        self.time_series = time_series
        self.first_year = first_year
        self.last_year = last_year

    #return una lista di 12 elementi che rappresenta la differenza media
    #tra un anno e il seguente
    # [ 16.25 , 16 , 23 ...]