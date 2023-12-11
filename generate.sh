#!/bin/bash


# Note: chmod +x generate.sh to allow running.

# Generate files for server
python3 -m grpc_tools.protoc -I./ --python_out=./redditServer --pyi_out=./redditServer --grpc_python_out=./redditServer reddit.proto

# Generate stubs for client
python3 -m grpc_tools.protoc -I./ --python_out=./redditClient --pyi_out=./redditClient --grpc_python_out=./redditClient reddit.proto