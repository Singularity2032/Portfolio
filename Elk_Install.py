######################################
## ADM
## Script to download and install the ENTIRE ELK stack
##Written in python for modularity
##V:1
##Author: Sm0k3
##
##
######################################
import os

#Top Stack Variables

Elk_Address = ""
cluster_name = ""




#Seeing if proper version of java is installed
def install_java_requirements():
    print "\n Lookin for the latest version of Java."
    print "\n The dashboard depends on it!"
    os.system("sudo java -v")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install openjdk-7-jre")

#Updating the system
def system_update():
    os.system("sudo apt-get update")

#Install Elasticsearch
def install_elasticsearch():
    print "\nDATA: Dowloading key for ELASTICSEARCH......."
    os.system("wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -")
    os.system("echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/Elasticsearch-2/x.list")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install elastic search")

#Starting Elastic Search
def start_ElasticSearch_Service():
    os.system("Sudo systemctl daemon-reload")
    os.system("sudo systemctl enable elasticsearch.service")
    os.system("sudo systemctl status elasticsearch.service")
    global cluster_name
    print "\nPlease chose a name for the Stack. Make it good!"
    print "\n P.S. You might want to write this down."
    cluster_name = raw_input("Enter a name for the new SIEM:")
    print "\nDATA: The cluster name is now: " + cluster_name + "\n"

#Set up Elasticsearch Configuration
def configure_ElasticSearch():
    with open("/etc/elasticsearch/elasticsearch.yml", "rt") as elasticConfig:
        with open("/etc/elasticsearch/elasticsearch.yml.new", "w") as newConf:
            for line in elasticConfig:
                if "cluster.name" in line:
                    newConf.write(line)
                    newConf.write("\ncluster.name:" + cluster_name +"\n")
                elif 
