import csv

with open("mycsv.csv","w",newline='',encoding="shift-jis") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["Top Gun","Risky Business","Minority Report"])
    w.writerow(["Titanic","The Revenant","Inception"])
    w.writerow(["Training Day","Man on Fire","Flight"])

with open("mycsv.csv","r",encoding="shift-jis") as f:
    print(f.read())

    
    
