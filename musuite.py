#!/usr/bin/env python3
import subprocess, os, sys, random, textwrap
from time import sleep
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromDictionary as cFD
from adjustables import lang,picklang,showhelp,pad,genredict,streamsdict,volume
Versie = "1.24"
Date = "2026-11-08"
hier = os.path.dirname(os.path.realpath(__file__))
os.chdir(hier)
colD = "\033[94m" # Directory
colG = "\033[93m" # Genre
colH = "\033[7m"  # Help
colJ = "\033[92m" # Ja
colN = "\033[91m" # Nee
colR = "\033[0m"  # RESET
colS = "\033[95m" # Stream
colT = "\033[96m" # Track
colV = "\033[32m" # Volume
colW = "\033[33m" # Willekeurig
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
backlijstbasis = ["B"]
backlijst = ["B","b"]
helplijstbasis = ["H"]
helplijst = ["H","h"]
langlijstbasis = ["L"]
langlijst = ["L","l"]
quitlijstbasis = ["Q"]
quitlijst = ["Q","q"]
neelijstCJ = ["i","li"]
jalijstCJ = ["a","la"]
neejaCJ = [colN+"li"+colR,colJ+"la"+colR]
neelijstEN = ["N","n","no"]
jalijstEN = ["Y","y","yes","Yes"]
neejaEN = [colN+"N"+colR,colJ+"Y"+colR]
neelijstIT = ["N","n","no","No"]
jalijstIT = ["S","s","si","sì","Si","Sì"]
neejaIT = [colN+"N"+colR,colJ+"S"+colR]
neelijstNL = ["N","n","nee","Nee"]
jalijstNL = ["J","j","ja","Ja"]
neejaNL = [colN+"N"+colR,colJ+"J"+colR]
manmpvCJ = ["man mpgv","woman mpv","hufu mpv"]
manmpvEN = ["man mpv","woman mpv"]
manmpvIT = ["man mpv","woman mpv","uomo mpv","donna mpv"]
manmpvNL = ["man mpv","woman mpv","vrouw mpv"]
mpvCJ = "ma hazeʃapaxa\"MPV\"\n"
mpvEN = "Starting playback with mpv\n"
mpvIT = "Avvio della riproduzione con mpv\n"
mpvNL = "Start afspelen met mpv\n"

def setlang(oldlang):
# Informatie over hucoji vind je op www.hucoji.org
# You can find information about hucoji at www.hucoji.org
# Puoi trovare informazioni su hucoji al sito www.hucoji.org
    pickdict = {
            "CJ":"hucoji",
            "EN":"English",
            "IT":"Italiano",
            "NL":"Nederlands"
            }
    picklijst = []
    for l in pickdict:
        picklijst.append(l.lower())
    longlang,templang = cFD([pickdict,0,oldlang,"> ",picklijst+quitlijst])
    newlang = templang.upper()
    if newlang in quitlijst:
        exit()
    with open("adjustables.py","r") as a:
        regels = a.readlines()
    with open("adjustables.py","w") as a:
        for r in regels:
            if r[:4] == "lang":
                r = "lang = \"%s\"\n" % (newlang)
            print(r, end = "", file = a)
    if newlang == "CJ":
        wraptext = "mo hame\"L\" hiʒizi huʃapaxa m haca humeʒi. mo hamela m hacaqe hiküi humeʒi haziʃapaxa:"
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
    elif newlang == "EN":
        wraptext = "You can call up this choice text with \"L\" from the main menu. Do you want to see this language choice again nevertheless the next time you start the program?"
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
    elif newlang == "IT":
        wraptext = "Puoi richiamare questa scelta con \"L\" dal menu principale. Vuoi rivedere questa scelta lo stesso la prossima volta che avvii il programma?"
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
    else:
        wraptext = "Je kunt deze keuze oproepen met \"L\" vanuit het hoofdmenu. Wil je deze taalkeuze toch opnieuw zien als je de volgende keer het programma start?"
        neelijst = neelijstNL
        jalijst = jalijstNL
        neeja = neejaNL
    for w in textwrap.wrap(wraptext,80):
        print(w)
    nj,index = cFNL([neeja,"A",0,0,"> ",jalijst+neelijst+quitlijst])
    if nj in quitlijst:
        exit()
    elif nj in neelijst+jalijst:
        with open("adjustables.py","r") as a:
            regels = a.readlines()
        with open("adjustables.py","w") as a:
            for r in regels:
                if r[:8] == "picklang":
                    if nj in neelijst:
                        r = "picklang = \"N\"\n"
                    else:
                        r = "picklang = \"Y\"\n"
                print(r, end = "", file = a)
    return newlang
if picklang == "Y":
    lang = setlang(lang)

def defgpad():
    if lang == "CJ":
        manmpg123 = manmpg123CJ
        manmpv = manmpvCJ
        man = manmpg123CJ+manmpvCJ
    elif lang == "EN":
        manmpg123 = manmpg123EN
        manmpv = manmpvEN
        man = manmpg123EN+manmpvEN
    elif lang == "IT":
        manmpg123 = manmpg123IT
        manmpv = manmpvIT
        man = manmpg123IT+manmpvIT
    else:
        manmpg123 = manmpg123NL
        manmpv = manmpvNL
        man = manmpg123NL+manmpvNL
    optie,index = cFNL([genrelijstlang,"A",1,1,"> ",helplijst+man+backlijst+quitlijst])
    if optie in quitlijst:
        exit()
    elif optie in backlijst:
        return optie
    elif optie in manmpg123:
        subprocess.run(["man", "mpg123"])
    elif optie in manmpv:
        subprocess.run(["man", "mpv"])
    elif optie in helplijst:
        hellup()
    if optie in genrelijstlang:
        optie = genrelijst[genrelijstlang.index(optie)]
    tracklijst = []
    gpad = os.path.join(pad,optie)
    return gpad

def printtracklijst(tracklijst):
    if lang == "CJ":
        print("ma hupa%swacoxa%spo hozizu %s" % (colT,colR,str(len(tracklijst))))
    elif lang == "EN":
        print("The %strack%s list contains %s %strack%ss" % (colT,colR,str(len(tracklijst)),colT,colR))
    elif lang == "IT":
        print("L’elenco delle %stracce%s contiene %s %sbrani%s" % (colT,colR,str(len(tracklijst)),colT,colR))
    else:
        print("De %strack%slijst bevat %s %strack%ss" % (colT,colR,str(len(tracklijst)),colT,colR))
    if len(tracklijst) > 50:
        print()
        if lang == "CJ":
            wraptext = "mu haca hupawacoxapo hoñepo m hupawacoxapoño hacapulilüi. mo hame\"ENTER\" m hazaca. mo hame\"B\" m hacaliqe hiŋi haza hiseco."
        elif lang == "EN":
            wraptext = "The track list is long and may not fit on your screen. The list is therefore displayed in multiple batches. Use \"Enter\" to display yhe next batch. Use \"B\" to break the display and continue to playback."
        elif lang == "IT":
            wraptext = "L’elenco delle tracce è lungo e potrebbe non entrare sullo schermo. L’elenco viene quindi mostrato in più parti. Usa \"Enter\" per visualizzare la prossima parte. Usa \"B\" per interrompere la visualizzazione e passare alla riproduzione."
        else:
            wraptext = "De tracklijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom in meerdere delen getoond. Gebruik \"Enter\" om het volgende deel te tonen. Gebruik \"B\" om de weergave af te breken en door te gaan naar afspelen."
        print(colT, end = "")
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print(colR)
        lenlijst = len(tracklijst)
        count = 0
        while count < lenlijst:
            track = os.path.basename(tracklijst[count])
            count += 1
            if len(track) > 80-3-maxlen:
                print(("{:%s}" % maxlen).format(count)+" : "+track[:39-maxlen]+"**"+track[len(track)-36:])
            else:
                print(("{:%s}" % maxlen).format(count)+" : "+track)
            if count % 50 == 0:
                go = input()
                if go in quitlijst:
                    exit()
                elif go in backlijst:
                    break
        print()
    else:
        lenlijst = len(tracklijst)
        count = 0
        while count < lenlijst:
            track = os.path.basename(tracklijst[count]) 
            count += 1
            if len(track) > 80-3-maxlen:
                print(("{:%s}" % maxlen).format(count)+" : "+track[:39-maxlen]+"**"+track[len(track)-36:])
            else:
                print(("{:%s}" % maxlen).format(count)+" : "+track)
    print()

