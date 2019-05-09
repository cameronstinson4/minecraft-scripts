#!/bin/bash

source /etc/environment

aws s3 sync /factorio/saves/ s3://"$S3_BUCKET_NAME"/
