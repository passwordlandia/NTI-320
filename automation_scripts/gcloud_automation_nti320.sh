#!/bin/bash

echo "This is jwade005's NTI-320 GCloud Automation"

echo "Authorizing jwade005 for this project..."
gcloud auth login wadejonathan005@gmail.com --no-launch-browser

echo "Enabling billing..."
gcloud alpha billing accounts projects link final-test-project-2 --account-id=00CB7D-C97746-2D8BC1

echo "Setting admin account-id..."
gcloud config set account wadejonathan005@gmail.com

echo "Setting the project for Configuration..."
gcloud config set project final-test-project-2

echo "Setting zone/region for Configuration..."
gcloud config set compute/zone us-west1-a

gcloud config set compute/region us-west1

echo "Creating firewall-rules..."
gcloud compute firewall-rules create allow-http --description "Incoming http allowed." \
    --allow tcp:80

gcloud compute firewall-rules create allow-nrpe --description "Allow nrpe-server communication." \
    --allow tcp:5666

gcloud compute firewall-rules create allow-ldap --description "Incoming ldap allowed." \
    --allow tcp:636

gcloud compute firewall-rules create allow-postgresql --description "Posgresql allowed." \
    --allow tcp:5432

gcloud compute firewall-rules create allow-https --description "Incoming https allowed." \
    --allow tcp:443

gcloud compute firewall-rules create allow-django --description "Django test server connection allowed." \
    --allow tcp:8000

gcloud compute firewall-rules create allow-ftp --description "FTP Allowed." \
    --allow tcp:21


echo "Creating the rpmbuild-server instance and running the install script..."
gcloud compute instances create rpmbuild-server \
    --image-family centos-7 \
    --image-project centos-cloud \
    --machine-type f1-micro \
    --scopes cloud-platform \
    --metadata-from-file startup-script=/Users/Jonathan/Desktop/NET320/NTI-320/automation_scripts/rpm-install-centos7.sh \

echo "Creating the rsyslog-server instance and running the install script..."
gcloud compute instances create rsyslog-server \
    --image-family centos-7 \
    --image-project centos-cloud \
    --machine-type f1-micro \
    --scopes cloud-platform \
    --metadata-from-file startup-script=/Users/Jonathan/Desktop/NTI310/NTI-310/automation_scripts/rsyslog-server-install.sh \

echo "Creating the ldap-server instance and running the install script..."
gcloud compute instances create ldap-server \
    --image-family centos-7 \
    --image-project centos-cloud \
    --machine-type f1-micro \
    --scopes cloud-platform \
    --metadata-from-file startup-script=/Users/Jonathan/Desktop/NTI310/NTI-310/automation_scripts/ldap-server-install.sh \

echo "Creating the nfs-server and running the install script..."
gcloud compute instances create nfs-server \
    --image-family centos-7 \
    --image-project centos-cloud \
    --machine-type f1-micro \
    --scopes cloud-platform \
    --metadata-from-file startup-script=/Users/Jonathan/Desktop/NTI310/NTI-310/automation_scripts/nfs-server-install.sh \

echo "Creating the postgres-a-test server and running the install script..."
gcloud compute instances create postgres-a-test \
    --image-family centos-7 \
    --image-project centos-cloud \
    --machine-type f1-micro \
    --scopes cloud-platform \
    --metadata-from-file startup-script=/Users/Jonathan/Desktop/NTI310/NTI-310/automation_scripts/postgres-install.sh \

echo "Creating the django-a-test server and running the install script..."
gcloud compute instances create django-a-test \
    --image-family centos-7 \
    --image-project centos-cloud \
    --machine-type f1-micro \
    --scopes cloud-platform \
    --metadata-from-file startup-script=/Users/Jonathan/Desktop/NTI310/NTI-310/automation_scripts/apache-django-install.sh \

sleep 120

# add script to add nrpe to each isntance (nagios-remote-istall-yum.sh)

# add wrapper script addon to startup scripts to create nagios config files for each instances (using genconfig_wrapper.sh)

# add scp commands to send nagios config files to the nagios server and test configuration (using gcloud_scp_nagios.sh)

# add for loops to add yum repository to each instance (using add_yum_repo.sh)


# exmaple for loop
# [root@test-vm-a Jonathan]# for i in $( gcloud compute instances list --zones us-west1-a | awk '{print $1}' | grep -v "NAME" );\
# >  do gcloud compute ssh --zone us-west1-a Jonathan@$i --command "touch jonathan.txt";\
# > done;


echo "Jwade005's Google Cloud NTI-320 Final Project Automatic Installation Complete. :)"
