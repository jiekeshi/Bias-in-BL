### Bias1

VSM:

| Project | MAP(Mis) | MAP(Remove_Mis) | Difference | d     |
| ------- | -------- | --------------- | ---------- | ----- |
| Ambari  | 0.159    | 0.158           | -0.63%     | 0.004 |
| Solr    | 0.875    | 0.833           | -4.80%     | 0.157 |
| Spark   | 0.361    | 0.364           | -0.83%     | 0.008 |



IncBL

| Project | MAP(Mis) | MAP(Remove_Mis) | Difference | d     |
| ------- | -------- | --------------- | ---------- | ----- |
| Ambari  | 0.220    | 0.222           | -0.91%     | 0.005 |
| Solr    | 1.000    | 1.000           | 0%         | 0     |
| Spark   | 0.489    | 0.489           | 0%         | 0     |

### Bias2



| Project   | Fully       | Partially | Not          |
| --------- | ----------- | --------- | ------------ |
| Ambari    | 426(20.96%) | 15(0.74%) | 1591(78.30%) |
| Spark     | 86(29.45%)  | 0         | 206(70.55%)  |
| Cassandra | 1(0.1%)     | 0         | 10(90.90%)   |
| Hbase     | 4(57.14%)   | 0         | 3(42.86%)    |
| Hive      | 3(20%)      | 0         | 12(80%)      |
| Bigtop    | 0           | 0         | 4(100%)      |
| Solr      | 0           | 0         | 3 (100%)     |
| Sqoop     | 0           | 0         | 1(100%)      |
| Tez       | 0           | 0         | 1(100%)      |
| Zookeeper | 1(100%)     | 0         | 0            |



IncBL:

| Project   | Fully | Partially | Not   |
| --------- | ----- | --------- | ----- |
| Ambari    | 0.287 | 0.137     | 0.206 |
| Spark     | 0.584 | 0         | 0.448 |
| Cassandra | 1.000 | 0         | 0.551 |
| Hbase     | 0.875 | 0         | 0.444 |
| Hive      | 1.000 | 0         | 0.635 |
| Bigtop    | 0     | 0         | 0.550 |
| Solr      | 0     | 0         | 1.000 |
| Sqoop     | 0     | 0         | 1.000 |
| Tez       | 0     | 0         | 0.500 |
| Zookeeper | 1.000 | 0         | 0     |



VSM

| Project   | Fully | Partially | Not   |
| --------- | ----- | --------- | ----- |
| Ambari    | 0.224 | 0.118     | 0.141 |
| Spark     | 0.458 | 0         | 0.325 |
| Cassandra | 1.000 | 0         | 0.388 |
| Hbase     | 0.875 | 0         | 0.666 |
| Hive      | 1.000 | 0         | 0.564 |
| Bigtop    | 0     | 0         | 0.424 |
| Solr      | 0     | 0         | 0.833 |
| Sqoop     | 0     | 0         | 1.000 |
| Tez       | 0     | 0         | 0.500 |
| Zookeeper | 1.000 | 0         | 0     |



VSM:

|             | Fully-Partial |      |            | Partially-Not |      |            | Fully-Not |       |            |
| ----------- | ------------- | ---- | ---------- | ------------- | ---- | ---------- | --------- | ----- | ---------- |
| **Project** | P-value       | d    | Eﬀect Size | P-value       | d    | Eﬀect Size | P-value   | d     | Eﬀect Size |
| Ambari      | 0.0004        | 0.33 | small      | 0.1369        | 0.09 | trivial    | 1.180e-15 | 0.293 | small      |
| Spark       |               |      |            |               |      |            | 0.0004    | 0.365 | small      |
| Hbase       |               |      |            |               |      |            | 0.2071    | 0.928 | large      |
| Hive        |               |      |            |               |      |            | 0.1020    | 1.180 | large      |
| Cassandra   |               |      |            |               |      |            | 0.1309    | 1.799 | very large |





IncBL

|             | Fully-Partial |      |            | Partially-Not |       |            | Fully-Not |       |            |
| ----------- | ------------- | ---- | ---------- | ------------- | ----- | ---------- | --------- | ----- | ---------- |
| **Project** | P-value       | d    | Eﬀect Size | P-value       | d     | Eﬀect Size | P-value   | d     | Eﬀect Size |
| Ambari      | 0.0002        | 0.44 | small      | 0.0583        | 0.219 | small      | 9.185e-13 | 0.253 | small      |
| Spark       |               |      |            |               |       |            | 0.0002    | 0.367 | small      |
| Hbase       |               |      |            |               |       |            | 0.0429    | 2.462 | very large |
| Hive        |               |      |            |               |       |            | 0.1318    | 1.009 | large      |
| Cassandra   |               |      |            |               |       |            | 0.2029    | 1.145 | large      |



### Bias3

IncBL

| Project | Dirty | Clean | Difference | d     |
| ------- | ----- | ----- | ---------- | ----- |
| Ambari  | 0.142 | 0.159 | 11.97%     | 0.063 |
| Spark   | 0.515 | 0.5   | -2.91%     | 0.051 |

VSM

| Project | Dirty | Clean | Difference | d     |
| ------- | ----- | ----- | ---------- | ----- |
| Ambari  | 0.106 | 0.123 | 16.03%     | 0.067 |
| Spark   | 0.145 | 0.202 | 39.31%     | 0.479 |