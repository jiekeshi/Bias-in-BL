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


# workbook = xlrd.open_workbook("../../data/Bias_2.xlsx")
# names = workbook.sheet_names()
# worksheet = workbook.sheet_by_index(0)
# name = worksheet.col_values(0)[1:]
# status = worksheet.col_values(3)[1:]

# # bias_1_mis = ["ambari", "solr", "spark"]
bias_1_not_mis = ["ambari", "solr", "spark", "bigtop", "cassandra", "hbase", "hive", "sqoop", "tez", "zookeeper"]


n_aps = []
f_aps = []
p_aps = []


for proj in bias_1_not_mis:
    with open("./data/bias1_not_mis/" + proj + "/results.json") as f:
        predictions = json.load(f)
    hit_1 = 0
    mrr = 0
    map_ = 0
    ranks = []
    aps = []
    
    for nam, pred in predictions.items():
        ground_truths = pred["truth"]
        for index, result in enumerate(pred["results"]):
            temp = []
            if result in ground_truths:
                ranks.append(index + 1)
                file_nums = len(pred["results"])
                temp.append(1/(index + 1))
            if not len(temp) == 0:
                aps.append(sum(temp)/len(temp))


     # Hit @ 1 and MRR
    for i in ranks:
        if i == 1:
            hit_1 += 1
        mrr += 1.0/i
    print("MRR", mrr/len(ranks), "hit@1", hit_1/len(ranks), "MAP", mean(aps))

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

# print(cohend(f_aps, p_aps), cohend(p_aps, n_aps), cohend(f_aps, n_aps))
# U1, p = mannwhitneyu(f_aps, p_aps)
# print(p)
# U1, p = mannwhitneyu(p_aps, n_aps)
# print(p) 
# U1, p = mannwhitneyu(f_aps, n_aps)
# print(p) 




