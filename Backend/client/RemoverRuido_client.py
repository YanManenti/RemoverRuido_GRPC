from __future__ import print_function

import logging

from grpc import insecure_channel

import RemoverRuido_pb2
import RemoverRuido_pb2_grpc

from scipy.io import wavfile
import numpy as np

channel_opt = [('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)]

def run():
    # loading audio
    rate, data = wavfile.read("../audio/music.wav")
    data=data[:,0]
    print("Will try to reducec noise ...")
    client = insecure_channel("localhost:50051", options=channel_opt)
    stub = RemoverRuido_pb2_grpc.ReduceNoiseStub(client)
    response = stub.NoiseReducer(RemoverRuido_pb2.ReduceRequest(audio=data.tobytes(), rate=rate))
    audio = np.frombuffer(response.audio, dtype=np.int16)
    wavfile.write("../reduced/music_2.wav", rate, audio)
    print("Greeter client received!")


if __name__ == "__main__":
    logging.basicConfig()
    run()
