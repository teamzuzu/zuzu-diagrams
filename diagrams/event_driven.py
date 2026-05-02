"""
Event-Driven Microservices diagram.
Generates: event_driven.png
"""

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.network import APIGateway

with Diagram("Event-Driven Microservices", filename="event_driven", show=False):
    api = APIGateway("API Gateway")
    bus = Eventbridge("Event Bus")

    with Cluster("Order Service"):
        order_fn = Lambda("order-handler")
        order_db = Dynamodb("orders")
        order_queue = SQS("order-queue")

    with Cluster("Notification Service"):
        notify_fn = Lambda("notify-handler")
        notify_topic = SNS("notifications")

    with Cluster("Analytics Service"):
        analytics_fn = Lambda("analytics-handler")
        analytics_db = Dynamodb("analytics")

    api >> order_fn >> order_db
    order_fn >> Edge(label="publish") >> bus
    bus >> order_queue >> notify_fn >> notify_topic
    bus >> analytics_fn >> analytics_db
