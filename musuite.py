#!/usr/bin/env python3
import subprocess, os, sys, random, textwrap
from time import sleep
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromDictionary as cFD
from adjustables import lang,picklang,showhelp,pad,genredict,streamsdict
Versie = "1.03"
Date = "2026-08-10"
hier = os.path.dirname(os.path.realpath(__file__))
os.chdir(hier)
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
neejaCJ = ["li","la"]
neelijstEN = ["N","n","no"]
jalijstEN = ["Y","y","yes","Yes"]
neejaEN = ["N","Y"]
neelijstIT = ["N","n","no","No"]
jalijstIT = ["S","s","si","sì","Si","Sì"]
neejaIT = ["N","S"]
neelijstNL = ["N","n","nee","Nee"]
jalijstNL = ["J","j","ja","Ja"]
neejaNL = ["N","J"]
manCJ = ["man mpg123","woman mpg123","hufu mpg123"]
manEN = ["man mpg123","woman mpg123"]
manIT = ["man mpg123","woman mpg123","uomo mpg123","donna mpg123"]
manNL = ["man mpg123","woman mpg123","vrouw mpg123"]
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
#)
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        Waarheid:Waar(                                          la
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#)   )
#WTI:ZNW(                                                        hu
#    zti:Keuze(                                                  me
#        Afstand:Hier(                                           ʒi
#)   )   )
#WTI:WW(                                                         ha
#    Progressie:Start(                                           zi
#        Activiteit:Actief(                                      ʃa
#            Status:Geordend(                                    xa
#                Schaling:Groep(                                 pa
#)   )   )   )   )
#mo hamela m haca humeʒi haziʃaxapa
#ZTI:Voorwaardelijk(                                             mo
#)
#WTI:BNW(                                                        ho
#    Afstand:Hier(                                               ʒi
#        WTI:ZNW(                                                hu
#            Afstand:Hier(                                       ʒi      
#                Progressie:Beginfase(                           ze      
#)   )   )   )   )
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        "L"(                                                    "L"
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#)   )
#WTI:ZNW(                                                        hu
#    zti:Keuze(                                                  me
#         Afstand:Hier(                                          ʒi
#)   )   )
#mo hoʒihuʒize hame"L" m haca humeʒi
        wraptext = "mo hamela m haca humeʒi haziʃaxapa. mo hoʒihuʒize hame\"L\" m haca humeʒi:"
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
        man = manCJ
    elif lang == "EN":
        man = manEN
    elif lang == "IT":
        man = manIT
    else:
        man = manNL
    optie,index = cFNL([genrelijstlang,"A",1,1,"> ",helplijst+man+backlijst+quitlijst])
    if optie in quitlijst:
        exit()
    elif optie in backlijst:
        return optie
    elif optie in man:
        subprocess.run(["man", "mpg123"])
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
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Materie:Iets(                                           wa
#            Registratie:Geluid(                                 co
#                Status:Geordend(                                xa
#)   )   )   )   )
#WTI:ZNW(                                                        hu
#    Tellen:0(                                                   bi
#)
#ma hupawacoxa hubi %s
        print("ma hupawacoxa hubi %s" % str(len(tracklijst)))
    elif lang == "EN":
        print("The track list contains %s tracks" % str(len(tracklijst)))
    elif lang == "IT":
        print("L’elenco delle tracce contiene %s brani" % str(len(tracklijst)))
    else:
        print("De tracklijst bevat %s tracks" % str(len(tracklijst)))
    if len(tracklijst) > 50:
        print()
        if lang == "CJ":
#ZTI:Oorzaak(                                                    mu
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#)   )
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Materie:Iets(                                           wa
#            Registratie:Geluid(                                 co
#                Status:Geordend(                                xa
#)   )   )   )   )
#WTI:BNW(                                                        ho      
#    Schaling:Groep(                                             pa
#        Grootte:Klein(                                          ñe
#            Schaling:Meervoud(                                  po
#)   )   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Materie:Iets(                                           wa
#            Registratie:Geluid(                                 co
#                Status:Geordend(                                xa
#                    Grootte:Groot(                              ño
#)   )   )   )   )   )
#WTI:BW(                                                         hi
#    Registratie:Zien(                                           ca
#        Schaling:Alles(                                         pu
#            Waarheid:Niet(                                      li
#                Waarheid:Misschien(                             lüi
#)   )   )   )   )
#mu haca hupawacoxa hopañepo m hupawacoxaño hicapulilüi
#ZTI:Voorwaarde(                                                 mo
#)
#WTI:WW(                                                         ha
#    ZTI:Keuze(                                                  me
#                "B"(                                            "B"
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#        Waarheid:Onwaar(                                        li
#            Tijd:Vanaf nu(                                      qe
#)   )   )   )
#mo hame"B" m hacaliqe
            wraptext = "mu haca hupawacoxa hopañepo m hupawacoxaño hicapulilüi. mo hame\"B\" m hacaliqe."
        elif lang == "EN":
            wraptext = "The track list is long and may not fit on your screen. The list is therefore displayed in multiple parts. Use \"B\" to break the display and continue to playback."
        elif lang == "IT":
            wraptext = "L’elenco delle tracce è lungo e potrebbe non entrare sullo schermo. L’elenco viene quindi mostrato in più parti. Usa \"B\" per interrompere la visualizzazione e passare alla riproduzione."
        else:
            wraptext = "De tracklijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom in meerdere delen getoond. Gebruik \"B\" om de weergave af te breken en door te gaan naar afspelen."
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print()
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
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        WTI:ZNW(                                                hu
#            Materie:Iets(                                       wa
#                Connectie:Binnen(                               ŋüi
#)   )   )   )   )
#WTI:ZNW(                                                        hu
#    Tellen:0(                                                   bi
#)
#ma hupahuwaŋüi hubi %s
        print("ma hupahuwaŋüi hubi %s" % str(len(mappenlijst)))
    elif lang == "EN":
        print("The folder list contains %s folders" % str(len(mappenlijst)))
    elif lang == "IT":
        print("L'elenco delle cartelle contiene %s cartelle" % str(len(mappenlijst)))
    else:
        print("De mappenlijst bevat %s mappen" % str(len(mappenlijst)))
    if len(mappenlijst) > 50:
        print()
        if lang == "CJ":
#ZTI:Oorzaak(                                                    mu
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#)       )
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        WTI:ZNW(                                                hu
#            Materie:Iets(                                       wa
#                Connectie:Binnen(                               ŋüi
#)   )   )   )   )
#WTI:BNW(                                                        ho      
#    Schaling:Groep(                                             pa
#        Grootte:Klein(                                          ñe
#            Schaling:Meervoud(                                  po
#)   )   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        wti:ZNW(                                                hu
#            Materie:Iets(                                       wa
#                Connectie:Binnen(                               ŋüi
#                    Grootte:Groot(                              ño
#)   )   )   )   )   )
#WTI:BW(                                                         hi
#    Registratie:Zien(                                           ca
#        Schaling:Alles(                                         pu
#            Waarheid:Niet(                                      li
#                Waarheid:Misschien(                             lüi
#)   )   )   )   )
#mu haca hupawacoxa hopañepo m hupawacoxaño hicapulilüi
#ZTI:Voorwaarde(                                                 mo
#)
#WTI:WW(                                                         ha
#    ZTI:Keuze(                                                  me
#        "B"(                                                    "B"
#)   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#        Waarheid:Onwaar(                                        li
#            Tijd:Vanaf nu(                                      qe
#)   )   )   )
#mo hame"B" m hacaliqe
            wraptext = "mu haca hupahuwaŋüi hopañepo m hupahuwaŋüiño hicapulilüi. mo hame\"B\" m hacaliqe."
        elif lang == "EN":
            wraptext = "The folder list is long and may not fit on your screen. The list is therefore displayed in multiple parts. Use \"B\" to break the display and continue to playback."
        elif lang == "IT":
            wraptext = "L'elenco delle cartelle è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato in più parti. Usa \"B\" per interrompere la visualizzazione e passare alla riproduzione."
        else:
            wraptext = "De mappenlijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom in meerdere delen getoond. Gebruik \"B\" of \"U\" om de weergave af te breken en door te gaan naar afspelen."
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print()
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
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Materie:Iets(                                           wa
#            Registratie:Geluid(                                 co
#                Status:Geordend(                                xa
#)   )   )   )   )
#WTI:ZNW(                                                        hu
#    Tellen:0(                                                   bi
#)
#ma hupawacoxa hubi %s
        print("ma hupawacoxa hubi %s" % str(len(tracklijst)))
    elif lang == "EN":
        print("The track list contains %s tracks" % str(len(tracklijst)))
    elif lang == "IT":
        print("L’elenco delle tracce contiene %s brani" % str(len(tracklijst)))
    else:
        print("De tracklijst bevat %s tracks" % str(len(tracklijst)))
    tracklijstverkort = []
    if len(tracklijst) > 50:
        print()
        if lang == "CJ":
#ZTI:Oorzaak(                                                    mu
#)
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#)   )
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Materie:Iets(                                           wa
#            Registratie:Geluid(                                 co
#                Status:Geordend(                                xa
#)   )   )   )   )
#WTI:BNW(                                                        ho      
#    Schaling:Groep(                                             pa
#        Grootte:Klein(                                          ñe
#            Schaling:Meervoud(                                  po
#)   )   )   )
#ZTI:Scheiding(                                                  m
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Materie:Iets(                                           wa
#            Registratie:Geluid(                                 co
#                Status:Geordend(                                xa
#                    Grootte:Groot(                              ño
#)   )   )   )   )   )
#WTI:BW(                                                         hi
#    Registratie:Zien(                                           ca
#        Schaling:Alles(                                         pu
#            Waarheid:Niet(                                      li
#                Waarheid:Misschien(                             lüi
#)   )   )   )   )
#mu haca hupawacoxa hopañepo m hupawacoxaño hicapulilüi
            wraptext = "mu haca hupawacoxa hopañepo m hupawacoxaño hicapulilüi."
        elif lang == "EN":
            wraptext = "The track list is long and may not fit on your screen. The list is therefore first displayed in multiple parts so you can see the numbers of the track(s) you want to select. After that, you will have the option to enter your final choice. Remember those numbers."
        elif lang == "IT":
            wraptext = "L'elenco delle tracce è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato inizialmente in più parti in modo che tu possa vedere i numeri delle tracce che desideri selezionare. Successivamente potrai inserire la tua scelta definitiva. Ricorda quei numeri."
        else:
            wraptext = "De tracklijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom eerst in meerdere delen getoond zodat je de nummers van de track(s) die je in je selectie wilt een keer hebt kunnen zien. Daarna krijg je de optie om je definitieve keuze in te geven. Onthoud die nummers."
        print()
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print()
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
#)
#WTI:Pers.vnw:2(                                                 hea
#)
#WTI:WW(                                                         ha
#    ZTI:Keuze(                                                  me
#        Waarheid:Concreet(                                      lo      
#)   )   )
#WTI:Bijwoord(                                                   hi
#    Tijd:Binnenkort(                                            qa
#)   )
#ma hea hamelo hiqa.
#WTI:Zin(                                                        ma
#)
#WTI:Pers.vnw:2(                                                 hea
#)
#WTI:WW(                                                         ha
#    Kennis:Denken(                                              de
#        Connectie:Gekoppeld(                                    ŋo
#            Schaling:Groep(                                     pa
#                Verlangen:Willen(                               ke
#                    Registratie:Horen(                          co
#)   )   )   )   )   )
#ma hea hadeŋopakeco.
#
#WTI:Zin(                                                        ma
#)
#WTI:Pers.vnw:2(                                                 hea
#)
#WTI:WW(                                                         ha
#    Activiteit:Beweging(                                        ʃe
#        Materie:Ding(                                           wo
#            "ENTER"(                                            "ENTER"
#)   )   )   )
#ma hea haʃewo"ENTER".
            wraptext = "hupazu. ma hea hamelo hiqa. ma hea hadeŋopakeco. ma hea haʃewo\"ENTER\"."
        elif lang == "EN":
            wraptext = "The end of the list has been reached and the option to enter your choice will follow. Remember the number(s) of the track(s) you want to select. Now first press \"Enter\""
        elif lang == "IT":
            wraptext = "La fine dell'elenco è stata raggiunta e a seguire ci sarà l'opzione per inserire la tua scelta. Ricorda il/i numero/i della/le traccia/e che desideri selezionare. Ora premi prima \"Invio\""
        else:
            wraptext = "Het einde van de lijst is bereikt en de optie om je keuze in te voeren volgt hierna. Onthoud de/het nummer(s) van de track(s) die je wilt selecteren. Druk nu eerst op \"Enter\""
        for i in textwrap.wrap(wraptext,80):
            print(i)
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
#)
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        WTI:ZNW(                                                hu
#            Materie:Iets(                                       wa
#                Connectie:Binnen(                               ŋüi
#)   )   )   )   )
#WTI:ZNW(                                                        hu
#    Tellen:0(                                                   bi
#)
#ma hupahuwaŋüi hubi %s
            print("ma hupahuwaŋüi hubi %s" % str(len(mappenlijst)))
        elif lang == "EN":
            print("The folder list contains %s folders" % str(len(mappenlijst)))
        elif lang == "IT":
            print("L'elenco delle cartelle contiene %s cartelle" % str(len(mappenlijst)))
        else:
            print("De mappenlijst bevat %s mappen" % str(len(mappenlijst)))
        print()
        if lang == "EN":
            wraptext = "The folder list is long and may not fit on your screen. The list is therefore first displayed in multiple parts so you can see the number(s) of the folder(s) you want to select. After that, you will have the option to enter your final choice. Remember those numbers."
        elif lang == "IT":
            wraptext = "L'elenco delle cartelle è lungo e potrebbe non entrare sullo schermo. L'elenco viene quindi mostrato inizialmente in più parti in modo che tu possa vedere il/i numero/i della/le cartella/e che desideri selezionare. Successivamente potrai inserire la tua scelta definitiva. Ricorda quei numeri."
        else:
            wraptext = "De mappenlijst is lang en past mogelijk niet op je scherm. De lijst wordt daarom eerst in meerdere delen getoond zodat je het/de nummer(s) van de map(pen) die je in je selectie wilt een keer hebt kunnen zien. Daarna krijg je de optie om je definitieve keuze in te geven. Onthoud die nummers."
        print()
        for i in textwrap.wrap(wraptext,80):
            print(i)
        print()
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
        if lang == "EN":
            wraptext = "The end of the list has been reached and the option to enter your choice will follow. Remember the number(s) of the folder(s) you want to select. Now first press \"Enter\""
        elif lang == "IT":
            wraptext = "La fine dell'elenco è stata raggiunta e a seguire ci sarà l'opzione per inserire la tua scelta. Ricorda il/i numero/i della/le cartella/e che desideri selezionare. Ora premi prima \"Invio\""
        else:
            wraptext = "Het einde van de lijst is bereikt en de optie om je keuze in te voeren volgt hierna. Onthoud het/de nummer(s) van de map(pen) die je wilt selecteren. Druk nu eerst op \"Enter\""
        for i in textwrap.wrap(wraptext,80):
            print(i)
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
#ZTI:Vraag(                                                      mi
#)
#WTI:BW(                                                         hi
#    Status:Rommelig(                                            xüe
#)   )
#mi hixüe
        willekeurig = "mi hixüe"
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    Progressie:Start(                                           ze
#        Activiteit:Beweging(                                    ʃe
#            "mpg123"(                                           "mpg123"
#)   )   )   )
#ma hazeʃe"mpg123"
        mpg123 = "ma hazeʃe\"mpg123\"\n"
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
    elif lang == "EN":
        willekeurig = "Random order?"
        mpg123 = "Starting playback with mpg123\n"
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
    elif lang == "IT":
        willekeurig = "Ordine casuale?"
        mpg123 = "Avvio della riproduzione con mpg123\n"
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
    else:
        willekeurig = "Willekeurige volgorde?"
        mpg123 = "Start afspelen met mpg123\n"
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
        elif ja.lower() in man:
            subprocess.run(["man", "mpg123"])
        elif ja.lower() in helplijst:
            hellup()
        if ja.lower() in neelijst:
            random = ""
    try:
        with open(os.path.join(pad,"tracklijst.m3u"),"w") as tl:
            for tr in tracklijst:
                print(tr, file=tl)
        print(mpg123)
        subprocess.run(["mpg123", "-vm%s" % (random), "-@", os.path.join(pad,"tracklijst.m3u")])
        os.remove(os.path.join(pad,"tracklijst.m3u"))
    except:
        pass

def hellup():
    if lang == "CJ":
        helpteksten = [
            "",
            "",
            "",
            # print as-is [3]
            """\\MAIN_FOLDER\\GENRE\\ALBUM             \\TRACK
 {\\    ...\\path}\\
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
                                          {track22.mp3}""",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
            ]
        neelijst = neelijstCJ
        jalijst = jalijstCJ
        neeja = neejaCJ
        man = manCJ
    elif lang == "EN":
        helpteksten = [
            "With musuite, you can play your organized music collection and saved online streams. Press \"Enter\" to proceed with your choice, \"B\" to interrupt the current function, or \"Q\" to quit. To change the language, you can select \"L\" in the main menu.",
            "musuite uses mpg123, available in most repositories, and \"chooseFromNumberedList.py\", which you can download from https://github.com/maestraccio/chooseFromNumberedList. Place it in the same directory as \"musuite.py\" and \"adjustables.py\".",
            "It is important, no, ESSENTIAL, that your organized music collection looks like this:",
            # print as-is [3]
            """\\MAIN_FOLDER\\GENRE\\ALBUM             \\TRACK
 {\\    ...\\path}\\
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
                                          {track22.mp3}""",
            "In the MAIN_FOLDER, the albums of your artists are sorted by genre. Each genre folder has a name that consists of exactly three letters, no more and no less. Inside the genre folders are the albums, and inside those are the music files. Do not use subfolders, do not place loose music files at another level.",
            "If your music collection is organized differently, adjust it. If you don’t want to, use another program.",
            "In the file \"adjustables.py\" (included and located in the same directory as this program), you specify the exact location of the MAIN_FOLDER after \"pad = \". Use the path formatting as used by your operating system. So, pay attention to whether you should use \"\\\" or \"/\".",
            "In the same file \"adjustables.py\", you can add descriptions to your genre names yourself. There are already examples you can use and/or modify. Genre names that appear in the list but not in your collection do not interfere. You can leave them as they are or remove them, whichever you prefer. After all, it is your collection.",
            "In the same file \"adjustables.py\", create a list of your favorite online streams, with a short description or the ICY-NAME.",
            "You have already understood that the file \"adjustables.py\" is important for the proper functioning of musuite. There are also a few other variables in it that you should better stay away from, or at least handle with great caution.",
            "Type your choice via the keyboard, or use the \"closing brackets\" (\")\", \"]\", \"}\", \">\": to move forward) and the \"opening brackets\" (\"(\", \"[\", \"{\", \"<\": to move backward). Press \"Enter\" to confirm your choice. There is no support for using a mouse or other pointer hardware in musuite. Some choice lists support multiple selections. In that case, enter the choice numbers or exact keys (case-sensitive), separated by commas, consecutively before pressing \"Enter\". For the genre selection, you can also quickly filter by using just the first letter or the first two letters of multiple genres you want to select at once.",
            "For playback, the program calls \"mpg123\". Make sure it is installed. For its use, consult the official man pages with the command \"man mpg123\" or \"woman mpg123\". Remember that \"mpg123\" does not support all music file types. The name says it all.",
            "Enjoy your listening!"
            ]
        neelijst = neelijstEN
        jalijst = jalijstEN
        neeja = neejaEN
        man = manEN
    elif lang == "IT":
        helpteksten = [
            "Con musuite puoi riprodurre la tua collezione musicale organizzata e gli stream online salvati. Premi \"Invio\" per procedere con la tua scelta, \"B\" per interrompere la funzione corrente o \"Q\" per uscire. Per cambiare la lingua, puoi selezionare \"L\" nel menu principale.",
            "musuite utilizza mpg123, disponibile nella maggior parte dei repository, e \"chooseFromNumberedList.py\", che puoi scaricare da https://github.com/maestraccio/chooseFromNumberedList. Posizionalo nella stessa cartella di \"musuite.py\" e \"adjustables.py\".",
            "È importante, anzi ESSENZIALE, che la tua collezione musicale organizzata sia strutturata così:",
            # print as-is [3]
            """\\CARTELLA_PRINCIPALE \\GENERE\\ALBUM              \\TRACCIA
          {\\...\\percorso}\\
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
                                                     {traccia22.mp3}""",
            "Nella CARTELLA_PRINCIPALE ci sono gli album dei tuoi artisti, organizzati per genere. Ogni cartella di genere ha un nome composto da esattamente tre lettere, non una di più e non una di meno. All'interno delle cartelle di genere ci sono gli album, e al loro interno i file musicali. Non usare sottocartelle, non mettere file musicali sciolti a un altro livello.",
            "Se la struttura della tua collezione musicale è diversa, modificala. Se non vuoi farlo, usa un altro programma.",
            "Nel file \"adjustables.py\" (fornito e situato nella stessa cartella di questo programma), specifichi tu stesso la posizione esatta della CARTELLA PRINCIPALE dopo \"pad = \". Utilizza la formattazione del percorso come viene utilizzata dal tuo sistema operativo. Fai quindi attenzione a utilizzare \"\\\" o \"/\" a seconda dei casi.",
            "Nello stesso file \"adjustables.pyi\", puoi aggiungere tu stesso descrizioni ai nomi dei tuoi generi. Ci sono già degli esempi che puoi utilizzare e/o modificare. I nomi dei generi che compaiono nella lista ma non nella tua raccolta non creano problemi. Puoi lasciarli così come sono o rimuoverli, come preferisci. Dopotutto, si tratta della tua raccolta.",
            "Sempre nel file \"adjustables.py\", crea anche una lista dei tuoi stream online preferiti, con una breve descrizione o il nome ICY-NAME.",
            "Hai già capito che il file \"adjustables.py\" è importante per il corretto funzionamento di musuite. All'interno ci sono anche alcune altre variabili con cui è meglio non avere a che fare, o almeno con cui bisogna maneggiare con grande cautela.",
            "Digita la tua scelta tramite la tastiera, oppure utilizza le parentesi chiuse (\")\", \"]\", \"}\", \">\": per andare avanti) e le parentesi aperte (\"(\", \"[\", \"{\", \"<\": per andare indietro). Premi \"Enter\" per confermare la tua scelta. Non è supportato l'uso di un mouse o di altre periferiche di puntamento in musuite. Alcune liste di scelta supportano più scelte. In tal caso, inserisci i numeri delle scelte o le chiavi esatte (sensibili alle maiuscole), separate da virgole, consecutivamente prima di premere \"Enter\". Per la selezione dei generi, puoi anche filtrare rapidamente utilizzando solo la prima lettera o le prime due lettere di più generi che vuoi selezionare contemporaneamente.",
            "Per la riproduzione, il programma richiama \"mpg123\". Assicurati che sia installato. Per il suo utilizzo, consulta le pagine man ufficiali con il comando \"man mpg123\" o \"donna mpg123\". Ricorda che \"mpg123\" non supporta tutti i formati di file musicali. Il nome dice già tutto.",
            "Buon ascolto!"
            ]
        neelijst = neelijstIT
        jalijst = jalijstIT
        neeja = neejaIT
        man = manIT
    else:
        helpteksten = [
            "Met musuite kun je je georganiseerde muziekverzameling en verzamelde online streams afspelen. Druk op \"Enter\" om na je keuze door te gaan, \"B\" om de huidige functie te onderbreken of \"Q\" om te stoppen. Om de taal te wijzigen kun je in het hoofdmenu \"L\" kiezen.",
            "musuite maakt gebruik van mpg123, beschikbaar in de meeste repo's, en van \"chooseFromNumberedList.py\", dat je kunt downloaden van https://github.com/maestraccio/chooseFromNumberedList. Plaats het in dezelfde map als \"musuite.py\" en \"adjustables.py\".",
            "Het is belangrijk, nee ESSENTIEEL dat je georganiseerde muziekverzameling er zo uitziet:",
            # print as-is [3]
            """\\HOOFDMAP \\GENRE\\ALBUM              \\TRACK
{\\.    ..\\pad}\\
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
                                         {track22.mp3}""",
            "In de HOOFDMAP staan de albums van je artiesten per genre gesorteerd. Iedere genre-map heeft een naam die uit precies drie letters bestaat, niet meer en niet minder. In de genre-mappen staan de albums en daarin staan de muziekbestanden. Gebruik geen submappen, plaats geen losse muziekbestanden op een ander niveau.",
            "Ziet de organisatie van jouw muziekcollectie er anders uit, pas die dan aan. Wil je dat niet, gebruik dan een ander programma.",
            "In het bestand \"adjustables.py\" (meegeleverd en staat in dezelfde map als dit programma) geef je zelf de exacte locatie op van de HOOFDMAP, achter \"pad = \". Gebruik de padnaamopmaak zoals die op jouw besturingssysteem wordt gebruikt. Let dus op of je \"\\\" of \"/\" moet gebruiken.",
            "In hetzelfde bestand \"adjustables.py\" kun je zelf beschrijvingen aan je genrenamen toevoegen. Er staan al voorbeelden in die je kunt gebruiken en/of aanpassen. Genrenamen die in de lijst staan maar niet in jouw verzameling voorkomen, staan je niet in de weg. Je kunt ze laten staan of verwijderen, wat jij wilt. Het is jouw verzameling.",
            "In dezelfde file \"adjustables.py\" maak je ook een lijst aan van je favoriete online streams, met een korte beschrijving of de ICY-NAME.",
            "Je hebt al begrepen dat het bestand \"adjustables.py\" belangrijk is voor de juiste werking van musuite. Er staan nog enkele andere variabelen in waar je beter vanaf kunt blijven, of ten minste met grote voorzichtigheid mee moet omgaan.",
            "Typ de optie van je keuze in via je toetsenbord, of gebruik de \"haakjes sluiten\" (\")\", \"]\", \"}\", \">\": vooruit) en de \"haakjes openen\" (\"(\", \"[\", \"{\", \"<\": achteruit) om er naartoe te bladeren. Druk op \"Enter\" om je keuze te bevestigen. Er is geen ondersteuning voor het gebruik van een muis of andere aanwijzerhardware in musuite. Sommige keuzelijsten ondersteunen meerdere keuzes. Voer in dat geval de keuzenummers of exacte keys (hoofdlettergevoelig) kommagescheiden achter elkaar in, voordat je op \"Enter\" drukt. Bij de genrekeuze kun je ook snel filteren op alleen de eerste letter of de eerste twee letters van meerdere genres die je tegelijk wilt selecteren.",
            "Voor het afspelen wordt het programma \"mpg123\" aangeroepen. Zorg ervoor dat het geïnstalleerd is. Voor het gebruik daarvan kun je de officiele manpages raadplegen met de opdracht \"man mpg123\" of \"vrouw mpg123\". Denk eraan dat \"mpg123\" niet alle muziekbestandstypen kan afspelen. De naam zegt genoeg.",
            "Veel luisterplezier!"
            ]
        neelijst = neelijstNL
        jalijst = jalijstNL
        neeja = neejaNL
        man = manNL
    for i in helpteksten:
        if i == helpteksten[3]:
            print(i)
        else:
            for w in textwrap.wrap(i,80):
                print(w)
        stop = input()
        if stop in backlijst:
            break
        elif stop in quitlijst:
            exit()
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
#            Status:Geordend(                                    xa
#                Schaling:Groep(                                 pa
#)   )   )   )   )
#mo hamela m haca hudaʒi haziʃaxapa
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
        wraptext = "mo hamela m haca hudaʒi haziʃaxapa. mo hame\"H\" himepu m hacadapaʒi:"
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
    elif nj in man:
        subprocess.run(["man", "mpg123"])
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

if lang == "EN":
    padtekst = "The path used as the MAIN_FOLDER for your music collection is:"
    gener = "Your music collection is being gathered, this may take a moment..."
elif lang == "IT":
    padtekst = "Il percorso utilizzato come CARTELLA_PRINCIPALE della tua raccolta musicale è:"
    gener = "Sto raccogliendo la tua collezione musicale, potrebbe richiedere un momento..."
else:
    padtekst = "Het pad dat gebruikt wordt als HOOFDMAP van je muziekcollectie is:"
    gener = "Je muziekcollectie wordt verzameld, dit kan even duren..."
for w in textwrap.wrap(padtekst,80):
    print(w)
print(pad)
print()
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
        mosdict = {
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#        "MP3"(                                                  "MP3"
#)   )   )
#WTI:BNW(                                                        ho
#    Connectie:Binnen(                                           ŋüi
#        Schaling:Meervoud(                                      po
#            wti:PV:2(                                           hea
#)   )   )   )
#huwa"MP3" hoŋüipohea
                "M":"huwa\"MP3\" hoŋüipohea",
#WTI:ZNW(                                                        hu
#    Activiteit:Beweging(                                        ʃe
#)   )
#WTI:BNW(                                                        ho
#    Afstand:Hier(                                               ʒi
#        Waarheid:Onwaar(                                        li
#)   )   )   
#huʃe hoʒili
                "S":"huʃe hoʒili"
                }
        zosdict = {
#WTI:WW(                                                         ha
#    zti:Keuze(                                                  me
#        Schaling:Groep(                                         pa
#            Connectie:Bijbehorend(                              ŋe
#)   )   )   )
#hamepaŋe
                "m":"hamepaŋe",
#WTI:WW(                                                         ha
#    Registratie:Zien(                                           ca
#        Progressie:Vooruitgang(                                 za
#            Status:Geordend(                                    xa
#)   )   )   )
#hacazaxa
                "c":"hacazaxa"
                }
        gmtdict = {
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Status:Gelijkmatig(                                     xi
#)   )   )
#hupaxi
                "G":"hupaxi",
#WTI:ZNW(                                                        hu
#    Schaling:Groep(                                             pa
#        Connectie:Samen(                                        ŋa
#)   )   )
#hupaŋa
                "M":"hupaŋa",
#WTI:ZNW(                                                        hu
#    Materie:Iets(                                               wa
#         Registratie:Horen(                                     co
#             Status:Geordend(                                   xa
#)   )   )   )
#huwacoxa
                "T":"huwacoxa"
                }
        man = manCJ
#ZTI:Vraag(                                                      mi
#)
#WTI:BW(                                                         hi
#    Status:Rommelig(                                            xüe
#)   )
#mi hixüe
        willekeurig = "mi hixüe"
#ZTI:Zin(                                                        ma
#)
#WTI:WW(                                                         ha
#    Progressie:Start(                                           ze
#        Activiteit:Beweging(                                    ʃe
#            "mpg123"(                                           "mpg123"
#)   )   )   )
#ma hazeʃe"mpg123"
        mpg123 = "ma hazeʃe\"mpg123\"\n"
    elif lang == "EN":
        hoofdmenu = " - - MAIN MENU - -"
        mosdict = {
                "M":"MP3 file(s) from own collection",
                "S":"online Stream"
                }
        zosdict = {
                "F":"Find by search term",
                "S":"Scroll"
                }
        gmtdict = {
                "G":"Genre, Style, Category",
                "F":"Folder, Album, Collection",
                "T":"Track, Song, Opus"
                }
        man = manEN
        willekeurig = "Random order?"
        mpg123 = "Starting playback with mpg123\n"
    elif lang == "IT":
        hoofdmenu = " - - MENU PRINCIPALE - -"
        mosdict = {
                "M":"File MP3 dalla collezione personale",
                "S":"Streaming online"
                }
        zosdict = {
                "C":"Cercare per termine di ricerca",
                "S":"Sfoglia"
                }
        gmtdict = {
                "G":"Genere, Stile, Categoria",
                "C":"Cartella, Album, Collezione",
                "T":"Traccia, Canzone, Numero"
                }
        man = manIT
        willekeurig = "Ordine casuale?"
        mpg123 = "Avvio della riproduzione con mpg123\n"
    else:
        hoofdmenu = " - - HOOFDMENU - -"
        mosdict = {
                "M":"MP3-bestand(en) uit eigen collectie",
                "S":"online Stream"
                }
        zosdict = {
                "Z":"Zoeken op zoekterm",
                "S":"Scrollen"
                }
        gmtdict = {
                "G":"Genre, Stijl, Categorie",
                "M":"Map, Album, Verzameling",
                "T":"Track, Lied, Opus"
                }
        man = manNL
        willekeurig = "Willekeurige volgorde?"
        mpg123 = "Start afspelen met mpg123\n"
    moslijst = []
    for i in mosdict:
        moslijst.append(i.lower())
    zoslijst = []
    for i in zosdict:
        zoslijst.append(i.lower())
    gmtlijst = []
    for i in gmtdict:
        gmtlijst.append(i.lower())
    print()
    print(hoofdmenu)
    v,k = cFD([mosdict,0,"M","> ",langlijst+helplijst+man+moslijst+backlijst+quitlijst])
    if k.upper() in quitlijst:
        exit()
    elif k.upper() in backlijst:
        pass
    elif k in man:
        subprocess.run(["man", "mpg123"])
    elif k in helplijst:
        hellup()
    elif k in langlijst:
        lang = setlang(lang)
    elif k.upper() == moslijst[1].upper():
        loopS = True
        while loopS == True:
            s,index = cFNL([streamslijst,"A",1,1,"> ",helplijst+man+backlijst+quitlijst])
            if s in quitlijst:
                exit()
            elif s in backlijst:
                break
            elif s in man:
                subprocess.run(["man", "mpg123"])
            elif s in helplijst:
                hellup()
            else:
                su = streamsdict[s]
                print(mpg123)
                subprocess.run(["mpg123", "-vm",  su])
    else:
        loopM = True
        while loopM == True:
            v,k = cFD([gmtdict,0,"G","> ",helplijst+man+gmtlijst+backlijst+quitlijst])
            if k.upper() in quitlijst:
                exit()
            elif k.upper() in backlijst:
                break
            elif k in man:
                subprocess.run(["man", "mpg123"])
            elif k in helplijst:
                hellup()
            elif k.upper() == gmtlijst[2].upper():
                loopMT = True
                while loopMT == True:
                    tracklijstkort = []
                    tracklijst = []
                    if lang == "EN":
                        zoekterm = input("Enter a search term (no exit command like \"Q\"):\n")
                    elif lang == "IT":
                        zoekterm = input("Inserisci un termine di ricerca (nessun comando di uscita come \"Q\"):\n")
                    else:
                        zoekterm = input("Voer een zoekterm in (geen afsluitopdracht zoals \"Q\"):\n")
                    if zoekterm in quitlijst:
                        exit()
                    elif zoekterm in backlijst:
                        break
                    elif zoekterm in man:
                        subprocess.run(["man", "mpg123"])
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
                            if lang == "EN":
                                wraptext = "Your search did not return any results. Remember that the search is case-sensitive."
                            elif lang == "IT":
                                wraptext = "La tua ricerca non ha restituito risultati. Ricorda che la ricerca distingue tra maiuscole e minuscole."
                            else:
                                wraptext = "Je zoekopdracht leverde geen resultaten op. Denk eraan dat de zoekopdracht hoofdlettergevoelig is."
                            for i in textwrap.wrap(wraptext,80):
                                print(i)
                            print()
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
                            elif tracksel in man:
                                subprocess.run(["man", "mpg123"])
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
                    if lang == "EN":
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
                    elif k in man:
                        subprocess.run(["man", "mpg123"])
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
                                if lang == "EN":
                                    zoekterm = input("Enter a search term (no exit command like \"Q\"):\n")
                                elif lang == "IT":
                                    zoekterm = input("Inserisci un termine di ricerca (nessun comando di uscita come \"Q\"):\n")
                                else:
                                    zoekterm = input("Voer een zoekterm in (geen afsluitopdracht zoals \"Q\"):\n")
                                if zoekterm in quitlijst:
                                    exit()
                                elif zoekterm in backlijst:
                                    break
                                elif zoekterm in man:
                                    subprocess.run(["man", "mpg123"])
                                else:
                                    for dirpath, dirnames, filenames in os.walk(pad):
                                        for mapp in dirnames:
                                            if zoekterm in mapp:
                                                mappenlijst.append(mapp)
                                                mappenlijstkort.append(mapp)
                                    mappenlijstkort = sorted(mappenlijstkort)
                                    if len(mappenlijstkort) < 1:
                                        print()
                                        if lang == "EN":
                                            wraptext = "Your search did not return any results. Remember that the search is case-sensitive."
                                        elif lang == "IT":
                                            wraptext = "La tua ricerca non ha prodotto risultati. Ricorda che la ricerca distingue tra maiuscole e minuscole."
                                        else:
                                            wraptext = "Je zoekopdracht leverde geen resultaten op. Denk eraan dat de zoekopdracht hoofdlettergevoelig is."
                                        for i in textwrap.wrap(wraptext,80):
                                            print(i)
                                        print()
                                    else:
                                        mappenlijstverkort = printmappenlijstmetsel(mappenlijstkort)
                                        lenml = len(str(len(mappenlijstverkort)))
                                        mappenlijstnogkorter = []
                                        for mapp in mappenlijstverkort:
                                            if len(mapp) > 80-3-maxlen-lenml:
                                                mappenlijstnogkorter.append(mapp[:40-maxlen-lenml]+"**"+mapp[len(mapp)-36:])
                                            else:
                                                mappenlijstnogkorter.append(mapp)
                                        mappsel,index = cFNL([mappenlijstnogkorter,"A",1,1,"> ",True,optieslijst+helplijst+man+backlijst+quitlijst])
                                        print("mappsel = ",mappsel)
                                        if mappsel in quitlijst:
                                            exit()
                                        elif mappsel in backlijst:
                                            break
                                        elif mappsel in man:
                                            subprocess.run(["man", "mpg123"])
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
                                for m in os.listdir(gpad):
                                    if os.path.isdir(os.path.join(gpad,m)):
                                        mpad = os.path.join(gpad,m)
                                        mappenlijst.append(mpad)
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
                                elif mappsel in man:
                                    subprocess.run(["man", "mpg123"])
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
                    elif optie in man:
                        subprocess.run(["man", "mpg123"])
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
