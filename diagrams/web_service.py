"""
Web Service Architecture diagram.
Generates: web_service.png
"""

from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, CloudFront, Route53
from diagrams.aws.storage import S3

with Diagram("Web Service Architecture", filename="web_service", show=False):
    dns = Route53("DNS")
    cdn = CloudFront("CDN")
    assets = S3("Static Assets")

    with Cluster("Load Balanced Web Tier"):
        lb = ELB("Load Balancer")
        with Cluster("Auto Scaling Group"):
            asg = AutoScaling("ASG")
            web_servers = [EC2("web-1"), EC2("web-2"), EC2("web-3")]

    cache = ElastiCache("Cache")

    with Cluster("Database Tier"):
        primary = RDS("Primary DB")
        replica = RDS("Read Replica")
        primary - replica

    dns >> cdn >> lb >> web_servers
    cdn >> assets
    web_servers >> cache
    web_servers >> primary
