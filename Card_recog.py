
# Python code to identify the card based on the photo sent by the ESP32-CAM

import tornado.ioloop
import tornado.web
import cv2 as cv
import numpy as np
import time




cardnames = ['no card found', 'ones','twos','threes','fours','fives','sixs','sevens','eights','nines','tens','elevens','twelves','thirteens',
            'onec','twoc','threec','fourc','fivec','sixc','sevenc','eightc','ninec','tenc','elevenc','twelvec','thirteenc',
            'oneh','twoh','threeh','fourh','fiveh','sixh','sevenh','eighth','nineh','tenh','elevenh','twelveh','thirteenh',
            'oned','twod','threed','fourd','fived','sixd','sevend','eightd','nined','tend','elevend','twelved','thirteend']

def readcard(espimg):
        #take input image and convert to grayscale
        img_rgb = cv.imread(espimg)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

        
        #spades library
        ones = cv.imread('1st.jpeg',0)
        twos = cv.imread('2st.jpeg',0)
        threes = cv.imread('3st.jpeg',0)
        fours = cv.imread('4st.jpeg',0)
        fives = cv.imread('5st.jpeg',0)
        sixs = cv.imread('6st.jpeg',0)
        sevens = cv.imread('7st.jpeg',0)
        eights = cv.imread('8st.jpeg',0)
        nines = cv.imread('9st.jpeg',0)
        tens = cv.imread('10st.jpeg',0)
        elevens = cv.imread('11st.jpeg',0)
        twelves = cv.imread('12st.jpeg',0)
        thirteens = cv.imread('13st.jpeg',0)

        #club library
        onec = cv.imread('1ct.jpeg',0)
        twoc = cv.imread('2ct.jpeg',0)
        threec = cv.imread('3ct.jpeg',0)
        fourc = cv.imread('4ct.jpeg',0)
        fivec = cv.imread('5ct.jpeg',0)
        sixc = cv.imread('6ct.jpeg',0)
        sevenc = cv.imread('7ct.jpeg',0)
        eightc = cv.imread('8ct.jpeg',0)
        ninec = cv.imread('9ct.jpeg',0)
        tenc = cv.imread('10ct.jpeg',0)
        elevenc = cv.imread('11ct.jpeg',0)
        twelvec = cv.imread('12ct.jpeg',0)
        thirteenc = cv.imread('13ct.jpeg',0)

        #heart library
        oneh = cv.imread('1ht.jpeg',0)
        twoh = cv.imread('2ht.jpeg',0)
        threeh = cv.imread('3ht.jpeg',0)
        fourh = cv.imread('4ht.jpeg',0)
        fiveh = cv.imread('5ht.jpeg',0)
        sixh = cv.imread('6ht.jpeg',0)
        sevenh = cv.imread('7ht.jpeg',0)
        eighth = cv.imread('8ht.jpeg',0)
        nineh = cv.imread('9ht.jpeg',0)
        tenh = cv.imread('10ht.jpeg',0)
        elevenh = cv.imread('11ht.jpeg',0)
        twelveh = cv.imread('12ht.jpeg',0)
        thirteenh = cv.imread('13ht.jpeg',0)

        #diamond library
        oned = cv.imread('1dt.jpeg',0)
        twod = cv.imread('2dt.jpeg',0)
        threed = cv.imread('3dt.jpeg',0)
        fourd = cv.imread('4dt.jpeg',0)
        fived = cv.imread('5dt.jpeg',0)
        sixd = cv.imread('6dt.jpeg',0)
        sevend = cv.imread('7dt.jpeg',0)
        eightd = cv.imread('8dt.jpeg',0)
        nined = cv.imread('9dt.jpeg',0)
        tend = cv.imread('10dt.jpeg',0)
        elevend = cv.imread('11dt.jpeg',0)
        twelved = cv.imread('12dt.jpeg',0)
        thirteend = cv.imread('13dt.jpeg',0)

        #intital values
        threshold = .9
        cardnum = 0

        #match
        while cardnum == 0:
            #test for spades
            res = cv.matchTemplate(img_gray,ones,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 1
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
                

            res = cv.matchTemplate(img_gray,twos,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 2
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,threes,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 3
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,fours,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 4
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,fives,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 5
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sixs,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 6
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sevens,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 7
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,eights,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 8
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname   

            res = cv.matchTemplate(img_gray,nines,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 9
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,tens,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 10
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,elevens,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 11
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twelves,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 12
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,thirteens,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 13
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            #test for clubs
            res = cv.matchTemplate(img_gray,onec,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 14
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twoc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 15
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,threec,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 16
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,fourc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 17
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,fivec,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 18
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sixc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 19
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sevenc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 20
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,eightc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 21
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname   

            res = cv.matchTemplate(img_gray,ninec,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 22
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,tenc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 23
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,elevenc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 24
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twelvec,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 25
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,thirteenc,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 26
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            #test for heart
            res = cv.matchTemplate(img_gray,oneh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 27
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twoh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 28
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,threeh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 29
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,fourh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 30
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,fiveh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 31
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sixh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 32
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sevenh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 33
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,eighth,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 34
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname   

            res = cv.matchTemplate(img_gray,nineh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 35
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,tenh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 36
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,elevenh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 37
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twelveh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 38
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,thirteenh,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 39
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            #test for diamond
            res = cv.matchTemplate(img_gray,oned,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 40
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twod,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 41
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,threed,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 42
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,fourd,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 43
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,fived,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 44
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sixd,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 45
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,sevend,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 46
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,eightd,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 47
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname   

            res = cv.matchTemplate(img_gray,nined,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 48
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname            

            res = cv.matchTemplate(img_gray,tend,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 49
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,elevend,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 50
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            res = cv.matchTemplate(img_gray,twelved,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 51
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname
            
            res = cv.matchTemplate(img_gray,thirteend,cv.TM_CCOEFF_NORMED)
            loc = np.where( res >= threshold)
            if loc[0].size > 0:
                cardnum = 52
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

            #reduce threshold if no card is found

            if cardnum == 0:
                threshold = threshold -.1
            if threshold <= .3:
                cardname = cardnames[cardnum]
                print(cardname)
                return cardname

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!!")
class ESPhandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world ESP please")
    def post(self):
       readcard('imagetest1.jpg')     
       if self.request.headers['Content-Type'] == 'image/jpg':
           self.write("go wild")
           print('go cats')
           img = self.request.body
           file = open('imgtest1.jpg', 'wb+')
           file.write(bytearray(img))
           file.close

readcard('imgtest1.jpg')

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ESP", ESPhandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

