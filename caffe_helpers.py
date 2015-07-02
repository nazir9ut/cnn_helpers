#!/usr/bin/env python
"""
classify.py is an out-of-the-box image classifer callable from the command line.

By default it configures and runs the Caffe reference ImageNet model.
"""
import numpy as np
import os
import sys
import argparse
import glob
import time

import caffe
import caffe.io




def init_caffe_netwrok():

    output_file = 'foo'
    mean_file = '/home/naz/.digits/jobs/20150624-125034-be77/mean.binaryproto'
    channel_swap = 0
    model_def = '/home/naz/.digits/jobs/20150624-132109-bb06/deploy.prototxt'
    gpu = True
    input_scale = 1.0
    pretrained_model = '/home/naz/.digits/jobs/20150624-132109-bb06/snapshot_iter_9170.caffemodel'
    image_dims = [227, 227]
    raw_scale = 255.0


    mean, channel_swap = None, None


    if mean_file:
        a = caffe.io.caffe_pb2.BlobProto()
        file = open(mean_file, 'rb')
        data = file.read()
        a.ParseFromString(data)

        means=a.data

        means=np.asarray(means)

        means=means.reshape(1,256,256)
    if channel_swap:
        channel_swap = [int(s) for s in channel_swap.split(',')]

    if gpu:
        caffe.set_mode_gpu()
        print("GPU mode")
    else:
        caffe.set_mode_cpu()
        print("CPU mode")

    # Make classifier.
    classifier = caffe.Classifier(model_def, pretrained_model,
            image_dims=image_dims, mean=mean,
            input_scale=input_scale, raw_scale=raw_scale,
            channel_swap=channel_swap)



    return classifier









def classify_many(input_files, classifier, is_raw = False):

    center_only = False


    inputs = []

    if not is_raw:
        # Load numpy array (.npy), directory glob (*.jpg), or image file.
        # input_file = os.path.expanduser(input_file)
        print("Loading files:")


        for file in input_files:
            inputs.append(caffe.io.load_image(file, color=False))


        print(type(inputs))


        for i in xrange(0, len(inputs), 1):
            inputs[i] = inputs[i][:,:,0]
            inputs[i] = np.reshape(inputs[i], (inputs[i].shape[0], inputs[i].shape[1], 1))

            inputs = np.array(inputs)


    else:
        inputs = input_files







    print("Classifying %d inputs." % len(inputs))



    # Classify.
    start = time.time()
    predictions = classifier.predict(inputs, not center_only)
    print("Done in %.2f s." % (time.time() - start))


    # result = []
    # for p in predictions:
    #     result = ['{0:.5f}'.format(p) for p in predictions[0]]

    # print(result)

    return predictions






