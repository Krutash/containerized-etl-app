Create a sqlLite3 Instance
Populate it with data

Create a Flask App for enabling API based access to the data
---> Why Flask? : > sqlLite is not server based, it's file DB
---> using Flask + sqlite instance we can containerize it

Create a MySQL server and deploy it on docker container
create data transfer lines from SQLite DB to MySQL
---> easy migration in container env.
---> isolated envs make failures isolated

Create a HDFS system and deploy it on docker
Default replication set to 3 datanodes

Create a scala ETL pipeline in spark
---> Read data from DB
---> Transform it in ETL cluster
---> Load it in HDFS storage


Designed and deployed a modular data pipeline using Dockerized services, including a Scala-based Spark ETL job to extract data from a MySQL container and load it into a distributed HDFS cluster.
Built a Java-based microservice API to dynamically trigger ETL jobs with configurable parameters like table name.
Integrated a Python Flask application as an optional lightweight data source via REST, and automated the pipeline using Docker Compose for local orchestration and testing.
