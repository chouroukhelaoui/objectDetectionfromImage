import cv2
import sys, getopt, argparse
import matplotlib.pyplot as plt # pip install matplotlib
parser = argparse.ArgumentParser()
parser.add_argument('--inputFile', type=str)
parser.add_argument('--outputFolderImg', type=str)
parser.add_argument('--outputFolderTxt', type=str)
args = parser.parse_args()
inputfile = args.inputFile
outputfiletxt = args.outputFolderTxt
outputfileimg = args.outputFolderImg
config_file = '/input/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = '/input/frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model,config_file)
classLabels = []
file_name = "/input/labels.txt"
with open(file_name , 'rt') as fpt:
    classLabels = fpt.read().rstrip("\n").split("\n")
#print(classLabels)
#print(len(classLabels))
model.setInputSize(320,320)
model.setInputScale(1.0/127.5) # 255/2 = 127.5
model.setInputMean((127.5,125.5,127.5)) # mobilenet => [-1;1] 
model.setInputSwapRB(True)
# read an Image
img = cv2.imread(inputfile)
plt.imshow(img) 
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
ClassIndex , confidece , bbox = model.detect(img,confThreshold=0.5)
print(ClassIndex)
font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN
for ClassInd , conf , boxes in zip(ClassIndex.flatten() , confidece.flatten() , bbox):
    cv2.rectangle(img,boxes,(255,0,0),2)
    print(classLabels[ClassInd - 1])
    cv2.putText(img,classLabels[ClassInd - 1],(boxes[0]+10 , boxes[1]+40) , font , fontScale = font_scale , color=(0,255,0),thickness = 3)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.savefig(outputfileimg+'/resultimage.png')
