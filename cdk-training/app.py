#!/usr/bin/env python3

import aws_cdk as cdk

# from cdk_training.cdk_training_stack import CdkTrainingStack
# from cdk_training.cdk_network_stack import CdkNetworkStack
from cdk_training.cdk_server_stack import CdkServerStack

app = cdk.App()
# CdkTrainingStack(app, "cdk-training")
# CdkNetworkStack(app, "cdknetworkstack")
CdkServerStack(app, "cdkserverstack")

app.synth()
