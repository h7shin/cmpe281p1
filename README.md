# Project 1 

Hyunwook Shin

## TODO List
- S3 with MultiAZ Replication [Completed]
- Route53 S3 Failover Routing [Testing]
- Backend RDS Solution [Initialized]
- MySQL Database Setup
- Backend EC2 Instances [Initialized]
- Application Server
- Autoscale Group [Testing]
- ELB for Backend [Testing]
- Frontend EC2 Instances
- Frontend server (CSS/Javascript/Firewall)
- ELB for Frontend
- CloudFront [Initialized]

## Resources Info

### EC2 Instances (Backend)
Name | resource | type | group | private ip | public ip | availability zone | comment 
 -- | -- | -- | -- | -- | -- | -- | --
cmpe281p1b1 | EC2 | t | AutoScalingP1 | 172.31.8.190 | 13.58.128.114 |  us-east-2b | Compute Resource 1
cmpe281p1b2 | EC2 | t | AutoScalingP1 | 172.31.9.104 | 18.216.74.19 |  us-east-2a | Compute Resource 2

### Database 
Name | Resource | Type | Public DNS | Availability Zone | Comment 
-- | -- | -- | -- | -- | --
cmpe281p1db | RDS | MySQL | cmpe281p1db.cmqx6tpknayx.us-east-2.rds.amazonaws.com | us-east-2a | MySQL RDS Server

### Distribution

Name | Origin | OAI | Public DNS | Comment 
--   | --     | -- | -- | --
First Dist | shinhw2b1.s3.amazonaws.com | Enabled | de4hx48qic7v4.cloudfront.net | Distribution to First Bucket
Second Dist | shinhw2b2.s3.amazonaws.com | Enabled | d1ol4nkxls3lbv.cloudfront.net | Distribution to Second Bucket

### Health Monitoring (Route 53)
Name | Resource | Type | Monitors | Comment 
 -- | -- | -- |  -- | -- 
bucket1 heath | R53 | health check | shinhw2b1.s3.amazonaws.com | TCP Port 80 Health check on primary origin bucket
bucket2 heath | R53 | health check | shinhw2b2.s3.amazonaws.com | TCP Port 80 Health check on secondary origin bucket

### ELB Backend
Name | resource | type | availability zone | comment 
 -- | -- | -- | -- | -- 
BackendHTTP | ElB | application | us-east-2a, us-east-2b | ELB for Backend EC2 instances (b1 and b2)
