import os

from aws_cdk import (
    core as cdk,
    aws_lambda,
    aws_apigateway,
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class ServiceStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        flask_handler = aws_lambda.Function(
            self,
            'FlaskHandler',
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.asset('lambda/' + os.environ['ZAPPA_LAMBDA_PACKAGE']),
            handler='handler.lambda_handler',
            timeout=core.Duration.seconds(15),
        )

        aws_apigateway.LambdaRestApi(
            self,
            'Endpoint',
            handler=flask_handler,
        )


