class QuickSight:
    def qs_list_users(quicksight, Namespace, AwsAccountId):
        # 사용자 목록 조회
        response = quicksight.list_users(
            Namespace = Namespace,
            AwsAccountId = AwsAccountId
        )
        # 사용자 정보 출력
        for user in response['UserList']:
            print(f"사용자 이름: {user['UserName']}, 이메일: {user['Email']}, 권한: {user['Role']}, 활성화: {user['Active']}, 타입: {user['IdentityType']}, arn: {user['Arn']}")

    def qs_register_user(quicksight, Namespace, AwsAccountId, Email, IdentityType, UserRole, UserName):
        # 사용자 등록 요청
        response = quicksight.register_user(
            Namespace       = Namespace,
            AwsAccountId    = AwsAccountId,
            Email           = Email,  
            IdentityType    = IdentityType, 
            UserRole        = UserRole,  
            UserName        = UserName
        )
        # 응답 확인
        if response['Status'] == 201:
            print(f"사용자 {response['User']['UserName']}가 Quicksight에 등록되었습니다.")
        else:
            print(f"사용자 등록에 실패했습니다. 응답 코드: {response['Status']}")