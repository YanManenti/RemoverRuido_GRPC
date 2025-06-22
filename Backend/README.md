`
python -m pip install grpcio
`

`
python -m pip install grpcio-tools
`

`
git clone -b v1.73.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
`

`
cd grpc/examples/python/helloworld
`

`
python greeter_server.py
`

New console:

`
cd grpc/examples/python/helloworld
`

`
python greeter_client.py
`

Rebuild:

`
python -m grpc_tools.protoc -I./Backend/protos --python_out=. --pyi_out=. --grpc_python_out=. ./Backend/protos/RemoverRuido.proto
`