import requests
import time
from random import randint
import re

#Test1

name = 'SenatorThomTillis'
url  = 'https://www.facebook.com/' + name

r = requests.get(url)

pg_content = str(r.content)
look_up_word1 = '<title id="pageTitle">'

a = pg_content.split(look_up_word1)
b = a[-1].split(" -")

pol_fb_page_name = b[0]

#test2

url = 'https://www.facebook.com/repschrader'
url2 = 'https://www.facebook.com/SenatorThomTillis'
url3 = 'https://www.facebook.com/RepSewell'
url4 = 'https://www.facebook.com/SenatorRandPaul'

r = requests.get(url4)

if r.status_code == 200:
    pg_content = str(r.content)
    look_up_word = 'og:title" content="', 

    a = pg_content.split(look_up_word)
    b = a[-1].split('')

    pol_fb_page_name = b[0]

    print(pol_fb_page_name)


#https://developers.facebook.com/docs/pages/searching/

test_url = "https://graph.facebook.com/pages/search?q=SenatorThomTillis&fields=id,name,location,link&access_token=EAADqFZC76BDMBAKP4bH4gzbN37Eltae8mSRZC2mbJeAtMyFBEi58x6UMRZCBCJ8bAbCryoat10ss2FdQfWRWMeKk4l9ZA94Eg7c7GdxbljeByFKU7hZC8tNInIlaliiJ0MhCuU3wGJeQ9uzPboaIXARWXQQDwWcso3CqDjJc3OB4KmFw7i0GRnx7FzrkRHPmGBO0RVuZC7zZCydeM6zenwZAhfZBBukqIytAZD"

requests.get(test_url) 



