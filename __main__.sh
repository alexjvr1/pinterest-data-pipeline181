#Create a .pem file locally that contains the local key for the key-pair to log onto AWS
#Change permission to be read only. This is a security feature and AWS will not connect if the permissions are anything otehr than read only  
chmod 400 *.pem

#Connect to the EC2 instance using ssh client
ssh -i "12d6e5017cf5-key-pair.pem" ec2-user@ec2-54-174-177-199.compute-1.amazonaws.com

#Set up Apache Kafka on the EC2 instance 
#1. install java if it is not yet installed
sudo yum install java-1.8.0

#2. install the same version as found on the AWS MSK cluster
wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz
tar -xzf kafka_2.12-2.8.1.tgz

#Set up IAM authentication
#1. install AWS MSK IAM authenticator
cd /home/ec2-user/kafka_2.12-2.8.1/libs
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.5/aws-msk-iam-auth-1.1.5-all.jar

#2. Set CLASSPATH used by Java to activate the AIM authenticator
export CLASSPATH=/home/ec2-user/kafka_2.12-2.8.1/libs/aws-msk-iam-auth-1.1.5-all.jar

#Create three topics
#Topic for Pinterest posts data
./kafka-topics.sh -bootstrap-server b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --command-config client.properties --create --topic 12d6e5017cf5.pin

#Topic for post geolocation data
./kafka-topics.sh -bootstrap-server b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --command-config client.properties --create --topic 12d6e5017cf5.geo

#Topic for post user data
./kafka-topics.sh -bootstrap-server b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098,b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098 --command-config client.properties --create --topic 12d6e5017cf5.user

#Connect MSK cluster to S3 bucket
##Create a custom plugin with MSK connect
###Install confluent.io
cd /home/ec2-user
wget https://d1i4a15mxbxib1.cloudfront.net/api/plugins/confluentinc/kafka-connect-s3/versions/10.0.3/confluentinc-kafka-connect-s3-10.0.3.zip

###Copy confluent.io to the user s3 bucket
aws s3 cp ./confluentinc-kafka-connect-s3-10.0.3.zip s3://user-12d6e5017cf5-bucket/kafka-connect-s3/

###Create a custom plugin on the MSK Connect console named 12d6e5017cf5-plugin
###Create a connector on the MSK Connect console named 12d6e5017cf5-connect
###Create a resource to allow PROXY integration in the user API on AWS
###Create an HTTP ANY method for the API and deploy it
###Modify the kafka-rest.properties file to allow IAM authentication to the MSK cluster

#Start the REST proxy on the EC2 machine
cd confluent-7.2.0/bin/
./kafka-rest-start /home/ec2-user/confluent-7.2.0/etc/kafka-rest/kafka-rest.properties


