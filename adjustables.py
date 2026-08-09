# Insert the path to the base folder that contains the folders of your organised
# music collection
pad = "/home/media/Samsung/maestraccio/Muziek/mp3/"
# Your organised music collection should contain only three-letter folder names.
# Add a description of the contents that somehow match the three letters. 
genredict = {
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
# Add URLs of your favourite online streaming services.
streamsdict = {
        "RDS Relax":"https://icstream.rds.radio/rdsrelax",
        "Radio Monte Carlo":"http://edge.radiomontecarlo.net/RMC.mp3",
        "Radio Kiss Kiss":"https://kisskiss.fluidstream.eu/KissKiss.mp3",
        "Sublime FM":"https://22663.live.streamtheworld.com/SUBLIME.mp3",
        "Smooth Jazz":"http://smoothjazz.cdnstream1.com/2585_320.mp3",
        "* - 1000 Italohits":"https://1000italohits.stream.laut.fm/1000italohits",
        "1000 Smoothhits":"https://1000smoothhits.stream.laut.fm/1000smoothhits",
        "* - 54 Funk Soul Dance":"https://54-funk-soul-dance.stream.laut.fm/54-funk-soul-dance",
        "Blues":"https://blues.stream.laut.fm/blues",
        "Bluesrock":"https://bluesrock.stream.laut.fm/bluesrock",
        "* - Chillout Area":"https://chillout-area.stream.laut.fm/chillout-area",
        "* - Chill Out Zone":"https://chilloutzone.stream.laut.fm/chilloutzone",
        "Disco":"https://disco.stream.laut.fm/disco",
        "Electrolounge":"https://electrolounge.stream.laut.fm/electrolounge",
        "* - Funk":"https://funk.stream.laut.fm/funk",
        "Funk2Disco":"https://funk2disco.stream.laut.fm/funk2disco",
        "Italia 1":"https://italia1.stream.laut.fm/italia1",
        "Italo-Disco":"https://italo-disco.stream.laut.fm/italo-disco",
        "Italy Music":"https://italymusic.stream.laut.fm/italymusic",
        "Jazz":"https://jazz.stream.laut.fm/jazz",
        "* - Jazzloft":"https://jazzloft.stream.laut.fm/jazzloft",
        "Jazzrockfusion":"https://jazzrockfusion.stream.laut.fm/jazzrockfusion",
        "Just Jazz":"https://justjazz.stream.laut.fm/justjazz",
        "Lounge-Radio":"https://loungeradio.stream.laut.fm/loungeradio",
        "Radiodigitalia Ricordi":"https://radiodigitalia-ricordi.stream.laut.fm/radiodigitalia-ricordi",
        "Salsa":"https://salsa.stream.laut.fm/salsa",
        "Smooth Jazz":"https://smooth-jazz.stream.laut.fm/smooth-jazz",
        "Soul":"https://soul.stream.laut.fm/soul",
        "Soulfood":"https://soulfood.stream.laut.fm/soulfood",
        "Soulradioclassics":"https://soulradioclassics.stream.laut.fm/soulradioclassics",
        "The Bugcast":"http://stream.otherside.network:8904/listen.mp3"
        }
# Here, the language is set. The best way is to set this with  the setlang
# function in the program. Valid options are currently "NL", "EN" and "IT".
lang = "EN"
# Set to "N" if you don't want to see the language selection  at startup, or to
# "Y" if you do This is also done from the setlang function in the program
picklang = "Y"
# Set to "N" if you don't want to see the help at startup, or to "Y" if you do
# This is also done from the showhelp function in the program
showhelp = "Y"
