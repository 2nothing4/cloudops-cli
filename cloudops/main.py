#!/usr/bin/env python3
import boto3
import click


def get_client(service):
    return boto3.client(
        service,
        endpoint_url="http://localhost:4566",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1"
    )


@click.group()
def cli():
    """CloudOps CLI — AWS resource manager via LocalStack"""
    pass


@cli.command()
def health():
    """Check LocalStack health"""
    try:
        response = get_client("s3").list_buckets()
        click.echo("LocalStack: OK")
        click.echo(f"S3 buckets: {len(response['Buckets'])}")
    except Exception as e:
        click.echo(f"LocalStack: FAILED — {e}")
        raise SystemExit(1)


@cli.command()
def s3_list():
    """List S3 buckets"""
    s3 = get_client("s3")
    response = s3.list_buckets()
    for bucket in response.get("Buckets", []):
        click.echo(bucket["Name"])


if __name__ == "__main__":
    cli()
