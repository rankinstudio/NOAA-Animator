__author__ = 'David Rankin, David@rankinstudio.com'

from urllib.request import urlopen
from urllib.request import Request
import urllib
import os
import os.path
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext
from itertools import tee, islice, chain, zip_longest
from decimal import Decimal
import glob
import tkinter.messagebox
import time
from bs4 import BeautifulSoup



#example
#http://radar.weather.gov/ridge/RadarImg/N0R/ICX/?C=M;O=A LAST MODIFIED
#url = 'http://radar.weather.gov/ridge/RadarImg/N0R/ICX/' BASE RADAR
#       http://radar.weather.gov/ridge/RadarImg/N0R/ICX/ICX_20150503_2103_N0R.gif

class Application(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #SETUP MENU STRUCTURE
        menubar = Menu(root)

        #SETUP FILE MENU
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="About", command= self.show_about)
        menubar.add_cascade(label="About", menu=aboutmenu)

        #ADD MENUBAR TO CONFIG
        root.config(menu=menubar)

        self.instructions = Label(self, text = "SELECT RADAR:")
        self.instructions.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.instructions2 = Label(self, text = "SELECT PRODUCT:")
        self.instructions2.grid(row = 0, column = 1, columnspan = 2, sticky = W)

        #SETUP SELECT RADAR
        self.site = StringVar(self)
        self.site.set("icx-Cedar City, UT") # initial value
        option = OptionMenu(self, self.site,
            "abc-Bethel, AK",
            "abr-Aberdeen, SD",
            "abx-Albuquerque, NM",
            "acg-Sitka, AK",
            "aec-Nome, AK",
            "ahg-Kenei, AK",
            "aih-Middleton, AK",
            "akc-King Salmon, AK",
            "akq-Richmond, VA",
            "ama-Amarillo, TX",
            "amx-Miami, FL",
            "apd-Fairbanks, AK",
            "apx-Gaylord, MI",
            "arx-LaCrosse, WI",
            "atx-Seattle, WA",
            "bbx-Beale AFB, CA",
            "bgm-Binghamton, NY",
            "bhx-Eureka, CA",
            "bis-Bismarck, ND",
            "blx-Billings, MT",
            "bmx-Birmingham, AL",
            "box-Boston, MA",
            "bro-Brownsville, TX",
            "buf-Buffalo, NY",
            "byx-Key West, FL",
            "cae-Columbia, SC",
            "cbw-Caribou, ME",
            "cbx-Boise, ID",
            "ccx-State College, PA",
            "cle-Cleveland, OH",
            "clx-Charleston, SC",
            "crp-Corpus Christi, TX",
            "cxx-Burlington, VT",
            "cys-Cheyenne, WY",
            "dax-Sacremento, CA",
            "ddc-Dodge City, KS",
            "dfx-Laughlin AFB, TX",
            "dgx-Brandon, MS",
            "dix-Philadelphia, PA",
            "dlh-Duluth, MN",
            "dmx-Des Moines, IA",
            "dox-Dover AFB, DE",
            "dtx-Detroit, MI",
            "dvn-Quad Cities, IA",
            "dyx-Dyess AFB, TX",
            "eax-KC, MO",
            "emx-Tucson, AZ",
            "enx-Albany, NY",
            "eox-Ft. Rucker, AL",
            "epz-El Paso, TX",
            "esx-Las Vegas, NV",
            "evx-Eglin AFB, FL",
            "ewx-Austin, TX",
            "eyx-Edwards AFB, CA",
            "fcx-Roanoke, VA",
            "fdr-Frederick, OK",
            "fdx-Cannon AFB, NM",
            "ffc-Atlanta, GA",
            "fsd-Sioux Falls, SD",
            "fsx-Flagstaff, AZ",
            "ftg-Denver, CO",
            "fws-Dallas, TX",
            "ggw-Glasgow, MT",
            "gjx-Grand Junction, CO",
            "gld-Goodland, KS",
            "grb-Green Bay, WI",
            "grk-Ft Hood, TX",
            "grr-Muskegon, MI",
            "gsp-Spartanburg, SC",
            "gua-Andersen AFB, Guam",
            "gwx-Columbus AFB, MS",
            "gyx-Gray/Portland, ME",
            "hdx-Holloman AFB, NM",
            "hgx-Houston, TX",
            "hki-South Kauai, HI",
            "hkm-Kohala, HI",
            "hmo-Molokai, HI",
            "hnx-Joaquin Valley, CA",
            "hpx-Ft. Campbell, KY",
            "htx-Hytop, AL",
            "hwa-South Hawaii, HI",
            "ict-Wichita, KS",
            "icx-Cedar City, UT",
            "iln-Cincinnati, OH",
            "ilx-Springfield, IL",
            "ind-Indianapolis, IN",
            "inx-Tulsa, OK",
            "iwa-Phoenix, AZ",
            "iwx-Webster, IN",
            "jax-Jacksonville, FL",
            "jgx-Robins AFB, GA",
            "jkl-Jackson, KY",
            "jua-San Juan, PR",
            "lbb-Lubbock, TX",
            "lch-Lake Charles, LA",
            "lix-New Orleans, LA",
            "lnx-North Platte, NE",
            "lot-Chicago, IL",
            "lrx-Elko, NV",
            "lsx-St Louis, MO",
            "ltx-Wilmington, NC",
            "lvx-Louisville, KY",
            "lwx-Washington DC",
            "lzk-Little Rock, AR",
            "maf-Odessa, TX",
            "max-Medford, OR",
            "mbx-Minot AFB, ND",
            "mhx-Morehead City, NC",
            "mkx-Milwaukee, WI",
            "mlb-Melbourne, FL",
            "mob-Mobile, AL",
            "mpx-Minn-St.P, MN",
            "mqt-Marquette, MI",
            "mrx-Knoxville, TN",
            "msx-Missoula, MT",
            "mtx-Salt Lake, UT",
            "mux-San Francisco, CA",
            "mvx-Fargo, ND",
            "mxx-Maxwell AFB, AL",
            "nkx-San Diego, CA",
            "nqa-Memphis, TN",
            "oax-Omaha, NE",
            "ohx-Nashville, TN",
            "okx-New York City, NY",
            "otx-Spokane, WA",
            "pah-Paducah, KY",
            "pbz-Pittsburgh, PA",
            "pdt-Pendleton, OR",
            "poe-Ft Polk, LA",
            "pux-Pueblo, CO",
            "rax-Raleigh-Durham, NC",
            "rgx-Reno, NV",
            "riw-Riverton, WY",
            "rlx-Charleston, WV",
            "rtx-Portland, OR",
            "sfx-Idaho falls, ID",
            "sgf-Springfield, MO",
            "shv-Shreveport, LA",
            "sjt-San Angelo, TX",
            "sox-March AFB, CA",
            "srx-Ft. Smith, AR",
            "tbw-Tampa Bay, FL",
            "tfx-Great Falls, MT",
            "tlh-Tallahassee, FL",
            "tlx-Oklahoma City, OK",
            "twx-Topeka, KS",
            "tyx-Montague, NY",
            "udx-Rapid City, SD",
            "uex-Grand Island, NE",
            "vax-Moody AFB, GA",
            "vbx-Vandenberg AFB, CA",
            "vnx-Vance AFB, OK",
            "vtx-Los Angeles, CA",
            "vwx-Evansville, IN",
            "yux-Yuma, AZ"
                            )
        option.grid(row = 1, column = 0, sticky = W)
        #option.config(width = 15)

        #SELECT PRODUCT
        self.product = StringVar(self)
        self.product.set("N0R: Base Reflect") # initial value
        option = OptionMenu(self, self.product,
                            "N0R: Base Reflect",
                            "N0S: Relative Motion",
                            "N0V: Base Velocity",
                            "N1P: 1 Hour Precip",
                            "NCR: Comp. Reflect",
                            "NTP: Total Precip",
                            )
        option.grid(row = 1, column = 1, sticky = W)

        #REFRESH TIME
        self.refresht = StringVar(self)
        self.refresht.set("2 Min") # initial value
        option = OptionMenu(self, self.refresht,
                            "1 Min",
                            "2 Min",
                            "5 Min",
                            "10 Min",
                            )
        option.grid(row = 2, column = 1, sticky = W)

        #NUMBER OF IMAGES TO ANIMATE
        self.imgs2show = StringVar(self)
        self.imgs2show.set("40")
        option = OptionMenu(self, self.imgs2show,
                            "15",
                            "30",
                            "40",
                            "60",
                            "ALL",
                            )
        option.grid(row = 3, column = 1, sticky = W)

        #START TIMER BUTTON    command= lambda: action(someNumber)
        self.buttonT = Button(self, text='START TIMER', command= self.make_url)
        self.buttonT.grid(row= 4, column =0, sticky = W)

        #STOP TIMER BUTTON
        self.buttonTS = Button(self, text='STOP TIMER', command= self.stopt)
        self.buttonTS.grid(row= 4, column =1, sticky = W)
        self.buttonTS.configure(state=DISABLED)

        #LABEL INSTRUCTIONS
        self.instructions3 = Label(self, text = "GET IMAGES EVERY:")
        self.instructions3.grid(row = 2, column = 0, columnspan = 2, sticky = W)

        #LABEL INSTRUCTIONS
        self.instructions4 = Label(self, text = "IMAGES TO ANIMATE:")
        self.instructions4.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        #LABEL STATUS
        self.instructions4 = Label(self, text = "STATUS:")
        self.instructions4.grid(row = 5, column = 0, columnspan = 2, sticky = W)

        #TEXT AREA UPDATED
        self.text = tkinter.scrolledtext.ScrolledText(self, width = 39, height = 13, wrap = WORD)
        self.text.grid(row = 5, column = 0, columnspan = 2, sticky = W)
        self.text.config(state=DISABLED)

        self.pb = ttk.Progressbar(root,orient ="horizontal",length = 280, mode ="determinate", maximum = 100)
        self.pb.grid()
        #self.pb.start()

        #SETUP TIME TEXT AT BOTTOM
        self.sec = 0
        self.time = Label(root, fg='green')
        self.time.grid()

        #SETUP VARIABLES
        self.t = False
        self.Pathname = ""
        self.Version = "1.2"
        self.download_progress = 0

        #AUTOSTART?
        self.repeat()

    #SETUP TIMER FUNCTION
    def repeat(self):
        self.t = True
        timeout = self.refresht.get()
        if timeout == "1 Min":
            self.settimer = 60000
        if timeout == "2 Min":
            self.settimer = 120000
        if timeout == "5 Min":
            self.settimer = 300000
        if timeout == "10 Min":
            self.settimer = 600000
        self.time['text'] = "Timer Running : Downloads Run: " + str(self.sec)
        self.id = self.time.after(self.settimer, self.make_url)
        #print("Started")

    def stopt(self):
        self.t = False
        self.time.after_cancel(self.id)
        self.buttonT.configure(state=NORMAL,text = "START TIMER")
        self.buttonTS.configure(state=DISABLED)
        #stop progress bar
        self.pb.stop()
        self.pb.update()
        self.time['text'] = "Timer Stopped"
        #print("Stopped")
        self.update()

