import boto3

def Allusers():
	iam = boto3.client('iam')

	paginator = iam.get_paginator('list_users')

	for response in paginator.paginate():
		for user in response['Users']:
			username = user['UserName']
			Arn = user['Arn']

			print('Username :  {},  Arn : {}'.format(username, Arn))


Allusers()