list_of_pol_pgnames = ['SenatorThomTillis', 'USCongressmanFilemonVela', 'reppaultonko', 'DonaldNorcrossNJ', '153423912663', 'repalgreen', 'RepDonBeyer', 'RepRogerWilliams', 'CongressmanSethMoulton', 'replizcheney', 'RepRoybalAllard', 'mitchmcconnell', 'SenatorRandPaul', 'RepSteveScalise', 'RepMoBrooks', 'CongressmanAlexMooney', 'RepJackBergman', 'RepWesterman', 'RepMcEachin', 'CongresswomanAnnieKuster', 'RepFrankLucas', 'CongressmanTedDeutch', 'GwenSMoore', 'RepTedLieu', 'RepGregMurphy', 'senatordebfischer', 'RepBobGibbs', 'AndyHarrisMD', 'WhipHoyer', 'CongressmanMichaelF.Q.SanNicolas', 'congressmangkbutterfield', 'SenatorTimScott', 'RepJohnCurtis', 'CongressmanNadler', '50375006903', 'RepBarbaraLee', 'jeffmerkley', 'JoeManchinIII', 'RepBost', 'CongressmanBuchanan', 'RepJeffDuncan', 'Congressman.Keating', 'RepSewell', 'RepRickCrawford', 'RepChrisStewart', 'zoelofgren', 'CongressmanWarrenDavidson', 'drnealdunnfl2', 'RepTomSuozzi', 'SenatorLankford', 'RepCheri', 'RepKinzinger', 'marshablackburn', 'SenBrianSchatz', 'RepDonBacon', 'SenatorHassan', 'senshelley', 'senatorcantwell', 'BlaineLuetkemeyer', '113303673339', 'RepJohnLarson', 'senatortester', 'RepRouzer', 'RobertAderholt', 'reptrey', 'jameseclyburn', 'RepRichHudson', 'RickScottSenOffice', 'SenGaryPeters', 'repschrader', 'RepKweisiMfume', 'CongressmanSteveCohen', 'senatortammybaldwin', 'RepAdamSchiff', 'RepBobbyScott', 'RepEliseStefanik', 'senatorelizabethwarren', 'CongressmanMattCartwright', 'RepAmiBera', 'CongressmanKevinMcCarthy', 'RepAnthonyBrown', 'repgaramendi', 'CongressmanDavidCicilline', 'RepJimBanks', 'JodeyArrington', 'repgracemeng', 'bill.posey15', 'senatorchriscoons', 'RepTedBudd', 'RepBrianHiggins', 'RepMarkTakano', 'CongressmanBennieGThompson', 'emanuelcleaverii', 'RepMarkDeSaulnier', 'RepHuffman', 'SenatorTomCotton', 'repscottperry', 'RepresentativeValDemings', 'senatorjimrisch', 'ScottDesJarlaisTN04', 'RepLarryBucshon', 'repchuck', 'RepWalberg', 'senbennetco', 'RepLoisFrankel', 'reptomrice', 'CongressmanClayHiggins', 'SenatorJohnHoeven', 'RepBonnie', 'RepHuizenga', 'CongressmanMikeDRogers', 'RepJoyceBeatty', 'SenatorSasse', 'CongressmanMarcVeasey', 'DianaDeGette', 'chrismurphyct', 'gregorymeeksny05', 'CongressmanDKDavis', 'CongresswomanRosaDeLauro', 'senatorbencardin', 'SenatorMikeRounds', 'RepAustinScott', 'mcmorrisrodgers', '152569121550', 'RepJuliaBrownley', 'USSenTinaSmith', 'repmarkpocan', 'timryan', 'herrerabeutler', 'sen.johncornyn', 'repstephenlynch', 'RepJoshG', 'RepJuanVargas', 'CongressmanGuthrie', 'repfrankpallone', '81058818750', 'tomcarper', 'repgosar', 'senjoniernst', 'CongressmanBillFoster', 'repcardenas', 'SenatorKaine', 'RepJimMcGovern', 'RepConorLamb', 'RepAdamSmith', 'RepDavidKustoff', 'RepDebbieLesko', 'RepKathleenRice', 'johnbarrasso', 'SenJackReed', 'RepJimmyPanetta', 'RepSteveChabot', 'reprobinkelly', 'pascrell', 'CongressmanKevinCramer', 'CongressmanGarretGraves', 'JohnKennedyLouisiana', 'senatorfeinstein', 'RepMullin', 'RepRubenGallego', 'RepScottPeters', 'joecourtney', 'RepSmucker', 'TomColeOK04', 'CongresswomanLindaSanchez', 'CongressmanDougLamborn', 'RepMikeJohnson', 'SenatorRichardBurr', 'repbrianmast', 'repjimjordan', 'RepMikeTurner', 'DonaldPayneJr', 'SenatorPatrickLeahy', 'RepTomReed', 'CongressmanBoyle', 'SenatorCortezMasto', 'ChelliePingree', 'RepRoKhanna', 'senatormikelee', 'CongressmanHalRogers', 'SenatorMarcoRubio', 'jerrymoran', 'chrisvanhollen', 'RepDelBene', 'CongressmanJimHimes', 'RepRobWittman', 'CongressmanRickAllen', 'jiminhofe', 'RepEspaillat', 'RepDebbieDingell', 'RepBradWenstrup', 'RepKarenBass', 'TXRandy14', 'RepFredUpton', 'SenatorTedCruz', 'RepresentativeMarcyKaptur', 'RepMikeGallagher', 'RepDonYoung', '395759603917487', 'susancollins', 'RepBillJohnson', '118514606128', 'RepRonEstes', 'RepSeanMaloney', 'RepMcKinley', 'SenatorAngusSKingJr', 'senronjohnson', 'repdavidschweikert', 'RepMikeThompson', 'RepMoolenaar', 'RepAndyBiggs', 'RepStephMurphy', 'sanfordbishop', 'RepSarbanes', 'CongressmanGaryPalmer', 'RepSteveWomack', 'RepLeeZeldin', 'RepDanKildee', 'JoeWilson', '81125319109', 'congressmancomer', '96007744606', 'GusBilirakis', '115356957005', 'RepDwightEvans', 'RepPerlmutter', 'RepJackieWalorski', 'CongressmanBradSchneider', 'CongressmanFredKeller', 'aumuaamata', 'CongressmanJodyHice', 'reprichardneal', 'replahood', 'SenatorDurbin', 'RepGrothman', 'RepLouCorrea', 'SenatorWhitehouse', 'RepLaMalfa', 'CongressmanMcHenry', 'RepVirginiaFoxx', 'CongressmanGerryConnolly', 'SenDanSullivan', 'RepAndyBarr', 'repbrianfitzpatrick', 'mdiazbalart', 'SenatorBlunt', 'CongresswomanTitus', 'stevenpalazzo', 'USSenatorLindseyGraham', 'RepDrewFerguson', 'mikecrapo', 'SenatorStabenow', 'DutchRupp', 'lloyddoggett', 'CongressmanEricSwalwell', 'judgecarter', 'RepJimCosta', 'RepAnnaEshoo', 'RepJackyRosen', 'CongressmanRaulRuizMD', 'senatorhirono', 'RepThomasMassie', 'congresswomanbonamici', 'SenLisaMurkowski', 'RepWilson', 'RepNormaTorres', 'RepJohnKatko', 'RepGraceNapolitano', 'JohnBoozman', 'RepHakeemJeffries', 'RepJudyChu', 'RepDaveJoyce', 'MartinHeinrich', '191056827594903', 'reploudermilk', 'CongressmanMattGaetz', 'jefffortenberry', 'RepRickLarsen', 'SenBlumenthal', 'RepAnnWagner', 'michaeltmccaul', 'RepRodneyDavis', 'RichardShelby', 'RepChrisSmith', 'doris.matsui', 'RepRutherfordFL', 'repsaludcarbajal', 'PeterWelch', 'CongressmanAndreCarson', 'NancyPelosi', 'SenDuckworth', 'CongressmanGT', 'congressmanraja', 'CongresswomanNorton', 'senatormenendez', 'JimCooper', 'MaxineWaters', 'SteveDainesMT', 'USCongressmanVicenteGonzalez', 'RepCarolynMaloney', 'CongressmanDarrenSoto', 'senschumer', 'repstaceyplaskett', 'CongresswomanAdams', 'Rep.Billy.Long', 'congressmanbuddycarter', 'SenatorShaheen', 'USRepKathyCastor', 'boblatta', 'CongresswomanSinema', 'RepJennifferGonzalezColon', 'repbettymccollum', 'repyvettedclarke', 'RepCharlieCrist', 'usrepmikedoyle', 'senatortoomey', 'RepJayapal', '326420614138023', 'RepLowenthal', 'SenatorSherrodBrown', 'jerrymcnerney', 'repjasonsmith', 'CongresswomanEBJtx30', 'CongresswomanSheilaJacksonLee', '70063393423', '63158229861', 'RepWebster', '214258646163', 'JackieSpeier', 'kevinbrady', 'senrobportman', 'Rep.BluntRochester', 'RepBrianBabin', 'repraskin', 'reptomemmer', 'repdanbishop', 'repmikequigley', 'MarkRWarner', 'EdJMarkey', 'senatorsanders', 'repohalleran', 'grassley', 'RepRalphNorman', 'RepDWS', 'RepMorganGriffith', 'MarkAmodeiNV2', 'RepJimmyGomez', 'Rep.Grijalva', 'repronkind', 'janschakowsky', 'SenKirstenGillibrand', 'repkenbuck', 'reppeteaguilar', 'RepDavidEPrice', 'SenatorToddYoung', 'CongressmanJimLangevin', 'RepFrenchHill', 'CongresswomanClark', 'SenatorBobCasey', 'Congresswoman.Hartzler', 'derek.kilmer', 'reptrentkelly', 'SenMarkKelly', 'congressmanbobbyrush', 'CongresswomanBarragan', 'RepKayGranger', 'michaelcburgess', 'RepPeterDeFazio', 'SenatorWicker', 'RepMikeGarcia', 'RepAlLawsonJr', 'RepNewhouse', '8037068318']

