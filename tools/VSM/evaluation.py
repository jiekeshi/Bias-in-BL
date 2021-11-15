import json
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Dataset", "Hit@1", "MRR", "MAP"]
bias_1_mis = ["ambari", "solr", "spark"]
bias_1_not_mis = ["ambari", "bigtop", "cassandra", "hbase", "hive", "solr", "spark", "sqoop", "tez", "zookeeper"]
for proj in bias_1_mis:
    with open("./data/bias1_mis/" + proj + "/results.json") as f:
        predictions = json.load(f)

    ranks = []
    aps = []
    for pred in predictions.values():
        ground_truths = pred["truth"]
        for index, result in enumerate(pred["results"]):
            temp = []
            if result in ground_truths:
                ranks.append(index + 1)
                file_nums = len(pred["results"])
                temp.append(1/(index + 1))
            if not len(temp) == 0:
                aps.append(sum(temp)/len(temp))

    hit_1 = 0
    mrr = 0
    map_ = 0

    for i in ranks:
        if i == 1:
            hit_1 += 1
        mrr += 1.0/i

    x.add_rows([[proj, round(hit_1/len(ranks), 4), round(mrr/len(ranks), 4), round(sum(aps)/len(aps), 4)]])
    # print("Hit@1: {}, MRR: {}".format(hit_1/len(ranks), mrr/len(ranks)), sum(aps)/len(aps))

print(x)

x = PrettyTable()
x.field_names = ["Dataset", "Hit@1", "MRR", "MAP"]

for proj in bias_1_not_mis:
    with open("./data/bias1_not_mis/" + proj + "/results.json") as f:
        predictions = json.load(f)

    ranks = []
    aps = []
    for pred in predictions.values():
        ground_truths = pred["truth"]
        for index, result in enumerate(pred["results"]):
            temp = []
            if result in ground_truths:
                ranks.append(index + 1)
                file_nums = len(pred["results"])
                temp.append(1/(index + 1))
            if not len(temp) == 0:
                aps.append(sum(temp)/len(temp))

    hit_1 = 0
    mrr = 0
    map_ = 0

    for i in ranks:
        if i == 1:
            hit_1 += 1
        mrr += 1.0/i

    x.add_rows([[proj, round(hit_1/len(ranks), 4), round(mrr/len(ranks), 4), round(sum(aps)/len(aps), 4)]])
    # print("Hit@1: {}, MRR: {}".format(hit_1/len(ranks), mrr/len(ranks)), sum(aps)/len(aps))

print(x)


