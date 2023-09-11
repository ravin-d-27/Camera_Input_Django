from django.shortcuts import render

# Create your views here.
import cv2
from django.http import StreamingHttpResponse

def process_video(request):

    cap = cv2.VideoCapture(0) # Integrated Web Cam
    while True:
        success,frame = cap.read()
        _,im = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + im.tobytes() + b'\r\n\r\n')

    cap.release()

def display_render(request):
    return StreamingHttpResponse(process_video(request),content_type="multipart/x-mixed-replace;boundary=frame")

def home(request):
    return render(request,'Vid_Feed/home.html')