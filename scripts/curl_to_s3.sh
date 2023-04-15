#!/bin/sh

 curl -L --get https://api.serpwow.com/search \
    -d api_key="6521809044384F6486918BFCB59AF83D" \
    -d q="farts" \
    -d engine="google" \
    -d page="1" \
    -d num="10" \
        -o  output_1.txt
