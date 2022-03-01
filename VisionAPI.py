from email.mime import image
from http import client
import os
import io
from pydoc import cli
from urllib import response
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'omega-metric-340408-82d17f9ca0b4.json'


# First Student
client = vision.ImageAnnotatorClient()
FOLDER_PATH = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI'
IMAGE_FILE = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI/images/1.jpeg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text

file = open(
    "/home/shudhanshu0011/Project0/scienceday/plagia/student1.txt", "w+")
file.truncate(0)
file.write(docText)
file.close()


# Second Student
client = vision.ImageAnnotatorClient()
FOLDER_PATH = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI'
IMAGE_FILE = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI/images/2.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text

file = open(
    "/home/shudhanshu0011/Project0/scienceday/plagia/student2.txt", "w+")
file.truncate(0)
file.write(docText)
file.close()


# Third Student
client = vision.ImageAnnotatorClient()
FOLDER_PATH = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI'
IMAGE_FILE = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI/images/3.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text

file = open(
    "/home/shudhanshu0011/Project0/scienceday/plagia/student3.txt", "w+")
file.truncate(0)
file.write(docText)
file.close()


# Fourth Student
client = vision.ImageAnnotatorClient()
FOLDER_PATH = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI'
IMAGE_FILE = r'/home/shudhanshu0011/Project0/scienceday/ScienceDAyProjectAI/images/4.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text

file = open(
    "/home/shudhanshu0011/Project0/scienceday/plagia/student4.txt", "w+")
file.truncate(0)
file.write(docText)
file.close()
