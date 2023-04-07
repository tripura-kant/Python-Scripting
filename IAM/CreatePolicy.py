import boto3
import json

def Create_Policy():
	iam = boto3.client('iam')

	user_policy = {
		"Version":"2012-10-17",
		"Statement":[
			{
				"Effect":"Allow",
				"Action":"*",
				"Resource":"*"
			}

		]
	}

	response = iam.create_policy(
		PolicyName = 'PyFullAccess',
		PolicyDocument=json.dumps(user_policy)
		)

	print(response)

Create_Policy()






