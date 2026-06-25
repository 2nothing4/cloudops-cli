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
    """CloudOps CLI — AWS resource manager via LocalStack/Moto"""
    pass


@cli.command()
def health():
    """Check LocalStack/Moto health"""
    try:
        response = get_client("s3").list_buckets()
        click.echo("Moto: OK")
        click.echo(f"S3 buckets: {len(response['Buckets'])}")
    except Exception as e:
        click.echo(f"Moto: FAILED — {e}")
        raise SystemExit(1)


@cli.command()
def s3_list():
    """List S3 buckets"""
    s3 = get_client("s3")
    response = s3.list_buckets()
    for bucket in response.get("Buckets", []):
        click.echo(bucket["Name"])


@cli.command()
def ec2_list():
    """List EC2 instances"""
    ec2 = get_client("ec2")
    response = ec2.describe_instances()
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            click.echo(f"{instance['InstanceId']} — {instance['State']['Name']}")


@cli.command()
@click.option("--name", default="test-instance", help="Instance name tag")
def ec2_create(name):
    """Create EC2 instance"""
    ec2 = get_client("ec2")
    response = ec2.run_instances(
        ImageId="ami-12345678",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": name}]
        }]
    )
    instance_id = response["Instances"][0]["InstanceId"]
    click.echo(f"Created: {instance_id}")


@cli.command()
@click.argument("instance_id")
def ec2_terminate(instance_id):
    """Terminate EC2 instance"""
    ec2 = get_client("ec2")
    ec2.terminate_instances(InstanceIds=[instance_id])
    click.echo(f"Terminated: {instance_id}")


if __name__ == "__main__":
    cli()
