"""
CI/CD Pipeline diagram.
Generates: ci_cd_pipeline.png
"""

from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.container import Docker
from diagrams.onprem.vcs import Github
from diagrams.aws.compute import ECS, ECR, Fargate
from diagrams.aws.network import ELB


with Diagram("CI/CD Pipeline", filename="ci_cd_pipeline", show=False):
    repo = Github("GitHub Repo")

    with Cluster("GitHub Actions"):
        ci = GithubActions("CI Workflow")
        build = Docker("Build & Push")

    registry = ECR("Container Registry")

    with Cluster("Production"):
        lb = ELB("Load Balancer")
        with Cluster("ECS Cluster"):
            svc = ECS("Service")
            tasks = [Fargate("task-1"), Fargate("task-2")]

    repo >> Edge(label="push / PR") >> ci
    ci >> Edge(label="on success") >> build
    build >> Edge(label="push image") >> registry
    registry >> Edge(label="deploy") >> svc
    lb >> svc >> tasks
