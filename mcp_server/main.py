# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:57:47+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    IncerCertificatePostRequest,
    IncerCertificatePostResponse,
    IncerCertificatePostResponse1,
    IncerCertificatePostResponse2,
    IncerCertificatePostResponse3,
    IncerCertificatePostResponse4,
    IncerCertificatePostResponse5,
    IncerCertificatePostResponse6,
    RmcerCertificatePostRequest,
    RmcerCertificatePostResponse,
    RmcerCertificatePostResponse1,
    RmcerCertificatePostResponse2,
    RmcerCertificatePostResponse3,
    RmcerCertificatePostResponse4,
    RmcerCertificatePostResponse5,
    RmcerCertificatePostResponse6,
    RscerCertificatePostRequest,
    RscerCertificatePostResponse,
    RscerCertificatePostResponse1,
    RscerCertificatePostResponse2,
    RscerCertificatePostResponse3,
    RscerCertificatePostResponse4,
    RscerCertificatePostResponse5,
    RscerCertificatePostResponse6,
    SicrdCertificatePostRequest,
    SicrdCertificatePostResponse,
    SicrdCertificatePostResponse1,
    SicrdCertificatePostResponse2,
    SicrdCertificatePostResponse3,
    SicrdCertificatePostResponse4,
    SicrdCertificatePostResponse5,
    SicrdCertificatePostResponse6,
)

app = MCPProxy(
    description="eDistrict Chandigarh(http://chdservices.gov.in/) is the online service delivery portal for Chandigarh Administration. Certain documents issued by it (e.g. Senior Citizen Identity Card) can be pulled into citizens' DigiLocker accounts.",
    termsOfService='https://apisetu.gov.in/terms.php',
    title='eDistrict Chandigarh, Chandigarh',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/ditch/v3'}],
)


@app.post(
    '/incer/certificate',
    description=""" API to verify Income Certificate. """,
    tags=['certificate_requests'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def incer(body: IncerCertificatePostRequest = None):
    """
    Income Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/rmcer/certificate',
    description=""" API to verify Marriage Certificate. """,
    tags=['certificate_requests'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def rmcer(body: RmcerCertificatePostRequest = None):
    """
    Marriage Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/rscer/certificate',
    description=""" API to verify Residence Certificate. """,
    tags=['certificate_requests'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def rscer(body: RscerCertificatePostRequest = None):
    """
    Residence Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sicrd/certificate',
    description=""" API to verify Senior Citizen Identity Card/ Certificate. """,
    tags=['certificate_requests'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def sicrd(body: SicrdCertificatePostRequest = None):
    """
    Senior Citizen Identity Card/ Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
