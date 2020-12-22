# Read .aedat4 file from DAVIS346, obtaining events, frames.
# Jianing Li, Peking university, lijianing@pku.edu.cn, Aug.28th, 2020.

import argparse
import numpy as np
import os
from dv import AedatFile
import cv2

parser = argparse.ArgumentParser(
    description='Read the .aedat file from DAVIS346.')

parser.add_argument(
    '-p',
    '--path_to_dataset',
    default = './raw_dataset/0001_orange.aedat4',
    #default = './datasets/gesture.aedat4',
    help='the .aedat4 file path'
)


def make_color_histo(events, img=None, width=346, height=260):
    """
    simple display function that shows negative events as blue dots and positive as red one
    on a white background
    args :
        - events structured numpy array: timestamp, x, y, polarity.
        - img (numpy array, height x width x 3) optional array to paint event on.
        - width int.
        - height int.
    return:
        - img numpy array, height x width x 3).
    """
    if img is None:
        img = 255 * np.ones((height, width, 3), dtype=np.uint8)
    else:
        # if an array was already allocated just paint it grey
        img[...] = 255
    if events.size:
        assert events['x'].max() < width, "out of bound events: x = {}, w = {}".format(events['x'].max(), width)
        assert events['y'].max() < height, "out of bound events: y = {}, h = {}".format(events['y'].max(), height)

        ON_index = np.where(events['polarity'] == 1)

        img[events['y'][ON_index], events['x'][ON_index], :] = [30, 30, 220] * events['polarity'][ON_index][:, None]  # red

        OFF_index = np.where(events['polarity'] == 0)
        img[events['y'][OFF_index], events['x'][OFF_index], :] = [200, 30, 30] * (events['polarity'][OFF_index] + 1)[:,None]  # blue
    return img


def events_to_event_images(input_file, output_file, event_numbers):
    """
    Mapping asynchronous events into event images
    args :
        - input_file:.aedat file, saving dvs events.
        - output_file: the output filename saving timestamps.
        - event number: generating an event image needs event number.
    return:
        - event_image
        - timestamp file: .txt, saving the timestamps for event images.
    """
    with AedatFile(input_file) as f:
        events = np.hstack([event for event in f['events'].numpy()])
        frame_index = 0
        file = open(output_file, 'w')

        for event_index in range(0, len(events), event_numbers):
            rec_events = events[event_index:event_index + event_numbers]
            event_image = make_color_histo(rec_events)
            frame_index = frame_index + 1

            save_frame = './save_images/frame_test_{}.png'.format(frame_index)
            cv2.imwrite(save_frame, event_image)
            print('The {} timestamp is {}'.format(frame_index, events['timestamp'][event_index]))
            file.write('The {} frame, the timestamp is {}'.format(frame_index, events['timestamp'][event_index]) + "\n")  # save the timestamp

        file.close()


def _main(args):
    input_file = os.path.expanduser(args.path_to_dataset)

    with AedatFile(input_file) as f:
        events = np.hstack([event for event in f['events'].numpy()])

        event_numbers = 1500000
        frame_index = 0
        file = open('./timestamp_file.txt', 'w')
        for event_index in range(0, len(events), event_numbers):
            rec_events = events[event_index:event_index+event_numbers]
            event_image = make_color_histo(rec_events)
            frame_index = frame_index + 1

            save_frame = './save_images/frame_test_{}.png'.format(frame_index)
            cv2.imwrite(save_frame, event_image)
            cv2.imshow('out', event_image)
            cv2.waitKey(500)
            print('The {} timestamp is {}'.format(frame_index, events['timestamp'][event_index]))
            file.write('The {} frame, the timestamp is {}'.format(frame_index, events['timestamp'][event_index]) + "\n")  # save the timestamp

        file.close()


if __name__ == '__main__':
    _main(parser.parse_args())



