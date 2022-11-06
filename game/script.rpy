﻿# define characters
define h1 = Character ("‎   Asprak Senpai   ‎", color = "#879af2") # h1 = heroine 1 \ asprak senpai
define you = Character("‎      You     ‎") # you
define friend = Character("‎     Friend   ‎")
define ag = Character("‎     Attendance Guy   ‎")
define friend2 = Character("‎     Senpai's Friend   ‎")
define waitress = Character("‎     Waitress   ‎")

# gambar chara
## 
transform kiri:
    xalign 0
    yalign 1.0
transform kanan:
    xalign 1.0
    yalign 1.0

image asprak_senpai = "characters/Asprak_Labcoat_Smile.png"
image asprak_smile_1 = "characters/Asprak_Labcoat_Smile1.png"
image asprak_surprised ="characters/Asprak_Labcoat_Suprised.png"
image asprak_wink = "characters/Asprak_Labcoat_Wink.png"
# image asprak_senpai_blush
# image asprak_senpai_cry
# image asprak_nutup_mata

image asprak_disgust = "characters/Asprak_Labcoat_Disgust.png"
image tangan hp = "characters/pegang_hp.png"
# image friend_1
# image ag
# image friend_2
# image waitress1 


# background

image black = "black.png"
image kamar bangun = "scenes/pov_bangun_tidur.jpg"
image kamar bangun_blink = "scenes/pov_bangun_tidur_blink.jpg"
image gerbang1 = "scenes/gerbang1.jpg"
image gerbang2 = "scenes/gerbang2.jpg"
image gerbang3 = "scenes/gerbang3.jpg"
image jalan kosong1 = "scenes/jalan_kosong1.jpg"
image jalan kosong2 = "scenes/jalan_kosong2.jpg"
image jalan mobil1 = "scenes/jalan_mobil1.jpg"
image jalan mobil2 = "scenes/jalan_mobil2.jpg"
image jalan mobil3 = "scenes/jalan_mobil3.jpg"
image jalan mobil4 = "scenes/jalan_mobil4.jpg"
image jalan motor1 = "scenes/jalan_motor1.jpg"
image jalan motor2 = "scenes/jalan_motor2.jpg"
image kantin ramai1 = "scenes/kantin1.jpg"
image kantin ramai2 = "scenes/kantin2.jpg"
image kantin ramai3 = "scenes/kantin3.jpg"
image kantin meja = "scenes/kantin_meja.jpg"
image kos bukapintu = "scenes/kos_bukapintu.jpg"
image kos bukakunci = "scenes/kos_bukakunci.jpg"
image kos lorong1 = "scenes/kos_lorong1.jpg"
image kos lorong2 = "scenes/kos_lorong2.jpg"
image kos lorong3 = "scenes/kos_lorong3.jpg"
image kos meja_kosong = "scenes/kos_meja_kosong.jpg"
image kos meja_laptop = "scenes/kos_meja_laptop.jpg"
image kos sofa_close = "scenes/kos_sofa_close.jpg"
image kos sofa_far = "scenes/kos_sofa_far.jpg"
image kos sofa_duduk = "scenes/kos_sofa_duduk.jpg"
image kos luar = "scenes/kos_luar.jpg"
image lab barometer = "scenes/lab_barometer.jpg"
image lab komputer1 = "scenes/lab_komputer1.jpg"
image lab komputer2 = "scenes/lab_komputer2.jpg"
image lab datang = "scenes/lab_kosong.jpg"
image lab kosong = "scenes/lab_datang.jpg"
image lab pulang = "scenes/lab_pulang.jpg"
image lab loker_buka = "scenes/lab_loker_buka.jpg"
image lab loker_tutup = "scenes/lab_loker_tutup.jpg"
image lab lorong_datang = "scenes/lab_lorong_datang.jpg"
image lab lorong_pulang = "scenes/lab_lorong_pulang.jpg"
image lab meja = "scenes/lab_meja.jpg"
image lab papan1 = "scenes/lab_papan1.jpg"
image lab papan2 = "scenes/lab_papan2.jpg"
image lab pintu_lab = "scenes/lab_pintu.jpg"
image lab ramai1 = "scenes/lab_ramai1.jpg"
image lab ramai2 = "scenes/lab_ramai2.jpg"
image lab timbangan = "scenes/lab_timbangan.jpg"
image lift buka = "scenes/lift_buka.jpg"
image lift tutup = "scenes/lift_tutup.jpg"
image lift pencet = "scenes/lift_pencet.jpg"

# character 
# image asprak_senpai = "characters\asprak_senpai.png"

# non character
image tangan hp = "characters/pegang_hp.png"
image blink = "blink.png"

# sound
define audio.alarm = "sound/sfx/alarm.mp3"
define audio.yawn = "sound/sfx/yawn.mp3"
define audio.bukujatoh = "sound/sfx/bukujatoh.mp3"