def printmappenlijst(mappenlijst):
    if lang == "CJ":
        print("ma hu%swaŋüi%spa hozizu %s" % (colD,colR,str(len(mappenlijst))))
    elif lang == "EN":
        print("The %sfolder%s list contains %s %sfolder%ss" % (colD,colR,str(len(mappenlijst)),colD,colR))
    elif lang == "IT":
        print("L'elenco delle %scartelle%s contiene %s %scartelle%s" % (colD,colR,str(len(mappenlijst)),colD,colR))
    else:
        print("De %smap%spenlijst bevat %s %smap%spen" % (colD,colR,str(len(mappenlijst)),colD,colR))
    if len(mappenlijst) > 50:
        print()
        if lang == "CJ":
            wraptext = "mu haca hupahuwaŋüipa hoñepo m hupahuwaŋüipaño hacapulilüi. mo hame\"ENTER\" m hazaca. mo hame\"B\" m hacaliqe hiŋi haza hiseco."
        elif lang == "EN":
            wraptext = "The folder list is long and may not fit on your screen. The list is therefore displayed in multiple batches. Use \"Enter\" to display the next batch. Use \"B\" to break the display and continue to playback."
        elif lang == "IT":
            wraptext = "L'elenco delle cartelle è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato in più parti. Usa \"Enter\" per visualizzare la prossima parte. Usa \"B\" per interrompere la visualizzazione e passare alla riproduzione."
        else:
            wraptext = "De mappenlijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom in meerdere delen getoond. Gebruik \"Enter\" om het volgende deel te tonen. Gebruik \"B\" om de weergave af te breken en door te gaan naar afspelen."
        print(colD,end="")
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print(colR)
        lenlijst = len(mappenlijst)
        count = 0
        while count < lenlijst:
            mapp = os.path.basename(mappenlijst[count])
            count += 1
            if len(mapp) > 80-3-maxlen:
                print(("{:%s}" % maxlen).format(count)+" : "+mapp[:39-maxlen]+"**"+mapp[len(mapp)-36:])
            else:
                print(("{:%s}" % maxlen).format(count)+" : "+mapp)
            if count % 50 == 0:
                go = input()
                if go in quitlijst:
                    exit()
                elif go in backlijst:
                    break
        print()
    else:
        lenlijst = len(mappenlijst)
        count = 0
        while count < lenlijst:
            mapp = os.path.basename(mappenlijst[count]) 
            count += 1
            if len(mapp) > 80-3-maxlen:
                print(("{:%s}" % maxlen).format(count)+" : "+mapp[:39-maxlen]+"**"+mapp[len(mapp)-36:])
            else:
                print(("{:%s}" % maxlen).format(count)+" : "+mapp)
    print()

def printtracklijstmetsel(tracklijst):
    if lang == "CJ":
        print("ma hupa%swacoxa%spa huzizu %s" % (colT,colR,str(len(tracklijst))))
    elif lang == "EN":
        print("The %strack%s list contains %s %strack%ss" % (colT,colR,str(len(tracklijst)),colT,colR))
    elif lang == "IT":
        print("L’elenco delle %stracce%s contiene %s %sbrani%s" % (colT,colR,str(len(tracklijst),colT,colR)))
    else:
        print("De %strack%slijst bevat %s %strack%ss" % (colT,colR,str(len(tracklijst)),colT,colR))
    tracklijstverkort = []
    if len(tracklijst) > 50:
        print()
        if lang == "CJ":
            wraptext = "mu haca hupawacoxapo hoñepo m hupawacoxapoño hicapulilüi. mo haŋoda hubiŋowacoxapo m haʃa haŋome hiqa."
        elif lang == "EN":
            wraptext = "The track list is long and may not fit on your screen. The list is therefore first displayed in multiple parts so you can see the numbers of the track(s) you want to select. After that, you will have the option to enter your final choice. Remember those numbers."
        elif lang == "IT":
            wraptext = "L'elenco delle tracce è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato inizialmente in più parti in modo che tu possa vedere i numeri delle tracce che desideri selezionare. Successivamente potrai inserire la tua scelta definitiva. Ricorda quei numeri."
        else:
            wraptext = "De tracklijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom eerst in meerdere delen getoond zodat je de nummers van de track(s) die je in je selectie wilt een keer hebt kunnen zien. Daarna krijg je de optie om je definitieve keuze in te geven. Onthoud die nummers."
        print(colT)
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print(colR)
        lenlijst = len(tracklijst)
        count = 0
        while count < lenlijst:
            track = tracklijst[count] 
            count += 1
            if len(track) > 80-3-maxlen:
                print(("{:%s}" % maxlen).format(count)+" : "+track[:39-maxlen]+"**"+track[len(track)-36:])
                tracklijstverkort.append(track[:39-maxlen]+"**"+track[len(track)-36:])
            else:
                print(("{:%s}" % maxlen).format(count)+" : "+track)
                tracklijstverkort.append(track)
            if count % 50 == 0:
                go = input()
                if go in quitlijst:
                    exit()
                elif go in backlijst:
                    break
        print()
        if lang == "CJ":
            wraptext = "hupazu. ma hea hamelo hiqa. ma hea haŋoda hubiŋowacoxapo. ma hea haʃa\"ENTER\"."
        elif lang == "EN":
            wraptext = "The end of the list has been reached and the option to enter your choice will follow. Remember the number(s) of the track(s) you want to select. Now first press \"Enter\""
        elif lang == "IT":
            wraptext = "La fine dell'elenco è stata raggiunta e a seguire ci sarà l'opzione per inserire la tua scelta. Ricorda il/i numero/i della/le traccia/e che desideri selezionare. Ora premi prima \"Invio\""
        else:
            wraptext = "Het einde van de lijst is bereikt en de optie om je keuze in te voeren volgt hierna. Onthoud de/het nummer(s) van de track(s) die je wilt selecteren. Druk nu eerst op \"Enter\""
        print(colT,end="")
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print(colR)
        go = input()
        if go in quitlijst:
            exit()
    else:
        lenlijst = len(tracklijst)
        count = 0
        while count < lenlijst:
            track = tracklijst[count] 
            count += 1
            if len(track) > 80-3-maxlen:
                tracklijstverkort.append(track[:39-maxlen]+"**"+track[len(track)-36:])
            else:
                tracklijstverkort.append(track)
    print()
    return tracklijstverkort

