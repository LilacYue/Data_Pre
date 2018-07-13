# -*- coding: utf-8 -*-
"""
change format1:
img_path
num
<face bbox1>
<face bbox2>
...
to format2:
img_path bbox
img_path bbox
...

@author: Lilac
"""
print(__doc__)

def totxt():
    wider_anno_path="/Data/Wider_Face/wider_face_split/wider_face_train_bbx_gt.txt"
    save_path="/Data/Wider_Face/wider_face_train_format2.txt"
    with open (save_path,"w") as outfile:
        with open(wider_anno_path,"r") as infile:
            lines=infile.readlines()
            #print lines
            index=0
            for line in lines:
                if "_" in line:
                    # print line
                    img_path = line.strip(("\n"))
                    index += 1
                    print "img_num finished: "+str(index)
                else:
                    if " " in line:
                        a = map(int, line.strip("\n").split(" ")[0:4])
                        bbox = str(a[0]) + " " + str(a[1]) + " " + str(a[2]) + " " + str(a[3])
                        outfile.writelines(img_path + " " + str(bbox) + "\n")




if __name__ == '__main__':
    totxt()
