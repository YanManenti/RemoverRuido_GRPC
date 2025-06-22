from concurrent import futures
import logging

import grpc
import RemoverRuido_pb2
import RemoverRuido_pb2_grpc

import noisereduce as nr
import numpy as np

channel_opt = [('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)]

class Greeter(RemoverRuido_pb2_grpc.ReduceNoiseServicer):
    def NoiseReducer(self, request, context):
        # Back to np.ndarray
        audio = np.frombuffer(request.audio, dtype=np.int16)
        # noisereduction
        reduced_noise = nr.reduce_noise(y=audio, sr=request.rate)  # WORKS
        return RemoverRuido_pb2.ReduceReply(audio=reduced_noise.tobytes())


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)])
    RemoverRuido_pb2_grpc.add_ReduceNoiseServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
