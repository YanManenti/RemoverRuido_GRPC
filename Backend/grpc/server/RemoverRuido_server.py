from concurrent import futures
import logging

import grpc

import RemoverRuido_pb2
import RemoverRuido_pb2_grpc
import reduce

channel_opt = [('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)]

class ReduceNoise(RemoverRuido_pb2_grpc.ReduceNoiseServicer):
    def NoiseReducer(self, request, context):
        return RemoverRuido_pb2.ReduceReply(audio=reduce.reduce(request.audio, request.rate))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=channel_opt)
    RemoverRuido_pb2_grpc.add_ReduceNoiseServicer_to_server(ReduceNoise(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
