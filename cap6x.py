import cv2
import numpy as np
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description='one object images')
    parser.add_argument('--name', dest='name', default='1',type=str)
    parser.add_argument('--direction', dest='direction', default='1',type=str)
    parser.add_argument('--char', dest='char', default='0', type=str)
    parser.add_argument('--date', dest='date', default='201801', type=str)
    

    args = parser.parse_args()
    return args



def get_data():
    
    caps = ['cap90a1','cap45a1','cap60a1','cap90a2','cap45a2','cap60a2']
    caps_id = [0,2,4,1,3,5]
    width = [800]*6
    height = [600]*6
    for i in range(6):                
        vars()[caps[i]] = cv2.VideoCapture(caps_id[i])
        vars()[caps[i]].set(3,width[i])
        vars()[caps[i]].set(4,height[i])
    
    rwh = 450
    time=0
    capim = False

    area = [[360,350,980,1000],
            [360,350,980,1000],
            [360,350,980,1000],
            [360,350,980,1000],
            [360,350,980,1000],
            [360,350,980,1000],
            [360,350,980,1000],
            [360,350,980,1000]]
    
    n=1
    time=0
    capim = False
  
    while (True):
        images0 = []
        images1 = []
        for i in range(6):
            _,im0 = vars()[caps[i]].read()
            _,im1 = vars()[caps[i]].read()
            #cv2.rectangle(im0, (area[i][0],area[i][1]), (area[i][2],area[i][3]), (0,0,0), 2)
            cv2.line(im0, (200,300), (600,300), (255,0,0), 2)
            cv2.putText(im0, caps[i], (100,100), 0, 2, (0,255,0),8)
            im0=cv2.resize(im0,(400,300),interpolation=cv2.INTER_AREA)
            images0.append(im0)
            images1.append(im1)

        images_l1 = np.concatenate((images0[0],images0[1],images0[2]),axis=1)
        images_l2 = np.concatenate((images0[3],images0[4],images0[5]),axis=1)
        images_all = np.concatenate((images_l1,images_l2),axis=0)
        images_all[:,400-2:400+1]=(0,0,0)
        images_all[:,400*2-2:400*2+1]=(0,0,0)
        images_all[300-2:300+1,:]=(0,0,0)
        cv2.imshow('x4',images_all)
        time+=1
        if capim==True and time%4==0:
            for i in range(6):
                cv2.imwrite(args.name+'/'+caps[i]+'/'+args.direction+'/'+args.name+'_'+args.char+'_'+args.date+'_'+caps[i]+'_'+str(args.direction)+'_'+str(n)+'.jpg',images1[i])
            print '--------------------------------------------------->>> %s'%str(n)
            n+=1

        k = cv2.waitKey(10)&0xFF
        if n == 33:
            break
        if k == 27:
            break
        if k == 32:
            capim = not capim
    cv2.destroyAllWindows()
    for i in range(4):
        vars()[caps[i]].release()


if __name__ == '__main__':
    args = parse_args()
    caps = ['cap90a1','cap90a2','cap45a1','cap45a2','cap60a1','cap60a2']
    
    for i in range(6):
        imdir = args.name+'/'+caps[i]+'/'+args.direction
        if not os.path.exists(imdir):
            os.makedirs(imdir)
            print 'creat:%s'%imdir
    get_data()
