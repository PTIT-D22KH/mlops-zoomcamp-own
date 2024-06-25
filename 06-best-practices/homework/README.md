docker-compose up

aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration

aws configure (or you have to export 
- export AWS_ACCESS_KEY_ID=abc
- export AWS_SECRET_ACCESS_KEY=xyz)

EXPORT S3_ENDPOINT_URL='http://localhost:4566'

export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"