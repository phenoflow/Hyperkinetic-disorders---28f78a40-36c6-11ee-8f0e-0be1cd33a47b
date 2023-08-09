# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"8BPT.00","system":"readv2"},{"code":"E2E1.00","system":"readv2"},{"code":"E2Ez.00","system":"readv2"},{"code":"Eu90z00","system":"readv2"},{"code":"Eu90z12","system":"readv2"},{"code":"101067.0","system":"med"},{"code":"107332.0","system":"med"},{"code":"108002.0","system":"med"},{"code":"1458.0","system":"med"},{"code":"25469.0","system":"med"},{"code":"33505.0","system":"med"},{"code":"3775.0","system":"med"},{"code":"41769.0","system":"med"},{"code":"45263.0","system":"med"},{"code":"45799.0","system":"med"},{"code":"50015.0","system":"med"},{"code":"52602.0","system":"med"},{"code":"58069.0","system":"med"},{"code":"6510.0","system":"med"},{"code":"6512.0","system":"med"},{"code":"6519.0","system":"med"},{"code":"96770.0","system":"med"},{"code":"9715.0","system":"med"},{"code":"97421.0","system":"med"},{"code":"9972.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hyperkinetic-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hyperkinetic-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hyperkinetic-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hyperkinetic-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
