import csv
fn = "csvreport (2).csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)
    for j in listReport:
        print(j)

fn = "csvreport (2).csv"
with open(fn) as csvFile:
    csvdictReader = csv.DictReader(csvFile)
    for j in csvdictReader:
        print(j["工會團體類別"], j["勞工團體單位數（單位:個）"])

fn = "writerow.csv"
with open(fn, 'w', newline="", encoding="utf-8") as fff:
    fffWriter = csv.writer(fff)
    fffWriter.writerow(['name', 'height', 'weight'])
    fffWriter.writerow(['joy', '180', '67'])
    fffWriter.writerow(['ken', '170', '66'])


fn = "TaipeiWeatherJan.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
