import Quartz
import Vision
from Foundation import NSURL
import sys, glob, os

def recognize(path):
    url = NSURL.fileURLWithPath_(path)
    req = Vision.VNRecognizeTextRequest.alloc().init()
    res = Vision.VNImageRequestHandler.alloc().initWithURL_options_(url, None)
    res.performRequests_error_([req], None)
    texts = []
    for result in req.results():
        texts.append(result.topCandidates_(1)[0].string())
    return " ".join(texts)

for img in glob.glob("/Users/michaelperinwogenburg/Desktop/Screenshots/*.png"):
    txt = recognize(img)
    if any(c in txt for c in "のるすで日本語中文"):
        print(f"FOUND: {img}")
        sys.exit(0)
print("Not found")
