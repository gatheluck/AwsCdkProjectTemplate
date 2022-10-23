import sys

import aws_cdk as cdk

if sys.version_info >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final

from src.stacks.sample_minimal_lambda import SampleMinimalAppStack

app: Final = cdk.App()
SampleMinimalAppStack(app, "sample-minimal")

app.synth()
