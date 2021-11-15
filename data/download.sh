gdown https://drive.google.com/uc?id=1MaueUJCcPLHaJux8jTyVdBVhc55pO_y0
gdown https://drive.google.com/uc?id=1j5geXJQeIBGN-fcULYV-ZgEAeByjGofS
unzip Bias_1_not_misclassified.zip
unzip Bias_1_misclassified.zip
mkdir codebase
cd codebase
git clone https://github.com/apache/ambari.git
git clone https://github.com/apache/bigtop.git
git clone https://github.com/apache/cassandra.git
git clone https://github.com/apache/hbase.git
git clone https://github.com/apache/hive.git
git clone https://github.com/apache/solr.git
git clone https://github.com/apache/spark.git
git clone https://github.com/apache/sqoop.git
git clone https://github.com/apache/tez.git
git clone https://github.com/apache/zookeeper.git