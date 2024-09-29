import boto3
from dotenv import load_dotenv
load_dotenv()
import os
import json

ROLE = os.getenv("ROLE")
LAMBDA_FUNCTION_NAME="eivindsPythonLambdaFunction"
lambda_client = boto3.client('lambda', region_name='eu-north-1')

def create_lambda_function():
	with open('function.zip', 'rb') as f:
		zipped_code = f.read()

	response = lambda_client.create_function(
		FunctionName=LAMBDA_FUNCTION_NAME,
		Runtime='python3.12',
		Role=ROLE,
		Handler='eivinds_lambda_function.lambda_handler', # NOTE this must be the path to the handler function (so: <python filename>.lambda_handler)
		Description='This is a lambda function created using boto3 which performs multiplication<<<<<<<<<<<<<<<',
		Code=dict(ZipFile=zipped_code),
	)
	return response

def update_lambda_function():
	with open('function.zip', 'rb') as f:
		zipped_code = f.read()

	response = lambda_client.update_function_code(
		FunctionName=LAMBDA_FUNCTION_NAME,
		ZipFile=zipped_code,
		Publish=True
	)
	return response

def delete_lambda_function():
	response = lambda_client.delete_function(
		FunctionName=LAMBDA_FUNCTION_NAME
	)
	return response

def invoke_lambda_function():
	payload = {"a": 5, "b": 10}
	response = lambda_client.invoke(
		FunctionName=LAMBDA_FUNCTION_NAME,
		InvocationType='RequestResponse',
		Payload=json.dumps(payload)
	)
	return response['Payload'].read().decode('utf-8')


def check_status(function_name = LAMBDA_FUNCTION_NAME):
	response = lambda_client.get_function(FunctionName=function_name)
	return response


if __name__ == '__main__':
	# create_lambda_function()
	# print(check_status())
	pass

