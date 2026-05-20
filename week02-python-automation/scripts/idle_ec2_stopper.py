import boto3
import argparse
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def find_idle_instances(region='us-east-1', cpu_threshold=5.0):
    ec2 = boto3.client('ec2', region_name=region)
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    idle = []
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            iid = instance['InstanceId']
            stats = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': iid}],
                StartTime=datetime.utcnow() - timedelta(hours=24),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )
            if stats['Datapoints']:
                avg_cpu = sum(d['Average'] for d in stats['Datapoints']) / len(stats['Datapoints'])
                if avg_cpu < cpu_threshold:
                    idle.append({'id': iid, 'avg_cpu': round(avg_cpu, 2)})
                    logging.info(f"IDLE: {iid} avg CPU={avg_cpu:.2f}%")
            else:
                logging.info(f"NO DATA YET: {iid}")
                idle.append({'id': iid, 'avg_cpu': 0.0})
    return idle


def stop_instances(instance_ids, dry_run=True):
    ec2 = boto3.client('ec2')
    for iid in instance_ids:
        if dry_run:
            logging.info(f"DRY RUN — would stop: {iid}")
        else:
            ec2.stop_instances(InstanceIds=[iid])
            logging.info(f"STOPPED: {iid}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--threshold', type=float, default=5.0)
    parser.add_argument('--region', type=str, default='us-east-1')
    args = parser.parse_args()
    idle = find_idle_instances(region=args.region, cpu_threshold=args.threshold)
    print(f"\nFound {len(idle)} idle instances:")
    for i in idle:
        print(f"  {i['id']}  avg CPU: {i['avg_cpu']}%")
    stop_instances([i['id'] for i in idle], dry_run=not args.execute)
