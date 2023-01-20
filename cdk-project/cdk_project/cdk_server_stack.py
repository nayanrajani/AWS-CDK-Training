from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    Stack
)
import base64
from constructs import Construct

with open("./userdata.sh") as f:
    user_data = f.read()


class CdkServerStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc=ec2.Vpc, ServerSG=ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Instance Role and SSM Managed Policy
        role = iam.Role(self, "InstanceSSM",
                        assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(
            "AmazonSSMManagedInstanceCore"))
        self.server1 = ec2.Instance(self, "server1",
                                    instance_name="server1",
                                    instance_type=ec2.InstanceType("t2.micro"),
                                    vpc=vpc,
                                    vpc_subnets=ec2.SubnetSelection(
                                          subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
                                    machine_image=ec2.MachineImage.latest_amazon_linux(
                                        virtualization=ec2.AmazonLinuxVirt.HVM),
                                    security_group=ServerSG,
                                    user_data=ec2.UserData.custom(user_data),
                                    role=role,
                                    )
