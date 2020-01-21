#-*-coding:utf8:-*-

import androidhelper,time

droid = androidhelper.Android()
droid.startSensingTimed(1,500)

result = droid.sensorsReadAccelerometer().result
print(result)

