import os
import pandas


columns = list('Atoms Step Temp PotEng KinEng Press Volume Density TotEng c_pern c_kern'.split())
data = []

with os.scandir('Sem1_dimers_data') as entries:
    for entry in entries:
        if entry.is_dir():
            continue
        if not entry.name.endswith('.log'):
            continue
        with open('Sem1_dimers_data/' + entry.name, 'r') as logfile:
            i = 0
            for line in logfile:
                if i < 58:
                    i += 1
                    continue
                subdata = list(map(float, line.split()))
                data.append(subdata)
                break

dframe = pandas.DataFrame(data, columns=columns)
dframe.to_csv('result_table.csv')

data2 = []
for col in columns:
    subdata2 = [sum(dframe[col]), sum(dframe[col]) / len(dframe[col]), dframe[col].std()]
    data2.append(subdata2)
tdata2 = [[data2[j][i] for j in range(len(data2))] for i in range(len(data2[0]))]
dframechars = pandas.DataFrame(tdata2, columns=columns, index=['Суммарное значение', 'Среднее значение',
                                                               'Среднеквадратическое отклонение'])
dframechars.to_csv('characteristics_table.csv')