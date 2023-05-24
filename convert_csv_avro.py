import pandas as pd 
import json

# read the CSV file
df = pd.read_csv('test.csv')

# create a dictionary to map S3 data types to Avro data types
data_type_mapping = {
    "date": {"type": "int", "logicalType": "date"},
    "decimal": {"type": "bytes", "logicalType": "decimal", "precision": 16, "scale": 2},
    "timestamptz":{"type": "long", "logicalType": "timestamp-millis"},
    "string": "string",
    "boolean": "boolean",
    "long": "long",
    "float": "float",
    "int": "int",
    "double": "double"
}

# create a dictionary to map S3 required data to Avro nullable status
required_mapping = {
    'NOT NULL': False,
    'NULL': True
}

# convert S3 data types to Avro data types and add S3 required data
df['AVRO Data Type'] = df['\nS3 Data Type'].astype(str).apply(lambda x: data_type_mapping.get(x.split('(')[0]))
df['AVRO Nullable'] = df['\nS3 Required Data'].apply(lambda x: required_mapping.get(x, True))



# create Avro schema
schema = []

for i, row in df.iterrows():
    if row['AVRO Nullable'] == True:
        schema.append({'name': row['\nField Name'], 'type': ['null', row['AVRO Data Type']], 'default': None})
    else:
        schema.append({'name': row['\nField Name'], 'type': [row['AVRO Data Type']]})

# Define the output file path
output_file = 'test.avsc'

# print Avro schema
print(schema)

# Write the schema to the output file
with open(output_file, 'w') as f:
    json.dump(schema, f, indent=3)

print(f'Successfully wrote Avro schema to file: {output_file}')