def printmappenlijstmetsel(mappenlijst):
    mappenlijstverkort = []
    if len(mappenlijst) > 50:
        if lang == "CJ":
            print("ma hupa%shuwaŋüi%spa hozizu %s" % (colD,colR,str(len(mappenlijst))))
        elif lang == "EN":
            print("The %sfolder%s list contains %s %sfolder%ss" % (colD,colR,str(len(mappenlijst)),colD,colR))
        elif lang == "IT":
            print("L'elenco delle %scartelle%s contiene %s %scartelle%s" % (colD,colR,str(len(mappenlijst)),colD,colR))
        else:
            print("De %smap%spenlijst bevat %s %smap%spen" % (colD,colR,str(len(mappenlijst)),colD,colR))
        print()
        if lang == "CJ":
            wraptext = "mu haca hupawaŋüipa hoñepo m hupawaŋüipaño hicapulilüi. mo haŋoda hubiŋowaŋüipo m haʃa haŋome hiqa."
        elif lang == "EN":
            wraptext = "The folder list is long and may not fit on your screen. The list is therefore first displayed in multiple parts so you can see the number(s) of the folder(s) you want to select. After that, you will have the option to enter your final choice. Remember those numbers."
        elif lang == "IT":
            wraptext = "L'elenco delle cartelle è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato inizialmente in più parti in modo che tu possa vedere il/i numero/i della/le cartella/e che desideri selezionare. Successivamente potrai inserire la tua scelta definitiva. Ricorda quei numeri."
        else:
            wraptext = "De mappenlijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom eerst in meerdere delen getoond zodat je het/de nummer(s) van de map(pen) die je in je selectie wilt een keer hebt kunnen zien. Daarna krijg je de optie om je definitieve keuze in te geven. Onthoud die nummers."
        print(colD)
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print(colR)
        lenlijst = len(mappenlijst)
        count = 0
        while count < lenlijst:
            mapp = mappenlijst[count] 
            count += 1
            if len(mapp) > 80-3-maxlen:
                print(("{:%s}" % maxlen).format(count)+" : "+mapp[:39-maxlen]+"**"+mapp[len(mapp)-36:])
                mappenlijstverkort.append(mapp[:39-maxlen]+"**"+mapp[len(mapp)-36:])
            else:
                print(("{:%s}" % maxlen).format(count)+" : "+mapp)
                mappenlijstverkort.append(mapp)
            if count % 50 == 0:
                go = input()
                if go in quitlijst:
                    exit()
                elif go in backlijst:
                    break
        print()
        if lang == "CJ":
            wraptext = "hupazu. ma hea hamelo hiqa. ma hea haŋoda hubiŋowaŋüipo. ma hea haʃa\"ENTER\"."
        elif lang == "EN":
            wraptext = "The end of the list has been reached and the option to enter your choice will follow. Remember the number(s) of the folder(s) you want to select. Now first press \"Enter\""
        elif lang == "IT":
            wraptext = "La fine dell'elenco è stata raggiunta e a seguire ci sarà l'opzione per inserire la tua scelta. Ricorda il/i numero/i della/le cartella/e che desideri selezionare. Ora premi prima \"Invio\""
        else:
            wraptext = "Het einde van de lijst is bereikt en de optie om je keuze in te voeren volgt hierna. Onthoud het/de nummer(s) van de map(pen) die je wilt selecteren. Druk nu eerst op \"Enter\""
        print(colD)
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print(colR)
        go = input()
        if go in quitlijst:
            exit()
    else:
        lenlijst = len(mappenlijst)
        count = 0
        while count < lenlijst:
            mapp = mappenlijst[count] 
            count += 1
            if len(mapp) > 80-3-maxlen:
                mappenlijstverkort.append(track[:39-maxlen]+"**"+mapp[len(mapp)-36:])
            else:
                mappenlijstverkort.append(mapp)
    print()
    return mappenlijstverkort

def setvol(oldvol):
    if lang == "CJ":
        setvol = "ma haŋo hucoñazi hame huzi\"0\"zu\"100\" (hiqi %s):\n" % (oldvol)
    elif lang == "EN":
        setvol = "Set the starting volume to a scale of 0 to 100 (now %s):\n" % (oldvol)
    elif lang == "IT":
        setvol = "Imposta il volume di partenza su una scala da 0 a 100 (ora %s):\n" % (oldvol)
    else:
        setvol = "Stel het startvolume in op een schaal van 0 tot 100 (nu %s):\n" % (oldvol)
    loop = True
    while loop == True:
        newvol = input(colV+setvol+colR)
        try:
            if 0 <= int(newvol) <= 100:
                with open("adjustables.py","r") as a:
                    regels = a.readlines()
                with open("adjustables.py","w") as a:
                    for r in regels:
                        if r[:6] == "volume":
                            r = "volume = \"%s\"\n" % (newvol)
                        print(r, end = "", file = a)
                    return newvol
        except:
            if newvol == "":
                return oldvol
            elif newvol in quitlijst:
                exit()
            elif newvol in backlijst:
                return oldvol
            elif newvol.lower() in manmpg123:
                subprocess.run(["man", "mpg123"])
            elif newvol.lower() in manmpv:
                subprocess.run(["man", "mpv"])

def play(tracklijst):
    vol = setvol(volume)
    if lang == "CJ":
        manmpg123 = manmpg123CJ
        manmpv = manmpvCJ
        man = manmpg123CJ+manmpvCJ
        willekeurig = colW+"ma hixüe hamelamli"+colR
        mpg123 = mpg123CJ
        mpv = mpvCJ
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
    elif lang == "EN":
        manmpg123 = manmpg123EN
        manmpv = manmpvEN
        man = manmpg123EN+manmpvEN
        willekeurig = colW+"Random order?"+colR
        mpg123 = mpg123EN
        mpv = mpvEN
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
    elif lang == "IT":
        manmpg123 = manmpg123IT
        manmpv = manmpvIT
        man = manmpg123IT+manmpvIT
        willekeurig = colW+"Ordine casuale?"+colR
        mpg123 = mpg123IT
        mpv = mpvIT
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
    else:
        manmpg123 = manmpg123NL
        manmpv = manmpvNL
        man = manmpg123NL+manmpvNL
        willekeurig = colW+"Willekeurige volgorde?"+colR
        mpg123 = mpg123NL
        mpv = mpvNL
        neelijst = neelijstNL
        jalijst = jalijstNL
        neeja = neejaNL
    if len(tracklijst) == 0:
        return
    random = "--shuffle"
    if len(tracklijst) != 1:
        print(willekeurig)
        ja,index = cFNL([neeja,"A",0,1,"> ",helplijst+man+jalijst+neelijst+backlijst+quitlijst])
        if ja.lower() in quitlijst:
            exit()
        elif ja.lower() in backlijst:
            return
        elif ja.lower() in helplijst:
            hellup()
        elif ja.lower() in manmpg123:
            subprocess.run(["man", "mpg123"])
        elif ja.lower() in manmpv:
            subprocess.run(["man", "mpv"])
        if ja.lower() in neelijst:
            random = ""
    try:
        with open(os.path.join(pad,"tracklijst.m3u"),"w") as tl:
            for tr in tracklijst:
                print(tr, file=tl)
        print(mpv)
        subprocess.run(["mpv", random, "--loop-playlist", "--volume=%s" % (vol), os.path.join(pad,"tracklijst.m3u")])
        os.remove(os.path.join(pad,"tracklijst.m3u"))
    except:
        pass

