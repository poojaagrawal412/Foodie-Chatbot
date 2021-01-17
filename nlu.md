## intent:affirm
- yes
- of course
- sure
- yeah
- ok
- cool
- go for it
- yep
- yep, will do thank you
- I'm sure I will!
- oh awesome!
- Yes
- accept
- I accept
- i accept
- ok i accept
- I changed my mind. I want to accept it
- ok cool
- alright
- i will!
- ok, I behave now
- yop
- oki doki
- yes please
- yes please!
- jo
- yep if i have to
- amayzing
- confirm
- nice
- coolio
- definitely yes without a doubt
- yas
- yup
- perfect
- sure thing
- absolutely
- Oh, ok
- Sure
- hm, i'd like that
- ja
- sure!
- yes i accept
- Sweet
- amazing!
- how nice!
- cool!
- yay
- yes accept please
- great
- oh cool
- yes
- fine
- i will take that
- that sounds just right

## intent:goodbye
- goodbye
- goodnight
- good bye
- good night
- see ya
- toodle-oo
- bye bye
- gotta go
- farewell
- catch you later
- bye for now
- bye
- bye was nice talking to you
- bye udo
- bye bye bot
- bye bot
- k byyye
- talk to you later
- ciao
- Bye bye
- then bye
- Have a nice day!
- bye!
- Take care!

## intent:deny
- no
- nope
- definitely not
- never
- absolutely not
- i don't think so
- i'm afraid not
- no sir
- no ma'am
- no way
- no sorry
- No, not really.
- nah not for me
- nah
- no and no again
- no go
- no thanks
- decline
- deny
- i decline
- never mind
- nevermind
- I'm not giving you my email address
- no I haven't decided yet if I want to sign up
- I don't want to give it to you
- I'm not going to give it to you
- no i don't accept
- no!!!!
- no you did it wrong
- no i can't
- i'm not sure
- NEIN
- nein
- not really
- i guess it means - no
- i don't want to
- i don't want either of those
- nah thanks
- neither of these
- i don't like that option
- neither will work
- suggest some other option
- is this the best you can do

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Hola
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hallo
- heeey
- hi hi
- hey
- hey hey
- hello there
- hi
- hello
- yo
- hola
- hi?
- hey bot!
- hello friend
- good morning
- hii
- hello sweet boy
- yoo
- hey there
- hiihihi
- hello sweatheart
- hellooo
- helloooo
- heyo
- ayyyy whaddup
- hello?
- Hallo
- heya
- hey bot
- howdy
- Hellllooooooo
- whats up
- Hei
- Well hello there ;)
- I said, helllllloooooO!!!!
- Heya
- Whats up my bot
- hiii
- heyho
- hey, let's talk
- hey let's talk
- jojojo
- hey dude
- hello it is me again
- what up
- hi there
- hi
- jop
- hi friend
- hi there it's me
- good evening
- good morning
- good afternoon

## intent:thankyou
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you
- thanks
- thanks!
- Cool. Thanks
- thanks
- thanks this is great news
- thank you
- great thanks
- Thanks!
- cool thanks
- thanks for forum link, I'll check it out
- thanks!

## intent:ask_budget
 - I want to eat at a place between [300](budgetmin) and [700](budgetmax)
 - I am fine with an expensive place
 - I am looking for a dinner place at less than [300](budgetmin)
## intent:ask_email
 - Please enter your email id
 - Sure! Please enter your email id
 - Sure! Please provide your email id
 - Please help with your email id
## intent:ask_emailid
- can u mail me the information to [abc@abc.com](emailid)?
- can u mail to [test@tes.com](emailid)?
- can u mail me at [test-123.456@dom.123.co.in](emailid)?
- email address - [test.some@gmail.co.in](emailid). Mail this list.
- email me at [email-123@domina.com](emailid)
- mail me [emial@domain.io](emailid)
- my email address [email.123-abc@domain.123.com](emailid)
- please mail me the list to [123-email@domain.co.in](emailid)
- please send me the list to [123@domain.net](emailid)
- please send this to [email.123@123.456.com](emailid)
- send this to [abc-email@abc.com](emailid)
- send to [abc_123-email@abc123.com](emailid)
- this is my email address - [email-abc_123@abc.com.edu](emailid). send me an email.
<!-- no entity -->
- can u share this information over email?
- can u send me an email?
- mail me the list
- email me a list of top 10 restaurants
- mail me the names of restaurants
- please send me an email
- please share this with me
- send me an email
- share some more restaurant names with me
- share this over mail
- share this information with me over email

