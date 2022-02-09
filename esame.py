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
       

        #se il file non si può aprire
        try:
            
            #inizializzo
            def __init__(self, name):

                self.name = name

                #prova a cercare un'estensione del file
                try:

                    #se il tipo del file è .csv
                    if self.name.split(".")[-1] == "csv":

                        #apre il file
                        self.my_file = open(self.name, 'r')

                    #altrimenti, se non ha estensione csv raise ExamException
                    else:
                        raise ExamException("il file non ha estensione .csv")

                except:
                    raise ExamException("il file non si può aprire, deve avere un'estensione .csv")

        except:
            raise ExamException("file non trovato")

        #prende data e n.passeggeri e li mette in una lista
        def get_data(self):

            #lista vuota in cui aggiunge la coppia di elementi data/passeggeri
            lista = []

            try:

                #divide gli elementi nel file e li aggiune ad una lista
                for lines in self.my_file:
                    
                    line = lines.split(',')

                    lista.append(line)

            except:
                raise ExamException("il file non è leggibile riga per riga")
                
            #chiude il file
            self.my_file.close()

            #ritorna la lista
            return lista
    
    except:
        raise ExamException("qualcosa non funziona, non sò cosa")

#return una lista di 12 elementi che rappresenta la differenza media
#tra un anno e il seguente
# [ 16.25 , 16 , 23 ...]