def hellup():
    if lang == "CJ":
        helpteksten = [
                """hiʒu:                                                                           
"B"          : hazüi                                                            
"H"          : haca huda                                                        
"Q"          : hasüu                                                            
"hufu mpv”   : haca huda huʃapaxa"MPV"                                          
                                                                                
hiʒizi huʃapaxa:                                                                
"L" : hame hucodo                                                               
                                                                                
hiʒiŋüi hupamepa:                                                               
">”          : hase                                                             
"<”          : hasüe                                                            
"*”          : hamepu                                                           
2,5,11,17,23 : hamepo hixi"CSV"                                                 """,
            "ma huʃapaxa\"MUSUITE\" hacosi huwacoxapa hoxa hiŋi hucoxazaʒili. me mo haʃa huwo\"ENTER\" mom haza mem mo haʃa huwo\"B\" mom hazüi mem mo haʃa huwo\"Q\" mom hasüu. mo hiʒizeʃapaxa hameʃa huwo\"L\" m hame humahapa hoxili.",
            "mo huʃapaxa\"MPV\" hoŋüi\"REPO\"poo hili hiŋi hu\"\'chooseFromNumberedList.py\'\" hoŋüi\"\'https://github.com/maestraccio/chooseFromNumberedList\'\" hili m haʃali huʃapaxa\"MUSUITE\". ma haŋüi huwaŋüi hiŋa huwa\"\'musuite.py\'\" hiŋi huwa\"\'adjustables.py\'\".",
            "ma hupawacoxapo haku hoxa hixi:",
            # print as-is [3]
            """\\huwaŋüi_hupawacoxapopo\\hucoxacoxi\\huwaŋüi                  \\huwacoxa           
 {\\   ...   \\huwaŋüiʒi}\\                                                        
                        {   ABC  }\\                                             
                                   {hufu(pa)A - huwacoxapaB}\\                   
                                                             {huwacoxa1.mp3}    
                                                             {huwacoxa2.mp3}    
                                   {huwacoxapaZ - hufu(pa)Q}\\                   
                                                             {huwacoxa3.mp3}    
                                                             {huwacoxa4.mp3}    
                        {   JZZ  }\\                                             
                                   {huwacoxapaD - hufu(pa)C}\\                   
                                                             {huwacoxa5.mp3}    
                                                             {huwacoxa6.mp3}    
                                   {hufu(pa)R - huwacoxapaY}\\                   
                                                             {huwacoxa7.mp3}    
                                                             {huwacoxa8.mp3}    
                        {   POP  }\\                                             
                                   {hufu(pa)E - huwacoxapaF}\\                   
                                                             {huwacoxa11.mp3}   
                                                             {huwacoxa12.mp3}   
                                   {hufu(pa)S - huwacoxapaX}\\                   
                                                             {huwacoxa21.mp3}   
                                                             {huwacoxa22.mp3}   """,
            "ma hiŋüi huwaŋüiʒi hupawacoxapopo hoxa hihucoxacoxi. ma huwaŋüihucoxacoxi huhizizubo hoŋüuñaliŋüuñüali. ma huwacoxapo hiŋüi huwaŋüipo hiŋüi hucoxacoxipo. ma haŋüili huwacoxa me hiŋüi huwaŋüipo hopebe m hiŋüu huwaŋüipo.",
            "mo hupawacoxapa hihea hoxili mom me haxasexi mem haʃali huʃapaxa\"MUSUITE\".",
            "ma hea haŋo huhi hiŋo huwaŋüiʒi hiŋüi huwa\"\'adjustables.py\'\" hixi \"\'pad = \"(huhiʒi)\"\'\". ma huwa\"\'adjustables.py\'\" hiŋüi huwaŋüi hiŋa huwa\"\'musuite.py\'\". mu hiŋüi hu\"OS\"xili huwaŋüahipo hoxili m hea hame\"\\\"m\"/\" hiŋo\"OS\".",
            "ma huhiŋo hucoxacoxi hiŋüi huwa\"\'adjustables.py\'\" haxililüi heaka huhiŋo hucoxacoxi. ma hea haʃaxili haŋo huhipo hiŋüi huwa\"\'adjustables.py\'\". ma hea hamelamli haŋo huhipoxili.",
            "ma hea haŋo huhipo hucoxazaʒili hiŋüi huwa\"\'adjustables.py\'\". ma hamelamli haŋolüi huhi\"ICY\".",
            "ma hea hado mo huwa\"\'adjustables.py\'\"li m huʃapaxa\"MUSUITE\" haʃali. ma headu huwapo hiŋüi huwa\"\'adjustables.py\'\" me haxüidu m haxüili.",
            "ma hea haŋo hume huwopo hiŋüi hu\"KEYBOARD\" me mo hea haʃa humepo\"),],},>\" mom hase mem mo hea haʃa humepo\"(,[,{,<\" mom hasüe. mo haʃewo\"ENTER\" m haŋome. ma haʃali hu\"MOUSE\" hiŋüi huʃapaxa\"MUSUITE\". ma haʃame hupo hiŋüi humepapobüi huŋo\"COMMA\"ŋüamepo hizu haʃa\"ENTER\". mo haʃa huwoŋehucoxacoxi hubüimezibemziba m hapahucoxacoxixipu.",
            "mo haʃa huʃapaxa\"MUSUITE\" m huku huʃapaxa\"MPV\". ma haku huʃapaxa\"MPV\" hoŋo hiʒi. mo haʃawopa\"\'hufu mpv\'\" m haca hudapo huʃapaxa\"MPV\".",
            "ma heepa haka mu heaga m haʃa huʃapaxa\"MUSUITE\"."
            ]
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
        manmpv = manmpvCJ
        man = manmpvCJ
    elif lang == "EN":
        helpteksten = [
        """Everywhere:                                                                     
"B”          : Back                                                             
"H”          : Help                                                             
"Q”          : Quit                                                             
"man mpv”    : or "woman mpv" : mpv manual                                      
                                                                                
In main menu:                                                                   
"L”          : Language selection                                               
                                                                                
In selection lists:                                                             
">”          : Scroll forward                                                   
"<”          : Scroll backward                                                  
"*”          : Select all                                                       
2,5,11,17,23 : CSV-style multiple selections                                    """,
            "With musuite, you can play your organized music collection and saved online streams. Press \"Enter\" to proceed with your choice, \"B\" to interrupt the current function, or \"Q\" to quit. To change the language, you can select \"L\" in the main menu.",
            "musuite uses mpv, available in most repositories, and \"chooseFromNumberedList.py\", which you can download from https://github.com/maestraccio/chooseFromNumberedList. Place it in the same directory as \"musuite.py\" and \"adjustables.py\".",
            "It is important, no, ESSENTIAL, that your organized music collection looks like this:",
            # print as-is [3]
            """\\MAIN_FOLDER\\GENRE\\ALBUM             \\TRACK                                     
{\\ ...\\path}\\                                                                   
             {ABC}\\                                                             
                   {artistA - albumB}\\                                          
                                      {track1.mp3}                              
                                      {track2.mp3}                              
                   {albumZ - artistQ}\\                                          
                                      {track3.mp3}                              
                                      {track4.mp3}                              
             {JZZ}\\                                                             
                   {albumD - artistC}\\                                          
                                      {track5.mp3}                              
                                      {track6.mp3}                              
                   {artistR - albumY}\\                                          
                                      {track7.mp3}                              
                                      {track8.mp3}                              
             {POP}\\                                                             
                   {artistE - albumF}\\                                          
                                      {track11.mp3}                             
                                      {track12.mp3}                             
                   {artistS - albumX}\\                                          
                                      {track21.mp3}                             
                                      {track22.mp3}                             """,
            "In the MAIN_FOLDER, the albums of your artists are sorted by genre. Each genre folder has a name that consists of exactly three letters, no more and no less. Inside the genre folders are the albums, and inside those are the music files. Do not use subfolders, do not place loose music files at another level.",
            "If your music collection is organized differently, adjust it. If you don’t want to, use another program.",
            "In the file \"adjustables.py\" (included and located in the same directory as this program), you specify the exact location of the MAIN_FOLDER after \"pad = \". Use the path formatting as used by your operating system. So, pay attention to whether you should use \"\\\" or \"/\".",
            "In the same file \"adjustables.py\", you can add descriptions to your genre names yourself. There are already examples you can use and/or modify. Genre names that appear in the list but not in your collection do not interfere. You can leave them as they are or remove them, whichever you prefer. After all, it is your collection.",
            "In the same file \"adjustables.py\", create a list of your favorite online streams, with a short description or the ICY-NAME.",
            "You have already understood that the file \"adjustables.py\" is important for the proper functioning of musuite. There are also a few other variables in it that you should better stay away from, or at least handle with great caution.",
            "Type your choice via the keyboard, or use the \"closing brackets\" (\")\", \"]\", \"}\", \">\": to move forward) and the \"opening brackets\" (\"(\", \"[\", \"{\", \"<\": to move backward). Press \"Enter\" to confirm your choice. There is no support for using a mouse or other pointer hardware in musuite. Some choice lists support multiple selections. In that case, enter the choice numbers or exact keys (case-sensitive), separated by commas, consecutively before pressing \"Enter\". For the genre selection, you can also quickly filter by using just the first letter or the first two letters of multiple genres you want to select at once.",
            "For playback, the program calls \"mpv\". Make sure it is installed. For its use, consult the official man pages with the command \"man mpv\" or \"woman mpv\".",
            "Enjoy your listening!"
            ]
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
        manmpv = manmpvEN
        man = manmpvEN
    elif lang == "IT":
        helpteksten = [
            """Ovunque:                                                                        
"B”          : Indietro                                                         
"H”          : Aiuto                                                            
"Q”          : Esci                                                             
"uomo mpv"   : o "donna mpv"    : Manuale mpv                                   
                                                                                
In menu principale:                                                             
"L”          : Selezione lingua                                                 
                                                                                
In liste di selezione:                                                          
">”          : Scorri avanti                                                    
"<”          : Scorri indietro                                                  
"*”          : Seleziona tutto                                                  
2,5,11,17,23 : Selezione multipla in stile CSV                                  """,
            "Con musuite puoi riprodurre la tua collezione musicale organizzata e gli stream online salvati. Premi \"Invio\" per procedere con la tua scelta, \"B\" per interrompere la funzione corrente o \"Q\" per uscire. Per cambiare la lingua, puoi selezionare \"L\" nel menu principale.",
            "musuite utilizza mpg123 e mpv, disponibile nella maggior parte dei repository, e \"chooseFromNumberedList.py\", che puoi scaricare da https://github.com/maestraccio/chooseFromNumberedList. Posizionalo nella stessa cartella di \"musuite.py\" e \"adjustables.py\".",
            "È importante, anzi ESSENZIALE, che la tua collezione musicale organizzata sia strutturata così:",
            # print as-is [3]
            """\\CARTELLA_PRINCIPALE \\GENERE\\ALBUM              \\TRACCIA                        
{\\   ...   \\percorso}\\                                                          
                       {ABC}\\                                                   
                             {artistaA - albumB}\\                               
                                                 {traccia1.mp3}                 
                                                 {traccia2.mp3}                 
                             {albumZ - artistaQ}\\                               
                                                 {traccia3.mp3}                 
                                                 {traccia4.mp3}                 
                       {JZZ}\\                                                   
                             {albumD - artistaC}\\                               
                                                 {traccia5.mp3}                 
                                                 {traccia6.mp3}                 
                             {artistaR - albumY}\\                               
                                                 {traccia7.mp3}                 
                                                 {traccia8.mp3}                 
                       {POP}\\                                                   
                             {artistaE - albumF}\\                               
                                                 {traccia11.mp3}                
                                                 {traccia12.mp3}                
                             {artistaS - albumX}\\                               
                                                 {traccia21.mp3}                
                                                 {traccia22.mp3}                """,
            "Nella CARTELLA_PRINCIPALE ci sono gli album dei tuoi artisti, organizzati per genere. Ogni cartella di genere ha un nome composto da esattamente tre lettere, non una di più e non una di meno. All'interno delle cartelle di genere ci sono gli album, e al loro interno i file musicali. Non usare sottocartelle, non mettere file musicali sciolti a un altro livello.",
            "Se la struttura della tua collezione musicale è diversa, modificala. Se non vuoi farlo, usa un altro programma.",
            "Nel file \"adjustables.py\" (fornito e situato nella stessa cartella di questo programma), specifichi tu stesso la posizione esatta della CARTELLA PRINCIPALE dopo \"pad = \". Utilizza la formattazione del percorso come viene utilizzata dal tuo sistema operativo. Fai quindi attenzione a utilizzare \"\\\" o \"/\" a seconda dei casi.",
            "Nello stesso file \"adjustables.py\", puoi aggiungere tu stesso descrizioni ai nomi dei tuoi generi. Ci sono già degli esempi che puoi utilizzare e/o modificare. I nomi dei generi che compaiono nella lista ma non nella tua raccolta non creano problemi. Puoi lasciarli così come sono o rimuoverli, come preferisci. Dopotutto, si tratta della tua raccolta.",
            "Sempre nel file \"adjustables.py\", crea anche una lista dei tuoi stream online preferiti, con una breve descrizione o il nome ICY-NAME.",
            "Hai già capito che il file \"adjustables.py\" è importante per il corretto funzionamento di musuite. All'interno ci sono anche alcune altre variabili con cui è meglio non avere a che fare, o almeno con cui bisogna maneggiare con grande cautela.",
            "Digita la tua scelta tramite la tastiera, oppure utilizza le parentesi chiuse (\")\", \"]\", \"}\", \">\": per andare avanti) e le parentesi aperte (\"(\", \"[\", \"{\", \"<\": per andare indietro). Premi \"Enter\" per confermare la tua scelta. Non è supportato l'uso di un mouse o di altre periferiche di puntamento in musuite. Alcune liste di scelta supportano più scelte. In tal caso, inserisci i numeri delle scelte o le chiavi esatte (sensibili alle maiuscole), separate da virgole, consecutivamente prima di premere \"Enter\". Per la selezione dei generi, puoi anche filtrare rapidamente utilizzando solo la prima lettera o le prime due lettere di più generi che vuoi selezionare contemporaneamente.",
            "Per la riproduzione, il programma richiama \"mpv\". Assicurati che sia installato. Per il suo utilizzo, consulta le pagine man ufficiali con il comando \"man mpv\" o \"donna mpv\".",
            "Buon ascolto!"
            ]
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
        manmpv = manmpvIT
        man = manmpvIT
    else:
        helpteksten = [
            """Overal:                                                                         
"B"          : Terug                                                            
"H"          : Help                                                             
"Q"          : Afsluiten                                                        
"man mpv"    : of "vrouw mpv"    : Handleiding mpv                              
                                                                                
In hoofdmenu:                                                                   
"L"          : Taalkeuze                                                        
                                                                                
In keuzelijsten:                                                                
">"          : Vooruit bladeren                                                 
"<"          : Achteruit bladeren                                               
"*"          : Alles selecteren                                                 
2,5,11,17,23 : Meerdere selecties in CSV-stijl                                  """,
            "Met musuite kun je je georganiseerde muziekverzameling en verzamelde online streams afspelen. Druk op \"Enter\" om na je keuze door te gaan, \"B\" om de huidige functie te onderbreken of \"Q\" om te stoppen. Om de taal te wijzigen kun je in het hoofdmenu \"L\" kiezen.",
            "musuite maakt gebruik van mpv, beschikbaar in de meeste repo's, en van \"chooseFromNumberedList.py\", dat je kunt downloaden van https://github.com/maestraccio/chooseFromNumberedList. Plaats het in dezelfde map als \"musuite.py\" en \"adjustables.py\".",
            "Het is belangrijk, nee ESSENTIEEL dat je georganiseerde muziekverzameling er zo uitziet:",
            # print as-is [3]
            """\\ HOOFDMAP\\GENRE\\ALBUM              \\TRACK                                      
{\\...\\pad}\\                                                                     
           {ABC}\\                                                               
                 {artiestA - albumB}\\                                           
                                     {track1.mp3}                               
                                     {track2.mp3}                               
                 {albumZ - artiestQ}\\                                           
                                     {track3.mp3}                               
                                     {track4.mp3}                               
           {JZZ}\\                                                               
                 {albumD - artiestC}\\                                           
                                     {track5.mp3}                               
                                     {track6.mp3}                               
                 {artiestR - albumY}\\                                           
                                     {track7.mp3}                               
                                     {track8.mp3}                               
           {POP}\\                                                               
                 {artiestE - albumF}\\                                           
                                     {track11.mp3}                              
                                     {track12.mp3}                              
                 {artiestS - albumX}\\                                           
                                     {track21.mp3}                              
                                     {track22.mp3}                              """,
            "In de HOOFDMAP staan de albums van je artiesten per genre gesorteerd. Iedere genre-map heeft een naam die uit precies drie letters bestaat, niet meer en niet minder. In de genre-mappen staan de albums en daarin staan de muziekbestanden. Gebruik geen submappen, plaats geen losse muziekbestanden op een ander niveau.",
            "Ziet de organisatie van jouw muziekcollectie er anders uit, pas die dan aan. Wil je dat niet, gebruik dan een ander programma.",
            "In het bestand \"adjustables.py\" (meegeleverd en staat in dezelfde map als dit programma) geef je zelf de exacte locatie op van de HOOFDMAP, achter \"pad = \". Gebruik de padnaamopmaak zoals die op jouw besturingssysteem wordt gebruikt. Let dus op of je \"\\\" of \"/\" moet gebruiken.",
            "In hetzelfde bestand \"adjustables.py\" kun je zelf beschrijvingen aan je genrenamen toevoegen. Er staan al voorbeelden in die je kunt gebruiken en/of aanpassen. Genrenamen die in de lijst staan maar niet in jouw verzameling voorkomen, staan je niet in de weg. Je kunt ze laten staan of verwijderen, wat jij wilt. Het is jouw verzameling.",
            "In dezelfde file \"adjustables.py\" maak je ook een lijst aan van je favoriete online streams, met een korte beschrijving of de ICY-NAME.",
            "Je hebt al begrepen dat het bestand \"adjustables.py\" belangrijk is voor de juiste werking van musuite. Er staan nog enkele andere variabelen in waar je beter vanaf kunt blijven, of tenminste met grote voorzichtigheid mee moet omgaan.",
            "Typ de optie van je keuze in via je toetsenbord, of gebruik de \"haakjes sluiten\" (\")\", \"]\", \"}\", \">\": vooruit) en de \"haakjes openen\" (\"(\", \"[\", \"{\", \"<\": achteruit) om er naartoe te bladeren. Druk op \"Enter\" om je keuze te bevestigen. Er is geen ondersteuning voor het gebruik van een muis of andere aanwijzerhardware in musuite. Sommige keuzelijsten ondersteunen meerdere keuzes. Voer in dat geval de keuzenummers of exacte keys (hoofdlettergevoelig) kommagescheiden achter elkaar in, voordat je op \"Enter\" drukt. Bij de genrekeuze kun je ook snel filteren op alleen de eerste letter of de eerste twee letters van meerdere genres die je tegelijk wilt selecteren.",
            "Voor het afspelen wordt het programma \"mpv\" aangeroepen. Zorg ervoor dat dat geïnstalleerd is. Voor het gebruik ervan kun je de officiele manpages raadplegen met de opdracht \"man mpv\" of \"vrouw mpv\".",
            "Veel luisterplezier!"
            ]
        neelijst = neelijstNL
        jalijst = jalijstNL
        neeja = neejaNL
        manmpv = manmpvNL
        man = manmpvNL
    for i in helpteksten:
        if (i == helpteksten[0]) or (i == helpteksten[4]):
            print(colH,end="")
            print(i)
            print(colR,end="")
        else:
            print(colH,end="")
            for w in textwrap.wrap(i,80):
                print(w)
            print(colR,end="")
        stop = input()
        if stop in backlijst:
            break
        elif stop in quitlijst:
            exit()
        elif stop.lower() in manmpv:
            subprocess.run(["man", "mpv"])
    if lang == "CJ":
        wraptext = "mo hame\"H\" hiru m hacadapaʒi. mo hamelaqi m haca hudaʒi haziʃapaxa:"
    elif lang == "EN":
        wraptext = "You can always call up this help text with \"H\". Do you want to see this help text again the next time you start the program?"
    elif lang == "IT":
        wraptext = "Puoi richiamare questa guida in qualsiasi momento con \"H\". Vuoi rivedere questa guida la prossima volta che avvii il programma?"
    else:
        wraptext = "Je kunt deze helptekst altijd oproepen met \"H\". Wil je deze helptekst opnieuw zien als je de volgende keer het programma start?"
    for w in textwrap.wrap(wraptext,80):
        print(w)
    nj,index = cFNL([neeja,"A",0,0,"> ",jalijst+neelijst+man+backlijst+quitlijst])
    if nj in quitlijst:
        exit()
    elif nj in backlijst:
        return
    elif nj.lower() in manmpv:
        subprocess.run(["man", "mpv"])
    elif nj in neelijst+jalijst:
        with open("adjustables.py","r") as a:
            regels = a.readlines()
        with open("adjustables.py","w") as a:
            for r in regels:
                if r[:8] == "showhelp":
                    if nj in neelijst:
                        r = "showhelp = \"N\"\n"
                    else:
                        r = "showhelp = \"Y\"\n"
                print(r, end = "", file = a)
