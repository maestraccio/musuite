#!/usr/bin/env python3
import subprocess, os, sys, random, textwrap
from time import sleep
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromDictionary as cFD
from adjustables import pad,genredict,streamsdict
Versie = "0.05"
Date = "2026-07-29"
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
wraptext = "Typ de optie van je keuze in op je toetsenbord, of gebruik de \"haakjes sluiten\" (\")\",\"]\",\"}\",\">\": vooruit) en \"haakjes openen\" (\"(\",\"[\",\"{\",\"<\": achteruit) om er naartoe te bladeren. Bevestig iedere keuze met \"Enter\". Ga terug naar het begin met \"B\" (Back) of \"U\" (Undo) of sluit het programma helemaal af met \"Q\" (Quit) of \"X\" (eXit). Voor het afspelen wordt het programma \"mpg123\" aangeroepen. Voor het gebruik daarvan kun je de officiele manpages raadplegen met de opdracht \"man mpg123\"."
for i in textwrap.wrap(wraptext,80):
    print(i)
print()
print("Veel luisterplezier!")
print()
man = ["man mpg123"]
streamslijst = []
for i in streamsdict:
    streamslijst.append(i)
mosdict = {
        "M":"MP3-file(s) uit eigen collectie",
        "S":"online Stream"
        }
moslijst = []
for i in mosdict:
    moslijst.append(i.lower())
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
backlijstbasis = ["B","U"]
backlijst = []
for i in backlijstbasis:
    j = ":"+i
    if i not in backlijst:
        backlijst.append(i.upper())
        backlijst.append(i.lower())
        backlijst.append(j.upper())
        backlijst.append(j.lower())
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
    if g in genredict:
        genrelijstlang.append(g+" : "+genredict[g])
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

def defgpad():
    optie,index = cFNL([genrelijstlang,"A",1,1,"-#>",man+backlijst+quitlijst])
    if optie in quitlijst:
        exit()
    elif optie in backlijst:
        return optie
    elif optie in man:
        subprocess.run(["man", "mpg123"])
    if optie in genrelijstlang:
        optie = genrelijst[genrelijstlang.index(optie)]
    tracklijst = []
    gpad = os.path.join(pad,optie)
    return gpad

def printtracklijst(tracklijst):
    print(len(tracklijst))
    wraptext = "De tracklijst is erg lang en past mogelijk niet op je scherm. De lijst wordt eerst in meerdere delen getoond zodat je de nummers van de track(s) die je in je selectie wilt een keer hebt kunnen zien. Daarna krijg je de optie om je definitieve keuze in te geven."
    print()
    for i in textwrap.wrap(wraptext,80):
        print(i)
    print()
    lenlijst = len(tracklijst)
    count = 0
    while count < lenlijst:
        track = os.path.basename(tracklijst[count]) 
        print(("{:%s}" % len(str(lenlijst))).format(tracklijst.index(tracklijst[count])+1)+" : "+track)
        count += 1
        if count % 50 == 0:
            go = input()
            if go in quitlijst:
                exit()
            elif go in backlijst:
                break
    print()
    wraptext = "Het einde van de lijst is bereikt en de optie om je keuze in te voeren volgt hierna. Onthoud de nummers van de mappen die je wilt selecteren. Druk nu eerst op \"Enter\""
    for i in textwrap.wrap(wraptext,80):
        print(i)
    go = input()
    if go in quitlijst:
        exit()

def printmappenlijst(mappenlijst):
    wraptext = "De mappenlijst is erg lang en past mogelijk niet op je scherm. De lijst wordt eerst in meerdere delen getoond zodat je de nummers van de map(pen) die je in je selectie wilt een keer hebt kunnen zien. Daarna krijg je de optie om je definitieve keuze in te geven."
    print()
    for i in textwrap.wrap(wraptext,80):
        print(i)
    print()
    lenlijst = len(mappenlijst)
    count = 0
    while count < lenlijst:
        mapp = os.path.basename(mappenlijst[count]) 
        print(("{:%s}" % len(str(lenlijst))).format(mappenlijst.index(mappenlijst[count])+1)+" : "+mapp)
        count += 1
        if count % 50 == 0:
            go = input()
            if go in quitlijst:
                exit()
            elif go in backlijst:
                break
    print()
    wraptext = "Het einde van de lijst is bereikt en de optie om je keuze in te voeren volgt hierna. Onthoud de nummers van de mappen die je wilt selecteren. Druk nu eerst op \"Enter\""
    for i in textwrap.wrap(wraptext,80):
        print(i)
    go = input()
    if go in quitlijst:
        exit()

