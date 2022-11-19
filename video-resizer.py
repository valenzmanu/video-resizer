import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="video input uri", type=str, required=True)
parser.add_argument("--output", help="video output uri",
                    type=str, default="output.mp4")
parser.add_argument("--output_res", help="output resolution",
                    type=int, nargs="+", required=True)
args = parser.parse_args()

input_video = args.input
output_video = args.output
new_res = tuple(args.output_res)
assert len(new_res) == 2

print(f"Loading {input_video}")
cap = cv2.VideoCapture(input_video)
fps = cap.get(cv2.CAP_PROP_FPS)
original_res = (width, height) = (int(cap.get(3)), int(cap.get(4)))
print(f"Loaded video file {input_video} with res {original_res} @ {fps} fps")
print(f"Changing {input_video} resolution: {original_res} --> {new_res} @ {fps} fps")

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(output_video, fourcc, fps, new_res)

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, new_res, fx=0, fy=0,
                       interpolation=cv2.INTER_CUBIC)
        out.write(b)
    else:
        break
print(f"Exported {output_video} with res {new_res} @ {fps} fps")
cap.release()
out.release()