if showhelp == "Y":
    hellup()

############################################

if lang == "CJ":
    padtekst = "ma huwaŋüiʒi hiŋüi huwa\"\'adjustables.py\'\":"
    gener = "mu hea haʃiqeñe m huwacoxapu haŋasepa hige..."
    klaar = "... hozu"
elif lang == "EN":
    padtekst = "The path used as the MAIN_FOLDER for your music collection, as specified in \'adjustables.py\', is:"
    gener = "Your music collection is being gathered, this may take a moment..."
    klaar = "... Done"
elif lang == "IT":
    padtekst = "Il percorso utilizzato come CARTELLA_PRINCIPALE della tua raccolta musicale, come specificato in \'adjustables.py\', è:"
    gener = "Sto raccogliendo la tua collezione musicale, potrebbe richiedere un momento..."
    klaar = "... Fatto"
else:
    padtekst = "Het pad dat nu gebruikt wordt als HOOFDMAP van je muziekcollectie, zoals vastgelegd in \'adjustables.py\', is:"
    gener = "Je muziekcollectie wordt verzameld, dit kan even duren..."
    klaar = "... Klaar"
for w in textwrap.wrap(padtekst,80):
    print(w)
print(pad)
print()
try:
    for w in textwrap.wrap(gener,80):
        print(w)
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
    allemappenlijst = []
    for g in genrelijst:
        for dirpath, dirnames, filenames in os.walk(os.path.join(pad,g)):
            for mapp in dirnames:
                allemappenlijst.append(mapp)
    extensielijst = [
        # Algemene audioformaten
        ".mp3",    # MPEG-1 Audio Layer III
        ".wav",    # Waveform Audio File Format
        ".aac",    # Advanced Audio Codec
        ".m4a",    # MPEG-4 Audio (AAC in MP4-container)
        ".mp4",    # MPEG-4 (kan AAC, ALAC, MP3 bevatten)
        ".flac",   # Free Lossless Audio Codec
        ".aiff",   # Audio Interchange File Format
        ".aif",    # Audio Interchange File Format (alternatieve extensie)
        ".alac",   # Apple Lossless Audio Codec (in .m4a of .caf)
        ".ogg",    # Ogg Vorbis
        ".oga",    # Ogg Audio (alternatief voor .ogg)
        ".opus",   # Open, royalty-free codec
        ".wma",    # Windows Media Audio
        ".ac3",    # Audio Codec 3 (Dolby Digital)
        ".dts",    # Digital Theater Systems
        ".ape",    # Monkey's Audio (lossless)
        ".wv",     # WavPack (lossless/lossy)

        # Minder courante formaten
        ".amr",    # Adaptive Multi-Rate
        ".au",     # Sun/NeXT audio format
        ".caf",    # Core Audio Format
        ".iff",    # Interchange File Format (Amiga)
        ".mid",    # MIDI (Musical Instrument Digital Interface)
        ".midi",   # MIDI (alternatieve extensie)
        ".mod",    # Module (tracker music)
        ".xm",     # Extended Module (tracker music)
        ".s3m",    # ScreamTracker 3 Module (tracker music)
        ".it",     # Impulse Tracker (tracker music)
        ".ra",     # RealAudio
        ".ram",    # RealAudio Metadata (vaak gekoppeld aan .ra)
        ".voc",    # Creative Voice File
        ".8svx",   # Amiga 8-bit sampled voice

        # Containerformaten met audio (extensies van de container, niet het audioformaat zelf)
        ".mkv",    # Matroska (kan meerdere audioformaten bevatten)
        ".avi",    # Audio Video Interleave (kan MP3, AC3, WMA, etc. bevatten)
        ".mov",    # QuickTime (kan AAC, ALAC, MP3 bevatten)
        ".webm",   # WebM (kan Vorbis, Opus bevatten)
        ".3gp",    # 3GPP (kan AAC, AMR bevatten)
        ".caf",    # Core Audio Format (kan AAC, ALAC bevatten)
    ]
    alletrackslijst = []
    for g in genrelijst:
        for m in allemappenlijst:
            for dirpath, dirnames, filenames in os.walk(os.path.join(pad,g,m)):
                for track in filenames:
                    for e in extensielijst:
                        if track.endswith(e):
                            alletrackslijst.append(track)
    maxlen = len(str(len(alletrackslijst)))
    streamslijst = []
    for i in streamsdict:
        streamslijst.append(i)
    optieslijst = ["*"]
    for i in genrelijst:
        if i[:1] not in optieslijst:
            optieslijst.append(i[:1].lower())
            optieslijst.append(i[:2].lower())
            optieslijst.append(i.lower())
            optieslijst.append(i[:1].upper())
            optieslijst.append(i[:2].upper())
    print(klaar)
    padwaar = True