# The game starts here.
label start:
    play sound alarm loop

    scene black with Dissolve(4)

    # play music "sound/Bar_at_the_port.mp3" loop 
    play sound yawn loop

    scene kamar bangun_blink with Dissolve(3)

    stop sound

    you "*wakes up at 06.30 AM on a Monday"
    
    scene kamar bangun with Dissolve(2)
    
    show tangan hp with moveinbottom

    you "*Checks his phone for time"
    you "\[Why did I wake up this early? I have no class on Mondays.\]"

    hide tangan with moveoutbottom

    scene kamar bangun_blink with Dissolve(1.5)
    you "*proceeds to close  his eyes, then remembers something"

    scene kamar bangun with Dissolve(1.5)
    you "\[I have a fucking physics practice session this morning.\]"

    scene beres2in_barang

    you "*MC prepares his stuffs and double-timed his way to ITB"

    scene gerbang3

    you "*MC looks at his watch as he passed through the gate, 07.00 AM"

    scene lab pintu_lab

    you "\[Fuck, I'm gonna be late\]"

    scene lab ramai1

    you "Excuse me!" #*as he pushed his way to the lab

    you "*MC somehow managed to enter the lab just as his group got called by the assistant for briefing"
    
    scene lab komputer1

    friend "Where have you been? We were looking for you."
    you "Sorry guys, I was-"

    scene lab papan2

    show asprak_senpai at left

    h1 "*clears throat"

    show asprak_senpai at right

    h1 "I'll start the briefing, now that your group is complete."
    h1 "Please note, I'm giving you *looking at MC some leniency just because this is your first session."
    h1 "Your next assistant might not be so forgiving."
    h1 "Gather all of your preliminary assignments on the desk before we start the test."
    h1 "Done? Good. Get your pen and papers, here's your test."
    h1 "*flips the whiteboard"

    scene lab papan3

    you "\[What the hell am I looking at?\]"
    you "\[What in the actual fuck is regression analysis\]"

    scene lab meja

    show asprak_smile_1 at right

    h1 "Five minutes remaining."
    hide asprak_smile_1

    you "Bro, could you help me out on that regression thing?"
    friend "Bro.. you passed 8th grade, right?"
    friend "You literally only have to find the slope of that equation. The. Slope. Of. The. Equation."
    you "How?"
    friend "It's literally written on the damn equation."

    scene lab papan2
    
    show asprak_senpai at right
    h1 "Alright, time's up, hand them in."
    h1 "*looks at MC's paper"
    h1 "*under her breath"
    h1 "\[What is wrong with this kid.\]"
    h1 "Kay, I'm (insert name), registration number (insert NIM), and I'm going to be your practice assistant for today."
    h1 "If you need any help for today's session, feel free to reach out."
    h1 "Your module for today will be Measurement and Physical Data Processing."
    h1 "I want you guys to split into three groups to make things faster. "

    h1 "First group, follow me to the barometer …"

    scene lab barometer 

    you "\[I don't know how to read this thing..\]"

    scene lab meja

    "*time skip, MC's group is tasked with this bad boy"
    "Insert gambar regresi linier"
    "*big F to him"
    
    show asprak_senpai at right

    h1 "*approaches MC, who is trying to figure out how to use a vernier caliper"
    h1 "You got the length of the first block, already?"

    you "Uhh, yeah? It's *looking at the caliper around 9.255 cm."

    show asprak_surprised at right
    h1 "What? How on earth did you get that number? Let me check."
    
    
    you "*measures"

    show asprak_disgust at right
    h1 "It says 9.55 cm."

    you "But-"

    h1 "You learned this back in middle school, dummy. You're supposed to understand this thing from the preliminaries."
    h1 "Now go weigh them at the scale."
    you "Ah, okay. I'm, uhh, gonna weigh them now."

    scene lab timbangan

    you "\[This should be easy enough\]"

    scene lab papan2

    show asprak_senpai at right
    h1 "Alright, the time for measurement is up. Get your journals, we're writing the Report."
    h1 "Before we start, I want to stress that the bulk of the score is at the observation and discussion part of your report, so make them well."
    h1 "Also, for Group 4, you can take out your calculators to get the regression equation."

    hide asprak_senpai
    you "Oh, no."

    scene lab loker_buka

    you "*fumbles around his bag and lab coat"

    show asprak_senpai at right
    h1 "Is something matter?"

    scene lab loker_tutup
    show asprak_senpai at right
    you "Uhh, yeah. I think I left my calculator back at my dorm."

    show asprak_disgust at right
    h1 "And I thought you couldn't mess up more. Go pair up with a friend."
    "*time skips, reports are submitted"
    hide asprak_disgust
    scene lab papan2

    show asprak_senpai at right
    h1 "Aaand, we're done. Thank you for coming to today's session."
    h1 "(MC), a word?"
    you "Am I in trouble?"
    h1 "For now, no. But you have taken quite the attention of other assistants."
    h1 "The assistants and practice chief have agreed to not go too rough on minor infractions, but looking at how your practice went, I think I have to warn you."
    h1 "Just make sure to come on time and come prepared. Capiche?"
    you "Understood."
    h1 "Good. Have a nice day, take care."
    hide asprak_senpai

    you "*pack his things and left the lab"

    scene lab lorong_pulang

    you "\[Well that went fantastic. Getting myself in the assistant's sight. What a wonderful way to start my week.\]"
    you "*still walking, reminisces on his senpai"
    you "\[But she's a lowkey cutie, though.\]"

    "*time skip to the afternoon, MC has finished his class for the day and just arrived at his mix-gender dorm"

    scene kos bukakunci with Pause(1.5)

    scene kos tiduran

    you "*laying down on his bed"
    you "\[Man, do I not love studying in ITB.\]"
    you "*reminisces on FL1 again"
    you "\[Stop thinking about her, you simp.\]"
    you "*stomach rumbles"
    you "\[Welp, I guess it's raid-the-fridge o'clock.\]"

    scene dapur_kulkas

    you "*walks to the lounge, opens the fridge, and finds a masterless oreo"
    you "\[They didn't call me a corsair back at high school for nothing.\]"

    you "*while reaching said oreo, he finds a bag of chips in one of the drawers"
    you "\[What kind of psychopath chills their chips?\]"

    play sound bukujatoh
    you "\[Huh?\]"

    scene kos sofa_far

    "*MC looks around to find the source, only to see FL1 laying on a sofa. "
    "She wears (insert clothes, don't wanna be held liable for the details), one hand inside a bag of chips, another hand just hanging out from the sofa."
    "Apparently, she fell asleep while reading a manga and got startled by it being dropped."
    "Reaching down to get the fallen manga, she sees MC by the fridge looking at her, dumbfounded."

    scene kos sofa_close

    you "Uhh, hi?"

    show asprak_surprised at right
    h1 "*squeals"
    h1"YOU DIDN'T SEE ANYTHING!"
    h1"*FL1 grabs her stuff and sprints to her room"

    scene kos lorong2

    you "\[...\]"
    you "\[The fuck just happened?\]"
    you "\[...\]"
    you "\[You know what? I'm not hungry.\]"

    scene dapur_kulkas ###########

    you "*returns the oreo and heads back to his room"

    "*time skip to the next day"
    scene pov_bangun_tidur


    show tangan hp with moveinbottom
    "*alarms blaring, MC wakes up, still can't wrap his head around yesterday's incident"
    hide tangan with moveoutbottom
    
    you "\[Did yesterday really happen? Was that really her?\]"
    you "*reminisces once more, fuckin simp"
    you "\[Why can't I stop thinking about her?\]"

    "*MC gets up and prepares for his day. Opening his door, our clumsy MC bumps into another person"
    
    scene kos bukapintu

    you "Ah, sorry. Didn't see you th-"
    show asprak_surprised
    "*Of course, it's FL1. They stare each other for quite some time before the silence got broken by MC's alarm. He reaches into his pocket and looks at his phone"
    hide asprak_surprised
    you "\[Oh shit, only half an hour remaining before class. Better get going now.\]"

    scene kos gerbang

    "*MC peers up and looks at the exit to find FL1 already closing the dorm's gate."

    scene kos luar

    you "\[Gotta take a shot.\]"
    you "*MC pockets his phone and runs up to her"


    # *he asked as he caught up to her while walking backwards

    scene jalan motor2

    you "Uhh, hey! Hey! How are you this morning?" 

    show asprak_disgust at right #mungkin bakal ada ekspresi lain
    h1 "*doesn't answer, eyes straight ahead"

    you "Uhh, you remember me, right? It's (insert MC's name), from the lab yesterda-"

    scene jalan mobil1

    show asprak_smile_1 at right
    h1 "*pulls MC closer to the side of the road since there's a car heading their way"

    scene jalan kosong1
    show asprak_smile_1 at right
    h1 "*spins MC around and tells him to walk correctly"

    scene jalan motor2
    show asprak_smile_1 at right
    h1 "Dummy, look where you're going when you walk."

    you "Oh shit."
    you "*looks at the car that just passed"
    you "Thanks."

    "*The campus is just a couple hundred meters ahead"

    you "So uhh, you're having a morning class, too?"

    hide asprak_smile_1
    show asprak_senpai at right # show asprak_senpai_blush at right
    "*FL1 doesn't answer"

    you "By the way, I really didn't expect us to live in the same dorm."
    "*FL1 gets flustered"

    scene kelas1

    show asprak_senpai
    you "*reminisces about FL1 back at the lab"
    hide asprak_senpai
    you "*reminisces about the incident yesterday"
    you "\[She's damn cute, I get that. But I didn't expect that big of a gap moe.\]"
    you "*reminiscing how flustered she got when they walk together"
    "*suddenly, people around him are shuffling around and lecturer is picking up their stuff"

    you "\[Hold up, the class is finished?\]"
    you "\[But I haven't understood shit.\]"
    you "\[Welp, that's two extra hours of independent learning.\]"
    you "*stomach rumbles"
    you "\[Oh yeah, I haven't had breakfast.\]"

    you "*MC got up and went to cafetaria and orders his lunch"

    scene kantin ramai3

    you "*bumps into his friend"
    you "Oh hey, getting some chow, too?"

    show friend_1 at right
    friend "Hey! Yeah. Didn't understand anything at class, my brain was too busy asking whether I should buy ayam geprek or ayam penyet for lunch."

    you "Damn, same. By the way, got any seats yet?"
    you "*MC eyes around to find an empty seat and instantly saw FL1 sitting alone at the far end of the cafetaria"

    friend "Nah, I'm taking it away, gonna have a group work right after this."

    friend "*looks at MC, looks at where he's looking"
    friend "But I guess you have a seat in mind already."

    you "W-What? Oh, no, I guess you're misinterpreting something."

    friend "Yeah, sure, sure. You've been eyeing our lab assistant since she scolded you about the caliper."

    you "What? No! It's just that we happen to live in the same dorm."

    friend "Real shit? Well you're in luck, my friend."
    "*both of their orders are finished"
    friend "Welp, gotta get going. See you around!"
    friend "*leans to MC and whispers"
    friend "And good luck."

    you "Hey, come back here! I'm not done yet!"

    you "See ya later!"

    scene kantin meja

    you "*glances at FL1"
    you "\[But coming to it again, why did I notice her that quickly in the first place?\]"
    you "*breathes in"
    you "\[Here we go.\]"

    you "*MC approaches the table"

    you "Hey! Is this seat taken?"

    show asprak_surprised at right
    h1 "shocked pikachu face, shakes her head"

    you "Mind if I sit here?"

    hide asprak_surprised
    show asprak_senpai at right #mungkin ada ekspresi lain
    h1 "*shakes her head, getting a bit tense"
    hide asprak_senpai

    you "*sits and starts to eat his meal"
    "*they both eat in silence, not daring to break the ice"
    you "\[Do I make her uncomfortable?\]"
    "*looks around for a vacant seat, but there isn't any"
    you "\[Better eat this quickly.\]"
    you "*finishing his lunch, he looks up to see FL1 staring at him"
    you "I-I think I ought to change tables."

    show asprak_senpai at right # show asprak_senpai_blush at right
    h1 "No, don't." #*holding the hem of his sleeve

    you "*sits back down"
    you "Okay?"
    # hide asprak_senpai_blush

    "*MC continues to eat his lunch in silence"

    # show asprak_senpai_blush at right
    h1 "Why do you keep approaching me?"

    you "I beg your pardon?" #*a bit shocked

    h1 "You heard me. But don't get it wrong, though. I just wanna know why."

    you "Well, for starters, I just want to be friends with you." 
    you "I mean, we live in the same dorm, we will bump into each other every day. Might as well get to know you better."
    you "\[And for the last part, I really want to know you better.\]"

    # hide asprak_senpai_blush
    # show asprak_senpai at right
    h1 "Oh, well that's nice."

    you "And we will meet each other every other week at the lab, so-"

    h1 "*stares daggers at MC"
    h1 "Thank you for bringing it up, but I much prefer that we stop talking about the lab."

    you "R-Right."
    you "\[Nearly stepped on a landmine back there.\]"

    h1 "If that's the case." 
    h1 "*she stands up and packs her stuff"
    h1 "I'll be in your care. I hope we can get to know each other better."

    you "Y-yeah. Me, too."

    h1 "Well, I have to tutor a freshman calculus class in half an hour. It's good to see you, take care." 
    hide asprak_senpai
    h1 "*leaves"

    scene kantin ramai2

    you "*looks at FL1 as she walks away"
    you "\[What a nice start.\]"

    # "*his phone vibrates rapidly, mafiki class' group chat is in chaos"
    # you "\[A fucking physics pop quiz in 30 minutes? Oh fuck.\]"

    # you "*books out to class to get some crash course"

    "*time skips to the next day"

    scene pov_bangun_tidur

    you "*wakes up startled"
    you "\[How come has the alarm not gone berserk yet? My sleep quality is getting a bit too suspicious.\]"
    #Hey, you. You're finally awake. *some 4th wall skyrim shit ?

    # you "\[Who the fuck is that?\]"
    show pegang_hp with moveinbottom
    you "*looks at phone for time"
    you "\[There's no way it's still 5 am. That was the best sleep I had in weeks. It must be 5 pm.\]"
    show pegang_hp with moveoutbottom

    you "*looks out his windows. The sky is still dark"
    you "\[Well I'll be damned.\]"

    show pegang_hp with moveinbottom
    you "*turns off alarms"
    show pegang_hp with moveoutbottom

    show asprak_senpai
    you "*reminisces on yesterday's encounter with senpai"
    hide asprak_senpai
    you "\[Welp, better get ready and find her again.\]"

    "*time skip to lunch"

    scene kantin ramai3

    you "*orders his food and looks around the cafeteria"
    you "\[Where is she?\]"

    show friend_1
    friend "Yo! Wanna join us?"
    you "\[Meh, I'll look for her at the lab after class.\]"

    you "Sure thing!"
    hide friend_1
    "*time skip to the afternoon, he went straight to the physics lab building and wait outside"

    scene lab datang
    
    you "\[Guess she's not here. Well, nice try, I guess.\]"

    scene lab pulang

    you "*heads back to his dorm"

    # #########################################################################################################################################

    scene kamar 

    you "*stomach rumbles"
    you "\[I literally just ate four hours ago.\]"
    you "*rumbles some more"
    you"\[Now, should I order a balanced meal like a responsible college student should or should I order diabetes incarnate?\]"
    "*spoiler alert, his intrusive thought wins"
    you "\[A wise person once said an apple a day keeps the doctor away. Unfortunately, I'm not a wise guy.\]"

    you "*orders a martabak manis"

    scene gofood alert
        
    "*his order arrives. He takes it and went to the lounge"

    scene sofa pov

    you "*sees FL1 on her phone"
    you "\[Time to shoot my shot\]"
    you "Fancy seeing you here."

    show asprak_surprised at right
    h1 "*kinda startled"

    hide asprak_surprised
    show asprak_senpai at right
    h1 "Hey, didn't see you there."

    you "*sits down"
    you "Do you mind?" #*point to the sofa

    h1 "*pats the cushion"
    h1 "C'mere."

    you "Nice."
    you "*opens the martabak"
    you "Here, take some."

    h1 "Ah, thank you."

    you "*turns the TV on"
    hide asprak_senpai

    "*they both sat and enjoy the sweet delicacy in silence"

    you "\[Gotta break the ice.\]"
    you "So, uhhh, what're you doing?"

    show asprak_senpai at right
    h1 "Oh, nothing. Just chilling and hunting for new mangas."

    you "\[Oh yeah, she's a closet weeb.\]"

    you "Oh really? You really didn't look like someone who would indulge herself in reading man-"

    show asprak_disgust at right
    h1 "*throws a pillow at MC"
    h1 "Shut."

    you "Ow."

    hide asprak_disgust
    show asprak_senpai at right
    h1 "Anyway, got any recommendations?"

    you "Meh, I don't know. Do you have any genre preferences in mind?"

    h1 "Anything with a lot of actions, especially the ones with some fantasy or magic or whatever you call it."

    you "Are isekais okay?"

    h1 "Preferably not, too cliche."

    you "Well shit. Fate?"

    h1 "I have watched, played, and read the franchise to oblivion."

    you "*kinda shocked pikachu face"
    you "\[H-hol up. Played? S-she couldn't have played the OG VN right?\]"

    h1 "Hey, are you okay? You look pretty shocked knowing I watch Fate."

    you "N-nothing. It's just that I rarely find someone that watches fate, too. By the way, which one is your favorite?"

    h1 "Surprisingly, Today's Menu for the Emiya Family. I think I got sick of all the misery sometime in the middle of reading Strange Fake."

    you "Very understandable."
    you "Have you tried Garden of Sinners?"

    h1 "Huh, didn't think of that. I've watched the anime, but I haven't really thought of reading the light novels. You know where to get them?"

    you "Uhh, maybe try the book store? I'd find a couple hidden gems here and there sometimes."

    h1 "*smiles"
    h1 "I'll try."

    you "Though if I were you, I'd just sail the high seas."

    h1 "Ah, a fellow corsair."

    you "*laughs"
    you "By the way, do you really love Fate that much?"

    h1 "Well, yes, at least when it comes to franchises. Shit slaps."
    h1 "I mean, where else can you find King Arthur portrayed as women. Mind the plural form."

    you "Shiiiiieeet. Coming to it, I'm quite surprised that FGO or Type-Moon has yet to make a Monty Python reference."

    h1 "Yeah, I really expected Artoria to ask something about swallows at least once."

    you "By the way, have you tried Tsukihime?"

    h1 "I have. As a matter of fact, I just finished the new one last week. Both routes."

    you "Damn."

    h1 "You got any anime or manga of your liking?"

    you "Do you know Ghost in the Shell?"

    h1 "The anime, right? Not the live action."

    you "Of fucking course, making a live action version of Ghost in the Shell was a
    mistake."

    h1 "I think that applies to a lot of anime."

    you "Anyway, there was this pretty old series called the Stand Alone Complex, made
    in the early 2000's or something. The first season was okay, but the second season
    was out of this world."

    h1 "Oh, does it have a great plot or something?"

    you "Nah, the overall plot is good, but not that remarkable. However, the mix
    between the subplots, soundtracks, and actions was something else. I haven't
    seen another anime that comes close."

    h1 "Action, you said?"

    you "Well, yeah. It's literally a cyberpunk police anime."

    h1 "I think I should give it a chance. I've watched the new one in Netflix, it was okay, I think?"

    h1  "But if it's about my actual favorite it's got to be those tearjerkers. You know, like Grave of the Firef-"

    you "Please don't elaborate further, I don't want to get PTSD at the moment."

    h1 "Sheeesh, okay."

    h1 "What about 5 cm/s?"

    you "Well that's pretty nice, but still, two literal idiots in love. Can't handle watching that for the second time."

    h1 "Ditto, by the way-"
    h1 "*interrupted by her phone vibrating"
    h1 "Oh shit, I forgot I have a group work due tomorrow. They're asking for my progress."

    you "Well? Get going already."

    h1 "Okay, okay, I'm going to my room."
    h1 "By the way, can I take another bite?"

    you "*sighs"
    you "Just take the damn box, there's like, what, four pieces left?"

    h1 "You sure?"

    you "Yeah, I'm full anyway."

    h1 "Bet. Thank youuuuuu." 
    h1 "*runs off"
    hide asprak_senpai

    you "\[She got the edge pieces.\]"
    you "\[Well, as long as she's happy, I don't care.\]" 
    you "\[It's just a glorified pancake, nothing big.\]" 

    "*time skip to praktikum 2. MC's having an all-nighter trying to speedrun TP Fisika. Sadly, his WD-40 lubed brain is having a pretty hard time"

    you "\[GOTTA FINISH THE FLOWCHARTS.\]"
    you "*checks his phone, his friend that had done his module the week before sends the procedure to derive an equation or something"
    you "*got a step wrong"
    you "FUCKING PIECE OF SHIT PHYSICS PRELIMINARY. DERIVE THIS, DERIVE THAT."
    you "*sits down, trying to calm himself"
    you "*chugs coffee that is more of a motor oil than coffee"
    you "\[Aight. Calm down, calm down, calm DOWN, CALM THE FUCK DOWN.\]"
    you "*threw his pen so hard it fucking broke"
    you "\[Aight, fuck this shit.\]" 
    you "*proceeds to draw the ugliest, pure undecipherable flowchart"
    you "*his 6 am alarm goes off"
    you "\[Great, no fucking sleep.\]"

    "*time skip to the actual praktikum"

    you "*arrives at the lab entrance"
    you "*takes his nametag off and presents it to the air"

    show ag at right
    ag "Uhh, hey. I'm right here."

    you "*got up from his trance and walked to the scanner"
    you "Oh, yeah. Sorry."
    hide ag 

    you "*enters the lab and goes to his desk"

    show asprak_senpai at right
    h1 "*notices"
    h1 "Huh?, a word?" 

    you "Yeah?"

    #mungkin ada ekspresi lain mungkin khawatir    
    h1 "Are you okay? To be honest, you look like shit."

    you "Never been better."

    h1 "Did you have any sleep last night?"

    you "If you count a bunch of two second microsleeps as sleep, then yes."

    h1 "*sighs"
    h1 "You know you have a lab session tomorrow, yet you still force yourself out. Was it the preliminaries?"

    you "*nods"

    h1 "Gosh, take care of yourself. You know you can just come over to my room if you got any problems."
    h1 "You know what? Take the day off. I'll go to the practice head and ask him to put put you in the reserve session."

    you "Nah, I'm good."

    h1 "Come on, there won't be any score discount if you're on sick leave."

    you "No, really, I'm okay. You're such a worrywart."

    h1 "Fine. But tell me if you feel sick or anything, okay?" 

    you "O-Okay"

    h1 "Good."
    hide asprak_senpai

    show asprak_surprised at right
    "*Suddenly, he faints on his way to the desk"
    hide asprak_surprised

    "*After some time, he wakes up in the infirmary"

    you "*slowly opens his eyes"
    you "Where am I?"
    you "\[Whatever this place is, it sure has some top notch pillow.\]"

    show asprak_senpai at right #mungkin ada ekspresi lain
    h1 "Hey, are you awake?"

    you "*his eyes shot open"
    "*he's in his senpai's lap, her hands stroking his head
    *they stare at each other"
    you "Uhh, yeah?"

    h1 "You big dummy, why didn't you tell me you're sick?"
    h1 "Do you know how worried I was?"

    you "*just nods his head, still can't believe he's in her lap while getting caressed"

    h1 "I mean, let's forget about you for once. Do you have any idea how dangerous it is to work half-awake IN A LABORATORY?"
    h1 "Do you even realize that you are a safety hazard at that moment?"

    you  "*nods and blushes"

    h1 "I mean, gosh, if you don't feel well, just say it. I don't want you to get hurt."

    you "*silent"

    h1 "Hey, are you even listening?"

    you "Yes. (clearly not listening)"

    h1 "*realizes that she's still stroking his hair while scolding him"
    h1 "*blushes too and stops stroking"

    you "Hey, why did you-"

    h1 "*stands up, MC fell on his head"

    you "Ow."
    # hide asprak_senpai
    # show asprak_senpai_blush at right
    h1 "J-Just take the day off and take care of yourself!"

    you "*sat back up"
    you "Hey, wait!"

    h1 "Just go back home! I'll take care of the reserve session. (runs, leaving the MC)"
    hide asprak_senpai # hide asprak_senpai_blush

    you "*stands up, dumbfounded"
    you "Damn. That felt good."

    "*time skip to the next day"

    you "*sits inside his room, he's free on Fridays"

    show asprak_senpai
    you "*reminiscing the lap pillow and headpats"
    hide asprak_senpai

    you "\[GAHD DAMN.\]"
    you "\[I NEED IT MORE.\]"
    you "\[I FUCKING NEED MORE LAP PILLOWS.\]"
    you "*slaps himself"
    you "Control yourself, Me."
    you "*decides to take a shower"
    you "*gets dressed and gets out of his room"
    you "*opens his door"

    show asprak_senpai at right
    you "*FL1 stands right in front of it"

    you "Oh shit."

    h1 "G-Good morning."

    you "Uhh, good morning?"

    h1 "How have you been? Are you okay?"
            
    you "Oh, I'm okay."

    h1 "Are you sure, though?"

    you "No, really. I'm fine now. I just woke up early."
    
    #mungkin ada ekspresi lain
    h1 "Thank God you're okay."
    h1 "By the way, I'm really sorry for, well-"

    you "Nah, it's fine. I mean, It's not like I can see you blush that red everyday ."

    you "\[I'm free today.\]"
    you "\[No homework or the ilk either.\]"
    you "\[Might as well.\]"
    you "Hey,  are you free this afternoon?"

    h1 "What?"

    you "I got a promo for two free movie tickets. I mean, if you're free, we can go to the cinema."

    h1 "Are you serious?"

    you "Of course I am."
    
    # hide asprak_senpai
    # show asprak_senpai_blush at right

    h1 "L-Let me check my schedule first."
        
    h1 "Well I don't have anything of importance to do past 4 am. Is it too late?"

    you "No, no, it's perfect. So, see you at 4 or 5?"

    h1 "O-Okay."

    # hide asprak_senpai_blush

    "*time skip to the afternoon"

    you "*got out of his room at 4 and finds FL1 already waiting at the dorm's lounge"

    # show asprak_senpai at right
    h1 "So, shall we?"

    you "Yeah, let's go."

    #*they walked to an alternate version of Jatos
    #you *looking at the movie schedule

    you "You got anything in mind?"

    h1 "I thought you already had the tickets."

    you "I have a promo for two free tickets, we can still choose the movie."

    h1 "Ah, I see."
    h1 "Miracle in Cell No. 7 it is, then."

    you "Alright."
    you "Two tickets for Miracle in Cell No. 7, please."

    hide asprak_senpai

    "*time skip"

    show asprak_senpai at right # show asprak_cry at right
    you "I *sniffle* I can't believe the world is so unfair."

    h1 "*literally crying a river"
    h1 "I know right.."
    
    you "Uhhmmm."
    you "Oh yeah, I forgot I have an assignment due tomorrow, but whatever."
    
    # hide asprak_cry
    # show asprak_senpai at right

    h1 "You should know better not to procrastinate, lest you faint again."

    you "But I'm going on a date with my cute lab assistant. I can't let the occasion go, can I?"
    you "*blushes, realizes what he just said"

    # hide asprak_senpai
    # show asprak_senpai_blush at right
    h1 "*blushes too"

    "*awkward silence"

    you "Do you wanna get a meal?"

    h1 "Y-Yes, please!"

    # hide asprak_senpai_blush
    "*time skip, they arrive at their dorm"
    
    # show asprak_senpai at right
    h1 "Hey btw. Thank you so, so much for the, uuuhmmm, outing."

    you "Don't mention it. We need to have some fun once in a while, don't we?"

    h1 "But really, you paid for the whole thing, I don't-"

    you "Shush, just consider it as a pay back for yesterday. Though, I think I have something to ask you."

    h1 "What is it?"

    you "Reduce the moe gap. I don't think I can hold my laughter if I see you in your asprak mode next session."

    h1 "*giggles"
    h1 "*leans in to MC and hugs him"
    h1 "Thank you."
    
    # hide asprak_senpai
    you "\[She hugs me. SHE IS HUGGING ME.\]"

    # show asprak_senpai_blush at right
    h1 "So, uhhh."
    h1 "Bye, have a good night!"
    h1 "*runs to her room in embarrassment"
    
    # hide asprak_senpai_blush

    you "*still can't comprehend what just happened"
    you "\[I'm not washing my clothes.\]"

    "*time skip, a couple days later, at lunch time"

    you "*has got his food and is looking for a seat"
    you "*sees the spot in front of FL1 is empty"

    show asprak_senpai at right
    h1 "*sees him and waves"

    you "*scoots there"
    you "Fancy seeing you here."

    h1 "Yeah, yeah, we've been sitting together at lunch for like, what, two weeks? Just get your ass here if you need a seat."

    you "Damn, no need to be so blunt."

    h1 "Yeah, whatever."

    you "By the way, you got class after lunch?"

    h1 "Yes, and then a group assignment. You?"

    you "Online class, the lecturer's sick, so I'm going to-"

    show friend_2 at left
    friend2 "Hey, girl. How've you been?"

    h1 "*caught off guard"
    h1 "Oh, hey there, I'm go-"

    friend2 "Oh look who we have here?"
    friend2 "Did you get yourself a boyfriend?"
    # hide asprak senpai
    # show asprak_senpai_blush at left
    you "*his brain short circuited"
    you "\[Boyfriend?\]"
    you "\[Am I in a relationship with her?\]"
    you "\[Well, of course I am, but is it that kind of relationship?\]"
    you "\[How the fuck am I supposed to answer them?\]"
    # hide asprak_senpai_blush
    #show asprak_senpai at left
    h1 "Come on, give him some slack."

    you "*moves aside"

    h1 "We're just having lunch. Y'all don't get some?"

    friend2 "Oh, we had one already. By the way, did you hear that …."

    you "\[Hol up. She doesn't deny it, though.\]"
    you "\[Could she?\]"
    you "\[Nah, I'm thinking too far off.\]"
    you "\[Or maybe?\]"

    friend2 "Oh shit, pop quiz, gotta go. See you later!"

    hide friend_2

    h1 "See ya, take care."

    hide asprak_senpai
    "*FL1 and MC continue to eat in silence"

    you "Uhh, senpai?"

    show asprak_senpai at right
    h1 "Yeah?"

    you "Did I hear it wrong or did you not answer your friends' question?"
    you "I mean, I know they're just joking and all, but-"

    # hide asprak_senpai
    # show asprak_senpai_blush at right
    h1 "Shut. Just eat your damn meal."
    hide asprak_senpai # hide asprak_senpai # hide asprak_senpai_blush

    you "\[T-This can't be.\]"
    you "\[God, I love her.\]"

    "*time skip to Thursday"

    "*MC just finished Praktikum 2 Pengkom"
    "*he couldn't understand a thing"
    "\[What was that.\]"
    "\[I'mma go touch some grass.\]"
    "*he prepares for a walk, but then he remembered something"
    "\[You know what will make this stroll better?\]"
    "*whips out his phone"
    "*calls FL1"

    show asprak_senpai at right
    h1 "Moshi-moshi."

    you "Hey, how's it going? You good?"

    h1 "Yes. Need something?"

    you "No, just wondering if you're free today?"

    h1 "My brother in harmonia progressio, I'm literally watching SpongeBob at the living room."

    you "*opens his door and heads to the lounge"
    you "*sees FL1 laying on the sofa while munching down an ice cream sandwich"
    you "So, you're free?"

    h1 "You're up to something?"

    you "I'm going outside, preferably touching some grass while at it. Wanna come?"

    h1 "Sure, wait a sec."

    #"*they walk outside"

    h1 "So, you know where we're going?"

    you "Good question, I have no idea."

    h1 "I have somewhere in mind."

    you "Wher-"
            
    h1 "Just wait and see."

    # MIXUE

    h1 "Ta da."

    you "Ice cream?"

    h1 "Not just ice cream though, there's smoothie and shit, too. Come on in, my treat."

    you "But I'm the one th-"
            
    h1 "*looking at the menu"
    h1 "So, what do you want?"

    you "Uhh, I want something simple. Prolly a vanilla soft serve and a boba."

    h1 "You know they can mix both of them together, right?"

    you "Sometimes, mixing similar food is not the best course of action. And I'm in the mood to savor each of them separately. "

    h1 "Damn, okay Anton Ego."
    you "*heads to the cashier"
    you "Hi, I'd like to order two vanilla soft serves and two brown sugar boba."

    you "\[She's in a really high spirit today.\]"

    h1 "Alright, we just have to wait for our ice cream now."

    you "Uh huh."

    "*silence"

    h1 "So, how's college?"

    you "So far? Not ideal, still got some skill issues with physics and chemistry. But calculus' not as hard as I thought, though."

    h1 "Remember, if you have any trouble, just hit me up."

    you "Yeah, yeah, I still remember your scolding when I was-"

    h1 "Do. Not. Continue." # *blushes

    you "By the way, how's Garden of Sinners."

    h1 "Found pdf's of some of the series. Pretty damn good, I must say."

    you "I know you'd like it." #*sips on his water bottle

    h1 "So, got any girls on your sights, yet?"

    you "*spits/choked on his water"
    you "Wh-What?"

    h1 "You heard me, big guy."

    you "What kind of question is that?"

    h1 "Oh come on, just answer it."

    you "W-Well, there's this one girl."

    h1 "Hmmm?"

    you "Uhhh."

    show waitress1 at left
    waitress "Order number 66."
    hide waitress1

    h1 "Hey, that's ours."
    h1 "*takes the order"
    h1 "Here are yours."

    you "Ah, thanks."

    h1 "Wanna go to the park?"

    you "S-Sure."

    "*they left the store, time skip to park. They got a seat there"

    h1 "You know what? They do taste good when separated."

    you "Right?"

    h1 "By the way, regarding my question earlier."

    h1 "I also have a guy in sight."

    you "\[Could it be me?\]"

    h1 "Truth to be told, I don't really care about getting into a, you know, relationship. But then, there was this lazy, sorry excuse of a physics student."

    you "\[She's talking about me.\]"

    h1 "This guy was, ugghhh. You know, I sometimes wonder how he got into ITB."
    h1 "He's pretty cute, not gonna lie. And he also as a tendency to force himself to do something he knows he can't."

    you "Sounds like someone I know."

    h1 "But due to circumstances, we got closer."
    h1 "And closer."
    h1 "And the fact he, too, is a weeb doesn't help."
    h1 "But, I think the weeb part seals the deal."
    h1 "Then we went on a date together."
    h1 "Had some pretty deep talk."
    h1 "And I think I fell for him."

    you "Oh, he's a weeb?"

    h1 "A big one, that is."

    you "He doesn't happen to like an old anime, does he?"

    h1 "If you count a 2004 anime that is now pretty obscure as old, then he does."

    you "Huh. I guess he suits you so much."

    h1 "That he does, (MC). That he does."

    you "Is there anything you like more about him?"

    h1 "Well, just normal stuff, I guess. It sure feels nice to have someone you can rely to, and be someone he can rely on, too."

    you "\[Yep, that's 100\% me.\]"
    you "Tell me."
    you "Do you love him?"

    h1 "Wanna know the answer?"

    you "*nods"

    h1 "Here's my answer, and I hope you do, too."
    hide asprak_senpai
    show asprak_senpai #show asprak_senpai_blush #mungkin ada ekspresi lain
    "*leans in and kisses him"
    hide asprak_senpai # hide asprak_senpai_blush
    
    
    # "*time skip, they're in a relationship"

    # you "*wakes up in the lounge's sofa on an early morning on Saturday"
    # you "\[Where the fuck am I?\]"
    # you "*looks around, sees that the TV is on and playing Netflix\]"
    # you "\[Ah, I overslept.\]"
    # you "\[Where is my phone.\]"

    # you "\[There it is.\]"
    # you "*checks the time, its 3 am"
    # "*looks around, the lounge looks like a damn landfill from all the wrappings and snack
    # packagings"

    # you "\[Better clean them up ASAP before I got scolded.\]"
    # you "*tried to stand up, but can't"
    # you "*realized his right arm fell asleep"

    # you "*lifts the blanket, only to see FL1 cuddling against him, her arms wrapped around his torso"

    return