## CMPE282 Project 1

- *University Name*: http://www.sjsu.edu/
- *Course*: Cloud Technologies
- *Professor* Sanjay Garje
- *ISA*: Divyankitha Urs
- *Student*: Hyunwook Shin https://www.linkedin.com/in/hwshin/

ID: 012507417

## Project Introduction

This is a GitHub repository containing the project used to deploy
highly-available and scalable web application designed for uploading
photos and pictures to the cloud. The user can choose to upload
a file, replace the same file with another content, edit file
information such as file name or description, delete file.

URL : elbfrontend.hyunwookshin.com

## How to build artifacts from source

- Clone this repo
- Go inside `src` source directory
- Run `make all`
- Verify that two artifacts are present (frontend and backend)
- Deploy the artifacts to EC2 instances using the installer scripts
- The installer scripts are found in package-level directories (frontend/backend)
- Please run the script as root user (`sudo su`) due to permission issues

```
ec2-instance$ ls

installer cmpe281p1.tgz

ec2-instance$ sudo su
ec2-instance# ./installer <tgz-file>

<server should be running immediately>

```

## Complete Features and Specification

- *Frontend* Three Pages, Main(list) page, Update page, delete page (JS/HTML/CSS/PHP)
- *Storage* Cross-region Replication Backend Storage in S2
- *Delivery/Network* Zero Downtime Maintenance of Content Delivery using Route 53
- *UX* Cache invalidation upon deletion and update using Lambda
- *Latency* Transfer acceleration for uploading files to S3
- *Transactions* Maximizing TPS using Hashes for Bucket Keys
- *Health Monitoring* Using cloudwatch monitoring of Autoscale Group via metrics
- *Failover and Load Balancing* Load balaners for Frontend and Backend Servers

## Source code organization

- Source are orgnizaed into packages under src
- `backend` contains the backend application server code (Python)
- `rdshandle` contains the RDS/MySQL thin wrapper
- `frontend` contains the PHP/Javascript/Python for frontend
- `cachehandle` lambda function for cache invalidation

## Core AWS Requirements and Components

- S3 with MultiAZ Replication [Completed]
- Route53 S3 Failover Routing [Completed]
- Backend RDS Solution [Completed]
- MySQL Database Setup [Completed]
- Backend EC2 Instances [Completed]
- Application Server [Completed]
- Autoscale Group [Completed]
- ELB for Backend [Completed]
- Frontend EC2 Instances [Completed]
- Frontend server (CSS/Javascript/Firewall) [Completed]
- ELB for Frontend [Completed]
- CloudFront [Completed]

## Resources Inventory

The following is a high level inventory of the resources used
for the is project. The exact details such as ip address or names may
have changed over time after subsequent iterations

### EC2 Instances (Backend)
The following are the EC2 compute resources for application servers.

Name | resource | type | group | private ip | public ip | availability zone | comment
 -- | -- | -- | -- | -- | -- | -- | --
cmpe281p1b1 | EC2 | t | AutoScalingP1 | 172.31.8.190 | 13.58.128.114 |  us-east-2b | Compute Resource 1
cmpe281p1b2 | EC2 | t | AutoScalingP1 | 172.31.9.104 | 18.216.74.19 |  us-east-2a | Compute Resource 2

### EC2 Instances (Frontend Backend)
The following are EC2 compute resouces (nano) for the frontend webservers (Apache)

Name | resource | type | group | private ip | public ip | availability zone | comment
 -- | -- | -- | -- | -- | -- | -- | --
cmpe281p1f1 | EC2 | t | AutoScalingP1-Frontend| 172.31.15.66 | 52.15.216.157 |  us-east-2a | Compute Resource 1
cmpe281p1f2 | EC2 | t | AutoScalingP1-Frontend | 172.31.26.154 | 18.221.67.155 |  us-east-2b | Compute Resource 2

### Database
The single AZ for the project.

Name | Resource | Type | Public DNS | Availability Zone | Comment:
---- | -- | -- | -- | -- | --
cmpe281p1db | RDS | MySQL | cmpe281p1db.cmqx6tpknayx.us-east-2.rds.amazonaws.com | us-east-2a | MySQL RDS Server

### Distribution
The following is the two Content distribution network for the project.

Name | Origin | OAI | Public DNS | Comment
--   | --     | -- | -- | --
First Dist | shinhw2b1.s3.amazonaws.com | Enabled | de4hx48qic7v4.cloudfront.net | Distribution to First Bucket
Second Dist | shinhw2b2.s3.amazonaws.com | Enabled | d1ol4nkxls3lbv.cloudfront.net | Distribution to Second Bucket

### Health Monitoring (Route 53m CloudWatch)
The health monitoring below is used by Route 53 (See Failover Route)

Name | Resource | Type | Monitors | Comment
 -- | -- | -- |  -- | --
bucket1 heath | R53 | health check | shinhw2b1.s3.amazonaws.com | TCP Port 80 Health check on primary origin bucket
bucket2 heath | R53 | health check | shinhw2b2.s3.amazonaws.com | TCP Port 80 Health check on secondary origin bucket

### Failover Route (Route 53)
The following are the two Route 53 records for Cloudfront

CNAME | FQDN | Target | Health Check
 --   |  --  |  --    | --
dist1 | dist1.hyunwookshin.com | de4hx48qic7v4.cloudfront.net | bucket1 health
dist1 | dist1.hyunwookshin.com | d1ol4nkxls3lbv.cloudfront.net | bucket2 health

### ELB Backend
The following are ELB backend load balancers for handling traffics to the frontend and backend application servers.

Name | resource | type | availability zone | comment
 -- | -- | -- | -- | --
BackendHTTP | ElB | application | us-east-2a, us-east-2b | ELB for Backend EC2 instances (b1 and b2)
FrontndHTTP | ElB | application | us-east-2a, us-east-2b | ELB for Backend EC2 instances (f1 and f2)
