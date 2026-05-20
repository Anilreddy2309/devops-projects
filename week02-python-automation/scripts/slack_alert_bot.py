import boto3
import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def get_cloudwatch_alarms(region='us-east-1'):
    """Get all CloudWatch alarms currently in ALARM state."""
    cw = boto3.client('cloudwatch', region_name=region)
    response = cw.describe_alarms(StateValue='ALARM')
    return response.get('MetricAlarms', [])


def post_to_slack(message):
    """Post a message to Slack channel."""
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    channel = os.environ['SLACK_CHANNEL_ID']
    try:
        client.chat_postMessage(channel=channel, text=message)
        logging.info("Message posted to Slack successfully")
    except SlackApiError as e:
        logging.error(f"Slack error: {e.response['error']}")


def run_alarm_check():
    region = os.getenv('AWS_REGION', 'us-east-1')
    alarms = get_cloudwatch_alarms(region=region)

    if not alarms:
        message = ":white_check_mark: *DevOps Alert Bot* — All CloudWatch alarms are OK!"
    else:
        lines = [f":red_circle: *DevOps Alert Bot* — {len(alarms)} active alarm(s)!\n"]
        for alarm in alarms:
            lines.append(
                f"• *{alarm['AlarmName']}*\n"
                f"  Reason: {alarm['StateReason']}\n"
            )
        message = "\n".join(lines)

    print(message)
    post_to_slack(message)


if __name__ == '__main__':
    run_alarm_check()
