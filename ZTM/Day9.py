import boto3

# set up the IAM client
iam = boto3.client('iam')

# get a list of all IAM users in the account
users = iam.list_users()['Users']

# iterate through each user and rotate their access keys
for user in users:
    username = user['UserName']
    access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']

    # delete all existing access keys for the user
    for key in access_keys:
        access_key_id = key['AccessKeyId']
        iam.delete_access_key(UserName=username, AccessKeyId=access_key_id)

    # create a new access key for the user
    new_key = iam.create_access_key(UserName=username)['AccessKey']
    access_key_id = new_key['AccessKeyId']
    secret_access_key = new_key['SecretAccessKey']

    print(
        f"Rotated access key for user {username}. New AccessKeyId: {access_key_id}, New SecretAccessKey: {secret_access_key}")