######################################## DOWNLOADER

# ********************** SHOW ABOUT *****************************

    def show_about(self):

        ABOUT_TEXT = """About
        NOAA ANIMATOR V1.2
        Program © 2015 David Rankin
        e-mail David@rankinstudio.com
        Website: http://www.rankinstudio.com/NOAA_ANIMATOR"""

        toplevel = Toplevel()
        toplevel.resizable(width=FALSE, height=FALSE)
        toplevel.title('About')
        toplevel.wm_iconbitmap('s.ico')
        label1 = Label(toplevel, text=ABOUT_TEXT, height=0, width=50, justify=LEFT)
        label1.grid()

    def make_soupkz(self, urlk):
            html3 = urlopen(urlk).read()
            return BeautifulSoup(html3, "lxml")

    def make_url(self): # Make URL from user selection

        self.text.config(state=NORMAL)
        self.text.delete(0.0, END) #clear textbox

        #CREATE RADAR URL FROM SELECTIONS
        radar= self.site.get()
        radar = radar[:3]
        radar = radar.upper() #change to upper case
        productv = self.product.get()
        productv = productv[:3]

        #STOP TIMER TO DOWNLOAD DATA
        if self.t == True:
            self.stopt()
            self.t = False
        # SET THE TIMER BUTTON TO DISABLED PREVENT MULTIPLE TIMERS
        self.sec += 1
        self.buttonT.configure(state=DISABLED,text = "TIMER RUNNING")
        self.update()

        #BASE URL
        self.burl = 'http://radar.weather.gov/ridge/RadarImg/'+ productv +'/' + radar + '/'
        self.urldata = 'http://radar.weather.gov/ridge/RadarImg/N0R/'
        self.urlimgzero = 'http://radar.weather.gov/ridge/RadarImg/'

        #MAKE THREE URLS FOR EACH SORT
        q1 = self.burl + '?C=D;O=D'
        q2 = self.burl + '?C=N;O=D'
        q3 = self.burl + '?C=M;O=D'

        self.urls = [q1,q2,q3]

        #FIRE GET IMAGES
        self.get_images(self.burl)

    def make_soupimgs(self, url):

        q = Request(url)
        q.add_header('User-Agent', 'Mozilla/5.0')
        q.add_header('Cache-Control', 'max-age=0')
        a = urlopen(q).read()

        return BeautifulSoup(a, "lxml")

    def make_soupcoords(self, urldata):

        html2 = urlopen(urldata).read()
        return BeautifulSoup(html2, "lxml")

    def get_images(self, url):
        self.text.config(state=NORMAL)
        #self.text.delete(0.0, END) #clear textbox
        self.time['text'] = "Downloading Images..."
        self.dl_p = 0
        self.pb.stop()
        self.pb.update()

        for url in self.urls:
            try: # CATCH NO INERNET ERROR
                soup = self.make_soupimgs(url)
                images = [link for link in soup.findAll('a')] # FIND ANCHORS
                image_links = [tag.get('href') for tag in images] #FROM A, GET HREF

                for each in image_links:

                    #UPDATE PROGRESS BAR
                    self.pb.config(mode="determinate")
                    self.dl_p = 100 / len(image_links)
                    self.pb.step(self.dl_p)
                    self.pb.update()

                    if(each is not None):  #MAKE SURE NOT EMPTY
                        if each.endswith("gif"):  #MAKE SURE .GIF FILE
                            try: #TRY, CATCH 404 ERROR

                                each = self.burl + each  #add the base url back to it to make it a full url
                                #print (each)      #print to test it is working
                                filename = each.split('/')[-1] #split the file name out starting from the right

                                mypathR = "RADAR"
                                mypath1 = filename.split('_')[1] #split the date out starting from the left
                                mypath2 = filename[:3] #split out ICX
                                mypath3 = filename.split('_')[3] #Get NOR.GIF
                                mypath3 = mypath3[:3] #GET NOR

                                fullpath = os.path.join(mypathR, mypath2, mypath3, mypath1) #Make NOR / ICX / DATE Path

                                if not os.path.isdir(fullpath): #See if it exists
                                    os.makedirs(fullpath) #If not, make it

                                fullFpath = os.path.join(mypathR, mypath2, mypath3, mypath1, filename) #use it and filename to create path to save images

                                if os.path.isfile(fullFpath): #chcek to see if image path already exists
                                    message = filename + ' exists \n'
                                    self.text.insert(0.0, message)
                                    self.update()
                                    continue

                                message = 'Downloading ' + filename +'\n' #UPDATE THIS
                                self.text.insert(0.0, message)
                                self.update()

                                urllib.request.urlretrieve(each, fullFpath) #download images each, to full path

                            except urllib.error.HTTPError as err: #catch 404 not found and continue
                                if err.code == 404:
                                    message = filename + ' Not found \n'
                                    self.text.insert(0.0, message)
                                    self.update()
                                    continue

                #return image_links    #return the links ENDS FOR LOOP

            except urllib.error.URLError: # CATCH NO INTERNET ERRORS!
                message = 'Connection Failed on Run: ' + str(self.sec) + '\n'
                self.text.insert(0.0, message)
                self.buttonT.configure(state=NORMAL,text = "START TIMER")
                self.update()

        #RESTART PROGRESS BAR
        self.pb.config(mode="indeterminate")
        self.pb.start()
        self.pb.update()

        message = 'Downloading Complete on Run: ' + str(self.sec) + '\n'
        self.text.insert(0.0, message)
        self.update()
        self.get_coords(self.urldata)

    def get_coords(self, urldata):

        self.text.config(state=NORMAL)

        try:
            datadir = os.path.join(os.getcwd(), "DATA")
            if os.path.isdir(datadir) and os.path.isdir(datadir) is not None: #CHECK FOR DATA DIR
                    message = 'DATA Directory Exists\n\n' #UPDATE THIS
                    self.text.insert(0.0, message)
                    self.update()
                    self.write_file() #CALL THE CREATE KML FILE
            else:

                #RESET PROGRESS BAR
                self.time['text'] = "Downloading Data Files..."
                self.dl_p = 0
                self.pb.stop()
                self.pb.update()

                message = 'Downloading Data. Please Wait...\n\n' #UPDATE THIS
                self.text.insert(0.0, message)
                self.update()

                soup = self.make_soupcoords(urldata)
                coords = [link for link in soup.findAll('a')] # FIND ANCHORS
                coord_links = [tag.get('href') for tag in coords]
                for each in coord_links:

                    self.dl_p = 100 / len(coord_links)
                    self.pb.config(mode="determinate")
                    self.pb.step(self.dl_p)
                    self.pb.update()

                    if(each is not None):
                        if each.endswith("gfw"):
                            try:
                                each = urldata + each
                                #print(each)
                                filename=each.split('/')[-1] #split the file name out starting from the right
                                dpath1 = os.getcwd()
                                dpath2 = "DATA"
                                fullpath = os.path.join(dpath1, dpath2) #Make NOR / ICX / DATE Path
                                if not os.path.isdir(fullpath): #See if it exists
                                    os.makedirs(fullpath) #If not, make it
                                fullFpath = os.path.join(dpath1, dpath2, filename)

                                if os.path.isfile(fullFpath): #chcek to see if image path already exists
                                    message = filename + ' exists \n'
                                    self.text.insert(0.0, message)
                                    self.update()
                                    continue

                                urllib.request.urlretrieve(each, fullFpath)

                            except urllib.error.HTTPError as err: #catch 404 not found and continue
                                if err.code == 404:
                                    message = ' Not found \n'
                                    self.text.insert(0.0, message)
                                    self.update()
                                    continue

                message = 'Data Downloaded \n' #UPDATE THIS
                self.text.insert(0.0, message)

                #CALL FUNCTION TO CREATE KML FILES
                self.write_file()

                #RESTART PROGRESS BAR
                self.pb.config(mode="indeterminate")
                self.pb.start()
                self.pb.update()

        except urllib.error.URLError: # CATCH NO INTERNET ERRORS!
            message = '(Data) Connection Failed on Run: ' + str(self.sec) + '\n'
            self.text.insert(0.0, message)
            self.update()
            return
        self.text.config(state=DISABLED)

