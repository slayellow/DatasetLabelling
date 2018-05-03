import os

class Labelling:

    '''
    Pedestrian Truck Car Cyclist Misc Van Tram Person_sitting
    Dontcare는 삭제
    Cyclist : 자전거 타는 사람
    Misc : 기타 탈것
    Tram : 전차
    '''
    def __init__(self):
        self.classes = []

    def search_classes(self):
        """
        :param path: 각각 Label이 있는 txt의 폴더 경로
        :rtype: object
        """
        for (path, dir, files) in os.walk("./Text/"):   # "./Text/" 자리가 path로 바뀐다.
            for filename in files:
                filepath = path+filename
                f = open(filepath, 'r')
                while True:
                    check = True
                    line = f.readline()
                    if not line: break
                    list = line.split()
                    if list[0] == 'DontCare':
                        continue
                    if self.classes == []:
                        self.classes.append(list[0])
                        continue
                    for cla in self.classes:
                        if cla == list[0]:
                            check = False
                            break
                    if check == False:
                        continue
                    else:
                        self.classes.append(list[0])
                f.close()

    def unify_label(self):
        for (path, dir, files) in os.walk("./Text/"):   # "./Text/" 자리가 path로 바뀐다.
            for filename in files:
                filepath = path+filename
                str = filepath+" "
                f = open(filepath, 'r')
                # 4,5,6,7
                while True:
                    check = True
                    line = f.readline()
                    if not line: break
                    list = line.split()
                    if list[0] == 'DontCare':
                        continue
                    for index, cla in enumerate(self.classes):
                        if cla == list[0]:
                            str = str + '%s %s %s %s %s '%(list[4], list[5], list[6], list[7], index)
                str = str+'\n'
                f.close()
                f = open("unified.txt",'a')
                f.write(str)
                f.close()


    def write_classes(self, filename):
        str = ""
        f = open(filename+".txt", 'w')
        for cla in self.classes:
            str = str + cla + " "
        f.write(str)
        f.close()