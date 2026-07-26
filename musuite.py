#!/usr/bin/env python3
import subprocess, os, sys, random
from time import sleep
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromDictionary as cFD
Versie = "0.02"
#MUSUITElogo="""
# /____    ___                        __          _\
#||____   ___  __  __  ___  __  __ (#)____   ___ __||
#||o____ __ _  __  __ // \| __  __ |_ __    //_\\ o||
#||o_ ____  _  __  __ \____ __  __ |_ __    __  __o||
#||__  __  ___  \\/|\ |\_//  \\/|\ |_  \\/| \\_// _||
# \                                                /
#"""
MUSUITElogo="""
 /____   ____                        __          _\\
||____   ___  __  __  ___  __  __ (#)____   ___ __||
||o____ __ _  __  __ // \\| __  __ |_ __    //_\\\\ o||
||o_ ____  _  __  __ \\____ __  __ |_ __    __  __o||
||__  __  ___  \\\\/|\\ |\\_//  \\\\/|\\ |_  \\\\/| \\\\_// _||
 \\                                                /
"""
for i in MUSUITElogo:
    print(i, end = "", flush = True)
    sleep(0.005)
print()
pad = "/home/media/Samsung/maestraccio/Muziek/mp3/"
stijlen = {
        "FLM":"Filmmuziek",
        "FSR":"Funk, Soul, R&B",
        "JZF":"Jazz - Fusion",
        "JZP":"Jazz - Piano",
        "JZV":"Jazz - Vocaal",
        "JZZ":"Jazz",
        "KLB":"Klassiek - Barok",
        "KLM":"Klassiek - Modern",
        "KLS":"Klassiek",
        "LAM":"Latijns-Amerikaans",
        "PPR":"Pop, Rock",
        "SSW":"SingerSongwriter",
        "VAR":"Various",
        "WLD":"Wereldmuziek"
        }
gmtdict = {
        "G":"Genre, Stijl, Categorie",
        "M":"Map, Album, Verzameling",
        "T":"Track, Song, Opus"
        }
gmtlijst = []
for i in gmtdict:
    gmtlijst.append(i.lower())
jalijst = ["j","ja","y","yes"]
neelijst = ["n","no","nee"]
janee = ["J","N"]
quitlijstbasis = ["Q","X"]
quitlijst = []
for i in quitlijstbasis:
    j = ":"+i
    if i not in quitlijst:
        quitlijst.append(i.upper())
        quitlijst.append(i.lower())
        quitlijst.append(j.upper())
        quitlijst.append(j.lower())
genrelijst = []
for i in os.listdir(pad):
    if os.path.isdir(pad+i):
        genrelijst.append(i)
genrelijst = sorted(genrelijst)
genrelijstlang = []
for g in genrelijst:
    if g in stijlen:
        genrelijstlang.append(g+" : "+stijlen[g])
    else:
        genrelijstlang.append(g)
genrelijstlang = sorted(genrelijstlang)
minleng = len(min(genrelijst, key=len))
optieslijst = ["*"]
for i in genrelijst:
    for l in range(minleng):
        if i[:l+1] not in optieslijst:
            optieslijst.append(i[:l+1])
            optieslijst.append(i.lower()[:l+1])

def play(tracklijst):
    print(len(tracklijst))
    if len(tracklijst) == 0:
        return
    elif len(tracklijst) > 99:
        print("De lijst is erg lang, wil je hem toch tonen?")
        ja,index = cFNL([janee,"A",1,2,"-#>",jalijst+neelijst+quitlijst])
        print(ja)
        if ja.lower() in quitlijst:
            exit()
        if ja.lower() in neelijst:
            pass
        else:
            for i in tracklijst:
                track = os.path.basename(i) 
                print(str(tracklijst.index(i)+1)+" : "+track)
    else:
        for i in tracklijst:
            track = os.path.basename(i) 
            print(str(tracklijst.index(i)+1)+" : "+track)
    random = ""
    if len(tracklijst) != 1:
        print("Willekeurige volgorde?")
        ja,index = cFNL([janee,"A",1,1,"-#>",jalijst+neelijst+quitlijst])
        if ja.lower() in quitlijst:
            exit()
        if ja.lower() in jalijst:
            random = "Z"
    try:
        with open(os.path.join(pad,"tracklijst.m3u"),"w") as tl:
            for tr in tracklijst:
                print(tr, file=tl)
        subprocess.run(["mpg123-alsa", "-vm%s" % (random), "-@", os.path.join(pad,"tracklijst.m3u")])
        os.remove(os.path.join(pad,"tracklijst.m3u"))
    except:
        pass

