#!/bin/bash

python3 enablecontrol.py

while true; do
    python3 takepic.py
    python3 getlastimage.py
    python3 examples/detect_image.py --model fish_model_edgetpu22.tflite --labels fishLabels22.txt --threshold 0.2 --input latest_image.jpg --count 10
    #sleep 1  # Adjust the sleep time as needed to control the frequency of execution
done
