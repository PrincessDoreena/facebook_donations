#!/bin/bash
mv video/res/stream.flv video/res/stream_play.flv
while [ ! ]
do
	ffmpeg -re -f concat -i video/res/streaminputs.txt -c copy -f flv 'rtmp url here' >> ~/streamlog 2>&1
done