class compute_avg_monthly_difference():

    try:

        #inizializzo, serie temporale: primo anno e ultimo anno da considerare
        def __init__(self, time_series, first_year, last_year):

            self.time_series = time_series
            #lista vuota che contiene time_series ripulita
            self.t_s_clean = []
            self.first_year = first_year
            self.last_year = last_year

            #si ripulisce time_series da errori di battitura o da dati non utili
            #si copia in un nuovo file pulito che si userà per il calcolo

            for riga in self.time_series:

                #verifica correttezza della riga
                try:

                    #se il primo elemento contiene una data
                    #il cui primo elemento è un anno: numero stringa convertibile in intero positivo maggiore di 1910 (prima non esistevano i voli di linea) e minore di 2022
                    #secondo elemento è un mese: numero stringa convertibile in intero compreso tra uno e 12
                    #e se il secondo elemento è un numero stringa convertibile in intero positivo maggiore di 0
                    try:
                        if int(riga[0].split('-')[0]) in range(1910,2023)  and int(riga[0].split('-')[1]) in range(1,13) and int(riga[1]) > 0:

                            #allora è una normale riga su cui si può operare,
                            #viene aggiunta alla serie temporale pulita
                            self.t_s_clean.append(riga)

                    #se non avviene niente di tutto questo
                    #si passa alla riga successiva
                    except:
                        pass

                #se qualcosa non dovesse rientrare in ogni caso
                except:
                    raise ExamException("il file è compromesso")

            #sapendo che i primi due elementi nella lista t_s_clean sono corretti e trattabili, elimina gli elementi che superano la lunghezza per ogni riga
            for i in range(0, len(self.t_s_clean) - 1):

                if len(self.t_s_clean[i]) > 2:

                    self.t_s_clean[i] = self.t_s_clean[i][:2]

            #controllo se il tipo degli anni è stringa e non altri
            if type(first_year) != str:

                raise ExamException("il valore del primo anno non è di tipo stringa")

            if type(last_year) != str:

                raise ExamException("il valore dell'ultimo anno non è di tipo stringa")

            #controllo se gli anni da stringa si possono convertire in numero intero
            try:
                int(first_year)
            
            except:
                raise ExamException("il valore del primo anno non è convertibile a numero intero")

            try:
                int(last_year)
            
            except:
                raise ExamException("il valore dell'ultimo anno non è convertibile a numero intero")

            #controlla se il primo anno è minore del secondo
            if int(self.first_year) >= int(self.last_year):
         
                raise ExamException("il primo anno non è strettamente minore del secondo")

            #ciliegina sulla torta: prima del 1910 non esistevano i voli di linea
            if int(self.first_year) < 1910:

                raise ExamException("prima del 1910 non esistevano i voli di linea")

            if int(self.last_year) < 1910:

                raise ExamException("prima del 1910 non esistevano i voli di linea")

            #controllo se il primo e l'ultimo anno sono contenuti nella serie temporale (non è detto che i dati in input siano in ordine crescente)   
            anni = []
            
            for riga in self.t_s_clean:

                #aggiungo tutti gli anni in una lista temporanea in formato intero
                anni.append(int(riga[0].split('-')[0]))

            #controlla se si può fare il minimo e il massimo sulla lista anni
            try:
                min(anni)
                max(anni)

            except:
                raise ExamException("Non si può operare su questo tipo di lista perchè non contiene alcun dato nel formato anno-mese/passeggeri")

            #se la lista anni contiene solo un anno allora non è possibile fare una media mensile
            if max(anni) == min(anni):

                raise ExamException("non è possibile fare l'incremento medio mensile su un solo anno")
                
            #controlla se l'intervallo degli anni è contenuto nella lista
            if (min(anni) <= int(self.first_year) < int(self.last_year) <= max(anni)) == False:

                raise ExamException("l'intervallo degli anni non è contenuto nella lista")

            #controllo se le date sono in ordine crescente senza ripetizioni
            #controlla l'ordine degli anni
            #dato l'elemento i-esimo
            for i in range(0, len(self.t_s_clean) - 2):

                #controlla i k-esimi elementi successivi
                for k in range(i + 1, len(self.t_s_clean) - 1):

                    #controlla l'ordine degli anni
                    if int(self.t_s_clean[i][0].split("-")[0]) > int(self.t_s_clean[k][0].split("-")[0]):

                        raise ExamException("la lista non è ordinata in ordine crescente per gli anni")
            
            #assunto che gli anni siano in ordine crescente
            #controlla l'ordine dei mesi
            #dato l'elemento i_esimo
            for i in range(0, len(self.t_s_clean) - 2):
               
                #considerato un anno
                year = int(self.t_s_clean[i][0].split("-")[0])

                lista_ord_mesi = []

                #se ci sono altri elementi successivi con quell'anno controlla se i mesi sono crescenti
                for k in range(i + 1, len(self.t_s_clean) - 1):

                    if int(self.t_s_clean[k][0].split("-")[0]) == year:

                        #aggiunge i mesi di quell'anno ad una lista vuota
                        lista_ord_mesi.append(self.t_s_clean[k][0].split("-")[1])

                #se ci sono più elementi con lo stesso mese
                if len(lista_ord_mesi) > 1:

                    #controlla se i mesi sono crescenti per quell'anno
                    for j in range(0, len(lista_ord_mesi) - 2):

                        if lista_ord_mesi[j] >= lista_ord_mesi[j + 1]:

                            raise ExamException("la lista non è ordinata in ordine strettamente crescente per i mesi: i mesi non sono in ordine crescente o sono presenti duplicati.")

        #funzione differenza media mensile
        def diff(self):

            #lista della variazione della media
            var_media = []

            #numero anni per cui dividere la somma per avere la media
            n = int(self.last_year) - int(self.first_year)

            #per ogni mese
            for mese in range(1,13):

                #lista del n.passeggeri corrispondenti in quel mese negli anni
                lista_mese = []

                #per tutti gli elementi nella serie temporale
                for elementi in self.t_s_clean:

                    #divide la data in anno e mese
                    data = elementi[0].split("-")

                    #per tutti gli anni inclusi nell'intervallo 
                    if (int(self.first_year) <= int(data[0]) <= int(self.last_year)):
                    
                        #si considera il mese corrispondente 
                        if int(data[1]) == mese:

                            #si aggiunge alla lista mesi il numero passeggeri corrispondente 
                            lista_mese.append(int(elementi[1]))

                            #altrimenti non succede nulla e si và avanti al prossimo elemento

                #variabile somma per la somamtoria al numeratore 
                somma = 0

                #se per quel mese sono stati trovati più di due dati n.passeggeri
                if len(lista_mese) >= 2:

                    #per ogni anno in quel mese
                    for i in range(0, len(lista_mese) - 1):

                        #sommatoria passeggeri
                        somma = somma + (lista_mese[i + 1] - lista_mese[i])

                #altrimenti se la lista è vuota o contiene un solo elemento
                elif len(lista_mese) <= 1:
                    #non si procede con la sommatoria e la var somma rimane 0
                    somma = 0

                #si aggiunge alla lista la media
                var_media.append(somma/n)

            return var_media
    
    except:
        raise ExamException("qualcosa non funziona, non sò cosa")

