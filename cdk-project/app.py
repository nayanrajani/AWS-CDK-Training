#!/usr/bin/env python3

import aws_cdk as cdk

# from cdk_project.cdk_training_stack import CdkTrainingStack
from cdk_project.cdk_network_stack import CdkNetworkStack
from cdk_project.cdk_server_stack import CdkServerStack
from cdk_project.cdk_security_stack import CdkSecurityStack
from cdk_project.cdk_alb_stack import CdkALBStack
from cdk_project.cdk_db_stack import CdkDBStack
from cdk_project.cdk_s3_stack import CdkS3Stack


app = cdk.App()


# CdkTrainingStack(app, "cdk-training")
vpcstack = CdkNetworkStack(app, "cdknetworkstack")
securitystack = CdkSecurityStack(app, "cdksecuritystack", vpc=vpcstack.vpc)
serverstack = CdkServerStack(app, "cdkserverstack", vpc=vpcstack.vpc,
                             ServerSG=securitystack.ServerSG, PrivateServerSG=securitystack.PrivateServerSG)
lbstack = CdkALBStack(app, "cdkalbstack", vpc=vpcstack.vpc,
                      serveralbsg=securitystack.serveralbsg, privatealbsg=securitystack.privatealbsg, server1=serverstack.server1, server2=serverstack.server2, server3=serverstack.server3, server4=serverstack.server4)
dbstack = CdkDBStack(app, "cdkdbstack", vpc=vpcstack.vpc,
                     RDSSG=[securitystack.RDSSG])

s3buckets = CdkS3Stack(app, "cdks3stack")

app.synth()