################################ WRITE KML FILES

    def write_file(self):

        """Create KML Files"""
        radar= self.site.get()
        radar = radar[:3]
        radar = radar.upper() #change to upper case

        #TRACK EACH FOLDER FILE LIST SEPARATELY
        self.fulllist = []

        #Make the coordinates
        # IMG 600 X 550
        self.imgw = 600
        self.imgh = 550

        datadir = os.path.join(os.getcwd(), "DATA")
        name = radar + "_N0R_0.gfw"
        for root, dirs, files in os.walk(datadir):
            if name in files:
                #FIND THE CONFIG FILE BASED ON RADAR SELECTED
                name = os.path.join(root, name)
                with open(name, "r") as f:
                    searchlines = f.readlines()
                    #LINES are 0 to 5
                    #NORTH = LINE 5
                    #SOUTH = (NORTH) - (LINE 0 * IMG HEIGHT)
                    #EAST = (WEST) - (LINE2 * IMG WIDTH)
                    #WEST = LINE 4
                    smult = searchlines[0] # South Multiplier
                    smult = Decimal(smult)#CONVER TO DECIMAL
                    emult = searchlines[3]
                    emult = Decimal(emult)
                    self.coorn = searchlines[5] # NORTH
                    self.coorn = Decimal(self.coorn) #CONVER TO DEC
                    self.coorw = searchlines[4] #WEST
                    self.coorw = Decimal(self.coorw)#CONVERT TO DEC
                    #CALCULATE SOUTH AND EAST
                    self.coors = (self.coorn) - (smult * self.imgh)
                    self.coore = (self.coorw) - (emult * self.imgw)
                    #print(self.coorn, self.coors, self.coore, self.coorw)
                    #return
            else: # CATCH NO CONFIG FILE FOUND
                message = 'Config File Not Found in DATA Directory. Delete DATA Folder and Retry \n\n'
                self.text.insert(0.0, message)
                self.update()
                return

        #SETUP PATH TO SAVE KML FILE
        pathR = "RADAR"
        productv = self.product.get()
        productv = productv[:3]

        #GET SITE NAME TO CREATE KML WITH IT
        sitename = self.site.get()
        sitename = sitename.split('-')[1]

        #WHERE TO SAVE KML
        self.kmlpath = os.path.join(os.getcwd(),pathR, radar, productv)

        #LIST THE DIRECTORIES IN THE KML PATH
        self.dirs = os.listdir(self.kmlpath) ## FIX ON NO CONNECTION!

        #PREVIOUS AND NEXT ITTERATOR ! AWESOME ! - DEFINED LATER
        def previous_and_next(some_iterable):
            items, nexts = tee(some_iterable, 2)
            nexts = chain(islice(nexts, 1, None), [None])
            return zip_longest(items, nexts)


        for self.file in self.dirs: # GET THE DATED FOLDER WITH IMAGES
            if len(self.file) == 8: # MAKE SURE IT IS JUST THE FOLDER

                #IGNORE ANYTHING BUT THE GIFS!
                onlygifs = os.path.join(self.kmlpath, self.file, '*.gif')
                listing = glob.glob(onlygifs)

                # COMBINE ALL IMAGE FILES IN ALL FOLDERS INTO ONE LIST!
                self.fulllist = self.fulllist + listing

        #TRIM THE LIST BY SPECIFIED IMAGE COUNT
        trim = self.imgs2show.get()
        if trim == "ALL":
            print("ALL SELECTED!")
            #print(len(self.fulllist))
        else:
            trim = int(trim)
            trim = -abs(trim)
            self.fulllist = self.fulllist[trim:]
            #print(len(self.fulllist))

        #WRITE THE LIST TO KML FILE!!!
        print (time.strftime("%Y%m%d"))
        #ICX_20150503_2103_N0R.gif

        self.f = open(self.kmlpath + "/" + sitename + '.kml','w') #CREATE MATCHING KML FILE NAME
        #self.f = open(self.kmlpath + "/" + self.file + '.kml','w') #CREATE MATCHING KML FILE NAME
        self.f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        self.f.write('<kml xmlns="http://earth.google.com/kml/2.1"> \n')
        self.f.write('<Folder> \n')
        self.f.write('       <name>'+sitename+'</name>\n')

        #for self.img in self.imgs: #DEFINE THE ITEM HERE NEW!! WORKS
        for item, nxt in previous_and_next(self.fulllist):

            if nxt is not None:
               nxt = nxt.split('\\')[-1]
            item = item.split('\\')[-1]
            #print ("Item is now", item, "next is", nxt)

            self.f.write("      <GroundOverlay>\n")
            self.f.write("       <name>Current Radar</name>\n")
            self.f.write("       <drawOrder>24</drawOrder>\n")
            self.f.write("          <TimeSpan>\n")

            if nxt is not None:
                chref = item[4:12]
                cyear = item[4:8]
                cmonth = item[8:10]
                cday = item[10:12]
                chour = item[13:15]
                cminute = item[15:17]
                begin = cyear+"-"+cmonth+"-"+cday+"T"+chour+":"+cminute+":00Z"

                nyear = nxt[4:8]
                nmonth = nxt[8:10]
                nday = nxt[10:12]
                nhour = nxt[13:15]
                nminute = nxt[15:17]
                endt = nyear+"-"+nmonth+"-"+nday+"T"+nhour+":"+nminute+":00Z"

                self.f.write("            <begin>"+begin+"</begin>\n")
                self.f.write("            <end>"+endt+"</end>\n")
                self.f.write("          </TimeSpan>\n")
                self.f.write("        <Icon>\n"
                             "          <href>./"+ chref + '/' + item + "</href>\n"
                             "           <viewBoundScale>0.99</viewBoundScale>\n"
                             "        </Icon>\n"
                             "        <LatLonBox>\n"
                             "               <north>"+str(self.coorn)+"</north>\n"
                             "               <south>"+str(self.coors)+"</south>\n"
                             "               <east>"+str(self.coore)+"</east>\n"
                             "               <west>"+str(self.coorw)+"</west>\n"
                             "        </LatLonBox>\n"
                             "        </GroundOverlay>\n\n")

            if nxt is None: # CAPTRUE LAST END TIME AND COPY THE PREVIOUS TIME
                chref=item[4:12]
                cyear = item[4:8]
                cmonth = item[8:10]
                cday = item[10:12]
                chour = item[13:15]
                cminute = item[15:17]
                begin = cyear+"-"+cmonth+"-"+cday+"T"+chour+":"+cminute+":00Z"

                nyear = cyear
                nmonth = cmonth
                nday = cday
                nhour = chour
                nminute = cminute
                nminutef = int(nminute) + 5 #FIX THIS FOR TIME OVER 59min

                if nminutef > 59:
                    nminutef = 59

                endt = nyear+"-"+nmonth+"-"+nday+"T"+nhour+":"+str(nminutef)+":00Z"

                self.f.write("            <begin>"+begin+"</begin>\n")
                self.f.write("            <end>"+endt+"</end>\n")
                self.f.write("          </TimeSpan>\n")
                self.f.write("        <Icon>\n"
                             "          <href>./"+ chref + '/' + item + "</href>\n"
                             "           <viewBoundScale>0.99</viewBoundScale>\n"
                             "        </Icon>\n"
                             "        <LatLonBox>\n"
                             "               <north>"+str(self.coorn)+"</north>\n"
                             "               <south>"+str(self.coors)+"</south>\n"
                             "               <east>"+str(self.coore)+"</east>\n"
                             "               <west>"+str(self.coorw)+"</west>\n"
                             "        </LatLonBox>\n"
                             "        </GroundOverlay>\n\n")
                self.lastimage = cmonth+"/"+cday+"/"+cyear+" - "+chour+":"+cminute+"UTC"
                #END OF FOR IMAGES IN FOLDER

        #WRITE END OF KML FILE
        self.f.write('</Folder>\n')
        self.f.write('</kml>\n')
        self.f.close()

        #GET KML PATH TO PRINT INFO
        kpath = os.path.join(self.kmlpath, sitename+".kml")
        message = "KML Generated at:\n\n"+kpath+"\n\nLatest Image:"+self.lastimage+"\n\n"
        self.buttonTS.configure(state=NORMAL)
        self.text.insert(0.0, message)
        self.update()
        self.repeat()

#################################################  SETUP APPLICATION

root = Tk()
root.title("NOAA ANIMATOR")
root.geometry("335x400")
try:
    root.wm_iconbitmap('s.ico')
    #root.mainloop()
except TclError:
    print ('No ico file found')
app = Application(root)
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