except:
    if lang == "CJ":
        print("%sma hiʒi huwa\"MP3\"li.%s ma haco hame hucoxaza hoʒili hixüili" % (colN,colR))
    elif lang == "EN":
        print("%sNo MP3 files found.%s You can only choose to listen from your online streams" % (colN,colR))
    elif lang == "CJ":
        print("%sNessun file MP3 trovato.%s Puoi solo sceglere di ascolare dagli streaming online" % (colN,colR))
    else:
        print("%sGeen MP3-bestanden gevonden.%s Je kunt alleen luisteren naar je keuze uit online streams" % (colN,colR))
    streamslijst = []
    for i in streamsdict:
        streamslijst.append(i)
    padwaar = False

############################################

loop = True
while loop == True:
    if lang == "CJ":
        hoofdmenu = " - - huʒize - -"
        mpv = mpvCJ
        mosdict = {
                "m":colT+"hu\"MP3\"ʒipo"+colR,
                "z":colS+"hucoxazaʒili"+colR
                }
        zosdict = {
                "x":colD+"hawaʒixiʒa"+colR,
                "z":colD+"hazaca"+colR
                }
        gmtdict = {
                "x":colG+"hupacoxacoxi"+colR,
                "w":colD+"huwaŋüi"+colR,
                "c":colT+"huwacoxa"+colR
                }
        manmpv = manmpvCJ
        man = manmpvCJ
    elif lang == "EN":
        hoofdmenu = " - - MAIN MENU - -"
        mpv = mpvEN
        mosdict = {
                "M":colT+"MP3 file(s) from own collection"+colR,
                "S":colS+"online Stream"+colR
                }
        zosdict = {
                "F":colD+"Find by search term"+colR,
                "S":colD+"Scroll"+colR
                }
        gmtdict = {
                "G":colG+"Genre, Style, Category"+colR,
                "F":colD+"Folder, Album, Collection"+colR,
                "T":colT+"Track, Song, Opus"+colR
                }
        manmpv = manmpvEN
        man = manmpvEN
    elif lang == "IT":
        hoofdmenu = " - - MENU PRINCIPALE - -"
        mpv = mpvIT
        mosdict = {
                "M":colT+"File MP3 dalla collezione personale"+colR,
                "S":colS+"Streaming online"+colR
                }
        zosdict = {
                "C":colD+"Cercare per termine di ricerca"+colR,
                "S":colD+"Sfoglia"+colR
                }
        gmtdict = {
                "G":colG+"Genere, Stile, Categoria"+colR,
                "C":colD+"Cartella, Album, Collezione"+colR,
                "T":colT+"Traccia, Canzone, Numero"+colR
                }
        manmpv = manmpvIT
        man = manmpvIT
    else:
        hoofdmenu = " - - HOOFDMENU - -"
        mpv = mpvNL
        mosdict = {
                "M":colT+"MP3-bestand(en) uit eigen collectie"+colR,
                "S":colS+"online Stream"+colR
                }
        zosdict = {
                "Z":colD+"Zoeken op zoekterm"+colR,
                "S":colD+"Scrollen"+colR
                }
        gmtdict = {
                "G":colG+"Genre, Stijl, Categorie"+colR,
                "M":colD+"Map, Album, Verzameling"+colR,
                "T":colT+"Track, Lied, Opus"+colR
                }
        manmpv = manmpvNL
        man = manmpvNL
    moslijst = []
    for i in mosdict:
        moslijst.append(i.lower())
    zoslijst = []
    for i in zosdict:
        zoslijst.append(i.lower())
    gmtlijst = []
    for i in gmtdict:
        gmtlijst.append(i.lower())
    loop = True
    while loop == True:
        if padwaar == True:
            print()
            print(hoofdmenu)
            v,k = cFD([mosdict,0,"M","> ",langlijst+helplijst+man+moslijst+backlijst+quitlijst])
            if k.upper() in quitlijst:
                exit()
            elif k.upper() in backlijst:
                pass
            elif k.lower() in manmpv:
                subprocess.run(["man", "mpv"])
            elif k in helplijst:
                hellup()
            elif k in langlijst:
                lang = setlang(lang)
            else:
                break
        else:
            k = moslijst[1]
            break
    if k.upper() == moslijst[1].upper():
        loopS = True
        while loopS == True:
            s,index = cFNL([streamslijst,"A",1,1,"> ",helplijst+man+backlijst+quitlijst])
            if s in quitlijst:
                exit()
            elif s in backlijst:
                break
            elif s.lower() in manmpv:
                subprocess.run(["man", "mpv"])
            elif s in helplijst:
                hellup()
            else:
                su = streamsdict[s]
                print(mpv)
                volume = setvol(volume)
                subprocess.run(["mpv", "--volume=%s" % volume, su])
    else:
        loopM = True
        while loopM == True:
            v,k = cFD([gmtdict,0,"G","> ",helplijst+man+gmtlijst+backlijst+quitlijst])
            if k.upper() in quitlijst:
                exit()
            elif k.upper() in backlijst:
                break
            elif k.lower() in manmpv:
                subprocess.run(["man", "mpv"])
            elif k in helplijst:
                hellup()
            elif k.upper() == gmtlijst[2].upper():
                loopMT = True
                while loopMT == True:
                    tracklijstkort = []
                    tracklijst = []
                    if lang == "CJ":
                        zoekterm = input("ma hizi haŋowaŋekaca hizu haʃa\"ENTER\". ma hameli huwoŋoʃazu holüi\"Q\":\n")
                    elif lang == "EN":
                        zoekterm = input("Enter a search term (no exit command like \"Q\") and press \"Enter\":\n")
                    elif lang == "IT":
                        zoekterm = input("Inserisci un termine di ricerca (nessun comando di uscita come \"Q\") e premi \"Invio\":\n")
                    else:
                        zoekterm = input("Voer een zoekterm in (geen afsluitopdracht zoals \"Q\") en druk op \"Enter\":\n")
                    if zoekterm in quitlijst:
                        exit()
                    elif zoekterm in backlijst:
                        break
                    elif zoekterm.lower() in manmpv:
                        subprocess.run(["man", "mpv"])
                    else:
                        for dirpath, dirnames, filenames in os.walk(pad):
                            for track in filenames:
                                if zoekterm in track:
                                    for e in extensielijst:
                                        if track.endswith(e):
                                            tracklijst.append(track)
                                            tracklijstkort.append(track)
                        tracklijstkort = sorted(tracklijstkort)
                        if len(tracklijstkort) < 1:
                            print()
                            if lang == "CJ":
                                wraptext = "ma hupasüi hoñüi. ma hade huwañexiwañoli."
                            elif lang == "EN":
                                wraptext = "Your search did not return any results. Remember that the search is case-sensitive."
                            elif lang == "IT":
                                wraptext = "La tua ricerca non ha restituito risultati. Ricorda che la ricerca distingue tra maiuscole e minuscole."
                            else:
                                wraptext = "Je zoekopdracht leverde geen resultaten op. Denk eraan dat de zoekopdracht hoofdlettergevoelig is."
                            print(colN,end="")
                            for i in textwrap.wrap(wraptext,80):
                                print(i)
                            print(colR)
                        else:
                            tracklijstverkort = printtracklijstmetsel(tracklijstkort)
                            lentl = len(str(len(tracklijstverkort)))
                            tracklijstnogkorter = []
                            for track in tracklijstverkort:
                                if len(track) > 80-3-maxlen-lentl:
                                    tracklijstnogkorter.append(track[:40-maxlen-lentl]+"**"+track[len(track)-36:])
                                else:
                                    tracklijstnogkorter.append(track)
                            tracksel,index = cFNL([tracklijstnogkorter,"A",1,1,"> ",True,helplijst+man+backlijst+quitlijst])
                            if tracksel in quitlijst:
                                exit()
                            elif tracksel in backlijst:
                                break
                            elif tracksel in manmpv:
                                subprocess.run(["man", "mpv"])
                            elif tracksel in helplijst:
                                hellup()
                            else:
                                tracklijstdef = []
                                for i in tracksel:
                                    for dirpath, dirnames, filenames in os.walk(pad):
                                        for track in filenames:
                                            if tracklijstkort[tracklijstnogkorter.index(i)] in track:
                                                tracklijstdef.append(os.path.join(dirpath, track))
                                tracklijst = sorted(tracklijstdef)
                                printtracklijst(tracklijst)
                                play(tracklijst)
            elif k.upper() == gmtlijst[1].upper():
                loopMM = True
                while loopMM == True:
                    if lang == "CJ":
                        wraptext = "me hawaʒaxiʒi m hazaxaca."
                    elif lang == "EN":
                        wraptext = "Do you want to search using a search term or browse through the collection?"
                    elif lang == "IT":
                        wraptext = "Vuoi effettuare una ricerca con un termine specifico o scorrere la collezione?"
                    else:
                        wraptext = "Wil je zoeken met een zoekopdracht of scrollen door de verzameling?"
                    v,k = cFD([zosdict,0,"S","> ",helplijst+man+zoslijst+backlijst+quitlijst])
                    print(k)
                    if k in quitlijst:
                        exit()
                    elif k in backlijst:
                        break
                    elif k.lower() in manmpv:
                        subprocess.run(["man", "mpv"])
                    elif k in helplijst:
                        hellup()
                    else:
                        if k.upper() == zoslijst[0].upper():
                            loopMMZ = True
                            while loopMMZ == True:
                                mappenlijstkort = []
                                mappenlijst = []
                                tracklijstkort = []
                                tracklijstverkort = []
                                if lang == "CJ":
                                    zoekterm = input("ma hizi haŋowaŋekaca hizu haʃa\"ENTER\". ma hameli huwoŋoʃazu holüi\"Q\":\n")
                                elif lang == "EN":
                                    zoekterm = input("Enter a search term (no exit command like \"Q\") and press \"Enter\":\n")
                                elif lang == "IT":
                                    zoekterm = input("Inserisci un termine di ricerca (nessun comando di uscita come \"Q\") e premi \"Invio\":\n")
                                else:
                                    zoekterm = input("Voer een zoekterm in (geen afsluitopdracht zoals \"Q\") en druk op \"Enter\":\n")
                                if zoekterm in quitlijst:
                                    exit()
                                elif zoekterm in backlijst:
                                    break
                                elif zoekterm.lower() in manmpv:
                                    subprocess.run(["man", "mpv"])
                                else:
                                    for dirpath, dirnames, filenames in os.walk(pad):
                                        for mapp in dirnames:
                                            if zoekterm in mapp:
                                                mappenlijst.append(mapp)
                                                mappenlijstkort.append(mapp)
                                    mappenlijstkort = sorted(mappenlijstkort)
                                    if len(mappenlijstkort) < 1:
                                        print()
                                        if lang == "CJ":
                                            wraptext = "ma hupasüi hoñüi. ma hade huwañexiwañoli."
                                        elif lang == "EN":
                                            wraptext = "Your search did not return any results. Remember that the search is case-sensitive."
                                        elif lang == "IT":
                                            wraptext = "La tua ricerca non ha prodotto risultati. Ricorda che la ricerca distingue tra maiuscole e minuscole."
                                        else:
                                            wraptext = "Je zoekopdracht leverde geen resultaten op. Denk eraan dat de zoekopdracht hoofdlettergevoelig is."
                                        print(colN,end="")
                                        for i in textwrap.wrap(wraptext,80):
                                            print(i)
                                        print(colR)
                                    else:
                                        mappenlijstverkort = printmappenlijstmetsel(mappenlijstkort)
                                        lenml = len(str(len(mappenlijstverkort)))
                                        mappenlijstnogkorter = []
                                        try:
                                            for mapp in mappenlijstverkort:
                                                if len(mapp) > 80-3-maxlen-lenml:
                                                    mappenlijstnogkorter.append(mapp[:40-maxlen-lenml]+"**"+mapp[len(mapp)-36:])
                                                else:
                                                    mappenlijstnogkorter.append(mapp)
                                        except:
                                            pass
                                        mappsel,index = cFNL([mappenlijstnogkorter,"A",1,1,"> ",True,optieslijst+helplijst+man+backlijst+quitlijst])
                                        if mappsel in quitlijst:
                                            exit()
                                        elif mappsel in backlijst:
                                            break
                                        elif mappsel in manmpv:
                                            subprocess.run(["man", "mpv"])
                                        elif mappsel in helplijst:
                                            hellup()
                                        else:
                                            if mappsel == "*":
                                                mappsel = []
                                                for m in mappenlijstnogkorter:
                                                    mappsel.append(m)
                                            tracklijstdef = []
                                            for m in mappsel:
                                                m = mappenlijstkort[mappenlijstnogkorter.index(m)]
                                                for g in genrelijst:
                                                    for dirpath, dirnames, filenames in os.walk(os.path.join(pad,g,m)):
                                                        for track in filenames:
                                                            for e in extensielijst:
                                                                if track.endswith(e):
                                                                    tracklijstdef.append(os.path.join(pad,g,m,track))
                                            tracklijst = sorted(tracklijstdef)
                                            printtracklijst(tracklijst)
                                            play(tracklijst)
                        else:
                            loopMMS = True
                            while loopMMS == True:
                                gpad = defgpad()
                                if gpad in backlijst:
                                    break
                                mappenlijst = []
                                try:
                                    for m in os.listdir(gpad):
                                        if os.path.isdir(os.path.join(gpad,m)):
                                            mpad = os.path.join(gpad,m)
                                            mappenlijst.append(mpad)
                                except:
                                    pass
                                mappenlijst = sorted(mappenlijst)
                                mappenlijstkort = []
                                optielijst = []
                                for i in mappenlijst:
                                    mappenlijstkort.append(i[len(gpad)+1:])
                                mappenlijstverkort = printmappenlijstmetsel(mappenlijstkort)
                                lenml = len(str(len(mappenlijstverkort)))
                                mappenlijstnogkorter = []
                                for mapp in mappenlijstverkort:
                                    if len(mapp) > 80-3-maxlen-lenml:
                                        mappenlijstnogkorter.append(mapp[:40-maxlen-lenml]+"**"+mapp[len(mapp)-36:])
                                    else:
                                        mappenlijstnogkorter.append(mapp)
                                mappsel,index = cFNL([mappenlijstnogkorter,"A",1,1,"> ",True,optieslijst+helplijst+man+backlijst+quitlijst])
                                if mappsel in quitlijst:
                                    exit()
                                elif mappsel in backlijst:
                                    break
                                elif mappsel in manmpv:
                                    subprocess.run(["man", "mpv"])
                                elif mappsel in helplijst:
                                    hellup()
                                else:
                                    if mappsel == "*":
                                        mappsel = []
                                        for m in mappenlijstnogkorter:
                                            mappsel.append(m)
                                    tracklijstdef = []
                                    for m in mappsel:
                                        m = mappenlijstkort[mappenlijstnogkorter.index(m)]
                                        for g in genrelijst:
                                            for dirpath, dirnames, filenames in os.walk(os.path.join(pad,g,m)):
                                                for track in filenames:
                                                    for e in extensielijst:
                                                        if track.endswith(e):
                                                            tracklijstdef.append(os.path.join(pad,g,m,track))
                                    tracklijst = sorted(tracklijstdef)
                                    printtracklijst(tracklijst)
                                    play(tracklijst)
            else:
                loopMG = True
                while loopMG == True:
                    optie,index = cFNL([genrelijstlang,"A",1,1,"> ",True,helplijst+man+optieslijst+backlijst+quitlijst])
                    if optie in quitlijst:
                        exit()
                    elif optie in backlijst:
                        break
                    elif optie in manmpv:
                        subprocess.run(["man", "mpv"])
                    elif optie in helplijst:
                        hellup()
                    elif type(optie) == str:
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
                                        for e in extensielijst:
                                            if track.endswith(e):
                                                tpad = os.path.join(mpad,track)
                                                tracklijst.append(tpad)
                        else:
                            tracklijst = []
                            keuzelijst = []
                            optie = optie.upper()
                            for i in genrelijst:
                                if optie in [i[:1],i[:2],i]:
                                    if i not in optieslijst:
                                        keuzelijst.append(i)
                            print(keuzelijst)
                            optie = keuzelijst
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
                                        for e in extensielijst:
                                            if track.endswith(e):
                                                tpad = os.path.join(mpad,track)
                                                tracklijst.append(tpad)
                        tracklijst = sorted(tracklijst)
                        printtracklijst(tracklijst)
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
                            printtracklijst(tracklijst)
                            play(tracklijst)
