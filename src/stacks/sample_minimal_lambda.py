import sys

from aws_cdk import Duration, Stack, aws_apigateway, aws_lambda
from constructs import Construct

if sys.version_info >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final


class SampleMinimalAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(scope, construct_id, **kwargs)

        _api: Final = aws_apigateway.RestApi(
            self,
            "sample_minimal_app_rest_api",
            rest_api_name="sample_minimal_app_api",
        )

        _lambda: Final = aws_lambda.DockerImageFunction(
            self,
            "sample-minimal-lambda-container",
            function_name="sample_minimal_lambda_app_api",
            code=aws_lambda.DockerImageCode.from_image_asset(
                build_args={},
                directory="src/sample_minimal_lambda/",
                target="lambda",
                cmd=["handlers.sample_minimal_handler"],
            ),
            timeout=Duration.seconds(120),
            memory_size=2048,
        )

        _api.root.add_resource(path_part="sample").add_method(
            "GET",
            aws_apigateway.LambdaIntegration(_lambda),
        )
