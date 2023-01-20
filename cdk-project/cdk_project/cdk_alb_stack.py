from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as elbv2_target,
    aws_ec2 as ec2,
    Stack
)
from constructs import Construct


class CdkALBStack(Stack):

    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, serveralbsg: ec2.SecurityGroup, server1: ec2.Instance, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ec2alb = elbv2.ApplicationLoadBalancer(
            self, "EC2ALB",
            load_balancer_name="EC2ALB",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC),
            internet_facing=True,
            security_group=serveralbsg
        )
        listener = ec2alb.add_listener(
            "http",
            port=80,
            open=True
        )

        listener.add_targets(
            'ec2albtarget',
            port=80,
            targets=[elbv2_target.InstanceTarget(server1, 80)]
        )
