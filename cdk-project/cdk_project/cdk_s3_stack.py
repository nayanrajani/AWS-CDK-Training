import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3
)


class CdkS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        mybucket = s3.Bucket(
            self,
            bucket_name="my-cdk-training-bucket",
            id="cdk-training-id",
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            versioned=False,
        )
