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

    try:
        #inizializzo

        #se il file non si può aprire
        try:

            def __init__(self, name):

                self.name = name

                #se il tipo del file è .csv
                if self.name.split(".")[-1] == "csv":

                    #apre il file
                    self.my_file = open(self.name, 'r')

                #altrimenti, se non ha estensione csv raise ExamException
                else:
                    raise ExamException("il file non ha estensione .csv")

        except:
            raise ExamException("file non trovato")

        #prende data e sales e li mette in una lista
        def get_data(self):

            lista = []

            #divide gli elementi nel file e li aggiune ad una lista
            for lines in self.my_file:
                
                line = lines.split(',')

                lista.append(line)
                
            #chiude il file
            self.my_file.close()

            #ritorna la lista
            return lista
    
    except:
        print("qualcosa non funziona, non sò cosa")

#return una lista di 12 elementi che rappresenta la differenza media
#tra un anno e il seguente
# [ 16.25 , 16 , 23 ...]

class compute_avg_monthly_difference():

    try:

        def __init__(self, time_series, first_year, last_year):

            self.time_series = time_series
            self.first_year = first_year
            self.last_year = last_year

        def diff(self):

            #lista della variazione della media
            var_media = []

            #numero anni per cui dividere la somma per avere la media
            n = int(self.last_year) - int(self.first_year)

            #per ogni mese
            for mese in range(1,12):

                #lista dei valori corrispondenti quel mese negli anni
                lista_mese = []

                #per tutti gli elementi nella serie temporale
                for elementi in self.time_series:

                    #divide la data in anno e mese
                    data = elementi[0].split("-")

                    #se non è la prima riga
                    if data[0] != "date":

                        #per tutti gli anni inclusi nell'intervallo 
                        if (int(self.first_year) <= int(data[0]) <= int(self.last_year)):
                        
                            #si considera il mese corrispondente 
                            if int(data[1]) == mese:

                                #si aggiunge alla lista mesi il numero passeggeri corrispondente 
                                lista_mese.append(int(elementi[1]))

                #variabile somma per la somamtoria al numeratore 
                somma = 0

                #per ogni anno in quel mese
                for i in range(0, len(lista_mese) - 1):

                    #sommatoria passeggeri
                    somma = somma + (lista_mese[i + 1] - lista_mese[i])

                #si aggiunge alla lista la media
                var_media.append(somma/n)

            return var_media
    
    except:
        print("qualcosa non funziona, non sò cosa")

