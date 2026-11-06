#!/usr/bin/env python3
import subprocess, os, sys, random, textwrap
from time import sleep
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromDictionary as cFD
from adjustables import lang,picklang,showhelp,pad,genredict,streamsdict,volume
Versie = "1.21"
Date = "2026-11-05"
hier = os.path.dirname(os.path.realpath(__file__))
os.chdir(hier)
colD = "\033[94m"
colG = "\033[93m"
colH = "\033[7m"
colJ = "\033[92m"
colN = "\033[91m"
colR = "\033[0m"
colS = "\033[95m"
colT = "\033[96m"
colW = "\033[33m"
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
manmpg123CJ = ["man mpg123","woman mpg123","hufu mpg123"]
manmpg123EN = ["man mpg123","woman mpg123"]
manmpg123IT = ["man mpg123","woman mpg123","uomo mpg123","donna mpg123"]
manmpg123NL = ["man mpg123","woman mpg123","vrouw mpg123"]
manmpvCJ = ["man mpgv","woman mpv","hufu mpv"]
manmpvEN = ["man mpv","woman mpv"]
manmpvIT = ["man mpv","woman mpv","uomo mpv","donna mpv"]
manmpvNL = ["man mpv","woman mpv","vrouw mpv"]
#ZTI:ZIN(                                                        ma
#    WTI:WW(                                                     ha
#        Progressie:Start(                                       ze
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "MPG123"(                               "MPG123"
#    )   )   )   )   )   )
#)
#ma hazeʃapaxa"mpg123"
mpg123CJ = "ma hazeʃapaxa\"MPG123\"\n"
mpg123EN = "Starting playback with mpg123\n"
mpg123IT = "Avvio della riproduzione con mpg123\n"
mpg123NL = "Start afspelen met mpg123\n"
mpvCJ = "ma hazeʃapaxa\"MPV\"\n"
mpvEN = "Starting playback with mpv\n"
mpvIT = "Avvio della riproduzione con mpv\n"
mpvNL = "Start afspelen met mpv\n"

def setvol(oldvol):
    if lang == "CJ":
        setvol = "ma haŋo hucoña hame huzi\"0\"zu\"100\" (hiqi %s):\n" % (oldvol)
    elif lang == "EN":
        setvol = "Set the volume to a scale of 0 to 100 (now %s):\n" % (oldvol)
    elif lang == "IT":
        setvol = "Imposta il volume su una scala da 0 a 100 (ora %s):\n" % (oldvol)
    else:
        setvol = "Stel het volume in op een schaal van 0 tot 100 (nu %s):\n" % (oldvol)
    loop = True
    while loop == True:
        newvol = input(setvol)
        try:
            if 0 <= int(newvol) <= 100:
                with open("adjustables.py","r") as a:
                    regels = a.readlines()
                with open("adjustables.py","w") as a:
                    for r in regels:
                        if r[:6] == "volume":
                            r = "volume = \"%s\"\n" % (newvol)
                        print(r, end = "", file = a)
                    return int(newvol)
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
#ZTI:Voorwaardelijk(                                             mo
#    WTI:WW(                                                     ha
#        zti:Keuze(                                              me
#            Waarheid:Waar(                                      la
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            Registratie:Zien(                                   ca
#        )   )
#        WTI:ZNW(                                                hu
#            zti:Keuze(                                          me
#                Afstand:Hier(                                   ʒi
#        )   )   )
#        WTI:WW(                                                 ha
#            Progressie:Start(                                   zi
#                Activiteit:Actief(                              ʃa
#                    Schaling:Groep(                             pa
#                        Status:Geordend(                        xa
#        )   )   )   )   )
#    )
#)
#mo hamela m haca humeʒi haziʃapaxa
#ZTI:Voorwaardelijk(                                             mo
#    WTI:WW(                                                     ha
#        zti:Keuze(                                              me
#            "L"(                                                "L"
#    )   )   )
#    WTI:BW(                                                     hi
#        Afstand:Hier(                                           ʒi
#            Progressie:Start(                                   zi
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#    )   )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            Registratie:Zien(                                   ca
#        )   )
#        WTI:ZNW(                                                hu
#            zti:Keuze(                                          me
#                 Afstand:Hier(                                  ʒi
#        )   )   )
#    )
#)
#mo hame"L" hiʒizi huʃapaxa m haca humeʒi
        wraptext = "mo hamela m haca humeʒi haziʃapaxa. mo hame\"L\" hiʒizi huʃapaxa m haca humeʒi:"
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
    elif newlang == "EN":
        wraptext = "Do you want to see this language choice again the next time you start the program? You can call up this choice text with \"L\" from the main menu:"
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
    elif newlang == "IT":
        wraptext = "Vuoi rivedere questa scelta la prossima volta che avvii il programma? Puoi richiamare questa scelta con \"L\" dal menu principale:"
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
    else:
        wraptext = "Wil je deze taalkeuze opnieuw zien als je de volgende keer het programma start? Je kunt deze keuze oproepen met \"L\" vanuit het hoofdmenu:"
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
#ZTI:Zin(                                                        ma
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Geluid(                             co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#    )   )   )   )   )  )
#    WTI:BNW(                                                    ho
#        Progressie:Start(                                       zi
#            Progressie:Eind(                                    zu
#    )   )   )
#)
#ma hupawacoxapa hozizu %s
        print("ma hupa%swacoxa%spa hozizu %s" % (colT,colR,str(len(tracklijst))))
    elif lang == "EN":
        print("The %strack%s list contains %s %strack%ss" % (colT,colR,str(len(tracklijst)),colT,colR))
    elif lang == "IT":
        print("L’elenco delle %stracce%s contiene %s %sbrani%s" % (colT,colR,str(len(tracklijst)),colT,colR))
    else:
        print("De %strack%slijst bevat %s %strack%ss" % (colT,colR,str(len(tracklijst)),colT,colR))
    if len(tracklijst) > 50:
        print()
        if lang == "CJ":
#ZTI:Oorzaak(                                                    mu
#    WTI:WW(                                                     ha
#        Registratie:Zien(                                       ca
#    )   )
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Geluid(                             co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#    )   )   )   )   )   )
#    WTI:BNW(                                                    ho      
#            Grootte:Klein(                                      ñe
#                Schaling:Meervoud(                              po
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:ZNW(                                                hu
#            Schaling:Groep(                                     pa
#                Materie:Iets(                                   wa
#                    Registratie:Geluid(                         co
#                        Status:Geordend(                        xa
#                            Schaling:Groep(                     pa
#                                Grootte:Groot(                  ño
#        )   )   )   )   )   )   )
#        WTI:WW(                                                 ha
#            Registratie:Zien(                                   ca
#                Schaling:Alles(                                 pu
#                    Waarheid:Niet(                              li
#                        Waarheid:Misschien(                     lüi
#        )   )   )   )   )
#    )
#)
#mu haca hupawacoxapa hoñepo m hupawacoxapaño hacapulilüi
#ZTI:Voorwaarde(                                                 mo
#    WTI:WW(                                                     ha
#        ZTI:Keuze(                                              me
#            "B"(                                                "B"
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            Registratie:Zien(                                   ca
#                Waarheid:Onwaar(                                li
#                    Tijd:Vanaf nu(                              qe
#        )   )   )   )
#    )
#)
#mo hame"B" m hacaliqe
            wraptext = "mu haca hupawacoxapa hoñepo m hupawacoxapaño hacapulilüi. mo hame\"B\" m hacaliqe."
        elif lang == "EN":
            wraptext = "The track list is long and may not fit on your screen. The list is therefore displayed in multiple parts. Use \"B\" to break the display and continue to playback."
        elif lang == "IT":
            wraptext = "L’elenco delle tracce è lungo e potrebbe non entrare sullo schermo. L’elenco viene quindi mostrato in più parti. Usa \"B\" per interrompere la visualizzazione e passare alla riproduzione."
        else:
            wraptext = "De tracklijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom in meerdere delen getoond. Gebruik \"B\" om de weergave af te breken en door te gaan naar afspelen."
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
#ZTI:Zin(                                                        ma
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Connectie:Binnen(                               ŋüi
#                    Schaling:Groep(                             pa
#    )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Progressie:Start(                                       zi
#            Progressie:Eind(                                    zu
#    )   )   )
#)
#ma huwaŋüipa hozizu %s
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
#ZTI:Oorzaak(                                                    mu
#    WTI:WW(                                                     ha
#        Registratie:Zien(                                       ca
#    )       )
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Connectie:Binnen(                               ŋüi
#                    Schaling:Groep(                             pa
#    )   )   )   )  )
#    WTI:BNW(                                                    ho      
#        Grootte:Klein(                                          ñe
#            Schaling:Meervoud(                                  po
#    )   )  )
#    ZTI:Scheiding(                                              m
#        WTI:ZNW(                                                hu
#            Schaling:Groep(                                     pa
#                wti:ZNW(                                        hu
#                    Materie:Iets(                               wa
#                        Connectie:Binnen(                       ŋüi
#                            Schaling:Groep(                     pa
#                                Grootte:Groot(                  ño
#        )   )   )   )   )   )  )
#        WTI:WW(                                                 ha
#            Registratie:Zien(                                   ca
#                Schaling:Alles(                                 pu
#                    Waarheid:Niet(                              li
#                        Waarheid:Misschien(                     lüi
#        )   )   )   )   )
#    )
#)
#mu haca hupawacoxapa hoñepo m hupawacoxapaño hacapulilüi
#ZTI:Voorwaarde(                                                 mo
#    WTI:WW(                                                     ha
#        ZTI:Keuze(                                              me
#            "B"(                                                "B"
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            Registratie:Zien(                                   ca
#                Waarheid:Onwaar(                                li
#                    Tijd:Vanaf nu(                              qe
#        )   )   )   )
#    )
#)
#mo hame"B" m hacaliqe
            wraptext = "mu haca hupahuwaŋüipa hoñepo m hupahuwaŋüipaño hacapulilüi. mo hame\"B\" m hacaliqe."
        elif lang == "EN":
            wraptext = "The folder list is long and may not fit on your screen. The list is therefore displayed in multiple parts. Use \"B\" to break the display and continue to playback."
        elif lang == "IT":
            wraptext = "L'elenco delle cartelle è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato in più parti. Usa \"B\" per interrompere la visualizzazione e passare alla riproduzione."
        else:
            wraptext = "De mappenlijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom in meerdere delen getoond. Gebruik \"B\" of \"U\" om de weergave af te breken en door te gaan naar afspelen."
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
#ZTI:Zin(                                                        ma
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Geluid(                             co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#    )   )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Progressie:Start(                                       zi
#            Progressie:Eind(                                    zu
#    )   )   )
#)
#ma hupawacoxapa huzizu %s
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
#ZTI:Oorzaak(                                                    mu
#    WTI:WW(                                                     ha
#        Registratie:Zien(                                       ca
#    )   )
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Geluid(                             co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#    )   )   )   )   )   )
#    WTI:BNW(                                                    ho      
#        Grootte:Klein(                                          ñe
#            Schaling:Meervoud(                                  po
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:ZNW(                                                hu
#            Schaling:Groep(                                     pa
#                Materie:Iets(                                   wa
#                    Registratie:Geluid(                         co
#                        Status:Geordend(                        xa
#                            Schaling:Groep(                     pa
#                                Grootte:Groot(                  ño
#        )   )   )   )   )   )   )
#        WTI:BW(                                                 hi
#            Registratie:Zien(                                   ca
#                Schaling:Alles(                                 pu
#                    Waarheid:Niet(                              li
#                        Waarheid:Misschien(                     lüi
#        )   )   )   )   )
#    )
#)
#mu haca hupawacoxapa hoñepo m hupawacoxapaño hicapulilüi
#ZTI:Zin(                                                        ma
#    WTI:WW(                                                     ha
#        Connectie:Koppel(                                       ŋo
#            Kennis:Weten(                                       da
#                zti:Keuze(                                      me
#    )   )   )   )
#)
#ZTI:Zin(                                                        ma
#    WTI:WW(                                                     ha
#        Activiteit:Bewging(                                     ʃa
#            zti:Keuze(                                          me
#    )   )   )
#    WTI:BW(                                                     hi
#        Tijd:Binnenkort(                                        qa
#    )   )
#)
#ma haŋodame. ma haʃame hiqa.
            wraptext = "mu haca hupawacoxapa hoñepo m hupawacoxapaño hicapulilüi. ma haŋodame. ma haʃame hiqa."
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
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Progressie:Eind(                                        zu
#)   )   )
#hupazu.
#ZTI:Zin(                                                        ma
#    WTI:Pers.vnw:2(                                             hea
#    )
#    WTI:WW(                                                     ha
#        Waarheid:Concreet(                                      lo      
#            ZTI:Keuze(                                          me
#    )   )   )
#    WTI:Bijwoord(                                               hi
#        Tijd:Binnenkort(                                        qa
#    )   )
#)
#ma hea halome hiqa.
#WTI:Zin(                                                        ma
#    WTI:Pers.vnw:2(                                             hea
#    )
#    WTI:WW(                                                     ha
#        Connectie:Gekoppeld(                                    ŋo
#            Kennis:Weten(                                       da
#                Schaling:Groep(                                 pa
#                    Verlangen:Willen(                           ke
#                        Registratie:Horen(                      co
#    )   )   )   )   )   )
#)
#ma hea haŋodapakeco.
#ZTI:Zin(                                                        ma
#    WTI:Pers.vnw:2(                                             hea
#    )
#    WTI:WW(                                                     ha
#        Activiteit:Beweging(                                    ʃe
#            Materie:Ding(                                       wo
#                "ENTER"(                                        "ENTER"
#    )   )   )   )
#)
#ma hea haʃewo"ENTER".
            wraptext = "hupazu. ma hea halome hiqa. ma hea haŋodapakeco. ma hea haʃewo\"ENTER\"."
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
                #print(("{:%s}" % maxlen).format(count)+" : "+track[:39-maxlen]+"**"+track[len(track)-36:])
                tracklijstverkort.append(track[:39-maxlen]+"**"+track[len(track)-36:])
            else:
                #print(("{:%s}" % maxlen).format(count)+" : "+track)
                tracklijstverkort.append(track)
    print()
    return tracklijstverkort

def printmappenlijstmetsel(mappenlijst):
    mappenlijstverkort = []
    if len(mappenlijst) > 50:
        if lang == "CJ":
#ZTI:Zin(                                                        ma
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            WTI:ZNW(                                            hu
#                Materie:Iets(                                   wa
#                    Connectie:Binnen(                           ŋüi
#                        Schaling:Groep(                         pa
#    )   )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Progressie:Start(                                       zi
#            Progressie:Eind(                                    zu
#    )   )   )
#)
#ma hupahuwaŋüipa hozizu %s
            print("ma hupa%shuwaŋüi%spa hozizu %s" % (colD,colR,str(len(mappenlijst))))
        elif lang == "EN":
            print("The %sfolder%s list contains %s %sfolder%ss" % (colD,colR,str(len(mappenlijst)),colD,colR))
        elif lang == "IT":
            print("L'elenco delle %scartelle%s contiene %s %scartelle%s" % (colD,colR,str(len(mappenlijst)),colD,colR))
        else:
            print("De %smap%spenlijst bevat %s %smap%spen" % (colD,colR,str(len(mappenlijst)),colD,colR))
        print()
        if lang == "CJ":
#ZTI:Oorzaak(                                                    mu
#    WTI:WW(                                                     ha
#        Registratie:Zien(                                       ca
#    )       )
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            WTI:ZNW(                                            hu
#                Materie:Iets(                                   wa
#                    Connectie:Binnen(                           ŋüi
#                        Schaling:Groep(                         pa
#    )   )   )   )   )    )
#    WTI:BNW(                                                    ho      
#        Grootte:Klein(                                          ñe
#            Schaling:Meervoud(                                  po
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:ZNW(                                                hu
#            Schaling:Groep(                                     pa
#                wti:ZNW(                                        hu
#                    Materie:Iets(                               wa
#                        Connectie:Binnen(                       ŋüi
#                            Schaling:Groep(                     pa
#                                Grootte:Groot(                  ño
#        )   )   )   )   )   )   )
#        WTI:BW(                                                 hi
#            Registratie:Zien(                                   ca
#                Schaling:Alles(                                 pu
#                    Waarheid:Niet(                              li
#                        Waarheid:Misschien(                     lüi
#        )   )   )   )   )
#    )
#)
#mu haca hupawacoxapa hoñepo m hupawacoxapaño hicapulilüi
#ZTI:Zin(                                                        ma
#    WTI:WW(                                                     ha
#        Connectie:Koppel(                                       ŋo
#            Kennis:Weten(                                       da
#                zti:Keuze(                                      me
#    )   )   )   )
#)
#ZTI:Zin(                                                        ma
#    WTI:WW(                                                     ha
#        Activiteit:Bewging(                                     ʃa
#            zti:Keuze(                                          me
#    )   )   )
#    WTI:BW(                                                     hi
#        Tijd:Binnenkort(                                        qa
#    )   )
#)
#ma haŋodame. ma haʃame hiqa.
            wraptext = "mu haca hupawacoxa hopañepo m hupawacoxaño hicapulilüi. ma haŋodame. ma haʃame hiqa."
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
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Progressie:Eind(                                        zu
#)   )   )
#hupazu.
#ZTI:Zin(                                                        ma
#    WTI:Pers.vnw:2(                                             hea
#    )
#    WTI:WW(                                                     ha
#        Waarheid:Concreet(                                      lo      
#            ZTI:Keuze(                                          me
#    )   )   )
#    WTI:Bijwoord(                                               hi
#        Tijd:Binnenkort(                                        qa
#    )   )
#)
#ma hea halome hiqa.
#WTI:Zin(                                                        ma
#    WTI:Pers.vnw:2(                                             hea
#    )
#    WTI:WW(                                                     ha
#        Connectie:Gekoppeld(                                    ŋo
#           Kennis:Weten(                                        da
#                Schaling:Groep(                                 pa
#                    Verlangen:Willen(                           ke
#                        Registratie:Horen(                      co
#    )   )   )   )   )   )
#)
#ma hea hadeŋopakeco.
#
#WTI:Zin(                                                        ma
#    WTI:Pers.vnw:2(                                             hea
#    )
#    WTI:WW(                                                     ha
#        Activiteit:Beweging(                                    ʃe
#            Materie:Ding(                                       wo
#                "ENTER"(                                        "ENTER"
#    )   )   )   )
#)
#ma hea haʃewo"ENTER".
#hupazu. ma hea hamelo hiqa. ma hea haŋodapakeco. ma hea haʃewo"ENTER"
            wraptext = "hupazu. ma hea hamelo hiqa. ma hea haŋodapakeco. ma hea haʃewo\"ENTER\""
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
                #print(("{:%s}" % maxlen).format(count)+" : "+mapp[:39-maxlen]+"**"+mapp[len(mapp)-36:])
                mappenlijstverkort.append(track[:39-maxlen]+"**"+mapp[len(mapp)-36:])
            else:
                #print(("{:%s}" % maxlen).format(count)+" : "+mapp)
                mappenlijstverkort.append(mapp)
    print()
    return mappenlijstverkort

def play(tracklijst):
    if lang == "CJ":
        manmpg123 = manmpg123CJ
        manmpv = manmpvCJ
        man = manmpg123CJ+manmpvCJ
#ZTI:Zin(                                                        ma
#    WTI:BW(                                                     hi
#        Status:Rommelig(                                        xüe
#    )   )
#    WTI:WW(                                                     ha
#        ZTI:keuze(                                              me
#            Waarheid:Waar(                                      la
#                ZTI:scheiding(                                  m
#                    Waarheid:Onwaar(                            li
#    )   )   )   )   )
#)
#ma hixüe hamelamli
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
    random = "Z"
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
                #print(colT+tr+colR, file=tl)
                print(tr, file=tl)
        print(mpg123)
        vol = setvol(volume)
        factor = int(vol/100*32768)
        subprocess.run(["mpg123", "-f %s" % (factor), "-vm%s" % (random), "-@", os.path.join(pad,"tracklijst.m3u")])
        os.remove(os.path.join(pad,"tracklijst.m3u"))
    except:
        pass

def hellup():
    if lang == "CJ":
        helpteksten = [
                """hiʒu:                                                                           
"B"           : hazüi                                                           
"H"           : haca huda                                                       
"Q"           : hasüu                                                           
"hufu mpg123” : haca huda huʃapaxa"MPG123"                                      
"hufu mpv”    : haca huda huʃapaxa"MPV"                                         
                                                                                
hiʒizi huʃapaxa:                                                                
"L" : hame hucodo                                                               
                                                                                
hiʒiŋüi hupamepa:                                                               
">”           : hase                                                            
"<”           : hasüe                                                           
"*”           : hamepu                                                          
2,5,11,17,23  : hamepo hixi"CSV"                                                """,
#ZTI:Zin(                                                        ma
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#                    "MUSUITE"(                                  "MUSUITE"
#    )   )   )   )   )
#    WTI:WW(                                                     ha
#        Registratie:Horen(                                      co
#            Richting:0(                                         si
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Horen(                              co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#    )   )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Status:Geordend(                                        xa
#    )   )
#    WTI:BW(                                                     hi
#        Connectie:Los(                                          ŋi
#    )   )
#    WTI:ZNW(                                                    hu
#        Registratie:Horen(                                      co
#            Status:Geordend(                                    xa
#                Progressie:Vooruitgang(                         za
#                    Frequentie:Altijd(                          ru 
#                        Afstand:Hier(                           ʒi
#                            Waarheid:Onwaar(                    li
#    )   )   )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Schaling:Meervoud(                                      po
#    )   )
#)
#ma huʃapaxa"MUSUITE" hacosi hupawacoxapa hoxa hiŋi hucoxazaruʒili hopo.
#ZTI:Keuze(                                                      me
#    ZTI:Voorwaarde(                                             mo
#        WTI:WW(                                                 ha
#            Activiteit:Beweging(                                ʃe
#                Materie:Ding(                                   wo
#                    "ENTER"(                                    "ENTER"
#        )   )   )   )
#        WTI:Voorwaarde:Scheiding(                               mom
#            WTI:WW(                                             ha
#                Progressie:Vooruitgang(                         za
#            )   )
#        )
#    )
#    WTI:Keuze:Scheiding(                                        mem
#    )
#    ZTI:Voorwaarde(                                             mo
#        WTI:WW(                                                 ha
#            Activiteit:Beweging(                                ʃe
#                Materie:Ding(                                   wo
#                    "B"(                                        "B"
#        )   )   )   )
#        WTI:Voorwaarde:Scheiding(                               mom
#            WTI:WW(                                             ha
#                Progressie:Omkeer(                              züi
#            )   )
#        )
#    )
#    WTI:Keuze:Scheiding(                                        mem
#    )
#    ZTI:Voorwaarde(                                             mo
#        WTI:WW(                                                 ha
#            Activiteit:Beweging(                                ʃe
#                Materie:Ding(                                   wo
#                    "Q"(                                        "Q"
#        )   )   )   )
#        WTI:Voorwaarde:Scheiding(                               mom
#            WTI:WW(                                             ha
#                Richting:Weg(                                   süu
#            )   )
#        )
#    )
#)
#me mo haʃewo"ENTER" mom haza mem mo haʃewo"B" mom hazüi mem mo haʃewo"Q" mom hasüu.
#ZTI:Voorwaarde(                                                 mo
#    WTI:BW(                                                     hi
#        Afstand:Hier(                                           ʒi
#            Progressie:Beginfase(                               ze
#                Activiteit:Actief(                              ʃa
#                    Schaling:Groep(                             pa
#                        Status:Geordend(                        xa
#    )   )   )   )   )   )
#    WTI:WW(                                                     ha
#        ZTI:keuze(                                              me
#            Activiteit:Beweging(                                ʃe
#                Materie:Ding(                                   wo
#                    "L"(                                        "L"
#    )   )   )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            ZTI:keuze(                                          me
#        )   )
#        WTI:ZNW(                                                hu
#            ZTI:zin(                                            ma
#                WTI:ww(                                         ha
#                    Schaling:Groep(                             pa
#        )   )   )   )
#        WTI:BNW(                                                ho
#            Status:Gelijk(                                      xi
#                Waarheid:Onwaar(                                li
#        )   )   )
#    )
#)
#mo hiʒizeʃapaxa hameʃewo"L" m hame humahapa hoxili
            "ma huʃapaxa\"MUSUITE\" hacosi hupawacoxapa hoxa hiŋi hucoxazaruʒili hopo. me mo haʃewo\"ENTER\" mom haza mem mo haʃewo\"B\" mom hazüi mem mo haʃewo\"Q\" mom hasüu. mo hiʒizeʃapaxa hameʃewo\"L\" m hame humahapa hoxili.",
#ZTI:Voorwaardelijk(                                             mo
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#                    "mpg123"(                                   "mpg123"
#    )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Connectie:Binnen(                                       ŋüi
#            "repo"(                                             "repo"
#                Schaling:Meervoud:3(                            poo
#    )   )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Los(                                          ŋi
#    )   )
#    WTI:ZNW(                                                    hu
#        "chooseFromNumberedList.py"(                            "chooseFromNumberedList.py"
#    )   )
#    WTI:BNW(                                                    ho
#        Connectie:Binnen(                                       ŋüi
#            "https://github.com/maestraccio/chooseFromNumberedList"("https://github.com/maestraccio/chooseFromNumberedList"
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            Activiteit:Actief(                                  ʃa
#        )   )
#        WTI:ZNW(                                                hu
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "MUSUITE"(                              "MUSUITE"
#        )   )   )   )   )
#    )
#)
#mo huʃapaxa"mpg123" hoŋüi"repo"poo hiŋi hu"chooseFromNumberedList.py" hoŋüi"https://github.com/maestraccio/chooseFromNumberedList" m haʃa huʃapaxa"MUSUITE"
#ZTI:ZIN(                                                        ma
#    WTI:WW(                                                     ha
#        Afstand:Hier(                                           ʒi
#            Connectie:Samen(                                    ŋa
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Materie:Ding(                                           wa
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "MUSUITE"(                              "MUSUITE"
#    )   )   )   )   )   )
#)
#ma haʒiŋa huwaʃapaxa"musuite"
            "mo huʃapaxa\"MPG123\" hiŋi huʃapaxa\"MPV\" hoŋüi\"REPO\"poo hiŋi hu\"\'chooseFromNumberedList.py\'\" hoŋüi\"\'https://github.com/maestraccio/chooseFromNumberedList\'\" m haʃa huʃapaxa\"MUSUITE\". ma haʒiŋa huwaʃapaxa\"MUSUITE\".",
#ZTI:ZIN(                                                        ma
#    WTI:WW(                                                     ha
#        Verlangen:Eisen(                                        ku
#    )   )
#    WTI:ZNW(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Horen(                              co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#    )   )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Status:Geordend(                                        xa
#    )   )
#    WTI:BW(                                                     hi
#        Status:Gelijk(                                          xi
#    )   )
#)
#ma haku hupawacoxapa hoxa hixi:
            "ma haku hupawacoxapa hoxa hixi:",
            # print as-is [3]
#            """\\MAIN_FOLDER\\GENRE\\ALBUM             \\TRACK
# {\\    ...\\path}\\
#                 {ABC}\\
#                       {artistA - albumB}\\
#                                          {track1.mp3}
#                                          {track2.mp3}
#                       {albumZ - artistQ}\\
#                                          {track3.mp3}
#                                          {track4.mp3}
#                 {JZZ}\\
#                       {albumD - artistC}\\
#                                          {track5.mp3}
#                                          {track6.mp3}
#                       {artistR - albumY}\\
#                                          {track7.mp3}
#                                          {track8.mp3}
#                 {POP}\\
#                       {artistE - albumF}\\
#                                          {track11.mp3}
#                                          {track12.mp3}
#                       {artistS - albumX}\\
#                                          {track21.mp3}
#                                          {track22.mp3}""",
####################################################################################################
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#        Connecte:Binnen(                                        ŋüi
#)   )   )
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#        Registratie:Horen(                                      co
#            Status:Geordend(                                    xa
#                Schaling:Groep(                                 pa
#                    Schaling:Meervoud(                          po
#)   )   )   )   )   )
#huwaŋüi huwacoxapapo
#WTI:ZNW(                                                        hu
#    Registratie:Horen(                                          co
#        Status:Geordend(                                        xa
#            Registratie:Horen(                                  co
#                Status:Gelijk(                                  xi
#)   )   )   )
#hucoxacoxi
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#        Connecte:Binnen(                                        ŋüi
#)   )   )
#huwaŋüi
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#         Registratie:Horen(                                     co
#             Status:Geordend(                                   xa
#)   )   )   )
#huwacoxa
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#        Connecte:Binnen(                                        ŋüi
#            Afstand:HIer(                                       ʒi
#)   )   )    )
#huwaŋüiʒi
#WTI:ZNW(                                                        hu
#    Natuur:Persoon(                                             fu
#        Schaling:Groep(                                         pa
#)   )   )
#hufu(pa)
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#        Registratie:Horen(                                      co
#            Status:Geordend(                                    xa
#                Schaling:Groep(                                 pa
#)   )   )   )   )
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#         Registratie:Horen(                                     co
#             Status:Geordend(                                   xa
#)   )   )   )
#huwacoxa

            """\\huwaŋüi_huwacoxapapo\\hucoxacoxi\\huwaŋüi                  \\huwacoxa             
 {\\    ...\\huwaŋüiʒi}\\                                                          
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
                                                           {huwacoxa22.mp3}     """,
#ZTI:ZIN(                                                        ma
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Connectie:Binnen(                                   ŋüi
#                Afstand:HIer(                                   ʒi
#    )   )   )    )
#    WTI:WTI(                                                    hu
#        Schaling:Groep(                                         pa
#            Materie:Iets(                                       wa
#                Registratie:Horen(                              co
#                    Status:Geordend(                            xa
#                        Schaling:Groep(                         pa
#                            Schaling:Meervoud(                  po
#    )   )   )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Status:Geordend(                                        xa
#    )   )
#    WTI:BW(                                                     hi
#        WTI:znw(                                                hu
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#                    Registratie:Horen(                          co
#                        Status:Gelijk(                          xi
#    )   )   )   )   )   )
#)
#ma hiŋüi huwaŋüiʒi hupawacoxapapo hoxa hihucoxacoxi
#ZTI:ZIN(                                                        ma
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Connectie:Binnen(                                   ŋüi
#                WTI:znw(                                        hu
#                    Registratie:Horen(                          co
#                        Status:Geordend(                        xa
#                            Registratie:Horen(                  co
#                                Status:Gelijk(                  xi
#    )   )   )   )   )   )   )   )
#    WTI:BW(                                                     hi
#        Progressie:Start(                                       zi
#            Progressie:Eind(                                    zu
#                Tellen:3(                                       bo
#    )   )   )   )
#    WTI:BNW(                                                    ho
#        Connectie:Buiten(                                       ŋüu
#            Grootte:Negatief(                                   ñüa
#                Waarheid:Onwaar(                                li
#                    Connectie:Buiten(                           ŋüu
#                        Grootte:Positief(                       ña
#                            Waarheid:Onwaar(                    li
#    )   )   )   )   )   )   )
#)
#ma huwaŋüihucoxacoxi hizizubo hoŋüuñüaliŋüuñali
#ZTI:ZIN(                                                        ma
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Connectie:Binnen(                                   ŋüi
#    )   )   )
#    WTI:BW(                                                     hi
#        WTI:znw(                                                hu
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#                    Registratie:Horen(                          co
#                        Status:Gelijk(                          xi
#                            Schaling:Meervoud(                  po
#    )   )   )   )   )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Schaling:Meervoud(                                      po
#            Connectie:Samen(                                    ŋa
#    )   )   )
#    WTI:BW(                                                     hi
#        WTI:znw(                                                hu
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#                    Schaling:Meervoud(                          po
#    )   )   )   )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#                    Schaling:Meervoud(                          po
#    )   )   )   )   )
#)
#ma hiŋüi huwaŋüi hihucoxacoxipo hiŋüi hupoŋa hihucoxapo huwacoxapo
#ZTI:ZIN(                                                        ma
#    WTI:WW(                                                     ha
#        Richting:Richting(                                      si
#            Waarheid:Onwaar(                                    li
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#    )   )   )   )
#)
#ZTI:Keuze(                                                      me
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#            Schaling:Meervoud(                                  po
#                Connectie:Samen(                                ŋa
#                    Connectie:Binnen(                           ŋüi
#                        Schaling:Meervoud(                      po
#                            Connectie:Samen(                    ŋa
#    )   )   )   )   )   )   )
#    ZTI:Scheiding(                                              m
#    )
#    WTI:BW(                                                     hi
#        Connectie:Buiten(                                       ŋüu
#            Schaling:Meervoud(                                  po
#                Connectie:Samen(                                ŋa
#    )   )   )   )
#)
#ma hasili huwacoxa me hiŋüipoŋaŋüipoŋa m hiŋüupoŋa
            "ma hiŋüi huwaŋüiʒi hupawacoxapapo hoxa hihucoxacoxi. ma huwaŋüihucoxacoxi hizizubo hoŋüuñüaliŋüuñali. ma hiŋüi hupoŋa hihucoxacoxipo hiŋüi hupoŋa hihucoxapo huwacoxapo. ma hasili huwacoxa me hiŋüipoŋaŋüipoŋa m hiŋüupoŋa.",
#ZTI:VOORWAARDELIJK(                                             mo
#   WTI:ZNW(                                                     hu
#       Materie:Iets(                                            wa
#           Registratie:Horen(                                   co
#               Status:Geordend(                                 xa
#                   Schaling:Groep(                              pa
#                       Connectie:Samen(                         ŋa
#   )   )   )   )   )   )
#   WTI:BNW(                                                     ho
#       Afstand:Hier(                                            ʒi
#           Richting:Opwaarts(                                   so
#               Status:Gelijk(                                   xi
#                   Waarheid:Onwaar(                             li
#   )   )   )   )   )
#   ZTI:Scheiding(                                               m
#       ZTI:KEUZE(                                               me
#           WTI:WW(                                              ha
#               Status:Geordend(                                 xa
#                   Richting:Vooruit(                            se
#                       Status:Gelijk(                           xi
#           )   )   )
#           ZTI:Keuze:Scheiding(                                 mem
#           )
#           WTI:WW(                                              ha
#               Activiteit:Actief(                               ʃa
#                   "musuite"(                                   "musuite"
#                       Waarheid:Onwaar(                         li
#           )   )   )   )
#       )
#   )
#)
#mo huwacoxapaŋa hoʒisoxili m me haxasexi mem haʃa"musuite"li
            "mo huwacoxapaŋa hoʒisoxili m me haxasexi mem haʃa\"MUSUITE\"li.",
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:2(                                                 hea
#    )
#    WTI:WW(                                                     ha
#        Connectie:Gekoppeld(                                    ŋo
#    )   )
#    WTI:ZNW(                                                    hu
#        WTI:BW(                                                 hi
#            Schaling:Meervoud(                                  po
#                Connectie:Samen(                                ŋa
#                    Progressie:Start(                           zi
#    )   )   )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            "'adjustables.py'"(                                 "'adjustables.py'"
#    )   )   )
#    WTI:BW(                                                     hi
#        Richting:NaarRechts(                                    sa
#            "'pad = '"(                                         "'pad = '"
#    )   )   )
#)
#ma hea haŋo huhipoŋazi hiŋüi huwa"'adjustables.py'" hisa"'pad = '"
#ZTI:ZIN(                                                        ma
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            "'adjustables.py'"(                                 "'adjustables.py'"
#    )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Schaling:Meervoud(                                      po
#            Connectie:Samen(                                    ŋa
#                Status:Gelijk(                                  xi
#    )   )   )  )
#    WTI:BW(                                                     hi
#        Connectie:Samen(                                        ŋa
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "'musuite.py'"(                         "musuite.py"
#    )   )   )   )   )   )
#)
#ma huwa"'adjustables.py'" hiŋüi hupoŋaxi hiŋa huwaʃapaxa"musuite.py"
#ZTI:OORZAAK(                                                    mu
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        "OS"(                                                   "OS"
#            Status:Gelijk(                                      xi
#                Waarheid:Onwaar(                                li
#    )   )   )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            Connectie:Tussen(                                   ŋüa
#                WTI:bw(                                         hi
#                    Schaling:Meervoud(                          po
#    )   )   )   )   )
#    WTI:BNW(                                                    ho
#        Status:Gelijk(                                          xi
#            Waarheid:Onwaar(                                    li
#    )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:PVNW:2(                                             hea
#        )
#        WTI:WW(                                                 ha
#            ZTI:keuze(                                          me
#                "\"(                                            "\"
#                    ZTI:Scheiding(                              m
#                        "/"(                                    "/"
#        )   )   )   )   )
#        WTI:BW(                                                 hi
#            Kennis:Begrip(                                      do
#        )   )
#    )
#)
#mu hiŋüi hu"OS"xili huwaŋüahipo hoxili m hea hame"\"m"/" hido
            "ma hea haŋo huhipoŋazi hiŋüi huwa\"\'adjustables.py\'\" hisa\"\'pad = \'\". ma huwa\"\'adjustables.py\'\" hiŋüi hupoŋaxi hiŋa huwaʃapaxa\"\'musuite.py\'\". mu hiŋüi hu\"OS\"xili huwaŋüahipo hoxili m hea hame\"\\\"m\"/\" hido.",
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:2(                                                 hea
#    )
#    WTI:WW(                                                     ha
#        Status:Ongelijk(                                        xüi
#            ZTI:keuze(                                          me
#                Waarheid:Waar(                                  la
#                    ZTI:scheiding(                              m
#                        Waarheid:Onwaar(                        li
#    )   )   )   )   )   )
#    WTI:ZNW(                                                    hu
#        WTI:BW(                                                 hi
#    )   )
#    WTI:BW(                                                     hi
#        Connectie:Samen(                                        ŋa
#    )   )
#    WTI:ZNW(                                                    hu
#        Registratie:Horen(                                      co
#            Status:Geordend(                                    xa
#                Registratie:Horen(                              co
#                    Status:Gelijk(                              xi
#    )   )   )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            "'adjustables.py'"(                                 "'adjustables.py'"
#    )   )   )
#)
#ma hea haxüimelamli huhi hiŋa hucoxacoxi hiŋüi huwa"'adjustables.py'"
#ZTI:ZIN(                                                        mo
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#                    "MUSUITE"(                                  "MUSUITE"
#    )   )   )   )   )
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#    )   )
#    WTI:BW(                                                     hi
#        Connectie:Samen(                                        ŋa
#    )   )
#    WTI:ZNW(                                                    hu
#        WTI:bw(                                                 hi
#            Status:Ongelijk(                                    xüi
#                Schaling:Meervoud(                              po
#    )   )   )
#)
#mo huʃapaxa"MUSUITE" haʃa hiŋa huhixüipo
            "ma hea haxüimelamli huhi hiŋa hucoxacoxi hiŋüi huwa\"\'adjustables.py\'\". mo huʃapaxa\"MUSUITE\" haʃa hiŋa huhixüipo.",
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:2(                                                 hea
#    )
#    WTI:WW(                                                     ha
#        Connectie:Gekoppeld:(                                   ŋo
#    )   )
#    WTI:ZNW(                                                    hu
#        WTI:bw(                                                 hi
#            Schaling:Meervoud(                                  po
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Registratie:Horen(                                      co
#            Status:Geordend(                                    xa
#                Progressie:Vooruitgang(                         za
#    )   )   )   )
#    WTI:BNW(                                                    ho
#        Afstand:Hier(                                           ʒi
#            Waarheid:Onwaar(                                    li
#    )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Gekoppeld(                                    ŋo
#            Waarheid:Misschien(                                 lüi
#    )   )   )
#    WTI:ZNW(                                                    hu
#        WTI:bw(                                                 hi
#            "ICY"(                                              "ICY"
#    )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            "'adjustables.py'"(                                 "'adjustables.py'"
#    )   )   )
#)
#ma hea haŋo huhipo hucoxaza hoʒili hiŋolüi huhi"ICY" hiŋüi huwa"'adjustables.py'"
            "ma hea haŋo huhipo hucoxaza hoʒili hiŋolüi huhi\"ICY\" hiŋüi huwa\"\'adjustables.py\'\".",
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:2(                                                 hea
#    )
#    WTI:WW(                                                     ha
#        Kennis:Begrip(                                          do
#    )   )
#    ZTI:Voorwaarde(                                             mo
#        WTI:ZNW(                                                hu
#            Materie:Iets(                                       wa
#                "'adjustables.py'"(                             "'adjustables.py'"
#                    Waarheid:Onwaar(                            li
#        )   )   )   )
#        ZTI:Scheiding(                                          m
#            WTI:ZNW(                                            hu
#                Activiteit:Actief(                              ʃa
#                    Schaling:Groep(                             pa
#                        Status:Geordend(                        xa
#                            "MUSUITE"(                          "MUSUITE"
#            )   )   )   )   )
#            WTI:WW(                                             ha
#                Activiteit:Actief(                              ʃa
#                    Waarheid:Onwaar(                            li
#            )   )   )
#        )
#    )
#)
#ma hea hado mo huwa"'adjustables.py'"li m huʃapaxa"MUSUITE" haʃali
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:2(                                                 hea
#        Kennis:Wijsheid(                                        du
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#                    Schaling:Meervoud(                          po
#    )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Iets(                                           wa
#            "'adjustables.py'"(                                 "'adjustables.py'"
#    )   )   )
#    ZTI:Keuze(                                                  me
#        WTI:WW(                                                 ha
#            Status:Ongelijk(                                    xüi
#                Kennis:Wijsheid(                                du
#        )   )   )
#        ZTI:Scheiding(                                          m
#        WTI:WW(                                                 ha
#            Status:Ongelijk(                                    xüi
#                Waarheid:Onwaar(                                li
#        )   )   )
#        )
#    )
#)
#ma headu huwapo hiŋüi huwa"'adjustables.py'" me haxüidu m haxüili
            "ma hea hado mo huwa\"\'adjustables.py\'\"li m huʃapaxa\"MUSUITE\" haʃali. ma headu huwapo hiŋüi huwa\"\'adjustables.py\'\" me haxüidu m haxüili.",
#ZTI:Keuze(                                                     me
#    WTI:PVNW:2(                                                hea
#    )
#    WTI:WW(                                                    ha
#        Connectie:Gekoppeld(                                   ŋo
#    )   )
#    WTI:ZNW(                                                   hu
#        ZTI:keuze(                                             me
#    )   )
#    WTI:ZNW(                                                   hu
#        Materie:Ding(                                          wo
#            Schaling:Meervoud(                                 po
#    )   )   )
#    WTI:BW(                                                    hi
#        Connectie:Binnen(                                      ŋüi
#    )   )
#    WTI:ZNW(                                                   hu
#        "KEYBOARD"(                                            "KEYBOARD"
#    )   )
#    ZTI:Scheiding:Keuze(                                       mem
#    )
#    ZTI:Voorwaarde(                                            mo
#        WTI:PVNW:2(                                            hea
#        )
#        WTI:WW(                                                ha
#            Activiteit:Actief(                                 ʃa
#        )   )
#        WTI:ZNW(                                               hu
#            ZTI:keuze(                                         me
#                Schaling:Groep(                                po
#                    ")", "]", "}", ">"(                        ")", "]", "}", ">"
#        )   )   )   )
#        ZTI:Scheiding:Voorwaarde(                              mom
#            WTI:WW(                                            ha
#                Richting:Vooruit(                              se
#            )   )
#        )
#    )
#    ZTI:Scheiding:Keuze(                                       mem
#    )
#    ZTI:Voorwaarde(                                            mo
#        WTI:PVNW:2(                                            hea
#        )
#        WTI:WW(                                                ha
#            Activiteit:Actief(                                 ʃa
#        )   )
#        WTI:ZNW(                                               hu
#            ZTI:keuze(                                         me
#                Schaling:Groep(                                po
#                    "(", "[", "{", "<"(                        "(", "[", "{", "<"
#        )   )   )   )
#        ZTI:Scheiding:Voorwaarde(                              mom
#            WTI:WW(                                            ha
#                Richting:Achteruit(                            süe
#            )   )
#        )
#    )
#)
#me hea haŋo hume huwopo hiŋüi hu"KEYBOARD" mem mo hea haʃa humepo"),],},>" mom hase mem mo hea haʃa humepo"(,[,{,<" mom hasüe
#ZTI:Voorwaarde(                                                 mo
#    WTI:WW(                                                     ha
#        Activiteit:Beweging(                                    ʃe
#            Materie:Ding(                                       wo
#                "ENTER"(                                        "ENTER"
#    )   )   )   )                         
#    WTI:Voorwaarde:Scheiding(                                   m
#        WTI:WW(                                                 ha
#            Connectie:Gekoppeld(                                ŋo
#                ZTI:keuze(                                      me
#        )   )   )
#    )
#)
#mo haʃewo"ENTER" m haŋome
#ZTI:ZIN(                                                        ma
#    WTI:ZNW(                                                    hu
#        "MOUSE"(                                                "MOUSE"
#    )   )
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#            Waarheid:Onwaar(                                    li
#    )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#                    "MUSUITE"(                                  "MUSUITE"
#    )   )   )   )   )
#)
#ma hu"MOUSE" haʃali hiŋüi huʃapaxa"MUSUITE"
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:2(                                                 hea
#    )
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#            ZTI:keuze(                                          me
#                Schaling:Meervoud(                              po
#    )   )   )   )
#    WTI:BW(                                                     hi
#        Connectie:Binnen(                                       ŋüi
#    )   )
#    WTI:ZNW(                                                    hu
#        ZTI:keuze(                                              me
#            Schaling:Groep(                                     pa
#                Schaling:Meervoud(                              po
#                    Tellen:Deel(                                büi
#    )   )   )   )   )
#    WTI:BW(                                                     hi
#        Progressie:Start(                                       zi
#    )   )
#    WTI:ZNW(                                                    hu
#        Connectie:Gekoppeld(                                    ŋo
#            "COMMA"(                                            "COMMA"
#                Connectie:Tussen(                               ŋüa
#                    ZTI:keuze(                                  me
#                        Schaling:Meervoud(                      po
#    )   )   )   )   )   )
#    WTI:BW(                                                     hi
#        Progressie:Eind(                                        zu
#    )   )
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#            Materie:Ding(                                       wo
#                "ENTER"(                                        "ENTER"
#    )   )   )   )
#)
#ma hea haʃamepo hiŋüi humepapobüi hizi huŋo"COMMA"ŋüamepo hizu haʃawo"ENTER"
    #"For the genre selection, you can also quickly filter by using just the first letter or the first two letters of multiple genres you want to select at once.",
#ZTI:Voorwaardelijk(                                             mo
#    WTI:PVNW:2(                                                 hea
#    )
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#    )   )
#    WTI:ZNW(                                                    hu
#        Materie:Ding(                                           wo
#            Connectie:Bijbehorend(                              ŋe
#                                                                hu
#                                                                co
#                                                                xa
#                                                                co
#                                                                xi
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Tellen:Deel(                                            büi
#            WTI:Keuze(                                          me
#                Progressie:Start(                               zi
#                    Tellen:1(                                   be
#                        ZTI:Scheiding(                          m
#                            Progressie:Start(                   zi
#                                tellen:2(                       ba
#    )   )   )   )   )   )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 ha
#            Schaling:Groep(                                     pa
#                                                                hu
#                                                                co
#                                                                xa
#                                                                co
#                                                                xi
#                Status:Gelijkmatig(                             xi
#                    Schaling:Alle(                              pu
#        )   )   )   )
#    )
#)
#mo hea haʃa huwoŋehucoxacoxi hubüimezibemziba m hapahucoxacoxixipu
            "me hea haŋo hume huwopo hiŋüi hu\"KEYBOARD\" mem mo hea haʃa humepo\"),],},>\" mom hase mem mo hea haʃa humepo\"(,[,{,<\" mom hasüe. mo haʃewo\"ENTER\" m haŋome. ma hu\"MOUSE\" haʃali hiŋüi huʃapaxa\"MUSUITE\". ma hea haʃamepo hiŋüi humepapobüi hizi huŋo\"COMMA\"ŋüamepo hizu haʃawo\"ENTER\". mo hea haʃa huwoŋehucoxacoxi hubüimezibemziba m hapahucoxacoxixipu.",
#            "For playback, the program calls \"mpg123\".
#ZTI:Voorwaardelijk(                                             mo
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#    )   )
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#                    "MUSUITE"(                                  "MUSUITE"
#    )   )   )    )    )
#    ZTI:Scheiding(                                              m
#        WTI:ZNW(                                                hu
#            Verlangen:Eisen(                                    ku
#        )   )
#        WTI:ZNW(                                                hu
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "MPG123"(                               "MPG123"
#        )   )   )   )   )
#    )
#)
#mo haʃa huʃapaxa"MUSUITE" m huku huʃapaxa"MPG123".
# Make sure it is installed.
#ZTI:ZIN(                                                        ma
#    WTI:WW(                                                     ha
#        Connectie:Gekoppeld(                                    ŋo
#            Kennis:Weten(                                       da
#    )   )   )
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#                    "MPG123"(                                   "MPG123"
#    )   )   )   )   )
#    WTI:BW(                                                     hi
#        Afstand:Hier(                                           ʒi
#    )   )
#)
#ma haŋoda huʃapaxa"MPG123" hiʒi
# For its use, consult the official man pages with the command \"man mpg123\" or \"woman mpg123\".
#ZTI:Voorwaarde(                                                 mo
#    WTI:WW(                                                     ha
#        Activiteit:Actief(                                      ʃa
#            Materie:Ding(                                       wo
#                Schaling:Groep(                                 pa
#                    "hufu mpg123"(                              "hufu mpg123"
#    )   )   )   )   )
#    ZTI:Scheiding(                                              m
#        WTI:WW(                                                 hu
#            Kennis:Weten(                                       da
#                Richting:Vooruit(                               se
#                    Schaling:Meervoud(                          po
#        )   )   )   )
#        WTI:ZNW(                                                hu
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "MPG123"(                               "MPG123"
#        )   )   )   )   )
#    )
#)
#mo haʃawopa"hufu mpg123" m hudasepo huʃapaxa"MPG123". 
# Remember that \"mpg123\" does not support all music file types. The name says it all.",
#ZTI:Oorzaak(                                                    mu
#    WTI:ZNW(                                                    hu
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#    )   )   )   )
#    WTI:Label(                                                  hi
#        "MPG123"(                                               "MPG123"
#    )   )
#    ZTI:Scheiding(                                              m
#        WTI:ZNW(                                                hu
#            Materie:Iets(                                       wa
#                Registratie:Horen(                              co
#                    Status:Geordend(                            xa
#                        Schaling:Alle(                          pu
#        )   )   )   )   )
#        WTI:WW(                                                 ha
#            Activiteit:Actief(                                  ʃa
#                Richting:Vooruit(                               se
#                    Registratie:Horen(                          co
#                        Waarheid:Onwaar(                        li
#        )   )   )   )   )
#    )
#)
#mu huʃapaxa hi"MPG123" m huwacoxapu haʃasecoli. 
            "mo haʃa huʃapaxa\"MUSUITE\" m huku huʃapaxa\"MPG123\" hiŋi huʃapaxa\"MPV\". ma haŋoda huʃapaxa\"MPG123\" hiŋi huʃapaxa\"MPV\" hiʒi. me mo haʃawopa\"\'hufu mpg123\'\" mom hudasepo huʃapaxa\"MPG123\" mem mo haʃawopa\"\'hufu mpv\'\" mom hudasepo huʃapaxa\"MPV\". mu huʃapaxa hi\"MPG123\" m huwacoxapu haʃasecoli. ",
#            "Enjoy your listening!"
#ZTI:ZIN(                                                        ma
#    WTI:PVNW:1(                                                 hee
#        Schaling:Groep(                                         pa
#    )   )
#    WTI:WW(                                                     ha
#        Verlangen:Wensen(                                       ka
#    )   )
#    ZTI:OORZAAK(                                                mu
#        ZTI:WW(                                                 ha
#            Activiteit:Actief(                                  ʃa
#        )   )
#        WTI:ZNW(                                                hu
#            Activiteit:Actief(                                  ʃa
#                Schaling:Groep(                                 pa
#                    Status:Geordend(                            xa
#                        "MUSUITE"(                              "MUSUITE"
#        )   )   )   )   )
#        ZTI:Scheiding(                                          m
#            WTI:PVNW:2(                                         hea
#                Gevoelens:Blijdschap(                           ga
#            )   )
#        )
#    )
#)
#ma heepa haka mu haʃa huʃapaxa"MUSUITE" m heaga.
            "ma heepa haka mu haʃa huʃapaxa\"MUSUITE\" m heaga."
            ]
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
        manmpg123 = manmpg123CJ
        manmpv = manmpvCJ
        man = manmpg123CJ+manmpvCJ
    elif lang == "EN":
        helpteksten = [
        """Everywhere:                                                                     
"B”          : Back                                                             
"H”          : Help                                                             
"Q”          : Quit                                                             
"man mpg123” : or "woman mpg123": mpg123 manual                                 
"man mpv”    : or "woman mpv"   : mpv manual                                    
                                                                                
In main menu:                                                                   
"L”          : Language selection                                               
                                                                                
In selection lists:                                                             
">”          : Scroll forward                                                   
"<”          : Scroll backward                                                  
"*”          : Select all                                                       
2,5,11,17,23 : CSV-style multiple selections                                    """,
            "With musuite, you can play your organized music collection and saved online streams. Press \"Enter\" to proceed with your choice, \"B\" to interrupt the current function, or \"Q\" to quit. To change the language, you can select \"L\" in the main menu.",
            "musuite uses mpg123 and mpv, available in most repositories, and \"chooseFromNumberedList.py\", which you can download from https://github.com/maestraccio/chooseFromNumberedList. Place it in the same directory as \"musuite.py\" and \"adjustables.py\".",
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
            "For playback, the program calls \"mpg123\" or \"mpv\". Make sure these are installed. For their use, consult the official man pages with the command \"man mpg123\" or \"woman mpg123\" for help on \"mpg123\" or \"man mpv\" or \"woman mpv\" for help on \"mpv\". Remember that \"mpg123\" does not support all music file types. The name says it all.",
            "Enjoy your listening!"
            ]
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
        manmpg123 = manmpg123EN
        manmpv = manmpvEN
        man = manmpg123EN+manmpvEN
    elif lang == "IT":
        helpteksten = [
            """Ovunque:                                                                        
"B”           : Indietro                                                        
"H”           : Aiuto                                                           
"Q”           : Esci                                                            
"uomo mpg123” : o "donna mpg123" : Manuale mpg123                               
"uomo mpv"    : o "donna mpv"    : Manuale mpv                                  
                                                                                
In menu principale:                                                             
"L”           : Selezione lingua                                                
                                                                                
In liste di selezione:                                                          
">”           : Scorri avanti                                                   
"<”           : Scorri indietro                                                 
"*”           : Seleziona tutto                                                 
2,5,11,17,23  : Selezione multipla in stile CSV                                 """,
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
            "Per la riproduzione, il programma richiama \"mpg123\" o \"mpv\". Assicurati che siano installati. Per il suo utilizzo, consulta le pagine man ufficiali con il comando \"man mpg123\" o \"donna mpg123\" per aiuto su \"mpg123\", o \"man mpv\" o \"donna mpv\" per aiuto su \"mpv\". Ricorda che \"mpg123\" non supporta tutti i formati di file musicali. Il nome dice già tutto.",
            "Buon ascolto!"
            ]
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
        manmpg123 = manmpg123IT
        manmpv = manmpvIT
        man = manmpg123IT+manmpvIT
    else:
        helpteksten = [
            """Overal:                                                                         
"B"          : Terug                                                            
"H"          : Help                                                             
"Q"          : Afsluiten                                                        
"man mpg123" : of "vrouw mpg123" : Handleiding mpg123                           
"man mpv"    : of "vrouw mpv"    : Handleiding mpv                              
                                                                                
In hoofdmenu:                                                                   
"L"          : Taalkeuze                                                        
                                                                                
In keuzelijsten:                                                                
">"          : Vooruit bladeren                                                 
"<"          : Achteruit bladeren                                               
"*"          : Alles selecteren                                                 
2,5,11,17,23 : Meerdere selecties in CSV-stijl                                  """,
            "Met musuite kun je je georganiseerde muziekverzameling en verzamelde online streams afspelen. Druk op \"Enter\" om na je keuze door te gaan, \"B\" om de huidige functie te onderbreken of \"Q\" om te stoppen. Om de taal te wijzigen kun je in het hoofdmenu \"L\" kiezen.",
            "musuite maakt gebruik van mpg123 en mpv, beschikbaar in de meeste repo's, en van \"chooseFromNumberedList.py\", dat je kunt downloaden van https://github.com/maestraccio/chooseFromNumberedList. Plaats het in dezelfde map als \"musuite.py\" en \"adjustables.py\".",
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
            "Voor het afspelen wordt het programma \"mpg123\" of \"mpv\" aangeroepen. Zorg ervoor dat die geïnstalleerd zijn. Voor het gebruik ervan kun je de officiele manpages raadplegen met de opdracht \"man mpg123\" of \"vrouw mpg123\" voor hulp bij \"mpg123\" of \"man mpv\" of \"vrouw mpv\" voor hulp bij \"mpv\". Denk eraan dat \"mpg123\" niet alle muziekbestandstypen kan afspelen. De naam zegt genoeg.",
            "Veel luisterplezier!"
            ]
        neelijst = neelijstNL
        jalijst = jalijstNL
        neeja = neejaNL
        manmpg123 = manmpg123NL
        manmpv = manmpvNL
        man = manmpg123NL+manmpvNL
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
        elif stop.lower() in manmpg123:
            subprocess.run(["man", "mpg123"])
        elif stop.lower() in manmpv:
            subprocess.run(["man", "mpv"])

    if lang == "CJ":
#ZTI:Voorwaardelijk(                                             mo
#)
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        Waarheid:Waar(                                          la
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#        Registratie:Zien(                                       ca
#)   )
#WTI:ZNW(                                                        hu
#    Kennis:Weten(                                               da
#        Afstand:Hier(                                           ʒi
#)   )   )
#WTI:WW(                                                         ha
#    Progressie:Start(                                           zi
#        Activiteit:Actief(                                      ʃa
#            Schaling:Groep(                                     pa
#                Status:Geordend(                                xa
#)   )   )   )   )
#mo hamela m haca hudaʒi haziʃapaxa
#ZTI:Voorwaarde(                                                 mo
#)
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        "H"(                                                    "Ḧ"
#)   )   )
#WTI:BW(                                                         hi
#    zti:Keuze(                                                  me
#        Afstand:Overal(                                         pu
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#        Kennis:Weten(                                           da
#            Schaling:Groep(                                     pa
#                Afstand:Hier(                                   ʒi
#)   )   )   )   )
#mo hame"H" himepu m hacadapaʒi
        wraptext = "mo hamela m haca hudaʒi haziʃapaxa. mo hame\"H\" himepu m hacadapaʒi:"
    elif lang == "EN":
        wraptext = "Do you want to see this help text again the next time you start the program? You can always call up this help text with \"H\":"
    elif lang == "IT":
        wraptext = "Vuoi rivedere questa guida la prossima volta che avvii il programma? Puoi richiamare questa guida in qualsiasi momento con \"H\":"
    else:
        wraptext = "Wil je deze helptekst opnieuw zien als je de volgende keer het programma start? Je kunt deze helptekst altijd oproepen met \"H\":"
    for w in textwrap.wrap(wraptext,80):
        print(w)
    nj,index = cFNL([neeja,"A",0,0,"> ",jalijst+neelijst+man+backlijst+quitlijst])
    if nj in quitlijst:
        exit()
    elif nj in backlijst:
        return
    elif nj.lower() in manmpg123:
        subprocess.run(["man", "mpg123"])
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
#ZTI:Zin(                                                        ma
#)
#WTI:ZNW(                                                        hu
#    Afstand:Hier(                                               ʒi
#        Materie:Iets(                                           wa
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#                    Schaling:Meervoud(                          po
#)   )   )   )   )   )
#WTI:ZNW(                                                        hu
#    Connectie:Binnen(                                           ŋüi
#        Progressie:Start(                                       zi
#            Tijd:Nu(                                            qi
#)   )   )   )
#ma huʒiwacoxapo huŋüiziqi
    padtekst = "ma huʒiwacoxapo huŋüiziqi:"
#ZTI:Oorzaak(                                                    mu
#)
#WTI:WW(                                                         ha
#    Tijd:VanafNu(                                               qe
#        Progressie:Vooruitgang(                                 za
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#    Connectie:Samen(                                            ŋa
#        Materie:Iets(                                           wa
#            Registratie:Horen(                                  co
#                Status:Geordend(                                xa
#                    Schaling:Meervoud(                          po
#)   )   )   )   )   )
#mu haqeza m haŋawacoxapo...
    gener = "mu haqeza m haŋawacoxapo..."
#WTI:BNW(                                                        ho
#    Progressie:Eindpunt(                                        zu
#)   )
#hozu
    klaar = "... hozu"
elif lang == "EN":
    padtekst = "The path used as the MAIN_FOLDER for your music collection is now:"
    gener = "Your music collection is being gathered, this may take a moment..."
    klaar = "... Done"
elif lang == "IT":
    padtekst = "Il percorso utilizzato come CARTELLA_PRINCIPALE della tua raccolta musicale adesso è:"
    gener = "Sto raccogliendo la tua collezione musicale, potrebbe richiedere un momento..."
    klaar = "... Fatto"
else:
    padtekst = "Het pad dat nu gebruikt wordt als HOOFDMAP van je muziekcollectie is:"
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
    extensielijst = [".mp1",".mp2",".mp3",".mpeg",".mpg",".mpga"]
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
        print("ma hiʒi huwa\"MP3\"li. ma haco hame hucoxaza hoʒili hixüili")
    elif lang == "EN":
        print("No MP3 files found. You can only choose to listen from your online streams")
    elif lang == "CJ":
        print("Nessun file MP3 trovato. Puoi solo sceglere di ascolare dagli streaming online")
    else:
        print("Geen MP3-bestanden gevonden. Je kunt alleen luisteren naar je keuze uit online streams")
    streamslijst = []
    for i in streamsdict:
        streamslijst.append(i)
    padwaar = False

############################################

loop = True
while loop == True:
    if lang == "CJ":
#WTI:ZNW(                                                        hu
#    Afstand:Hier(                                               ʒi
#        Prograssie:Beginfase(                                   ze
#)   )   )
#huʒize
        hoofdmenu = " - - huʒize - -"
        mpg123 = mpg123CJ
        mpv = mpvCJ
        mosdict = {
#WTI:ZNW(                                                        hu
#    "MP3"(                                                      "MP3"
#        Schaling:Groep(                                         pa
#)   )   )
#WTI:BNW(                                                        ho
#    Afstand:Hier(                                               ʒi
#)   )
#hu"MP3"pa hoʒi
                "M":colT+"hu\"MP3\"pa hoʒi"+colR,
#WTI:ZNW(                                                        hu
#    Registratie:Horen(                                          co
#        Status:Geordend(                                        xa
#            Progressie:Vooruitgang(                             za
#)   )   )   )
#WTI:BNW(                                                        ho
#    Afstand:Hier(                                               ʒi
#        Waarheid:Onwaar(                                        li
#)   )   )
#hucoxaza hoʒili
                "Z":colS+"hucoxaza hoʒili"+colR
                }
        zosdict = {
#WTI:WW(                                                         ha
#    Materie:Iets(                                               wa
#        Afstand:Daar(                                           ʒa
#            Status:Gelijkmatig(                                 xi
#                Afstand:Hier(                                   ʒi
#)   )   )   )   )
                "w":colD+"hawaʒaxiʒi"+colR,
#WTI:WW(                                                         ha
#    Progressie:Vooruitgang(                                     za
#        Status:Geordend(                                        xa
#            Registratie:Zien(                                   ca
#)   )   )   )
#hacazaxa
                "z":colD+"hazaxaca"+colR
                }
        gmtdict = {
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Registratie:Horen(                                      co
#            Status:Gelijkmatig(                                 xi
#)   )   )
#hupacoxi
                "G":colG+"hupacoxi"+colR,
#WTI:ZNW(                                                        hu
#    Schaling:Meervoud(                                          po
#        Connectie:Samen(                                        ŋa
#)   )   )
#hupoŋa
                "M":colD+"hupoŋa"+colR,
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#         Registratie:Horen(                                     co
#             Status:Geordend(                                   xa
#)   )   )   )
#huwacoxa
                "T":colT+"huwacoxa"+colR
                }
        manmpg123 = manmpg123CJ
        manmpv = manmpvCJ
        man = manmpg123CJ+manmpvCJ
    elif lang == "EN":
        hoofdmenu = " - - MAIN MENU - -"
        mpg123 = mpg123EN
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
        manmpg123 = manmpg123EN
        manmpv = manmpvEN
        man = manmpg123EN+manmpvEN
    elif lang == "IT":
        hoofdmenu = " - - MENU PRINCIPALE - -"
        mpg123 = mpg123IT
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
        manmpg123 = manmpg123IT
        manmpv = manmpvIT
        man = manmpg123IT+manmpvIT
    else:
        hoofdmenu = " - - HOOFDMENU - -"
        mpg123 = mpg123NL
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
        manmpg123 = manmpg123NL
        manmpv = manmpvNL
        man = manmpg123NL+manmpvNL
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
            elif k.lower() in manmpg123:
                subprocess.run(["man", "mpg123"])
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
            elif s.lower() in manmpg123:
                subprocess.run(["man", "mpg123"])
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
            elif k.lower() in manmpg123:
                subprocess.run(["man", "mpg123"])
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
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    Kennis:Denken(                                              de
#        Materie:Iets(                                           wa
#)   )   )
#WTI:WW(                                                         ha
#    Activiteit:Bewegen(                                         ʃa
#        Materie:Iets(                                           wa
#)   )   )
#WTI:WW(                                                         ha
#    Activiteit:Bewegen(                                         ʃa
#        Materie:Ding(                                           wo
#            "ENTER"(                                            "ENTER"
#)   )   )   )
#ma hadewa haʃawa haʃawo"ENTER"
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        Waarheid:Onwaar(                                        li
#)   )   )
#WTI:ZNW(                                                        hu
#    Materie:Ding(                                               wo
#        Connectie:Gekoppeld(                                    ŋo
#            Activiteit:Beweging(                                ʃa
#                Progressie:Eindpunt(                            zu
#)   )   )   )   )
#WTI:BNW(                                                        ho
#    Status:Gelijkmatig(                                         xi
#        "Q"(                                                    "Q"
#)   )   )
#ma hameli huwoŋoʃazu hoxi"Q"
                        zoekterm = input("ma hadewa haʃawa haʃawo\"ENTER\". ma hameli huwoŋoʃazu hoxi\"Q\":\n")
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
                    elif zoekterm.lower() in manmpg123:
                        subprocess.run(["man", "mpg123"])
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
#ZTI:Zin(                                                        ma
#)
#WTI:ZMW(                                                        hu
#    Schaling:Groep(                                             pa
#        Richting:Hierheen(                                      süi
#)   )   )
#WTI:BNW(                                                        ho
#    Grootte::NulNegatief(                                       ñüi
#)   )
#ma hupasüi hoñüi.
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    Kennis:Denken(                                              de
#)   )
#WTI:ZNW(                                                        hu
#    Status:Gelijk((                                             xi
#        Grootte:Klein(                                          ñe
#            Grootte:Groot(                                      ño
#                Waarheid:Onwaar(                                li
#)   )   )   )   )
#ma hade huxiñeñoli.
                                wraptext = "ma hupasüi hoñüi. ma hade huxiñeñoli."
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
                            elif tracksel in manmpg123:
                                subprocess.run(["man", "mpg123"])
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
#WTI:WW(                                                         ha
#    Materie:Iets(                                               wa
#        Afstand:Daar(                                           ʒa
#            Status:Gelijkmatig(                                 xi
#                Afstand:Hier(                                   ʒi
#)   )   )   )   )
#hawaʒaxiʒi
#WTI:WW(                                                         ha
#    Progressie:Vooruitgang(                                     za
#        Status:Geordend(                                        xa
#            Registratie:Zien(                                   ca
#)   )   )   )
#hacazaxa
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
                    elif k.lower() in manmpg123:
                        subprocess.run(["man", "mpg123"])
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
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    Kennis:Denken(                                              de
#        Materie:Iets(                                           wa
#)   )   )
#WTI:WW(                                                         ha
#    Activiteit:Bewegen(                                         ʃa
#        Materie:Iets(                                           wa
#)   )   )
#WTI:WW(                                                         ha
#    Activiteit:Bewegen(                                         ʃa
#        Materie:Ding(                                           wo
#            "ENTER"(                                            "ENTER"
#)   )   )   )
#ma hadewa haʃawa haʃawo"ENTER"
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        Waarheid:Onwaar(                                        li
#)   )   )
#WTI:ZNW(                                                        hu
#    Materie:Ding(                                               wo
#        Connectie:Gekoppeld(                                    ŋo
#            Activiteit:Beweging(                                ʃa
#                Progressie:Eindpunt(                            zu
#)   )   )   )   )
#WTI:BNW(                                                        ho
#    Status:Gelijkmatig(                                         xi
#        "Q"(                                                    "Q"
#)   )   )
#ma hameli huwoŋoʃazu hoxi"Q"
                                    zoekterm = input("ma hadewa haʃawa haʃawo\"ENTER\". ma hameli huwoŋoʃazu hoxi\"Q\":\n")
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
                                elif zoekterm.lower() in manmpg123:
                                    subprocess.run(["man", "mpg123"])
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
#ZTI:Zin(                                                        ma
#)
#WTI:ZMW(                                                        hu
#    Schaling:Groep(                                             pa
#        Richting:Hierheen(                                      süi
#)   )   )
#WTI:BNW(                                                        ho
#    Grootte::NulNegatief(                                       ñüi
#)   )
#ma hupasüi hoñüi.
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    Kennis:Denken(                                              de
#)   )
#WTI:ZNW(                                                        hu
#    Status:Gelijkmatig(                                         xi
#        Grootte:Klein(                                          ñe
#            Grootte:Groot(                                      ño
#                Waarheid:Onwaar(                                li
#)   )   )   )   )
#ma hade huxiñeñoli.
                                            wraptext = "ma hupasüi hoñüi. ma hade huxiñeñoli."
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
                                        elif mappsel in manmpg123:
                                            subprocess.run(["man", "mpg123"])
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
                                elif mappsel in manmpg123:
                                    subprocess.run(["man", "mpg123"])
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
                    elif optie in manmpg123:
                        subprocess.run(["man", "mpg123"])
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
