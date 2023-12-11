#!/bin/bash


# Note: chmod +x generate.sh to allow running.
python3 -m grpc_tools.protoc -I./ --python_out=./ --pyi_out=. --grpc_python_out=. reddit.proto