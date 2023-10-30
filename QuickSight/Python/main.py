import boto3
from botocore.config import Config
from quicksight import QuickSight

# 프록시 설정을 추가합니다.
# proxy_config = Config(proxies={'https': 'http://52.78.123.68:3128'})

# botocore 세션을 생성합니다.
# session = boto3.Session( config = proxy_config )
# Quicksight 클라이언트 생성
# quicksight_session = boto3.client('quicksight', region_name='ap-northeast-2', config = proxy_config)  # 본인의 리전에 맞게 변경하세요
# register_user   = QuickSight.register_user(quicksight_session, 'default', 'ACCOUNTID', 'test@exmaple.com', 'QUICKSIGHT', 'READER', 'test' )
# list_users      = QuickSight.list_users(quicksight_session, 'default', 'ACCOUNTID')
# generate_embed_url_for_registered_user = QuickSight.generate_embed_url_for_registered_user(quicksight_session, 'ACCOUNTID', 'Namespace', 'QuickSightUser', 60)