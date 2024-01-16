print('Labdien, esat sveicināti programmā, kura tika veidota priekš slinkā astrologa.')
arhivs = input('Vai Jums ir nepieciešams prognožu arhīvs novembrim?')
if arhivs == 'ja':
    kursh=input('Kādu horoskopu vēlaties apskatīt?: ')
while True:
    if arhivs == 'ja':
        kursh = capitalize(kursh=input('Kādu horoskopu vēlaties apskatīt?: '))
        
        horoskopi={
                'Auns':'Nelūkojoties apkārt un nenovirzoties no ceļa, profesionālajā aktivitātē izvēlies vienu svarīgāko mērķi un ej uz to. Aunam cilvēkiem būs labas izredzes mīlas attiecībās. Nelutini sevi ar atlaidēm un cīnies ar slinkumu.',
                'Vērsis':'Gadam ejot, lietas risināsies uz labo pusi. Ģimenes dzīve būs patīkama visa gada garumā, karjerā būs ievērojama izaugsme. Jums jābūt gatavam veikt nepieciešamās izmaiņas savā rutīnā un aptveriet jaunās atveres',
                'Dvīņi':'Jūs varat sagaidīt ģimenes paplašināšanos, pievienojot jaunus dalībniekus. Laulības dzīve būs svētlaimīga, un bērni mācībās būs izcili. Relaksācijas paņēmieni piemēram, joga un meditācija uzlabos jūsu emocionālo veselību.',
                'Vēzis':'Nebaidoties no publikas, iegūsiet apņēmību uzstāties. Uzsvars jāliek uz personīgo attīstību, un būs jāpieliek daudz domāšanas un pūļu. Jums būs jāiztur grūtības, kas radušās gada sākumā, un ar nepacietību jāgaida gads progresu un labklājību.',
                'Lauva':'Ļaujot savām izpausmēm vaļu, vari sastrādāt nedarbus, kurus vēlāk gauži nožēlosi. Profesionālajā sfērā izcelties ar lieliskām diplomāta manierēm būs pagrūti, tāpēc, svarīgo jautājumu risināšanai, deleģē kādu citu darbinieku. Finanšu jautājumus novembrī labāk neapspriest, un šī būs tava vājā vieta visa mēneša garumā.',
                'Jaunava':'Balstoties uz vēlmēm un iegribām, visu, kas skar naudas lietas, rūpīgi pārdomā un nepieņem galīgos lēmumus. Pārgrupējies un centies izdabūt iespējamo labumu no radušās situācijas, kā arī darbojies mierīgi, bez spriedzes un radušās problēmas centies risināt kolektīvi. Novembrī neaizņemies un neaizdod naudu, īpaši ap 8. novembra pilnmēness aptumsuma laiku.',
                'Svari':'Nebaidoties saslapināt kājas, novembra peļķēm bridīsi pāri. Mēdz teikt, ka nav slikta laika, ir tikai nepiemērots apģērbs, tad nu nodrošinies dažādām iespējām un situācijām. Atceries, ka neapmierinātība izraisa paaugstinātu asinsspiedienu un vēl derētu palietot kādas organismu stimulējošas tējiņas, piemēram, asinszāles tēju.',
                'Skorpions':'Savukārt novembrī ar to ekstrēmu vajadzētu piebremzēt, aizraujoties ar to, vari sarūpēt sev kādu traumu, kuru nāksies ilgi dziedēt. Tam, vai tu pirmais ieslēgsi gaismu un pēdējais izslēgsi, nebūs nekādas nozīmes, daudz lielāka jēga būs prasmei mobilizēties sarežģītās situācijās. Tāpēc atceries, ka jūtās ne viss, kas atļauts, ir pieņemams.',
                'Strēlnieks':'Skatoties uz pareģojumiem, neaizraujies ar mīlestības meklēšanu. Vientuļnieka un iekarotāja karagājiens novembrī vainagosies ar liktenīgu tikšanos, dzimušajām attiecībām lemts garš un krāšņs mūžs. Tev derētu objektīvi novērtēt savu uzvedību.',
                'Mežāzis':'Necenšoties sevi nodarbināt līdz spēku izsīkumam, ieteicams ievērot mērenu darba ritmu, jo tas nevairos ienākumus un panākumus. Novembrī nāks atskārsme, ka ne viss ir zelts, kas spīd, apstākļi būs atvēruši acis. Pirms 27. novembra pilnmēness citu cilvēku veiksmes stāsti var radīt spēcīgus pārdzīvojumus, tādēļ stiprini sevi un mācies novērtēt sevi salīdzinājumā ar citu paveikto.',
                'Ūdensvīrs':'It kā zudušo laiku meklējot, smeldzīgās izjūtas un ieskatīšanās pagātnes spogulī var uzjundīt emociju virkni. Uzņēmējdarbības un naudas pelnīšanas laukums rādās diezgan liels un labi pārskatāms. Globālās problēmas tavai profesionālai skatuvei metīs līkumu un ar pasaules glābšanu arī nebūs jānodarbojas, ja esi darba ņēmējs, liec aiz auss ieteikumu nezīmēties priekšniecībai un savu viedokli arī paturēt kā tikai savējo.',
                'Zivis':'Uzlecot saulītei, pilnīgi noteikti apjautīsi to, ka brīnumi notiek. Tā kā tev novembrī radīsies enerģijas uzkrājums, kurš arī kaut kur jāliek lietā, tu varētu savu nemiera spēku novadīt uz mīļajiem. Ķer impulsus, atsaucies uz aicinājumiem, ja tie rezonē ar tevi.'
                }
        if kursh == 'Auns':
            print(horoskopi['Auns'])
        elif kursh == 'Vērsis':
            print(horoskopi['Vērsis'])
        elif kursh == 'Dvīņi':
            print(horoskopi['Dvīņi'])
        elif kursh == 'Vēzis':
            print(horoskopi['Vēzis'])
        elif kursh == 'Lauva':
            print(horoskopi['Lauva'])
        elif kursh == 'Jaunava':                                        
            print(horoskopi['Jaunava'])
        elif kursh == 'Svari':
            print(horoskopi['Svari'])
        elif kursh == 'Skorpions':
            print(horoskopi['Skorpions'])
        elif kursh == 'Strelnieks':
            print(horoskopi['Strelnieks'])
        elif kursh == 'Mežāzis':
            print(horoskopi['Mežāzis'])
        elif kursh == 'Ūdensvīrs':
            print(horoskopi['Ūdensvīrs'])
        elif kursh == 'Zivis':
            print(horoskopi['Zivis'])

    else:
        print('Nu tad uzredzēšanos!')
        exit()
else:    
    exit('Jūs esiet ievadījis nepareizus datus.')
    