loop = True
while loop == True:
    v,k = cFD([gmtdict,0,"G","-#>",gmtlijst+quitlijst])
    if k.upper() in quitlijst:
        exit()
    if k.upper() == "T":
        tracklijstkort = []
        zoekterm = input("Voer een zoekterm in (geen afsluitopdracht zoals \"Q\"):\n")
        if zoekterm in quitlijst:
            exit()
        for dirpath, dirnames, filenames in os.walk(pad):
            for track in filenames:
                if zoekterm in track:
                    tracklijstkort.append(track)
        tracklijstkort = sorted(tracklijstkort)
        tracksel,index = cFNL([tracklijstkort,"A",1,1,"-#>",True,quitlijst])
        if tracksel in quitlijst:
            exit()
        tracklijst = []
        for i in tracksel:
            for dirpath, dirnames, filenames in os.walk(pad):
                for track in filenames:
                    if i in track:
                        tracklijst.append(os.path.join(dirpath, track))
        tracklijst = sorted(tracklijst)
        play(tracklijst)
    elif k.upper() == "M":
        optie,index = cFNL([genrelijstlang,"A",1,2,"-#>",quitlijst])
        if optie in quitlijst:
            exit()
        if optie in genrelijstlang:
            optie = genrelijst[genrelijstlang.index(optie)]
        tracklijst = []
        gpad = os.path.join(pad,optie)
        mappenlijst = []
        for m in os.listdir(gpad):
            if os.path.isdir(os.path.join(gpad,m)):
                mpad = os.path.join(gpad,m)
                mappenlijst.append(mpad)
        mappenlijst = sorted(mappenlijst)
        mappenlijstkort = []
        optielijst = []
        for i in mappenlijst:
            mappenlijstkort.append(i[len(gpad)+1:])
        optie,index = cFNL([mappenlijstkort,"A",1,1,"-#>",True,optieslijst+quitlijst])
        if optie in quitlijst:
            exit()
        if type(optie) == str:
            optie = optie.upper()
            for i in genrelijst:
                if optie in [i[:1],i[:2],i]:
                    if i not in optielijst:
                        optielijst.append(i)
            optie = optielijst
        tracklijst = []
        for o in optie:
            if o in mappenlijstkort:
                mmap = mappenlijst[mappenlijstkort.index(o)]
                mpad = os.path.join(gpad,mmap)
                for track in os.listdir(mpad):
                    if track.endswith(".mp3"):
                        tpad = os.path.join(mpad,track)
                        tracklijst.append(tpad)
        tracklijst = sorted(tracklijst)
        play(tracklijst)
    else:
        optielijst = []
        optie,index = cFNL([genrelijstlang,"A",1,2,"-#>",True,optieslijst+quitlijst])
        if optie in quitlijst:
            exit()
        if type(optie) == str:
            optie = optie.upper()
            for i in genrelijst:
                if optie in [i[:1],i[:2],i]:
                    if i not in optielijst:
                        optielijst.append(i)
            optie = optielijst
        for g in optie:
            if g in genrelijstlang:
                optie[optie.index(g)] = genrelijst[genrelijstlang.index(g)]
        if "*" in optie:
           tracklijst = []
           for g in genrelijst:
               gpad = os.path.join(pad,g)
               mappenlijst = []
               for m in os.listdir(gpad):
                   if os.path.isdir(os.path.join(gpad,m)):
                       mpad = os.path.join(pad,g,m)
                       mappenlijst.append(mpad)
               mappenlijst = sorted(mappenlijst)
               for m in mappenlijst:
                   mpad = os.path.join(gpad,m)
                   for track in os.listdir(mpad):
                       if track.endswith(".mp3"):
                           tpad = os.path.join(mpad,track)
                           tracklijst.append(tpad)
           tracklijst = sorted(tracklijst)
           play(tracklijst)
        elif len(optie) < 1:
            pass
        else:
           tracklijst = []
           for g in optie:
               gpad = os.path.join(pad,g)
               mappenlijst = []
               for m in os.listdir(gpad):
                   if os.path.isdir(os.path.join(gpad,m)):
                       mpad = os.path.join(pad,g,m)
                       mappenlijst.append(mpad)
               mappenlijst = sorted(mappenlijst)
               for m in mappenlijst:
                   mpad = os.path.join(gpad,m)
                   for track in os.listdir(mpad):
                       if track.endswith(".mp3"):
                           tpad = os.path.join(mpad,track)
                           tracklijst.append(tpad)
           tracklijst = sorted(tracklijst)
           play(tracklijst)
