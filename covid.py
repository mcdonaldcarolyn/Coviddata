
import csv
import matplotlib.pyplot as plt

filename = '/Users/carolynwhelpley/covid/data/massachusetts-history.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #print(index, column_header)

    cases = []
    for row in reader:
        print(row[4])
        print(".......")
        if (row[4]) != 0:
            case = (int(row[4]))
            cases.append(case)
        print(cases)
        

    plt.style.use('default')
    fig, ax = plt.subplots()
    ax.plot(cases, 'bo')
    #plt.axis([0, 200, 0, 7000])
    

    plt.title("Daily cases for MA, covid 19", fontsize=24)
    plt.xlabel(" ", fontsize=16)
    plt.ylabel("Case number", fontsize=16)
    plt.tick_params(axis='y', which='major', labelsize=16)
    #ax.set_ylim(0, 7000)

    plt.show()
