import json
from os import name
import xlrd
from scipy.stats import mannwhitneyu
# calculate the Cohen's d between two samples
from numpy.random import randn
from numpy.random import seed
from numpy import mean
from numpy import var
from math import sqrt
import copy


workbook = xlrd.open_workbook("../../data/Bias_2.xlsx")
names = workbook.sheet_names()
worksheet = workbook.sheet_by_index(0)
name = worksheet.col_values(0)[1:]
status = worksheet.col_values(3)[1:]

# # bias_1_mis = ["ambari", "solr", "spark"]
bias_1_not_mis = ["ambari", "solr", "spark", "bigtop", "cassandra", "hbase", "hive", "sqoop", "tez", "zookeeper"]


n_aps = []
f_aps = []
p_aps = []
f_id = []
n_id = []
p_id = []

for n, s in zip(name, status):
    if s == "Fully Localized":
        f_id.append(n)
    if s == "Not Localized":
        n_id.append(n)
    if s == "Partially Localized":
        p_id.append(n)


for proj in bias_1_not_mis:
    with open("./data/bias1_not_mis/" + proj + "/results.json") as f:
        predictions = json.load(f)
    
    ranks = []
    # f_aps = []
    
    for nam, pred in predictions.items():
        if nam.split(".")[0] in f_id:
            ground_truths = pred["truth"]
            for index, result in enumerate(pred["results"]):
                temp = []
                if result in ground_truths:
                    ranks.append(index + 1)
                    file_nums = len(pred["results"])
                    temp.append(1/(index + 1))
                if not len(temp) == 0:
                    f_aps.append(sum(temp)/len(temp))
    

    ranks = []
    # p_aps = []
    
    for nam, pred in predictions.items():
        if nam.split(".")[0] in p_id:
            ground_truths = pred["truth"]
            for index, result in enumerate(pred["results"]):
                temp = []
                if result in ground_truths:
                    ranks.append(index + 1)
                    file_nums = len(pred["results"])
                    temp.append(1/(index + 1))
                if not len(temp) == 0:
                    p_aps.append(sum(temp)/len(temp))
    
    ranks = []
    # p_aps = []
    
    for nam, pred in predictions.items():
        if nam.split(".")[0] in n_id:
            ground_truths = pred["truth"]
            for index, result in enumerate(pred["results"]):
                temp = []
                if result in ground_truths:
                    ranks.append(index + 1)
                    file_nums = len(pred["results"])
                    temp.append(1/(index + 1))
                if not len(temp) == 0:
                    n_aps.append(sum(temp)/len(temp))
    

    # # hit_1 = 0
    # # mrr = 0
    # # map_ = 0

    # # for i in ranks:
    # #     if i == 1:
    # #         hit_1 += 1
    # #     mrr += 1.0/i

    # # m_map = copy.deepcopy(aps)
    # # # print(m_map)
    # # # #x.add_rows([[proj, round(hit_1/len(ranks), 4), round(mrr/len(ranks), 4), round(sum(aps)/len(aps), 4)]])
    
    # # # # print("Hit@1: {}, MRR: {}".format(hit_1/len(ranks), mrr/len(ranks)), sum(aps)/len(aps))


    # # with open("./data/bias1_mis/" + proj + "/results.json") as f:
    # #     predictions = json.load(f)

    # # # ranks = []
    # # # aps = []
    # # for pred in predictions.values():
    # #     ground_truths = pred["truth"]
    # #     for index, result in enumerate(pred["results"]):
    # #         temp = []
    # #         if result in ground_truths:
    # #             ranks.append(index + 1)
    # #             file_nums = len(pred["results"])
    # #             temp.append(1/(index + 1))
    # #         if not len(temp) == 0:
    # #             aps.append(sum(temp)/len(temp))

    # # hit_1 = 0
    # # mrr = 0
    # # map_ = 0

    # # for i in ranks:
    # #     if i == 1:
    # #         hit_1 += 1
    # #     mrr += 1.0/i

    # n_map = aps

    # # function to calculate Cohen's d for independent samples
    def cohend(d1, d2):
        # calculate the size of samples
        n1, n2 = len(d1), len(d2)
        print(n2, n1)
        # calculate the variance of the samples
        s1, s2 = var(d1, ddof=0), var(d2, ddof=0)
        # calculate the pooled standard deviation
        s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
        
        # calculate the means of the samples
        u1, u2 = mean(d1), mean(d2)
        print(u2, u1)
        # calculate the effect size
        return (u2 - u1) / s

    # seed random number generator
    seed(1)
    # prepare data
    data1 = f_aps
    data2 = n_aps
    # calculate cohen's d
    d = cohend(data1, data2)
    print('Cohens d: %.10f' % d)
    U1, p = mannwhitneyu(data1, data2)
    print(p)

def cohend(d1, d2):
    # calculate the size of samples
    n1, n2 = len(d1), len(d2)
    print(n2, n1)
    # calculate the variance of the samples
    s1, s2 = var(d1, ddof=0), var(d2, ddof=0)
    # calculate the pooled standard deviation
    s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    
    # calculate the means of the samples
    u1, u2 = mean(d1), mean(d2)
    print(u2, u1)
    # calculate the effect size
    return (u2 - u1) / s

print(cohend(f_aps, p_aps), cohend(p_aps, n_aps), cohend(f_aps, n_aps))
U1, p = mannwhitneyu(f_aps, p_aps)
print(p)
U1, p = mannwhitneyu(p_aps, n_aps)
print(p) 
U1, p = mannwhitneyu(f_aps, n_aps)
print(p) 




