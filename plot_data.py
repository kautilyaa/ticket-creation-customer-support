import csv
import matplotlib.pyplot as plt

csv_filename = 'RPA_DATASET.csv'
csv_file = open(csv_filename, mode='r')
data_set = []
for row in list(csv.DictReader(csv_file)):
    data_set.append({'category': row['CATEGORY'], 'subject': row['REGARDING']})
csv_file.close()

stats_category = {}
stats_subject = {}
for row in data_set:
    if (not row['category'] in stats_category.keys()):
        stats_category[row['category']] = 0
    stats_category[row['category']] += 1
    if (not row['subject'] in stats_subject.keys()):
        stats_subject[row['subject']] = 0
    stats_subject[row['subject']] += 1

print(stats_category)

def plot_dict(d):
    x,y = d.keys(), d.values()
    plt.bar(x,y)
    plt.xticks(fontsize='8')
    plt.show()

plot_dict(stats_category)
plot_dict(stats_subject)

