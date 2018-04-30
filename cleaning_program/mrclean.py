import csv
words = []
bads=open("en.txt","r")
listbads=bads.read().split("\n")
with open('urban.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count=0
    for row in readCSV:
        if len(row)==6:
            count+=1
            if count % 10000 == 0:
                print(str(count))
            description = row[5]
            if description.find(";") != -1:
                description = description[:description.find(";")]
            description=description.replace("1.","")
            description=description.replace("1 ","")
            description=description.strip()
            description=' '.join(description.split())
            description=description.replace(" ,",",")
            description=description.replace("\n","")
            term=row[1].lower()
            mean=False
            for bad in listbads:
                if bad.lower() in term.lower() or bad.lower() in description.lower():
                    mean=True
            if len(description)>2 and term.find("/")==-1 and count % 3 == 0 and not mean and len(description)<150:
                words.append("%s: %s \n"%(term,description))
file=open("input.txt","w")
for word in words:
    file.write(word)
file.close()