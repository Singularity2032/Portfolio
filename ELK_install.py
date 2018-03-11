#/bin/python
######################################
##Amari Matthews
## Script to download and install the ENTIRE ELK stack
##Written in python for modularity
##V:1
##Author: Sm0k3
##
##
######################################
import os
import http
import pwd
import sys
#Top Stack Variables

Elk_Address = ""
cluster_name = ""

#Starting the main program.
def main():
    get_user_id()
    install_java_requirements(get_user_id)
    system_update(get_user_id)
    install_elasticsearch(get_user_id)
    start_ElasticSearch_Service(get_user_id)
    configure_ElasticSearch(get_user_id)
    install_Kibana(get_user_id)
    configure_Kibana()




#Get userid
def get_user_id():
    pwd.getpwuid( os.getuid() ).pw_uid = userid
    if (userid != 0 ):
        print ("\n Please run as root.")
    else:
        print("\n Installing Java Requirements")

#Seeing if proper version of java is installed
def install_java_requirements():
    print("\n Lookin for the latest version of Java.")
    print ("\n The dashboard depends on it!")
    os.system("sudo java -v")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install openjdk-7-jre")
    print("\n[STATUS] Updating SYSTEM")

#Updating the system
def system_update():
    os.system("sudo apt-get update")
    print("[STATUS] Downloading Elasticsearch")
#Install Elasticsearch
def install_elasticsearch():
    print(*"\nDATA: Dowloading key for ELASTICSEARCH.......")
    os.system("wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -")
    os.system("echo "deb - http://packages.elastic.co/elasticsearch/2.x/debian stable main")
    os.system("sudo tee -a /etc/apt/sources.list.d/Elasticsearch-2/x.list")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install elastic search")

#Starting Elastic Search
def start_ElasticSearch_Service():
    #Typical service restart and update. 
    os.system("Sudo systemctl daemon-reload")
    os.system("sudo systemctl enable elasticsearch.service")
    os.system("sudo systemctl status elasticsearch.service")
    global cluster_name
    #This is the use for the global variable. The global set brings the 
    print("\nPlease chose a name for the Stack. Make it good!")
    print("\n P.S. You might want to write this down.")
    cluster_name = input("Enter a name for the new SIEM: ")
    print("\nDATA: The cluster name is now: ") + cluster_name + ("\n")
    print("[STATUS] Configuration of ElasticSearch")

#Set up Elasticsearch Configuration
def configure_ElasticSearch():
    "cluster.name" == True 
    #Opening the Elastic Seach configuration as read only
    with open("/etc/elasticsearch/elasticsearch.yml", "rt") as elasticConfig:
        #Opening a new elasticsearch configuration file as the new config
        with open("/etc/elasticsearch/elasticsearch.yml.new", "w") as newElasticConf:
            #for each line in the Elasticsearch config, conduct a search for a column that says cluster.name
            for line in elasticConfig:
                if "cluster.name" in line:
                    newElasticConf.write(line)
                    #and if it is in the line, rewrite the configuration file and replace the cluster.name with the name the user set
                elif "cluster.name" in line: 
                    newElasticConf.write("cluster.name:" + cluster_name +"\n")
              #   elif: "elasitcsearch.url" in line:
              #      newElasticConf.write(line.replace('')) 
                #else something is horrifficly wrong and the file is broken. It must be fixed manually.
                else:
                    #Attempting to write to the confiuration file with the following per line.
                    newElasticConf.write("\nhttp.cors.allow-origin: "/.*/" ")
                    newElasticConf.write("\nhttp.cors.enable: true")
                    newConf.write(line)
                    print("\nDATA: Please manually set the cluster name in /etc/elasticsearch/elasticsearh.yml")
                    #Removing the old elasticsearch configuration file
                    os.system("sudo rm -f /etc/elasticsearch/elasticsearch.yml")
                    os.system("sudo cp /etc/elasticsearch/elasticsearch.yml.new /etc/elasticsearch/elasticsearch.yml")
                    os.system("sudo rm -f /etc/elasticsearch/elasticsearch.yml.new")
                    #Restarting the elasticsearch service
                    os.system("sudo systemctl restart elasticsearch.service")
                    os.system("sudo systemctl status elasticsearch.service")
                    print("\n[STATUS]Installing Kibana")

#Install of Kibana
def install_Kibana():
    os.system("sudo apt-get install kibana")

#Configure Kibanna
def configure_Kibana():
    with open("/etc/kibana/kibana.yml", "rt") as kibanaConfig:
        with open("/etc/kibanna/kibanna.yml.new", "w")as newKibannaConf:
            for line in kibanaConfig:
                if "server.host:" in line == False:
                    print("\n[ERROR] Can't properly edit Kibanna config")
                    else:
                        newKibannaConf.write("server.host: "localhost" " + line.strip())
                        
os.system("sudo rm -f /etc/kibana/kibana.yml")
os.system("sudo cp /etc/kibana/kibana.yml.new /etc/kibana/kibana.yml")
os.system("sudo rm -f /etc/kibana/kibana.yml.new")

print("\n[STATUS]Starting ElasticSearch as a service")

#Installing Kibana as a service
def kibanna_Service():
    os.system("sudo systemctl restart kibana")
    os.system("sudo systemctl enable kibana")
    os.system("sudo systemctl status kibana")
    print ("\n Kibana is now runing on port 5601")



#Installing Logstash 
#def install_LogStash():
# os.system("deb http://packages.elastic.co/logstash/2.0/debian stable main" | sudo tee -a /etc/apt/sources.list)
# os.system("sudo apt-get update")
# os.system("sudo apt-get install logstash")
# os.system("sudo systemctl daemon-reload")
# os.system("sudo systemctl enable logstash.service")
# os.system("sudo systemctl status logstash.service")

#Configuring Logstash
#def connfigure_LogStash():
# os.system("cd /etc/logstash/conf.d")
# os.system("sudo touch 01-input.conf 10-syslog.conf 30-luberjack-output.conf")
#  with open("/etc/logstash/conf.d") as lumberjackConfig:
# with open("01-input.conf") as lumberjackInput01:
# for line in lumberjackInput01:
# lumberjackInput01.write (


main()





    