set_of_pol_pgnames = {'SenatorThomTillis', 'USCongressmanFilemonVela', 'reppaultonko', 'DonaldNorcrossNJ', '153423912663', 'repalgreen', 'RepDonBeyer', 'RepRogerWilliams', 'CongressmanSethMoulton', 'replizcheney', 'RepRoybalAllard', 'mitchmcconnell', 'SenatorRandPaul', 'RepSteveScalise', 'RepMoBrooks', 'CongressmanAlexMooney', 'RepJackBergman', 'RepWesterman', 'RepMcEachin', 'CongresswomanAnnieKuster', 'RepFrankLucas', 'CongressmanTedDeutch', 'GwenSMoore', 'RepTedLieu', 'RepGregMurphy', 'senatordebfischer', 'RepBobGibbs', 'AndyHarrisMD', 'WhipHoyer', 'CongressmanMichaelF.Q.SanNicolas', 'congressmangkbutterfield', 'SenatorTimScott', 'RepJohnCurtis', 'CongressmanNadler', '50375006903', 'RepBarbaraLee', 'jeffmerkley', 'JoeManchinIII', 'RepBost', 'CongressmanBuchanan', 'RepJeffDuncan', 'Congressman.Keating', 'RepSewell', 'RepRickCrawford', 'RepChrisStewart', 'zoelofgren', 'CongressmanWarrenDavidson', 'drnealdunnfl2', 'RepTomSuozzi', 'SenatorLankford', 'RepCheri', 'RepKinzinger', 'marshablackburn', 'SenBrianSchatz', 'RepDonBacon', 'SenatorHassan', 'senshelley', 'senatorcantwell', 'BlaineLuetkemeyer', '113303673339', 'RepJohnLarson', 'senatortester', 'RepRouzer', 'RobertAderholt', 'reptrey', 'jameseclyburn', 'RepRichHudson', 'RickScottSenOffice', 'SenGaryPeters', 'repschrader', 'RepKweisiMfume', 'CongressmanSteveCohen', 'senatortammybaldwin', 'RepAdamSchiff', 'RepBobbyScott', 'RepEliseStefanik', 'senatorelizabethwarren', 'CongressmanMattCartwright', 'RepAmiBera', 'CongressmanKevinMcCarthy', 'RepAnthonyBrown', 'repgaramendi', 'CongressmanDavidCicilline', 'RepJimBanks', 'JodeyArrington', 'repgracemeng', 'bill.posey15', 'senatorchriscoons', 'RepTedBudd', 'RepBrianHiggins', 'RepMarkTakano', 'CongressmanBennieGThompson', 'emanuelcleaverii', 'RepMarkDeSaulnier', 'RepHuffman', 'SenatorTomCotton', 'repscottperry', 'RepresentativeValDemings', 'senatorjimrisch', 'ScottDesJarlaisTN04', 'RepLarryBucshon', 'repchuck', 'RepWalberg', 'senbennetco', 'RepLoisFrankel', 'reptomrice', 'CongressmanClayHiggins', 'SenatorJohnHoeven', 'RepBonnie', 'RepHuizenga', 'CongressmanMikeDRogers', 'RepJoyceBeatty', 'SenatorSasse', 'CongressmanMarcVeasey', 'DianaDeGette', 'chrismurphyct', 'gregorymeeksny05', 'CongressmanDKDavis', 'CongresswomanRosaDeLauro', 'senatorbencardin', 'SenatorMikeRounds', 'RepAustinScott', 'mcmorrisrodgers', '152569121550', 'RepJuliaBrownley', 'USSenTinaSmith', 'repmarkpocan', 'timryan', 'herrerabeutler', 'sen.johncornyn', 'repstephenlynch', 'RepJoshG', 'RepJuanVargas', 'CongressmanGuthrie', 'repfrankpallone', '81058818750', 'tomcarper', 'repgosar', 'senjoniernst', 'CongressmanBillFoster', 'repcardenas', 'SenatorKaine', 'RepJimMcGovern', 'RepConorLamb', 'RepAdamSmith', 'RepDavidKustoff', 'RepDebbieLesko', 'RepKathleenRice', 'johnbarrasso', 'SenJackReed', 'RepJimmyPanetta', 'RepSteveChabot', 'reprobinkelly', 'pascrell', 'CongressmanKevinCramer', 'CongressmanGarretGraves', 'JohnKennedyLouisiana', 'senatorfeinstein', 'RepMullin', 'RepRubenGallego', 'RepScottPeters', 'joecourtney', 'RepSmucker', 'TomColeOK04', 'CongresswomanLindaSanchez', 'CongressmanDougLamborn', 'RepMikeJohnson', 'SenatorRichardBurr', 'repbrianmast', 'repjimjordan', 'RepMikeTurner', 'DonaldPayneJr', 'SenatorPatrickLeahy', 'RepTomReed', 'CongressmanBoyle', 'SenatorCortezMasto', 'ChelliePingree', 'RepRoKhanna', 'senatormikelee', 'CongressmanHalRogers', 'SenatorMarcoRubio', 'jerrymoran', 'chrisvanhollen', 'RepDelBene', 'CongressmanJimHimes', 'RepRobWittman', 'CongressmanRickAllen', 'jiminhofe', 'RepEspaillat', 'RepDebbieDingell', 'RepBradWenstrup', 'RepKarenBass', 'TXRandy14', 'RepFredUpton', 'SenatorTedCruz', 'RepresentativeMarcyKaptur', 'RepMikeGallagher', 'RepDonYoung', '395759603917487', 'susancollins', 'RepBillJohnson', '118514606128', 'RepRonEstes', 'RepSeanMaloney', 'RepMcKinley', 'SenatorAngusSKingJr', 'senronjohnson', 'repdavidschweikert', 'RepMikeThompson', 'RepMoolenaar', 'RepAndyBiggs', 'RepStephMurphy', 'sanfordbishop', 'RepSarbanes', 'CongressmanGaryPalmer', 'RepSteveWomack', 'RepLeeZeldin', 'RepDanKildee', 'JoeWilson', '81125319109', 'congressmancomer', '96007744606', 'GusBilirakis', '115356957005', 'RepDwightEvans', 'RepPerlmutter', 'RepJackieWalorski', 'CongressmanBradSchneider', 'CongressmanFredKeller', 'aumuaamata', 'CongressmanJodyHice', 'reprichardneal', 'replahood', 'SenatorDurbin', 'RepGrothman', 'RepLouCorrea', 'SenatorWhitehouse', 'RepLaMalfa', 'CongressmanMcHenry', 'RepVirginiaFoxx', 'CongressmanGerryConnolly', 'SenDanSullivan', 'RepAndyBarr', 'repbrianfitzpatrick', 'mdiazbalart', 'SenatorBlunt', 'CongresswomanTitus', 'stevenpalazzo', 'USSenatorLindseyGraham', 'RepDrewFerguson', 'mikecrapo', 'SenatorStabenow', 'DutchRupp', 'lloyddoggett', 'CongressmanEricSwalwell', 'judgecarter', 'RepJimCosta', 'RepAnnaEshoo', 'RepJackyRosen', 'CongressmanRaulRuizMD', 'senatorhirono', 'RepThomasMassie', 'congresswomanbonamici', 'SenLisaMurkowski', 'RepWilson', 'RepNormaTorres', 'RepJohnKatko', 'RepGraceNapolitano', 'JohnBoozman', 'RepHakeemJeffries', 'RepJudyChu', 'RepDaveJoyce', 'MartinHeinrich', '191056827594903', 'reploudermilk', 'CongressmanMattGaetz', 'jefffortenberry', 'RepRickLarsen', 'SenBlumenthal', 'RepAnnWagner', 'michaeltmccaul', 'RepRodneyDavis', 'RichardShelby', 'RepChrisSmith', 'doris.matsui', 'RepRutherfordFL', 'repsaludcarbajal', 'PeterWelch', 'CongressmanAndreCarson', 'NancyPelosi', 'SenDuckworth', 'CongressmanGT', 'congressmanraja', 'CongresswomanNorton', 'senatormenendez', 'JimCooper', 'MaxineWaters', 'SteveDainesMT', 'USCongressmanVicenteGonzalez', 'RepCarolynMaloney', 'CongressmanDarrenSoto', 'senschumer', 'repstaceyplaskett', 'CongresswomanAdams', 'Rep.Billy.Long', 'congressmanbuddycarter', 'SenatorShaheen', 'USRepKathyCastor', 'boblatta', 'CongresswomanSinema', 'RepJennifferGonzalezColon', 'repbettymccollum', 'repyvettedclarke', 'RepCharlieCrist', 'usrepmikedoyle', 'senatortoomey', 'RepJayapal', '326420614138023', 'RepLowenthal', 'SenatorSherrodBrown', 'jerrymcnerney', 'repjasonsmith', 'CongresswomanEBJtx30', 'CongresswomanSheilaJacksonLee', '70063393423', '63158229861', 'RepWebster', '214258646163', 'JackieSpeier', 'kevinbrady', 'senrobportman', 'Rep.BluntRochester', 'RepBrianBabin', 'repraskin', 'reptomemmer', 'repdanbishop', 'repmikequigley', 'MarkRWarner', 'EdJMarkey', 'senatorsanders', 'repohalleran', 'grassley', 'RepRalphNorman', 'RepDWS', 'RepMorganGriffith', 'MarkAmodeiNV2', 'RepJimmyGomez', 'Rep.Grijalva', 'repronkind', 'janschakowsky', 'SenKirstenGillibrand', 'repkenbuck', 'reppeteaguilar', 'RepDavidEPrice', 'SenatorToddYoung', 'CongressmanJimLangevin', 'RepFrenchHill', 'CongresswomanClark', 'SenatorBobCasey', 'Congresswoman.Hartzler', 'derek.kilmer', 'reptrentkelly', 'SenMarkKelly', 'congressmanbobbyrush', 'CongresswomanBarragan', 'RepKayGranger', 'michaelcburgess', 'RepPeterDeFazio', 'SenatorWicker', 'RepMikeGarcia', 'RepAlLawsonJr', 'RepNewhouse', '8037068318'}

