import android
from wsgiref.simple_server import make_server

droid=android.Android()
pic='/sdcard/snapshot.jpg'

def camera(env,res):
  if env['PATH_INFO']=='/':
    droid.cameraCapturePicture(pic)
    res('200 OK',[('Content-type','image/jpeg')])
    return [file(pic).read()]

httpd=make_server('',9998,camera)
httpd.serve_forever()
