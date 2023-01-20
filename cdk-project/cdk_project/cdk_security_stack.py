from aws_cdk import (
    aws_ec2 as ec2,
    Stack
)
from constructs import Construct


class CdkSecurityStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.serveralbsg = ec2.SecurityGroup(self, 'Ec2LBSG',
                                             security_group_name='alb-sg',
                                             vpc=vpc,
                                             description='Ec2 ALB',
                                             allow_all_outbound=True
                                             )
        self.serveralbsg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            'allow from anywhere on port 80'
        )

        self.ServerSG = ec2.SecurityGroup(self, 'Server-1-SG',
                                          security_group_name='Server-1-SG',
                                          vpc=vpc,
                                          allow_all_outbound=True
                                          )
        self.ServerSG.connections.allow_from(
            self.serveralbsg,
            ec2.Port.tcp(80),
            'Allow only from LoadBalancer on 80'
        )
