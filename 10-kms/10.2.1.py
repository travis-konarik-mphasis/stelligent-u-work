import boto3

kms_client = boto3.client('kms')
s3_client = boto3.client('s3')

file_to_encrypt = open('secret.txt', 'r')
file_to_encrypt_contents = file_to_encrypt.read()
file_to_encrypt.close()
print("##########File To Encrypt Contents##########")
print(file_to_encrypt_contents)

kms_response = kms_client.encrypt(
    KeyId='alias/EasyToRemeber',
    Plaintext=file_to_encrypt_contents,
)
print("##########KMS Encrypt Response##########")
print(kms_response)

s3_client.put_object(
  Body=kms_response['CiphertextBlob'],
  Bucket='testbucket-10-2-1',
  Key='/encrypted-secret',
  )

s3_get_response = s3_client.get_object(
  Bucket='testbucket-10-2-1',
  Key='/encrypted-secret',
  )

print("##########S3 Get Response##########")
print(s3_get_response)

decrypt_response = kms_client.decrypt(
    CiphertextBlob=s3_get_response['Body'].read(),
    )

print("##########KMS Decrypt Response##########")
print(decrypt_response)

file_to_write = open('decrypted-secret.txt', 'wb')
file_to_write.write(decrypt_response['Plaintext'])
file_to_write.close()
