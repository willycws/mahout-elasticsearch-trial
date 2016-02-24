# mahout-elasticsearch-trial
Tryout mahout and elasticsearch POC on recommender system. Reference from <a href="https://www.mapr.com/products/mapr-sandbox-hadoop/tutorials/recommender-tutorial">https://www.mapr.com/products/mapr-sandbox-hadoop/tutorials/recommender-tutorial</a>

Hardware/Software tested with:
-Ubuntu 64bit 14.04
-Elasticsearch 1.4.2
-Maven 3.0.5
-Apache Mahout 0.10.0

Setup procedure:
-Elasticsearch 1.4.2
  1. wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.4.2.deb
  2. sudo dpkg -i elasticsearch-1.4.2.deb
  3. Configure config file - sudo nano /etc/elasticsearch/elasticsearch.yml
  4. --------cluster.name: elasticsearch
  5. --------node.name: "My First Node"
  6. --------index.number_of_shards: 1
  7. --------index.number_of_replicas: 0
  8. --------path.data: /home/osboxes/Documents/elasticsearch-index
  9. --------network.bind_host: localhost
  10. --------http.cors.enabled: true
  11. Start/Stop Elasticsearch: sudo /etc/init.d/elasticsearch start or stop 
