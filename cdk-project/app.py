#!/usr/bin/env python3

import aws_cdk as cdk

# from cdk_project.cdk_training_stack import CdkTrainingStack
from cdk_project.cdk_network_stack import CdkNetworkStack
from cdk_project.cdk_server_stack import CdkServerStack
from cdk_project.cdk_security_stack import CdkSecurityStack
from cdk_project.cdk_alb_stack import CdkALBStack

app = cdk.App()
# CdkTrainingStack(app, "cdk-training")
vpcstack = CdkNetworkStack(app, "cdknetworkstack")
securitystack = CdkSecurityStack(app, "cdksecuritystack", vpc=vpcstack.vpc)
serverstack = CdkServerStack(app, "cdkserverstack", vpc=vpcstack.vpc,
                             ServerSG=securitystack.ServerSG)
lbstack = CdkALBStack(app, "cdkalbstack", vpc=vpcstack.vpc,
                      serveralbsg=securitystack.serveralbsg, server1=serverstack.server1)


app.synth()
