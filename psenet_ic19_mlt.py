import numpy as np
from PIL import Image
from torch.utils import data
import util
import cv2
import random
import torchvision.transforms as transforms
import torch
import pyclipper
import Polygon as plg
from util.io_ import ls

ic19_root_dir = './data/IC19MLT/'
ic19_train_data_dir = ic19_root_dir + 'train_IC19MLT/'
ic19_train_gt_dir = ic19_root_dir + 'train_IC19MLT_gt/'