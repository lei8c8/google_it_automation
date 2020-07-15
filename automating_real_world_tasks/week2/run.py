#!/usr/bin/env python3

import os
import glob
import json
import requests

def get_file():
    source_path = "/data/feedback/"
    return glob.glob(source_path + '*.txt')

def process_requests():
    json_keys = ("title", "name", "date", "feedback")
    for f in get_file():
        i, answer = 0, {}
        with open(f) as fd:
            for l in fd:
                answer[json_keys[i]] = l.strip()
                i += 1
        response = requests.post("http://35.224.243.8/feedback/", json=answer)
        if not response.ok:
            print("Failed to post!")

if __name__ == '__main__':
    process_requests()