## intent:send_mail
- [email1_34-ret@host-name.123.com](emailid)

## intent:dont_send_email
- No need
- Not required
- Not required, thank you
- No thanks
- No thank you

## regex:emailid
- ([\w\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)

## intent:restaurant_search
<!-- only 'location' entity : 58 training samples-->
- Find me a place to eat in [Bangalore](location)
- I need a new restaurant in [Bengaluru](location)
- [Bhopal](location)
- help me find restaurant in [Bngalore](location)
- Could you find me a restaurant to eat at [bngalore](location)?
- [Bhubaneshwar](location)
- Can you find me a restaurant in [Bombay](location)?
- [Amritsar](location)
- [erode](location)
- [Jammu](location)
- [Kurnool](location)
- Hey, help me find a restaurant in [Mumbai](location)
- I need to find a restaurant in [Kolkata](location)
- [Pune](location)
- [Cyberabad](location)
- [calcuta](location)
- Find a restaurant for me in [Calcutta](location)
- Where should I eat in [Delhi](location)?
- [Delhi NCR](location)
- Suggest me a good restaurant around [New Delhi](location)
- [Bengaluru](location)
- [Amratsar](location)
- I need to find this restaurant in [Delhi](location)
- [Dilli](location)
- Show me the closest open restaurant in [Chennai](location)
- [Indore](location)
- [Jodhpur](location)
- Hey help me find a restaurant in [Madras](location)
- Help me find a restaurant in [Surat](location)
- Recommend me a restaurant around [Pune](location)
- [Goa](location)
- Could you find a restaurant for me in [Belgaum](location)? 
- [Chandigarh](location)
- [Rajahmundry](location)
- [Ujjain](location)
- Could you find a restaurant for me in [Bengaluru](location)? 
- Would you find me a restaurant in [Allahabad](location)??
- [vadodara](location)
- [Srinagar](location)
- Could you find me a restaurant in [Agra](location)? 
- Pick a restaurant for me, please in [Kochi](location)
- [Mysuru](location)
- How can you help me find a restaurant in [Jamshedpur](location)?
- [Thrissur](location)
- Can you find a restaurant for me in [Chandigarh](location)?
- [Lucknow](location)
- Would you find me a restaurant in [Visakhapatnam](location)??
- Could you find me a restaurant to eat at [Gurgaon](location)?
- [NewDelhi](location)
- [Surat](location)
- [Jamshedpur](location)
- Would you find me a restaurant in [calcutta](location)??
- Okay. Show me some in [bengaluru](location)
- Recommend me a restaurant around [Prayagraj](location)
- [Rourkela](location)
- [Vijayawada](location)
- [Ajmer](location)
- [Allahabad](location)
- [raurkela](location)
- Can you suggest some good restaurants in [bombay](location)
<!-- only 'cuisine' entity : 26 training samples -->
- I'm gonna need help finding a [indian](cuisine) restaurant
- [american](cuisine)
- i'm looking for a [Chinese](cuisine) restaurant
- Hey, can you help me with locating a [mexican](cuisine) restaurant
- i want a [french](cuisine) restaurant
- [chinese](cuisine)
- What's a good place to eat [mexican](cuisine) food
- Find a restaurant for me where I can eat [north indian](cuisine)
- Find a restaurant for me to eat [mexican](cuisine)
- [italian](cuisine)
- I am hungry, find me some place to go eat [italian](cuisine)
- Would you find a [south indian](cuisine) restaurant for me?
- Would you find a [american](cuisine) restaurant
- [north indian](cuisine)
- A place to eat [chinase](cuisine)
- I want to eat [italian](cuisine) food
- Please find me a [south-indian](cuisine) restaurant
- [south indian](cuisine)
- Quickly get me a [northindian](cuisine) place
- Where can i get [south-indina](cuisine) food?
- I need to find a restaurant [southindian](cuisine)
- [mexican](cuisine)
- A place to have [italian](cuisine) food
- Suggest me a good [mexican](cuisine) restaurant
- how can you help me find a [french](cuisine) restaurant?
- [italian](cuisine)
<!-- location + cuisine entities : 22 training samples -->
- I'm gonna need help finding a [indian](cuisine) restaurant in [Mysore](location)
- i'm looking for a [Chinese](cuisine) restaurant in [Lucknow](location)
- Hey, can you help me with locating a [mexican](cuisine) restaurant in [Lakhanpur](location)
- i want a [french](cuisine) restaurant in [Vizag](location)
- What's a good place to eat [mexican](cuisine) food in [Bangalore](location)
- Find a restaurant for me where I can eat [north indian](cuisine) in [Jaipur](location)
- Find a restaurant for me to eat [mexican](cuisine) at [Faridabad](location)
- I am hungry, find me some place to go eat [italian](cuisine) in [Goa](location)
- Would you find a [south indian](cuisine) restaurant for me in [Kozhikode](location)?
- Would you find a [american](cuisine) restaurant for me in [Trivandrum](location)?
- A place to eat [chinase](cuisine) in [Mysuru](location)
- Hey, can you help me with locating a [north indian](cuisine) restaurant in [calcuta](location)
- I want to eat [italian](cuisine) food in [cochin](location)
- Please find me a [south-indian](cuisine) restaurant in [madras](location)
- Quickly get me a [northindian](cuisine) place in [New Delhi](location)
- Where can i get [south-indina](cuisine) food in [Mangaluru](location)
- i'm looking for a [Chinese](cuisine) restaurant in [cyberabad](location)
- [chinese](cuisine) eating place in [mumbai](location)
- I want to eat [italian](cuisine) food in [Prayagraj](location)
- Okay. I want to eat [south indian](cuisine) in [allahabad](location)
- Okay. Show me some [north indian](cuisine) restaurants in [prayagraj](location)
- What's a good place to eat [mexican](cuisine) food in [chandighar](location)
- I need to find a restaurant
- Can you find me a good restaurant?
- Would you be able to search a place to eat?
- A place to have food
- Feeling hungry, can you help
- I am hungry, find a restaurant
- Get me some food quickly
- Pick some place for me to eat quickly
- Where can i get some food to eat
- i'm looking for a restaurant
- how can you help me find a restaurant
- pick a restaurant for me
- please find a restaurant for me
- I'm hungry. Looking out for some good restaurants
- I want to eat
- I am feeling hungry
- I need a new restaurant
- Suggest me a good restaurant
- where should i eat?
- I'm gonna need help finding a restaurant
- Show me an open restaurant
- Find a restaurant for me to eat

## lookup:cuisine
- american
- chinese
- italian
- mexican
- north indian
- south indian

## synonym:chinese
- Chinese
- Chinase

## synonym:south indian
- south-indian
- southindian
- south-indina
- South Indian

## synonym:north indian
- north-indian
- northindian
- north-indina
- North Indian

## synonym:bangalore
- Bangalore
- bngalore
- bengalluru
- Bangalor
- bangalore
- bengaluru

## synonym:delhi
- New Delhi
- Delhi
- NewDelhi
- Dilli
- Dellhi
- newdelhi
- Newdelhi
- new delhi
- new Delhi

## synonym:mumbai
- Bombay
- mumbai
- bombay

## synonym:kolkata
- Calcutta
- kolkata
- kolkatta
- calcutta
- calcuta

## synonym:chennai
- chennai
- madras
- Madras

## synonym:hyderabad
- hyderabad
- Secunderabad
- secunderabad
- cyberabad
- Cyberabad

## synonym:lucknow
- Lakhanpur

## synonym:mysore
- mysore
- mysuru
- Mysuru
- Mysore

## synonym:kochi
- kochi
- cochin
- Cochin

## synonym:Mangalore
- mangalore
- mangaluru
- Mangaluru

## synonym:Visakhapatnam
- visakhapatnam
- Vizag
- vizag

## synonym:Thiruvananthapuram
- thiruvananthapuram
- trivandrum
- Trivandrum
- Travancore
- travancore

## synonym:Vadodara
- vadodara
- Vadodra
- vadodra

## synonym:Jamshedpur
- jamshedpur
- Jamsedpur
- jamsedpur

## synonym:Rajahmundry
- rajahmundry
- Rajahmundri
- rajahmundri
- Rajamundry
- rajamundry
- Rajamundri
- rajamundri

## synonym:Rourkela
- rourkela
- Raurkela
- raurkela

## synonym:Amritsar
- amritsar
- Amratsar
- amratsar

## synonym:Chandigarh
- chandigarh
- Chandighar
- chandighar

## synonym:Allahabad
- prayagraj
- Prayagraj
- Allahabad
- allahabad

## synonym:Nashik
- nashik
- Nasik
- nasik

## synonym:Pondicherry
- pondicherry
- puducherry
- Puducherry