def play(tracklijst):
    if len(tracklijst) == 0:
        return
    elif len(tracklijst) > 50:
        print("De lijst is lang, wil je hem toch tonen?")
        ja,index = cFNL([janee,"A",1,2,"-#>",man+jalijst+neelijst+backlijst+quitlijst])
        if ja.lower() in quitlijst:
            exit()
        elif ja.lower() in backlijst:
            return
        elif ja.lower() in man:
            subprocess.run(["man", "mpg123"])
        elif ja.lower() in jalijst:
            printtracklijst(tracklijst)
    else:
        for i in tracklijst:
            track = os.path.basename(i) 
            print(str(tracklijst.index(i)+1)+" : "+track)
    random = "Z"
    if len(tracklijst) != 1:
        print("Willekeurige volgorde?")
        ja,index = cFNL([janee,"A",1,1,"-#>",man+jalijst+neelijst+backlijst+quitlijst])
        if ja.lower() in quitlijst:
            exit()
        elif ja.lower() in backlijst:
            return
        elif ja.lower() in man:
            subprocess.run(["man", "mpg123"])
        if ja.lower() in neelijst:
            random = ""
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
    v,k = cFD([mosdict,0,"M","-#>",man+moslijst+backlijst+quitlijst])
    if k.upper() in quitlijst:
        exit()
    elif k.upper() in backlijst:
        pass
    elif k in man:
        subprocess.run(["man", "mpg123"])
    elif k.upper() == "S":
        s,index = cFNL([streamslijst,"A",1,1,"-#>",man+backlijst+quitlijst])
        if s in quitlijst:
            exit()
        elif s in backlijst:
            pass
        elif s in man:
            subprocess.run(["man", "mpg123"])
        else:
            su = streamsdict[s]
            subprocess.run(["mpg123-alsa", "-vm",  su])
    else:
        v,k = cFD([gmtdict,0,"G","-#>",man+gmtlijst+backlijst+quitlijst])
        if k.upper() in quitlijst:
            exit()
        elif k.upper() in backlijst:
            pass
        elif k in man:
            subprocess.run(["man", "mpg123"])
        elif k.upper() == "T":
            tracklijstkort = []
            zoekterm = input("Voer een zoekterm in (geen afsluitopdracht zoals \"Q\"):\n")
            if zoekterm in quitlijst:
                exit()
            elif zoekterm in backlijst:
                pass
            elif zoekterm in man:
                subprocess.run(["man", "mpg123"])
            else:
                for dirpath, dirnames, filenames in os.walk(pad):
                    for track in filenames:
                        if zoekterm in track:
                            tracklijstkort.append(track)
                tracklijstkort = sorted(tracklijstkort)
                printtracklijst(tracklijstkort)
                tracksel,index = cFNL([tracklijstkort,"A",1,1,"-#>",True,man+backlijst+quitlijst])
                if tracksel in quitlijst:
                    exit()
                elif tracksel in backlijst:
                    pass
                elif tracksel in man:
                    subprocess.run(["man", "mpg123"])
                else:
                    tracklijst = []
                    for i in tracksel:
                        for dirpath, dirnames, filenames in os.walk(pad):
                            for track in filenames:
                                if i in track:
                                    tracklijst.append(os.path.join(dirpath, track))
                    tracklijst = sorted(tracklijst)
                    play(tracklijst)
        elif k.upper() == "M":
            gpad = defgpad()
            if gpad in backlijst:
                pass
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
            if len(mappenlijst) > 50:
                printmappenlijst(mappenlijstkort)
            optie,index = cFNL([mappenlijstkort,"A",1,1,"-#>",True,man+optieslijst+backlijst+quitlijst])
            if optie in quitlijst:
                exit()
            elif optie in backlijst:
                pass
            elif optie in man:
                subprocess.run(["man", "mpg123"])
            if type(optie) == str and optie not in man+optieslijst+backlijst+quitlijst:
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
            #optielijst = []
            optie,index = cFNL([genrelijstlang,"A",1,1,"-#>",True,man+optieslijst+backlijst+quitlijst])
            if optie in quitlijst:
                exit()
            elif optie in backlijst:
                pass
            elif optie in man:
                subprocess.run(["man", "mpg123"])
            elif type(optie) == str and optie not in man+backlijst+quitlijst:
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
                else:
                    optie = optie.upper()
                    for i in genrelijst:
                        if optie in [i[:1],i[:2],i]:
                            if i not in optielijst:
                                optielijst.append(i)
                    optie = optielijst
                    for g in optie:
                        if g in genrelijstlang:
                            optie[optie.index(g)] = genrelijst[genrelijstlang.index(g)]
                tracklijst = sorted(tracklijst)
                play(tracklijst)
            elif type(optie) == list: 
                if len(optie) < 1:
                    pass
                else:
                   tracklijst = []
                   for g in optie:
                       g = genrelijst[genrelijstlang.index(g)]
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
