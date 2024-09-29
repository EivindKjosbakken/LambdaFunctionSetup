import zipfile

file_to_zip = 'eivinds_lambda_function.py'
zip_file_name = 'function.zip'

with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    zipf.write(file_to_zip)