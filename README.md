# mahout-elasticsearch-trial
Tryout mahout and elasticsearch POC on recommender system. Reference from <a href="https://www.mapr.com/products/mapr-sandbox-hadoop/tutorials/recommender-tutorial">https://www.mapr.com/products/mapr-sandbox-hadoop/tutorials/recommender-tutorial</a>

#### Hardware/Software tested with
1. Ubuntu 64bit 14.04
2. Elasticsearch 1.4.2
3. Maven 3.0.5
4. Apache Mahout 0.10.0

#### Setup procedure:
###### Elasticsearch 1.4.2
1. wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.4.2.deb
2. sudo dpkg -i elasticsearch-1.4.2.deb
3. Configure config file - sudo nano /etc/elasticsearch/elasticsearch.yml
```
- cluster.name: elasticsearch
- node.name: "My First Node"
- index.number_of_shards: 1
- index.number_of_replicas: 0
- path.data: /home/osboxes/Documents/elasticsearch-index
- network.bind_host: localhost
- http.cors.enabled: true
```
4. Start/Stop Elasticsearch: sudo /etc/init.d/elasticsearch start or stop 
 
###### Maven 3.0.5
1. sudo apt-get install maven

###### Apache Mahout 0.10.0
1. Download the <a href="http://mirror.nus.edu.sg/apache/mahout/0.10.0/mahout-distribution-0.10.0-src.tar.gz">Mahout</a> ~/Downloads
2. Untar mahout-distribution-0.10.0-src.tar.gz. Rename folder to mahout
3. sudo mv ~/Downloads/mahout /opt
4. cd /opt/mahout
5. mvn install
6. Add mahout to the environment variables
7. sudo nano /etc/environment
```
- MAHOUT_HOME=/opt/mahout/
- Append to PATH variable: $MAHOUT_HOME/bin
```
8. Save the file
9. source /etc/environment
