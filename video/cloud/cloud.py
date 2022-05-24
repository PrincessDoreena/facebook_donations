import os
import random
import numpy as np
from PIL import Image
import wordcloud
from video.svg import svg

def generate_cloud(words, amount, maxamount):
    mask_small = "./video/cloud/res/mask_small.png"
    mask_small = np.array(Image.open(mask_small))
    mask_big = "./video/cloud/res/mask_big.png"
    mask_big = np.array(Image.open(mask_big))
    color_func = wordcloud.get_single_color_func("red")
    regexp = r"([^;]+);"
    words = list(words)
    if len(words) < 14:
        words = words + ["sample0", "sample1", "sample2", "sample3", "sample4",
                "sample5", "sample6", "sample7", "sample8", "sample9",
                "sample10", "sample11", "sample12"][:min(13, 14-len(words))]
    words = ";".join(words[:20]) + ";"

    cloud = wordcloud.WordCloud(regexp=regexp, mask=mask_small, color_func=color_func, background_color="#00000000", mode="RGBA", collocations=False)
    cloud.generate(words)
    cloud.to_file("./video/cloud/cloud_small.png")

    cloud = wordcloud.WordCloud(regexp=regexp, mask=mask_big, color_func=color_func, background_color="#00000000", mode="RGBA", collocations=False)
    cloud.generate(words)
    cloud.to_file("./video/cloud/cloud_big.png")

    svg.generate_svg(amount, maxamount)
    svg.render_svg()
    os.system("composite -gravity center video/cloud/cloud_small.png video/svg/out.png video/res/wc_small.png")
    os.system("composite -gravity center video/cloud/cloud_big.png video/svg/out.png video/res/wc_big.png")
    os.system("./video/cloud/genflv.sh")
    os.system("pkill startstream.sh")
    os.system("pkill -9 ffmpeg")
    os.system("./video/cloud/startstream.sh &")

if __name__ == "__main__":
    generate_cloud("")