polnames_already_fetched = {'Senator Thom Tillis', 'Congressman Filemon Vela', 'Paul D. Tonko', 'Donald Norcross', 'Gregorio Kilili Camacho Sablan', 'Rep. Al Green', 'Congressman Don Beyer', 'Roger Williams', 'Congressman Seth Moulton','Rep. Liz Cheney', 'Gwen S. Moore'}


new = set_of_pol_pgnames.difference(polnames_already_fetched)


#THE LOOP!

list_pol_fbpages = []
list_of_failed_request = []
fb_pop_up_blocked = []
nb_failed_requests = 0
nb_popup_blocked = 0

for politician in list_of_pol_pgnames:
    
    request  = 'https://www.facebook.com/' + politician
    
    #priting request just to ensure
    #print(request)

    r = requests.get(request)
    
    if r.status_code == 200:
        
        pg_content = str(r.content)

        look_up_word ='og:title" content="'

        a = pg_content.split(look_up_word)
        name_split = re.split('"', a[-1], maxsplit=1)
        
        pol_fb_page_name = name_split[0]

        if (pol_fb_page_name == "b'<!DOCTYPE html>\n<html lang=") | (pol_fb_page_name == "Log p&#xe5;, eller opret en profil for at se indholdet"):
            fb_pop_up_blocked.append(politician)
            nb_popup_blocked += 1
        else:
            list_pol_fbpages.append(pol_fb_page_name)

        #printing it as well as a safety if shit goes south as crashes.
        print(pol_fb_page_name)

        #Figure out how long sleep should be to not get "siden findes ikke / page not found"
        #don't think 30 secs will be sufficient however...
        time.sleep(randint(2,6))
    else:
        list_of_failed_request.append(politician)
        nb_failed_requests += 1

list_pol_fbpages

#Results fetched so far
set_of_polnames_already_fetched = {'Senator Thom Tillis', 'Congressman Filemon Vela', 'Paul D. Tonko', 'Donald Norcross', 'Gregorio Kilili Camacho Sablan', 'Rep. Al Green', 'Congressman Don Beyer', 'Roger Williams', 'Congressman Seth Moulton','Rep. Liz Cheney', 'Gwen S. Moore'}

#To create new list to fetch


