# need copy the log to local pc , in order to show  result direct
# savefig version will be finishe someday
import string
import matplotlib.pyplot as plt
def readLog(log_path):
    loss=[]
    arm_loss=[]
    odm_loss=[]
    with open(log_path,"r") as f1:
        for line in f1.readlines():
            if "Iteration" in line:
                if 'loss' in line:
                    loss_temp=line.split("=")[1].split(" ")[1]
                    #print loss_temp
                    loss.append(string.atof(loss_temp))
    return loss
#iter from begin to now
def draw(loss):
    f1 = plt.figure(1)
    #plt.subplot(211)
    #print range(1;loss)
    plt.scatter(xrange(len(loss)),loss,s=3)
    plt.show()

#detail about now
def draw2(loss,img_path):
    f1 = plt.figure(1)
    num=0 #from num to now to see
    #plt.subplot(211)
    #print range(1;loss)
    plt.scatter(xrange(len(loss)-num),loss[num:],s=1,color = 'm')
    #plt.scatter(xrange(len(arm_loss) - num), arm_loss[num:], s=1, color='c')
    #plt.scatter(xrange(len(odm_loss) - num), odm_loss[num:], s=1, color='r')
    #plt.xlim(xmax=7, xmin=0)
    #plt.ylim(ymax=4, ymin=0)
    #savefig(img_path"/1.jpg")
    plt.show()

if __name__ == '__main__':
    log_path="path//log//"
    logfile="log_label_0.txt"
    log_path=log_path+logfile
    loss=readLog(log_path)
    #print len(loss)

    #print len(loss[2:])
    draw2(loss)
    print "ok"
