import sys
sys.path.insert(0, 'scripts')
from unittest.mock import patch, MagicMock
from idle_ec2_stopper import stop_instances

def test_dry_run_never_calls_aws():
    """dry_run=True must NEVER call ec2.stop_instances"""
    with patch('boto3.client') as mock_boto:
        mock_ec2 = MagicMock()
        mock_boto.return_value = mock_ec2
        stop_instances(['i-abc123'], dry_run=True)
        mock_ec2.stop_instances.assert_not_called()

def test_execute_calls_aws_stop():
    """execute mode must call ec2.stop_instances"""
    with patch('boto3.client') as mock_boto:
        mock_ec2 = MagicMock()
        mock_boto.return_value = mock_ec2
        stop_instances(['i-abc123'], dry_run=False)
        mock_ec2.stop_instances.assert_called_once_with(InstanceIds=['i-abc123'])

def test_empty_list_does_nothing():
    """empty list should never call AWS"""
    with patch('boto3.client') as mock_boto:
        mock_ec2 = MagicMock()
        mock_boto.return_value = mock_ec2
        stop_instances([], dry_run=False)
        mock_ec2.stop_instances.assert_not_called()
