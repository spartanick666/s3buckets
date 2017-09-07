import boto3
import sys

# Let's use Amazon S3
s3 = boto3.resource('s3')
bucket_list = []


for x in s3.buckets.all():
    bucket_list.append(x.name)
print("\n" .join(bucket_list) + "\n")

s3 = boto3.client('s3')


for y in bucket_list:
    result = s3.get_bucket_acl(Bucket=y)
    file = open("test2.txt", "a")
    print(str(result))
    file.write(str(result))
    file.close()


