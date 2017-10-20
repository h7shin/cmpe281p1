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
Name | Resource | Type | Group | Public DNS | Private IP | Public IP | Availability Zone | Comment 
-- | -- | -- | -- | -- | -- | -- | -- | --
cmpe281p1b1 | EC2 | t | AutoScalingP1 || 172.31.8.190 | 13.58.128.114 |  us-east-2b | Compute Resource 1
cmpe281p1b2 | EC2 | t | AutoScalingP1 || 172.31.9.104 | 18.216.74.19 |  us-east-2a | Compute Resource 2
cmpe281p1db | RDS | MySQL || cmpe281p1db.cmqx6tpknayx.us-east-2.rds.amazonaws.com ||| us-east-2a | MySQL RDS Server
origin-Primary | R53 | CNAME || origin.shincloudhw.info | shinhw2b1.s3.amazonaws.com ||| Origin Primary Failover Routing Policy
origin-Secondary | R53 | CNAME || origin.shincloudhw.info | shinhw2b2.s3.amazonaws.com ||| Origin Secondary Failover Routing Policy
bucket1 heath | R53 | health check | | shinhw2b1.s3.amazonaws.com |||| TCP Port 80 Health check on primary origin bucket
bucket2 heath | R53 | health check | | shinhw2b2.s3.amazonaws.com |||| TCP Port 80 Health check on secondary origin bucket
