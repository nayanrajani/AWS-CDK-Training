from aws_cdk import (
    aws_rds as rds,
    aws_ec2 as ec2,
    Stack, RemovalPolicy
)
from constructs import Construct


class CdkDBStack(Stack):

    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, RDSSG: [ec2.SecurityGroup], **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        db = rds.DatabaseInstance(self,
                                  "My-RDS-DB",
                                  allocated_storage=100,
                                  storage_type=rds.StorageType.GP2,
                                  allow_major_version_upgrade=False,
                                  engine=rds.DatabaseInstanceEngine.mysql(
                                      version=rds.MysqlEngineVersion.VER_5_7_40),
                                  # Error for VER_5_7_16= Resource handler returned message: "Cannot find version 5.7.16 for mysql (Service: Rds, Status Code: 400, Request ID: d8c8ca3a-9d42-4ae7-ae07-be2dd658519d)" (RequestToken: 9c12f285-abfe-60a5-2307-2b692d47cf83, HandlerErrorCode: InvalidRequest)
                                  instance_type=ec2.InstanceType.of(
                                      ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.SMALL),
                                  vpc=vpc,
                                  vpc_subnets=ec2.SubnetSelection(
                                      subnet_group_name="DB"),
                                  security_groups=RDSSG,
                                  multi_az=False,
                                  deletion_protection=False,
                                  removal_policy=RemovalPolicy.DESTROY
                                  )
