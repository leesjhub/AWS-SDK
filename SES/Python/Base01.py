import boto3
from botocore.exceptions import ClientError

def send_email(client,sender, recipient, subject, body):
    # 이메일 보내기
    try:
        response = client.send_email(
            Destination = {
                'ToAddresses': [
                    recipient,
                ],
            },
            Message = {
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source = sender,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("이메일이 성공적으로 전송되었습니다.")
        print("Message ID: ", response['MessageId'])

if __name__ == "__main__":
    # AWS SES 클라이언트 생성
    sender      = "your_sender@example.com"
    recipient   = "recipient@example.com"
    subject     = "이메일 테스트"
    body        = "이메일이 성공적으로 전송되었습니다."
    region      = "your_aws_region"
    client      = boto3.client("ses", region_name = region)

    send_email(client, sender, recipient, subject, body)
