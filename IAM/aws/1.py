import boto3

s3 = boto3.resource('s3')
bucket_name = 't15aug1-tk1'

# all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
# if bucket_name not in all_my_buckets:
#     print(f"{bucket_name} Bucket does not exist in list..creating")
#     s3.create_bucket(Bucket=bucket_name)
#     print(f"{bucket_name} Bucket created")
# else:
#     print(f"{bucket_name} Bucket already exists !! ERROR!!!")
#
file1 = 'file1.txt'
file2 = 'file2.txt'
# s3.Bucket(bucket_name).upload_file(Filename=file2, Key=file2)
# print(f"{bucket_name} Bucket ME FILE UPLOADED")
#
# obj = s3.Object(bucket_name, file2)
# body = obj.get()['Body'].read()
# print(body)
#
# s3.Object(bucket_name, file1).put(Body=open(file2, 'rb'))
# obj = s3.Object(bucket_name, file1)
# body = obj.get()['Body'].read()
# print(body)

# s3.Object(bucket_name, file2).delete()
#
# print(f"{bucket_name} removed")
bucket = s3.Bucket('t15aug-tk1')
bucket.delete()
print(f"{bucket_name} deleted")
