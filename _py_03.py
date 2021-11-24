import sqlite3
fpt_data = sqlite3.connect("dbFPT.sqlite")
curs = fpt_data.cursor()

script = '''
DROP TABLE IF EXISTS InFos;

CREATE TABLE InFos(
    ProCode INTEGER PRIMARY KEY, 
    Deleted TEXT
);
'''
curs.executescript(script)

try:
    fname = "datafile.txt"
    fh = open(fname)
    line_count = 0
    for i in fh:
        line_count += 1
        if line_count == 1: continue
        line = i.strip().split()
        procode, deleted = int(line[0].strip()), line[3].strip()

        curs.execute("INSERT INTO InFos(ProCode, Deleted) VALUES (?, ?)", (procode, deleted))
    fpt_data.commit()
    script1 = "SELECT COUNT(*) FROM InFos"
    curs.execute(script1)
    numberOfRecord = curs.fetchone()[0]
    print("Number of processed records:", numberOfRecord)
    script2 = "SELECT * FROM InFos ORDER BY ProCode DESC LIMIT 3"

    print("\nProCode\tDeleted")
    for row in curs.execute(script2):
        print(row[0], row[1], sep= '\t')
    fpt_data.close()

except:
    print("File does not exist.")