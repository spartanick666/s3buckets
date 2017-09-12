import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
bucket_list = []
results_list = []

file = open("s3_bucket_access.txt", "w")

for x in s3.buckets.all():
    bucket_list.append(x.name)
    #print("\n" .join(bucket_list) + "\n")
file.write(str("\n" .join(bucket_list) + "\n"))

for number, letter in enumerate(bucket_list):
    print(number, letter)
print("\n")

s3 = boto3.client('s3')

for y in bucket_list:
    result = s3.get_bucket_acl(Bucket=y)
    results_list.append(result)
    #print(str(result))
    file.write("\n" + str(result) + "\n")
file.close()
for number, letter in enumerate(results_list):
    print(number, letter)

searchfile = open("s3_bucket_access.txt", "r")
for line in searchfile:
        if "global" in line:
            print("\n The following S3 bucket has public access" + line + "\n")
searchfile.close()

