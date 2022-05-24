#!/bin/bash
ffmpeg -y -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000 -framerate 1/3 -f image2 -pattern_type glob -loop 1 -i 'video/res/wc_*.png' -t 12 -vf scale=882:720,fps=fps=30 -c:v libx264 -g 60 -keyint_min 60 -pix_fmt yuv420p -b:v 1M -c:a aac -b:a 128k video/res/stream.flv
rm video/res/streaminputs.txt
for i in {0..10000}
do
	echo "file 'stream_play.flv'" >> video/res/streaminputs.txt
done
