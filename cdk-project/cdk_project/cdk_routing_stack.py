from constructs import Construct
from aws_cdk import (
    Stack,
    aws_route53 as r53,
    aws_elasticloadbalancing as lb
)


class CdkRoutingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
