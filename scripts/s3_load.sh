#!/bin/sh

./curl_to_s3.sh
aws s3 cp output_1.txt s3://uncleclam-webapp/