import csv


def CsvRead(filename):
    reader = csv.reader(file(filename, 'rb'))  
    return reader

#----------------------------------------------------------------------
def CsvWrite(filename):
    """"""
    

    writer = csv.writer(file(filename, 'wb'))  
    writer.writerow(['Column1', 'Column2', 'Column3'])  
    lines = [range(3) for i in range(5)]  
    for line in lines:  
        writer.writerow(line)  
        


if __name__ == '__main__':
    f = '/Users/LiuFaPeng/Downloads/GeoIP.csv'
    for line in CsvRead(f):
        print line
    
    