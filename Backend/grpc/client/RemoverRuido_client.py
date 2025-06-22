from __future__ import print_function

import logging
import pathlib

from grpc import insecure_channel

import RemoverRuido_pb2
import RemoverRuido_pb2_grpc

from scipy.io import wavfile
import numpy as np

channel_opt = [('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)]
sourcePath='../../audio/'
destinationPath='../../reduced/'

def run():
    for audio_file in pathlib.Path(sourcePath).glob('*.wav'):
        # loading audio
        rate, data = wavfile.read(sourcePath+audio_file.name)
        data=data[:,0]
        print("Will try to reduce noise ...")
        client = insecure_channel("localhost:50051", options=channel_opt)
        stub = RemoverRuido_pb2_grpc.ReduceNoiseStub(client)
        response = stub.NoiseReducer(RemoverRuido_pb2.ReduceRequest(audio=data.tobytes(), rate=rate))
        audio = np.frombuffer(response.audio, dtype=np.int16)
        wavfile.write(destinationPath+"REDUCED_"+audio_file.name, rate, audio)


if __name__ == "__main__":
    logging.basicConfig()
    run()
