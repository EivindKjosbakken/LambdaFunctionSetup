import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

	a, b = event['a'], event['b']
	result = multiplication(a,b)

	logger.info(f"Multiplication of {a} and {b} is {result}")
	result_object = {
		"result": result
	}
	return json.dumps(result_object)


def multiplication(a,b):
	return float(a) * float(b)
