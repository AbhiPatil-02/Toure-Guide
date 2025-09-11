#trail and error

'''


from tkinter import *
from tkinter import ttk






rt=Tk()
rt.title('Place Guide')
#P="abhi"
S="hi"
Pa="hi"
H="hi"
D="hi"

a=PhotoImage(file="C:\\Users\\Abhishek Patil\\python\\mini project\\bg1.png")
l1=Label(rt,image=a).pack()

custom_font = ("Arial", 16)
e1=Entry(rt,width=30,borderwidth=10,fg="black",font=custom_font).place(x=200,y=100)
l2=Label(rt,text="Enter Place",font=custom_font).place(x=80,y=110)

	
def search():
	l2=Label(rt,text='Place :-',font=custom_font).place(x=150,y=200)	 
	l3=Label(rt,text='State :-',font=custom_font).place(x=150,y=250)
	l4=Label(rt,text='Places :-',font=custom_font).place(x=150,y=300)
	l5=Label(rt,text='Hotels :-',font=custom_font).place(x=150,y=400)
	l6=Label(rt,text='Detail :-',font=custom_font).place(x=150,y=500)
	l7=Label(rt,text=P).place(x=250,y=200)	 
	l8=Label(rt,text=S).place(x=250,y=250)
	l9=Label(rt,text=Pa).place(x=250,y=300)
	l10=Label(rt,text=H).place(x=250,y=400)
	l11=Label(rt,text=D).place(x=250,y=500)
def clear():
	e1.delete(1, tk.END)

b1=Button(rt,text="Search",command=search).place(x=350,y=170)
b2=Button(rt,text="Clear",command=clear).place(x=450,y=170)

rt.mainloop()




'''


'''
data = {
    "amareshwara swamy temple":{
                  "place":"amareshwara temple",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":"Amararama is one of the five Pancharama Kshetras that are sacred to the Hindu god Siva. The temple is located in Amaravathi town of Palnadu district in the Indian state of Andhra Pradesh. Amareswara Swamy or Amaralingeswara Swamy refers to Lord Shiva in this temple. The temple is situated on the southern bank of Krishna River. The consort of Lord Amareswara Swamy is Bala Chamundika. The Sivalinga at this place is installed and established by Lord Indra.\n
Vasireddy Venkatadri Naidu, King of Chintapalli and later Dharanikota, was a great devotee of Amareswara. He expanded and renovated the temple. The popular legend has it that once during the course of putting down a rebellion in his land the King had to have recourse to a massacre of the Chenchus, whereupon he lost his mental peace, which he regained only when he came to Amaravati. He shifted his place from Chintapalli to Amaravati in 1796, and devoted his entire life, time and revenues to building temples for Lord Siva./n
He renovated the Amareswaraswamy temple here, engaged nine learned archakas for the daily archana of the Lord, and provided them with all the needs of livelihood, including 12 acres (49,000 m2) of land to each. The temple as it stands owes much to him. 
As per Legend, the demon king named Tarakasura defeated the gods after being awarded a boon by Lord Shiva. Shiva vowed to kill the demons and hence the gods came to reside here and since then the place came to be called Amaravati. Lord Shiva is worshipped as Amareswara with his consort Bala Chamundika, who is considered as the fourth of the 18 goddesses. srikrishnadevaraya had visited this temple after the war of kodapalli"
     },
     "kanaka durga malleshwari temple":{
                   "place":"kanaka durga temple",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Kanaka Durga Temple, also known as Sri Kanaka Durgamma Devasthanam, is a Hindu temple dedicated to Kanaka Durga. The deity in this temple is also popularly referred as Kanaka Durga.\n
The temple is located in Vijayawada, Andhra Pradesh, India on the Indrakeeladri Hills on the banks of Krishna River. Kaalika Purana, Durgaa Sapthashati and other Vedic literature have mentioned about Kanaka Durga on the Indrakeelaadri and have described the deity as Swayambhu, (self-manifested) in Triteeya Kalpa.\n
The popular legend is about the triumph of Kanaka Durga over the demon King Mahishasura. It is said that the growing menace of demons became unbearable for the natives. Sage Indrakila practiced severe penance, and when the goddess appeared the sage pleaded to her to reside on his head and keep a vigil on the wicked demons. As per his wishes of killing the demons, Durga made Indrakila her permanent abode. Later, she also slayed the demon king Mahishasura freeing the people of Vijayawada from evil.\n
At the Kanakadurga temple, the enchanting 4-foot-high (1.2 m) icon of the deity is bedecked in glittering ornaments and bright flowers. Her icon here depicts her eight-armed form, each holding a powerful weapon, in a standing posture over the demon Mahishashura and piercing him with her trident. The goddess is the epitome of beauty.\n
Kanaka Durga Temple is synonymous with Vijayawada. It is mentioned in the sacred texts.  View of Temple Complex from Prakasam Barrage A nearby temple viewed from Prakasam Barrage on night lights
It is mentioned in the Hindu scriptures that the deity in the Sri Kanaka Durgamma Devasthanam is regarded as Swayambhu or self-manifested, hence considered very powerful.\n
During the month of Sraavanam, Varalakshmi Vratam is performed on all Fridays with special reverence. More than 20,000 people attends the celebrations during this month.\n
During the month of Sraavanam, Varalakshmi Vratam is performed on all Fridays with special reverence. More than 20,000 people attends the celebrations during this month.
                   "near by hotels":"hotel sk riverfront\npanchavati residency\nhotel manorama\nred fox hotel\nhotel rn grand"
    },
    "nagarjun sagar dam":{
                   "place":"nagarjun sagar dam",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"The Nizam made the British engineers begin the survey work for this dam across the Krishna River in the year 1903.\n
The project's construction was officially inaugurated by Prime Minister Jawaharlal Nehru on 10 December 1955 and proceeded for the next twelve years. Raja Vasireddy Ramagopala Krishna Maheswara Prasad, popularly known as the late Muktyala Raja, was instrumental in the construction of the Nagarjuna Sagar Dam through active political lobbying and the donation of one hundred and ten million GBP in 1952.\n
22,000 ha (55,000 acres) of land. It was the tallest masonry dam in the world at that time, built entirely with local know-how under the engineering leadership of Kanuri Lakshmana Rao.\n
The reservoir water was released into the left and right bank canals by Prime Minister Indira Gandhi on 4 August 1967. Construction of the hydroelectric power plant followed, with power generation increasing between 1978 and 1985 as additional units came into service. In 2015, the diamond jubilee celebrations of the project's inauguration were held, alluding to the prosperity the dam has ushered into the region.\n
The construction of the dam submerged an ancient Buddhist settlement, Nagarjunakonda, which was the capital of the Ikshvaku dynasty in the 1st and 2nd centuries and the successors of the Satavahanas in the Eastern Deccan. Excavations yielded 30 Buddhist monasteries as well as artwork and inscriptions of historical importance. Prior to the reservoir's flooding, monuments were dug up and relocated. Some were moved to Nagarjunakonda, now an island in the middle of the reservoir. Others were moved to the nearby mainland village of Anupu.\n
The site of the dam was selected in 2022 to be developed as part of the UDAN scheme. The selection calls for the development of a water aerodrome at the site.
   },
   "the stupa":{
                  "place":"the stupa",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":"The stupa, or mahāchetiya, was possibly founded in the third century BCE in the time of Asoka but there is no decisive evidence for the date of foundation. The earliest inscription from the site belongs to the early centuries BCE but it cannot be assigned to Aśoka with certainty. The earliest phase from which we have architectural or sculpted remains seems to be post-Mauryan, from the 2nd century BCE.\n
The main construction phases of Amaravati fall in two main periods, with the stupa enlarged in the second by additions to the main solid earth mound, faced with brick, consisting of railings (vedikā) and carved slabs placed around the stūpa proper. As elsewhere these slabs are usually called 'drum slabs' because they were placed round the vertical lower part or "drum" (tholobate) of the stūpa.\n
In the early period (circa 200-100 BCE), the stūpa had a simple railing consisting of granite pillars, with plain cross-bars, and coping stones. The coping stones with youths and animal reliefs, the early drum slabs, and some other early fragments belong to this period. The stūpa must have been fairly large at this time, considering the size of the granite pillars (some of which are still seen in situ, following excavations).\n
Reconstruction of the Amaravati Stupa, by or after Sir Walter Elliott 1845. 
The late period of construction started around ca. 50 BCE and continued until circa 250 CE. The exterior surfaces of the stupa and the railings were in effect all new, with the old elements reused or discarded. James Burgess in his book of 1887 on the site.\n
During the period of the decline of Buddhism in India, the stupa was neglected and was buried under rubble and grass. A 14th-century inscription in Sri Lanka mentions repairs made to the stupa, and after that it was forgotten. The stupa is related to the Vajrayana teachings of Kalachakra, still practiced today in Tibetan Buddhism.[24] The Dalai Lama of Tibet conducted a Kalachakra initiation at this location in 2006, attended by over 100,000 pilgrims.
   },
   "lepakshi hanging pillar":{
                   "place":"lepakshi hanging pillar",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "details":"The Lepakshi Temple is world famous for one exclusive engineering marvel- the Lepakshi Hanging Pillar. The temple has total 70 beautifully carved stone pillars.\n
The Archaeological Survey of India has done research on the Lepakshi Hanging Pillar and has proved that the construction of the pillar was not a mistake and imperfection.\n
On the other hand, it was the reflection of the engineering excellence and architectural brilliance of the designers, builders and sculptors of the ancient era. One of them is hanging and it does not touch the ground.  There is some space between the base of the pillar and the ground. A piece of cloth or paper can be passed from below this pillar. The pillar is said to be in the hall where the reception ceremony of Shiva and Parvati’s marriage took place.
   },
   "jatayu earth center":{
                   "place":"jatayu earth center",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Jatayu Earth Center, also known as Jatayu Nature Park or Jatayu Rock, is a park and tourism centre at Chadayamangalam in Kollam district of Kerala, India.\n
It stands at an altitude of 350m (1200ft) above the mean sea level. Jatayu Nature Park holds the distinction of having the world’s largest bird sculpture, which is of Jatayu.\n
The sculpture measures 200 feet (61 m) long, 150 feet (46 m) wide, 70 feet (21 m) in height and occupies 15,000 square feet (1,400 m2) of floor area). It was sculpted by Rajiv Anchal. 
This rock-theme nature park was the first Public–private partnership tourism initiative in the state of Kerala under the BOT model. The park is about 38 km (24 mi) away from the city of Kollam and 46 km (29 mi) away from the state capital, Thiruvananthapuram.\n
The park located near the town of Chadayamangalam (Jatayumangalam), which was named for Jatayu. Jatayu was a demi-god in Ramayana (a Hindu epic) who had the form of a vulture.According to the epic, Ravana was attempting to abduct Sita to Lanka when Jatayu tried to rescue her. Jatayu fought valiantly with Ravana, but as Jatayu was very old Ravana soon defeated him, clipping his wings, and Jatayu fell onto the rocks in Chadayamangalam.\n
Rama and Lakshmana while on the search for Sita, chanced upon the stricken and dying Jatayu, who informed them of the battle with Ravana and told them that Ravana had headed South.
   },
   "lepakshi veerabhadra temple":{
                   "place":"lepakshi veerabhadra temple",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Veerabhadra temple is a Hindu temple located in the Lepakshi, in the state of Andhra Pradesh, India. The temple is dedicated to the Virabhadra, a fierce incarnation of Lord Shiva. Built in the 16th century, the architectural features of the temple are in the Vijayanagara style with profusion of carvings and paintings at almost every exposed surface of the temple. It is one of the centrally protected monuments of national importance and is considered one of the most spectacular Vijayanagara temples.\n
The fresco paintings are particularly detailed in very bright dresses and colours with scenes of Rama and Krishna from the epic stories of the Ramayana, the Mahabharata and the Puranas and they are well preserved.\n
There is a very large Nandi (bull), mount of Shiva, about 200 metres (660 ft) away from the temple which is carved from a single block of stone, which is said to be one of the largest of its type in the world. The temple is home to many Kannada inscriptions as its located close to Karnataka border.\n
The temple is built in the Vijayanagara architechtural style and segregated into three parts, with an assembly hall, an ante chamber and a Sanctum Sanctorum. Two enclosures encircle the temple and the outer walled enclosure has three gates. A hall full of sculptures and paintings leads to the Sanctum Sanctorum. The painted images are all of celestial beings, saints, musicians and dancers, along with images of the 14 avatars of Shiva.\n
The Sanctum is flanked by elaborately carved figurines of Ganga and Yamuna. Carved images of horses and soldiers adorn the exterior columns. The hall also features carved images of Natesha and Brahma, while the column at the southwest part of the hall features an image of Parvati. Many other paintings and carvings adorn the walls, columns and ceilings.\n A life-size image of Lord Veerabhadra, wielding arms and decorated with skulls is installed in the Sanctum Sanctorum. The complex also houses a separate chamber located in the eastern wing which depicts carved images of Shiva and Parvati on a boulder. A huge boulder also depicts a carved image of a muilti-hooded serpent shielding a Lingam. An image of Lord Vishnu is also installed in a separate chamber"
   },
   "akkamahadevi caves":{
                   "place":"akkamahadevi caves",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Akkamahadevi caves have been named after Akka Mahadevi, who was a great saint and philosopher of 12th century. She is associated with Veerashaiva Bhakti movement and is said to have contributed greatly to the movement as well as to the Kannada Bhakti literature. She has done penance here in the caves. As per legend, Akkamahadevi offered prayers to the Shivalingam inside the cave.\n
Located at a distance of 18 km from Srisailam, Akkamahadevi Caves are the best place to see in Srisailam if you are looking for some adventure. These caves is also a popular religious shrine and is dedicated to Lord Shiva. Akkamahadevi Caves, located near the Krishna River,are naturally formed.\n
Akkamahadevi Caves present enchanting scenic beauty and tranquil environment which is combined with a bit of adventure. Although there are many naturally formed caves in the Nallamala hill ranges; Akkamahadevi caves are one of the most captivating of all. Visiting Akka Mahadevi Caves is one of the best parts of Srisailam Tourism.\n
As these caves are located in the forest, tourists are required to first take boat ride from Patala Ganga. which is followed by a small trek of few minutes. The boat ride to the caves is through the River Krishna; it is around 1 hour long."
   },
   "octopus view point":{
                   "place":"octopus view point",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Octopus View Point is one of the latest additions to the tourist attractions in Srisailam in Andhra Pradesh. The view point is located 5 km before Domalpenta and offers amazing views of the adjoining forests, enchanting gorges and the mesmerising backwaters of Krishna River. Octopus View Point has been named so because of Krishna River down below that looks like an octopus spread between the hillocks. It provides a spectacular bird’s eye view of the entire valley below. In addition to that, there is a regular safari tour conducted by the reserve that is the major highlight of the place."
   },
   "sakshi ganapathi temple":{
                   "place":"sakshi ganapathi temple",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Sakshi Ganapati Temple is located on the way to Srisailam. An important part of any Srisailam tour, this temple is visited by every devotee who comes to seek blessings of Sri Mallikarjuna Swamy. Amid the panoramic background of nature, this temple is located just a few km away from the Shikaram.\n
It is believed that a visit to Srisailam goes unrecorded if a devotee doesn’t visit Sakshi Ganapati Temple. The main deity of this temple is Lord Ganesha. The word Shakshi means the one who witnesses, which is representative of the belief that Lord Ganesha keeps a record of everyone who visits Mallikarjuna Jyotirlinga, which is then shown to Lord Shiva.\n
The idol of Lord Ganesha is also representative of the belief. The black idol of the Lord is shown holding a book in the left hand and a stylus in the right hand as if recording the names of the pilgrims coming to this temple."
   },
   "sri bhramarambha mallikarjuna temple":{
                   "place":"sri bhramarambha mallikarjhuna temple",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Sri Bhramaramba Mallikarjuna Temple or Srisailam Temple is a Hindu temple dedicated to the deities Shiva and Parvati, located at Srisailam in the Indian state of Andhra Pradesh.\n
It is significant to the Hindu sects of both Shaivism and Shaktism as this temple is referred to as one of the twelve Jyotirlingas of Shiva and as one of the eighteen Shakti Pithas, centres of the Hindu Goddess. Shiva is worshiped as Mallikarjuna, and is represented by the lingam. His consort Parvati is depicted as Bhramaramba.\n
When Shiva and Parvati decided to find suitable brides for their sons. Shiva got Buddhi (intellect), Siddhi (spiritual power), and Riddhi (prosperity) married to Ganesha.\n
Kartikeya on his return was enraged and went away to stay alone on Mount Krauncha in Palani in the name of Kumara brahmachari. On seeing his father coming over to pacify him, he tried to move to another place, but on the request of the Devas, stayed close by. The place where Shiva and Parvati stayed came to be known as Srisailam.\nAs per Hindu legend, the presiding deity in the form of Linga (an iconic form of Shiva) was worshipped with jasmine (locally called in Telugu as Mallika), leading to the name of presiding deity as Mallikarjuna. 
Mahashivaratri is the main festival celebrated at Srisailam Mallikarjuna Swamy temple."
   },
   "srishailam dam":{
                   "place":"srishailam dam",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"The Srisailam project began in 1960, Initially only as a power project. After several delays, the main dam was finally completed twenty years later in 1980 July 26.\n
 In the meantime the project was converted into a multipurpose facility with a generating capacity of 770 megawatts (1,030,000 hp) by its second stage which was completed in 1987. The dam is to provide water for an estimated 2,000 square kilometres (770 sq mi). Under the right bank branch canal 790 square kilometres (310 sq mi) in Kurnool and Kadapa districts will have assured irrigation.\n
From the initial modest estimate of ₹38.47 crore for a power project the total cost of the multipurpose project was estimated to cross ₹1000 crore in its enlarged form. The dam has alone cost ₹404 crore together with the installation of four generating sets of 110 MW each. The right bank branch canal is estimated to cost ₹449 crore and the initial investment of ₹140 crore has been provided by the World Bank.\n
The projected cost-benefit ratio of the project has been worked out at 1:1.91 at 10% interest on capital outlay.. In 1998 a coffer dam was over topped by flooding. The power house required repairs and did not generate power for a year. On 2 October 2009, Srisailam dam experienced a record inflow which threatened the dam."
   },
   "kapila theertham":{
                   "place":"kapila theertham",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"Kapila Theertham is a famous Saivite Temple and Theertham, located at Tirupati in the Tirupati District of Andhra Pradesh, India. The idol is believed to be installed by Kapila Muni and hence Lord Siva here is referred to as Kapileswara.\n
The temple stands at the entrance to a mountain cave in one of the steep and vertical faces at the foot of the Tirumala hills which are part of Seshachalam Hills, where the waters of the mountain stream fall directly into Temple Pushkarini known as "Kapila Theertham". A huge stone statue of a seated bull "Nandhi", Shiva's steed, greets devotees and passersby at the entrance to the temple.\n
The Temple and Theertham had derived its name from Kapila Muni .According to Temple Legend Kapila Muni had performed penance to Siva at this place and blissed with the Muni's devotion, Siva and Parvathi presented themselves. The Lingam is believed to be self-manifested. Kapila muni is believed to emerged from the Bilam (Cavity) in the Pushkarini(Theertham) on to the earth.\n
The temple received very good patronage from the Kings of Vijayanagara in the 13th thru 16th centuries, especially Saluva Narasimha Deva Raya, and the eternally famous Sri Krishna Deva Raya, and some of the later rulers like Venkatapathi Raya, and Aliya Ramaraya, Sri Krishna Deva Raya's Son-in-law."
   },
   "sri ranganatha swamy temple":{
                   "place":"sri ranganatha swamy temple",
                   "state":"Andra Pradesh",
                   "places":--,
                   "hotels":--,
                   "detials":"The Sri Ranganthaswami Temple in Nellore, Andhra Pradesh, India is a Hindu temple dedicated to Lord Ranganatha a resting form of Lord Vishnu. This temple, also called Talpagiri Ranganathaswami temple or Ranganayakulu is one of the oldest temples in Nellore.\n
It is located on the banks of the Penna River and is believed to have been constructed in the 12th century. Just before the main entrance of the temple is a huge tower, called Gaaligopuram, which literally means "wind tower". This tower is approximately 70 feet high and has 10 feet of gold plated vessels on top of it, called kalashams.\n
The gopuram was constructed by Yeragudipati Venkatachalam panthulu. Every year during the month of March–April (which varies according to the Indian calendar) a grand festival is celebrated. These are called Brahmotsavam."
   },
   "sri kalahasti temple":{
                  "place":"sri kalahasti temple",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":"Situated in Chittoor, Srikalahasti Temple is popular among devotees who visit the temple along with the highly revered Tirupati Temple, which is just 36 km away. Dedicated to Lord Shiva, Kalahasti temple has immense religious importance for Hindus and was constructed in the year 1516 by Krishnadevraya, a king of the Vijayanagara empire.\n
The elaborate structure of the Srikalahasti temple complex is a breathtaking view right from the entrance. It has intricate carvings of numerous mythological illustrations that one can explore in the divine surroundings. This magnificent temple is often reffered as the Kailasa and Kashi of the south. The temple represents one of the five elements (Pancha Bhoota) - Air or Vayu.\n
The place has an abundance of vibrant, divine aura and has the potential to draw visitors with its ornate shrines and mesmerising beauty. Srikalahasti is an excellent example of South Indian temple architecture where highly ornamented gopurams with expansive intricately carved interiors unfold the magnificent treasures of the Dravidian style of architecture.\n
The temple is also regarded as Rahu-Ketkshetra and Dakshina Kailasam. The inner temple was constructed around the 5th century and the outer temple was constructed in the 11th century by the Rajendra Chola I, later Chola kings and the Vijayanagara kings. Shiva in his aspect as Vayu is worshipped as Kalahasteeswara."
   },
   "tirupathi vekateshwara temple":{
                  "place":"tirupathi venkateshwara temple",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":"Srimad-Bhagavatam describes the history of Tirumala that during Satya yuga, Hiranyaksha, due to his exploitative activities created a situation where the earth was drowned to the bottom of the Garbhodaka ocean. At that time, the demigods approached Lord Brahma who prayed to Lord Vishnu.Lord Vishnu then appeared from the nose of Brahma in the form of Sri Varahadev. He killed Hiryanaksha and lifted the earth, ‘Bhudevi’ with His tusks, and brought her to a safe position on top of the Garbhodaka ocean.\n
Venkateswara Temple is a landmark Vaishnavite temple situated in the hill town of Tirumala at Tirupati in Chittoor district of Andhra Pradesh, India. The Temple is dedicated to Lord Sri Venkateswara, an incarnation of Vishnu, who is believed to have appeared here to save mankind from trials and troubles of Kali Yuga. Hence the place has also got the name Kaliyuga Vaikuntham and Lord here is referred to as Kaliyuga Prathyaksha Daivam.\n
The temple is also known by other names like Tirumala Temple, Tirupati Temple, Tirupati Balaji Temple. Lord Venkateswara is known by many other names: Balaji, Govinda, and Srinivasa."
   },
   "kailasagiri":{
                  "place":"kailasagiri",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":"Situated on top of a hill in Visakhapatnam, Kailasagiri Park offers a panoramic view. Kailasagiri Park got its name from the 40 feet tall statue of Shiva and Parvati located here. The main attractions here include Floral Clock, Titanic Viewpoint, Jungle Trails, Shanti Ashram and Shank Chakra Nama.\n
It is a complete tourist destination that offers its visitors a degree of religion, adventure and joy. It is a center of tourist activities due to its serene environment and enchanting natural beauty.\nKailasagiri Park was developed by the Visakhapatnam Metropolitan Region Development Authority (VMRDA). The park is spread over 380 acres (150 ha) of land which includes vegetation and tropical trees.\n
Kailasagiri is one of the major attractions and a popular picnic spot for all the tourists visiting the beautiful city of Vizag.Kailasagiri is also a famous place for paragliding with excellent gliding facilities. There are many eateries around this park to satisfy one's hunger.
This beautiful hilltop is a must visit place for tourists for its breathtaking views and plethora of entertainment options.To protect the environment, VMRDA has declared the hill a plastic free zone.
It is a fun place for all age groups as it offers you a cable car ride at a very reasonable price.
There is a toy train that runs around the park and you can enjoy the train ride as well as the park and the amazing view."
   },
   "sri varaha lakshminarashima swamy temple":{
                  "place":"sri varaha lakshminarashima swamy temple",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":" Known as Simhachalam temple, is a Hindu temple located in the Simhachalam hills of the Eastern Ghats near the Visakhapatnam metropolis of Andhra Pradesh state , India . It is situated at a height of 300 meters and is dedicated to the " Varaha Narasimha " form of Lord Vishnu . Except on Akshaya Tritiya, this idol is covered with sandalwood on all other days due to which the idol looks like 'Shivlang'.\n
On the holy day of Akshaya Tritiya (Vaishakh month), the beauty of Sinhachal mountain is unique. On this holy day, Lord Lakshminrisingh present here is adorned with sandalwood. It is believed that the real form of the idol of the Lord can be seen only on this day. Sinhachal area is considered to be one of the very few ancient temples in the world built in the eleventh century.\n
It is believed that sage Pururava was once traveling by air with his wife Urvashi. During the journey, his plane got affected by some natural force and reached Sinhachal region of the south. He saw that the image of the Lord was contained in the womb of the earth. He took out this statue and cleaned the dust accumulated on it. During this time, a voice came from the sky that instead of cleaning this statue, it should be covered with sandalwood paste.\n
He also received an order in this Akashvani that this sandalwood paste would be removed from the body of this idol only once a year, on the third day of the month of Vaishakh, and the real idol could be seen. Following Akashvani, this statue was coated with sandalwood and the coating is removed from this statue only once a year. Since then the idol of Lord Shri Lakshminrisingh Swami was installed in Sinhachal itself.\n
The word 'Sinhachal' means mountain of lion. This mountain is considered to be the abode of Lord Narasimha, the fourth incarnation of Lord Vishnu . It is believed that Lord Narasimha had descended at this place to protect his devotee Prahlad . According to Sthal Purana, devotee Prahlad had built the first temple of Lord Narasimha at this place. Devotee Prahlad had built this temple after the killing of his father by Lord Narasimha.\n
But after Kritayuga , this temple could not be maintained and this temple fell into ruins. Later, Pururavas of Lunar dynasty once again discovered this temple and got it rebuilt. A view of the temple's complex in which the rajagopuram and the vimana can be seen adjacent to each other."
   },
   "submarine museum":{
                  "place":"submarine museum",
                  "state":"Andra Pradesh",
                  "places":--,
                  "hotels":--,
                  "detials":"During the Indo-Pakistani War of 1971, Kursura operated in the Arabian Sea. She was given the patrol duties at two designated areas before the war started, but was ordered to operate under two restrictions: she was not to cross demarcated shipping corridors and she could attack a target only after positive identification. The aims of her patrol were to sink any Pakistani naval warships, to sink merchant shipping when specifically ordered, and to conduct general patrol and surveillance. \n
She started from her home port on 13 November 1971 and reached her patrol location by 18 November. She remained there until 25 November when she was shifted to a new patrol location and remained there until 30 November. On 30 November, she rendezvoused with Karanj at sea to transfer instructions and subsequently then left for Bombay and reached there by 4 December 1971. During her patrols, she encountered fair weather and monitored a number of tankers and commercial aircraft flying on international routes. She was originally intended to lay mines but the plan was later cancelled."
   },
}




 
  
                   
import tkinter as tk    
from tkinter import ttk
from tkinter import messagebox


# Replace this placeholder data with your actual data
data = {
    "aizawl": {
        "place": "aizawl",
        "state": "Mizoram",
        "places":"durtlang hills,reiek,vantawang,Mizoram state,KV    paradise,soloman temple",
        "hotels":"    ",
        "details": " Aizwal is one of the oldest northeastern cities in India and the capital city of Mizoram. Sitting at a height of 1132 m above sea level, this beautiful Mizoram tourist place is inhabited predominantly by the Mizo tribe. The quaint little place is replete with lush greenery and an abundance of natural beauty.",
    },
    "serchhip": {
        "place": "Serchhip",
        "state": "Mizoram",
        "places":"vantawangfalls,chhingpuiithlan Thenzawlparagliding in serchhip",
        "hotels":"    ",
        "details": " Most famous for being the district with the highest literacy rate in India, Serchhip in Mizoram is a place that can provide you a unique and vibrant experience. This small town can give one the experience of a small village, the life, activities and colors that it sustains in the everyday. Some of the popular villages one can visit are the Neihloh and Buangpuri. The nature too plays a role in tourism with spots such as the Vantawng Khawhltha water fall. Other places here include the Chhingpui Thlan and Hriantrengna lung.",
    },
    "lunglei": {
        "place": "lunglei",
        "state": "Mizoram",
        "places":"khawlungwwildlife sanctuary,lunglei sight seeing,",
        "hotels":"    ",
        "details": "  Mizoram's Enthralling Off-Beat Paradise Lunglei Tourism natural setting. It is a small town, located around 170 km south of Aizawl whose name is derived from a bridge shaped rock found along Nghasih which is a tributary of the river Tlawng. Lunglei is an ideal offbeat destination for those who love natural sightseeing and adventure activities bundled into one. Trekking, bird watching and camping are among the popular activities opted by tourists coming to visit Lunglei. Lunglei is a biodiverse region, home to Thorangtlang Wildlife Sanctuary and Saza Wildlife Sanctuary. While Saza Wildlife Sanctuary is famous for hosting migratory and endemic bird species, Thorangtlang Wildlife Sanctuary is home to several animal species such as leopards, tigers, porcupines and leaf monkeys among many. Visiting the Lunglei Rock Bridge at the Nghasih stream is another popular activity while here. For those looking to learn about the culture and traditions of the region, the Saikuti Hall is a must-visit.",
    },
    "champhai": {
        "place": "champhai",
        "state": "Mizoram",
        "places":"rihsil,murlen national park,lengteng wildlife sanctuary ",
        "hotels":"    ",
        "details": "The town of Champhai on the eastern border of Mizoram close to the Indo-Myanmar border is the administrative headquarters of the Champhai district. It is located at a distance of 188 Kms from the capital of Aizawl and is strategically and commercially important for the state of Mizoram as well as for India. Champhai and its surrounding regions are primarily known for their natural beauty and vast valleys of rice fields. It is known as the 'Rice Bowl of Mizoram' due to being a major region of rice cultivation. Also, its vibrant seasonal orchids lend it a certain romanticism and aesthetic appeal.Champhai has a number of tourist attractions mostly including natural settings. These include a cave called the Kungawrhi Puk, a river called Tiau Lui, Lianchhiari Lunglen Tlang and a few more. Rih Dil Lake is another famous natural attraction known to Champhai and the state of Mizoram. Adventure enthusiast can indulge in some trekking at the Thasiama Seno Neihna which is about 83 Kms south of Champhai.",
    },
     "saiha": {
        "place": "saiha",
        "state": "Mizoram",
        "places":"plak wildlife sanctuary,palak dil",
        "hotels":"    ",
        "details": " Saiha is known as the fastest growing town in Mizoram, as the population has significantly risen in the last decade. Saiha is a census town in the Saiha district in Mizoram located at an average height of 729 meters above sea level. This town is considered to be a haven for angling enthusiasts.Revealing the mystery behind the name of the town, the name of the town was originally Siaha where 'Sia' stands for elephant and 'ha' meaning tooth - An elephant tooth. But the Mizos traditionally call it Saiha",
    },
     "vantawng": {
        "place": "vantawng falls",
        "state": "Mizoram",
        "places":"   ",
        "hotels":"hotel dinthar zara,zobawm homestay,aizwal guest house homestay ensuite",
        "details": " The highest waterfall in the state and the 13th highest in the country, the Vantawng Waterfalls is one of he most mesmerizing waterfalls of the North East. Vantawng falls are the pride of Mizoram and one of its prime attractions. The waterfall which is located 137 km away from the capital city of Aizawl is a gem in its own right. Tucked in between the verdant valleys with thick greenery around the waterfall seems like a river of white milk from distance.People flock from all directions of the state to have a look at its might and beauty. The waterfall can only be viewed from distance due to thick forest covering around it. It is located in the Vanva River near Thenzawl which is known for its rampaging speed of flow. Vantawng Falls are testament to the amazing natural beauty that is hidden within the North-East.",
    },
    "phawnpui": {
        "place": "phawnpui",
        "state": "Mizoram",
        "places":"",
        "hotels":" hotel dinthar zara,zobawm homestay,aizwal guest house homestay ensuite ",
        "details": "  Phawngpui is a quaint and serene village located in the state of Mizoram. Situated at an elevation of 2157 meters, this place proffers picturesque views. This place is surrounded by verdant trees and lofty mountains which in magnifying the beauty of the landscape. The place does not only have verdant and thick forests but is also bountiful in flora and fauna. If you want to add a bit of adventure to your trip, make sure to scale the Blue Mountain and enjoy the trek with mesmerizing scenic beauty. The trek to the top of the mountain will provide awestruck views of the whole place which will make you feel as if you are in heaven.",
    },
    "shillong": {
        "place": "Shillong",
        "state": "Meghalaya",
        "places": "Umiam Lake, Elephant Falls, Shillong Peak, Don Bosco Museum, Police Bazar, Meghalaya State Museum",
        "hotels": "   ",
        "details": "Nestled amidst the pine-clad hills, Shillong, the capital of Meghalaya, unfolds like a picturesque canvas at an elevation of 1496 meters. Revered as the 'Scotland of the East,' the city offers a delightful blend of captivating landscapes, pleasant weather, and rich traditions.\n\nShillong derives its name from Lei Shyllong, an idol worshipped at the Shillong Peak, and is home to diverse tribal communities like Khyrim, Mylliem, Maharam, Mallaisohmat, Bhowal, and Langrim, each contributing to the vibrant cultural tapestry.\n\nProminent attractions include Umiam Lake, a sprawling reservoir surrounded by hills that offer a serene escape, and the tranquility of the Elephant Falls, cascading gracefully amidst lush greenery. For adventure enthusiasts, the Laitlum Canyons unveil breathtaking panoramic views, making it a must-visit for trekking.\n\nShillong is not just a haven for nature lovers; it boasts museums and cultural gems like the Don Bosco Museum, showcasing the indigenous cultures of the Northeast. The Meghalaya State Museum is another treasure trove, delving into the state's heritage through artifacts and exhibits. The bustling Police Bazar, a vibrant market, captures the pulse of Shillong with its lively atmosphere and diverse shopping experiences.\n\nVenturing beyond the city limits, Mawphlang stands as a testament to Meghalaya's cultural heritage, known for its sacred groves and traditional rituals. On the other hand, Mawlynnong, acclaimed as the cleanest village in Asia, beckons with its living root bridges and pristine landscapes.\n\nShillong's musical heartbeat resonates through its title as the 'music capital of India.' The city's westernized culture and youthful vibe contribute to its dynamic music scene. Throughout the year, music events and festivals celebrate Shillong's rich musical heritage. The city's charm lies not just in its natural beauty but also in the warmth of its people, making it a destination that lingers in the hearts of those who explore its scenic wonders and cultural richness."
    },
    "elephanta": {
        "place": "Elephant Falls",
        "state": "Meghalaya",
        "places": "",
        "hotels": "Woodland Hill Stay, Mid Pine Homestay",
        "details": "Named after an Elephant-like stone at its foot, the Elephant Falls are amongst the most popular falls in the North-East, situated next to Shillong. It is a tourists' paradise with three layers of the falls accessible to the layman from different vantage points. The Britishers named this fall so owing to the presence of an elephant-shaped rock on one side of the fall. However, the stone disintegrated and was washed away due to an earthquake in 1897.\n\nElephant Waterfalls is a superb place for spending some time in the midst of nature while capturing the incredible moments for your keepsake.\n\nThe breathtaking Elephant falls were referred to as 'Ka Kshaid Lai Pateng Khohsiew' by the local Khasi people, which means 'The Three Step Waterfalls,' as these falls consist of three mesmerizing falls in succession. The first of the three waterfalls is tucked between the dense trees and is very broad. The second waterfall reduces to thin strands of water and is almost negligible in winters due to the receding water levels. The third and the most visible waterfall is the tallest with clear water flowing like a sheet of milk on the dark rocks in the backdrop. Out of the three, the third waterfall tends to strike the visitors as the most impressive. Elephant Falls is a great stopover destination before one heads for further journeys into Meghalaya. Located 12 km away from the capital city of Shillong, it is one of the most visited falls in the beautiful state."
    },

    "double_decker": {
        "place": "Double Decker Living Root Bridge",
        "state": "Meghalaya",
        "places": "Dawki, Nohkalikai Waterfalls, Mawlynnong, Mawsmai Falls, The Eco Park, Krem Phyllut, Mawsmai Cave, Thangkharang Park and Ka Khah Ramhah, Nongsawlia",
        "hotels": "7 Sisters Falls View Inn, Goshen Homestay",
        "details": "Hidden deep in the lush, green forests of the wettest place in India, Cherrapunjee, Meghalaya; one can find the magnificent Jingkieng Nongriat Double Decker Living Root Bridge, more commonly known as the Umshiang Double Decker Living Root Bridge or simply just the Double Decker Root Bridge. This area is famous for root bridges made of Indian Rubber Tree, but the Double Decker Bridge is the most famous of all due to its large size. It is 3 kilometers long and placed at a height of 2400 feet! A unique attraction and quite an innovative mix of nature and engineering. The Umshiang River flows beneath the bridge."
    },
    "cherrapunji": {
        "place": "Cherrapunji",
        "state": "Meghalaya",
        "places": "Double Decker Living Root Bridge, Dawki, Nohkalikai Waterfalls, Mawlynnong, Mawsmai Cave, Mawsmai Falls",
        "hotels": "Sulawado Resort, Polo Orchid Resort"
    },

    "mawsynram": {
        "place": "Mawsynram",
        "state": "Meghalaya",
        "places": "Mawsmai Caves, Mawsmai Falls, Nohkalikai Falls, Mawlyngbna, Cherrapunjee",
        "hotels": "Polo Orchid Resort, Aisha Guest House Bed and Breakfast"
    },
    "balpakram": {
        "place": "Balpakram National Park",
        "state": "Meghalaya",
        "places": "Siju Caves, Siju Wildlife Sanctuary, Nokrek National Park, Tura Peak, Rongbang Dar Waterfalls, Naphank Lake, Pelga Falls, Garo Hills",
        "hotels": "Hotel Polo Orchid Tura, Karlyansa Homestay",
        "details": "Located in the southern Garo Hills in Meghalaya, about 167 Kms from Tura, Balpakram National Park lies at an elevation of about 3,000 feet above sea level. The Park is a famous national park well known for its pristine beauty. The word Balpakram means the 'land of perpetual winds,' and the national park is blessed with charming grace and breathtaking scenes.\n\nThe government of Meghalaya created the Balpakram National Park on 15 February 1986. Today, the area boasts a myriad of species of fauna and flora, including the rare Lesser Panda, the Indian Bison, and the Stag-like Serow. A variety of very rare medicinal herbs, locally known as 'dikges,' also grow abundantly in Balpakram. One can find a deep gorge in Balpakram, popularly compared to the Grand Canyon of the United States. The gorge is referred to as the 'land of the spirits,' believed to be where the spirits of the dead live temporarily before embarking on the journey towards their final abode. The Balpakram National Park is rightly termed as a traveler's paradise and is a must-visit while in Meghalaya."
    },
    "william": {
        "place": "Williamnagar",
        "state": "Meghalaya",
        "places": "Simsang River, Naka Chiklong, Domre Falls, Mrik Wari, Siju Caves, Simsang Festival",
        "hotels": "",
        "details": "Williamnagar, located 244 Kms from Shillong, was formed around the former town of Simsanggre, based on the large plains of the Simsang River. A very remote area known for its abundance of natural beauty, being flanked by mountains and having a rich composition of both water and vegetation. Williamnagar, the headquarters of the East Garo Hills district of Meghalaya, was named after Captain Williamson A. Sangma, the first Chief Minister of the State of Meghalaya. Williamnagar is of immense historical importance as it was here that the Garos made their last major resistance to the British invasion into Garo Hills during the year 1837."
    },

    "nohkalikai": {
        "place": "Nohkalikai Waterfalls",
        "state": "Meghalaya",
        "places": "Nongsawlia, Mawsmai Cave, Krem Phyllut, Dainthlen Waterfall, The Eco Park, Thangkharang Park and Khoh Ramahah, Wabaka Falls, Mawsmai Falls",
        "hotels": "7 Sisters Falls View Inn, Goshen Homestay",
        "details": "Tallest Waterfall in India, Nohkalikai Waterfalls is the fourth-highest waterfalls in the world, plunging some 335 meters from a verdant cliff to the ground, giving the portrayal of immense and natural magnificence. The falls are one of the most beautiful and grand waterfalls in the country, tucked between the evergreen rainforest of the Khasi Hill. The falls plunge into a lagoon that is as blue as the afternoon sky. Nohkalikai Falls is one of the most popular and significant places to see in the North-East. The falls are attached to a sad story of a woman named Ka Likai, making it a place of historical significance."
    },

    "mawsmai": {
        "place": "Cherrapunjee",
        "state": "Meghalaya",
        "places": "Dawki, Nohkalikai Waterfalls, Mawlynnong, Mawsmai Falls, The Eco Park, Krem Phyllut, Mawsmai Cave, Thangkharang Park and Ka Khah Ramhah, Nongsawlia",
        "hotels": "7 Sisters Falls View Inn, Aisha Guest House",
        "details": "Meghalaya is home to some amazing and mysterious cave systems, and Mawsmai Cave is by far the most popular of the lot. Located just 6 km away from the heart of Cherrapunjee, Mawsmai cave is a breathtaking maze of caves in the East Khasi Hills of Meghalaya. The well-lit caves are a view to behold when the glistening lights meet with the limestone to create countless hues and patterns of light. There is plenty of flora and fauna within the cave to catch one's attention. The length of the cave is just 150 meters, which is not the longest compared to the other caves in the region, but it surely provides one a glimpse of life underground. Mawsmai Caves are best seen on a trip to Cherrapunjee or Shillong. Start your trip with Cherrapunjee, not missing the caves while here and follow it with a trip to Shillong."
    },


    "dwaki": {
        "place": "Meghalaya",
        "state": "Meghalaya",
        "places": "Cherrapunjee, Shillong, Jowai",
        "details": "Dawki, a small town in India located in the Jaintia Hills district of Meghalaya, has become a hotspot for travelers looking to explore the unexplored. Tourists visit here for its unique landscape, crystal-clear river, and beautiful greenery. The main reason why anyone should visit Dawki is to experience its pristine beauty and the crystal-clear Umngot River. The river is so clean that you can even see the riverbed from the surface. A popular activity here is to go for a boat ride along the river and witness the beautiful landscape. There are many tourist spots and attractions in Dawki that are worth exploring. One of the main attractions is the living root bridge, which is made by the local people from the roots of the rubber tree. The bridge is a unique example of nature's beauty and can be reached after a short trek. Other attractions include the Khasi Hills, the local markets, and the nearby rainforests. One of the highlights of Dawki is the Dawki-Shnongpdeng border, which is the only legal border between India and Bangladesh. Tourists can also visit the Shnongpdeng village and explore the local culture. When visiting Dawki, there are some things that travelers should keep in mind. It is advised to carry a valid ID proof and a travel permit from the local authorities. It is also important to dress accordingly and respect the local customs. Lastly, it is advisable to travel with a local guide who can provide valuable insights into the local culture and attractions. Overall, Dawki is a great place to explore the unexplored and experience nature's beauty. From the river to the local markets, there are plenty of attractions and activities to keep visitors entertained. With its pristine beauty, it is sure to become a favorite spot for travelers in the coming years.",
        "hotels": ""
    },
    "imphal": {
        "place": "Imphal",
        "state": "Manipur",
        "places": "Loktak Lake and Sendra Island, Kangla Fort, Tharon Cave, Shaheed Minar, INA Memorial, Keibul Lamjoa National Park",
        "hotels": "Manipur House, Nature's Retreat Homestay, John House, Hill View Homestay",
        "details": "Imphal has an untouched charm surrounding its natural beauty, sceneries, and landscapes as well as significant history leaving hints of the past around the city. The lush green landscapes, beautiful surroundings, unexplored territories, and undulating rivers of Imphal make for a great tourist destination. This site of the battle of Imphal during World War II assumes a certain importance, derived from history. The two together give Imphal a number of tourist destinations which include INA memorial, Manipur State museum, Kangla Fort, Langthabal, war cemeteries, Shri Govindjee temple as well as the Waithou and Loktal lake. Manipur Zoological gardens and Keibul Lamjao National park are also places one might not want to miss."
    },
    "thoubal": {
        "place": "Manipur",
        "state": "Manipur",
        "places": "Ikop, Khongjom, Loktak Lake, Lousi, Pumlen",
        "hotels": "",
        "details": "A well-developed city, Thoubal is a good holiday destination for those looking for a pleasant climate and numerous activities. Thoubal is almost ideal for trekking, hiking, and picnics given the abundance in flora and green landscapes as well as the various facilities available here. This city is most famous for the temples and the numerous water bodies all together making it a pretty much perfect getaway which will strike the right balance of urban and a lesser-known destination. Just to add in the environment a dash of activity and vibrancy, are the popular bazaars of the town such as the Ningombam Laxmi Bazaar and Athokpam Bazaar."
    },
    "tamenglong": {
        "place": "Manipur",
        "state": "Manipur",
        "places": "Barak Waterfalls, Zeilad Lake, Buning Meadows, Tharon Cave, Forests Nearby, Local Festivals",
        "hotels": ""
    },
    "chandel": {
        "place": "Manipur",
        "state": "Manipur",
        "places": "Yangoupokpi Lokchao Wildlife Sanctuary, Tengnoupal, Moreh",
        "hotels": "",
        "details": "Chandel, also known as Lamka is a tiny but scenic district in the North-Eastern state of Manipur. It is one of the main nine districts in the state and also the second least populous of all. Situated along the lines of the international border separating India and Myanmar, it has come to be known as Gateway to Myanmar. It lies about 64 kms away from Imphal, with NH-39 passing through. It’s famous for being home to more than 20 native tribes. Chandel is a wisp of culture and traditions, given the huge number of tribes that live here. Each tribe offers a unique identity to the area, where colours of their cultures are blown out in all directions. Travelers visiting Chandel can soak in the alluring art forms along with sprightly music and dance."
    },








}






def search_place():
    global nm
    

    place = entry.get()
    place=place.lower()
    if place in data:

        
        info_text.delete(1.0, tk.END) 
        info_text.insert(tk.END, f"Place: {data[place]['place']}\n\n"
                                  f"State: {data[place]['state']}\n\n"
                                  f"Places: {data[place]['places']}\n\n"
                                  f"Hotels: {data[place]['hotels']}\n\n"
                                  f"Details: {data[place]['details']}")
        
        

        global image_label
        nm=place
        img = tk.PhotoImage(file=place)
        image_label = tk.Label(window, image =img)
        image_label.place(x=750, y=280)
        engine.say(info_text.get(1.0, tk.END))
        engine.runAndWait()
    else:
       



        def pop():
            info_text.delete(1.0, tk.END)
            messagebox.showinfo('sorry',"Place Not Found\n\n\nCheck the spelling or enter different place")
        pop()

def clear_entry():
    entry.delete(0, tk.END)
    info_text.delete(1.0, tk.END)
    image_label.destroy()


window = tk.Tk()
window.title("Place Guide")

custom_font = ("Arial", 16)
a=tk.PhotoImage(file="C:\\Users\\Abhishek Patil\\python\\mini project\\bg1.png")
l1=tk.Label(window,image=a).pack()


#hariyana
image_path ="C:\\Users\\Abhishek Patil\\python\\mini project\\west bengal\\MIDNAPORE1.png"
sanctuary="C:\\Users\\Abhishek Patil\\python\mini project\\Haryana\\bird sanctuary 2)1.png"
chandigarh="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\Chandigarh (2)1.png"
damdama="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\damdama lake (2)1.png"
kurukshetra="C:\\Users\\Abhishek Patil\\python\\mini project\Haryana\\download (1)1.png"
kalesar="C:\\Users\Abhishek Patil\\python\mini project\\Haryana\\kalesar national park1.png"
manesar="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\manesar2)1.png"
morni="C:\\Users\\Abhishek Patil\\python\mini project\\Haryana\\morni hills)1.png"
panipat="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\panipat)1.png"
rohtak="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\rohtak)1.png"


#jarkhand
betal="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\betla national park1.png"
bokaro="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\bokaro steel cityd (1)1.png"
dhanbad="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\dhanbad (1)1.png"
hazarirbagh="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\hazariribagh (1)1.png"
jamshedpur="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\jamshedpur1)1.png"
massanjore="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\massanjore dam (1)1.png"
ranchi="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\ranchi1)1.png"


#kerla
bekal="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\bekal (1)1.png"
devikulam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\devikulam(1)1.png"
guruvayur="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\guruvayur1.png"
kasaragod="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kasaragod)1.png"
kochi="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kochi(2)1.png"
kollam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kollam)1.png"
kottayyam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kottayyam (1)1.png"
kovalam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kovalam1)1.png"
kumarakom="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kumarakom2)1.png"
kumuly="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kumuly1)1.png"
malampuja="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\malampuja)1.png"
muthanga="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\muthanga wildlife)1.png"
palakkad="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\palakkad)1.png"
peerumedu="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\peerumedu(1)1.png"
ponmudi="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\ponmudi(1)1.png"
ponnani="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\ponnani(1)1.png"
sabarimalad="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\sabarimalad (1)1.png"
thekkady="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\thekkady1)1.png"
thenmala="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\thenmala1)1.png"
thiolpetty="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\thiolpetty1)1.png"
trivandram="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\trivandram1)1.png"
wayanand="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\wayanand(2)1.png"






#manipur
chandel="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Manipur\\chandel (1)1.png"
inphal="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Manipur\\inphal)1.png"
loktak="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Manipur\\loktak lake (1)1.png"
tamengolong="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Manipur\\tamengolong(1)1.png"
thoubal="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Manipur\\thoubal (1)1.png"



#meghalay
balakram="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Meghalaya\\balakram national park1).png"
cherapunjee="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Meghalaya\\cherrapunjee (1)1.png"
double_decker="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\double decker bridge1)1.png"
dwaki="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\dwaki(1)1.png"
elephanta="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\elephant falls (1)1.png"
mawsmai="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\mawsmai caved (1)1.png"
nahkoli="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\nahkoli waterfalls (1)1.png"
shilong="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\\Meghalaya\\shillong1)1.png"
william="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\William nagar1)1.png"


#mizoram
aizawl="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\aizawl.png"
champhai="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Mizoram\\champhai (1)1.png"
lunglei="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\lunglei(1)1.png"
phawngupui="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\phawngpui(1)1.png"
saiha="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\saiha (1)1.png"
serchhipd="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\serchhipd (1)1.png"
vanthawng="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\vanthawng falls1)1.png"


#mp
bandhavgarh_park="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\bandhavgarh national park(1)1.png"
bhopal="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\bhopal (1)1.png"
dharampuri="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\dharampuri1)1.png"
gwalior="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\gwalior (1)1.png"
indore="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\indore(1)1.png"
jabalpur="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\jabalpur (1)1.png"
kanha="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\kanha national park (1)1.png"
kuno="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\kuno national park)1.png"
maheshwar="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\maheshwar1)1.png"
shivapuri="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\shivapuri (1)1.png"
uzzain="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\uzzain (1)1.png"



  
#img = tk.PhotoImage(file=place)



entry_label = tk.Label(window, text="Enter Place:",font=custom_font)
entry_label.place(x=80,y=110)

entry = tk.Entry(window ,width=30,borderwidth=10,fg="black",font=custom_font)
entry.place(x=200,y=100)



search_button = tk.Button(window, text="Search",bg='gray',fg='blue', command=search_place)
search_button.place(x=350,y=150)


info_text = tk.Text(window, width=50, height=22,bg='lightgrey',borderwidth=10,font=custom_font)
info_text.place(x=120,y=220)

clear_button = tk.Button(window, text="Clear",bg='gray',fg='red', command=clear_entry)
clear_button.place(x=600, y=110)





window.mainloop()





'''















import tkinter as tk    
from tkinter import ttk
from tkinter import messagebox
import my_img
import imgmod


data = {
    "aizawl": {
        "place": "aizawl",
        "state": "Mizoram",
        "places":"durtlang hills,reiek,vantawang,Mizoram state,KV    paradise,soloman temple",
        "hotels":"    ",
        "details": " Aizwal is one of the oldest northeastern cities in India and the capital city of Mizoram. Sitting at a height of 1132 m above sea level, this beautiful Mizoram tourist place is inhabited predominantly by the Mizo tribe. The quaint little place is replete with lush greenery and an abundance of natural beauty.",
    },
    "serchhip": {
        "place": "Serchhip",
        "state": "Mizoram",
        "places":"vantawangfalls,chhingpuiithlan Thenzawlparagliding in serchhip",
        "hotels":"    ",
        "details": " Most famous for being the district with the highest literacy rate in India, Serchhip in Mizoram is a place that can provide you a unique and vibrant experience. This small town can give one the experience of a small village, the life, activities and colors that it sustains in the everyday. Some of the popular villages one can visit are the Neihloh and Buangpuri. The nature too plays a role in tourism with spots such as the Vantawng Khawhltha water fall. Other places here include the Chhingpui Thlan and Hriantrengna lung.",
    },
    "lunglei": {
        "place": "lunglei",
        "state": "Mizoram",
        "places":"khawlungwwildlife sanctuary,lunglei sight seeing,",
        "hotels":"    ",
        "details": "  Mizoram's Enthralling Off-Beat Paradise Lunglei Tourism natural setting. It is a small town, located around 170 km south of Aizawl whose name is derived from a bridge shaped rock found along Nghasih which is a tributary of the river Tlawng. Lunglei is an ideal offbeat destination for those who love natural sightseeing and adventure activities bundled into one. Trekking, bird watching and camping are among the popular activities opted by tourists coming to visit Lunglei. Lunglei is a biodiverse region, home to Thorangtlang Wildlife Sanctuary and Saza Wildlife Sanctuary. While Saza Wildlife Sanctuary is famous for hosting migratory and endemic bird species, Thorangtlang Wildlife Sanctuary is home to several animal species such as leopards, tigers, porcupines and leaf monkeys among many. Visiting the Lunglei Rock Bridge at the Nghasih stream is another popular activity while here. For those looking to learn about the culture and traditions of the region, the Saikuti Hall is a must-visit.",
    },
    "champhai": {
        "place": "champhai",
        "state": "Mizoram",
        "places":"rihsil,murlen national park,lengteng wildlife sanctuary ",
        "hotels":"    ",
        "details": "The town of Champhai on the eastern border of Mizoram close to the Indo-Myanmar border is the administrative headquarters of the Champhai district. It is located at a distance of 188 Kms from the capital of Aizawl and is strategically and commercially important for the state of Mizoram as well as for India. Champhai and its surrounding regions are primarily known for their natural beauty and vast valleys of rice fields. It is known as the 'Rice Bowl of Mizoram' due to being a major region of rice cultivation. Also, its vibrant seasonal orchids lend it a certain romanticism and aesthetic appeal.Champhai has a number of tourist attractions mostly including natural settings. These include a cave called the Kungawrhi Puk, a river called Tiau Lui, Lianchhiari Lunglen Tlang and a few more. Rih Dil Lake is another famous natural attraction known to Champhai and the state of Mizoram. Adventure enthusiast can indulge in some trekking at the Thasiama Seno Neihna which is about 83 Kms south of Champhai.",
    },
     "saiha": {
        "place": "saiha",
        "state": "Mizoram",
        "places":"plak wildlife sanctuary,palak dil",
        "hotels":"    ",
        "details": " Saiha is known as the fastest growing town in Mizoram, as the population has significantly risen in the last decade. Saiha is a census town in the Saiha district in Mizoram located at an average height of 729 meters above sea level. This town is considered to be a haven for angling enthusiasts.Revealing the mystery behind the name of the town, the name of the town was originally Siaha where 'Sia' stands for elephant and 'ha' meaning tooth - An elephant tooth. But the Mizos traditionally call it Saiha",
    },
     "vantawng": {
        "place": "vantawng falls",
        "state": "Mizoram",
        "places":"   ",
        "hotels":"hotel dinthar zara,zobawm homestay,aizwal guest house homestay ensuite",
        "details": " The highest waterfall in the state and the 13th highest in the country, the Vantawng Waterfalls is one of he most mesmerizing waterfalls of the North East. Vantawng falls are the pride of Mizoram and one of its prime attractions. The waterfall which is located 137 km away from the capital city of Aizawl is a gem in its own right. Tucked in between the verdant valleys with thick greenery around the waterfall seems like a river of white milk from distance.People flock from all directions of the state to have a look at its might and beauty. The waterfall can only be viewed from distance due to thick forest covering around it. It is located in the Vanva River near Thenzawl which is known for its rampaging speed of flow. Vantawng Falls are testament to the amazing natural beauty that is hidden within the North-East.",
    },
    "phawnpui": {
        "place": "phawnpui",
        "state": "Mizoram",
        "places":"",
        "hotels":" hotel dinthar zara,zobawm homestay,aizwal guest house homestay ensuite ",
        "details": "  Phawngpui is a quaint and serene village located in the state of Mizoram. Situated at an elevation of 2157 meters, this place proffers picturesque views. This place is surrounded by verdant trees and lofty mountains which in magnifying the beauty of the landscape. The place does not only have verdant and thick forests but is also bountiful in flora and fauna. If you want to add a bit of adventure to your trip, make sure to scale the Blue Mountain and enjoy the trek with mesmerizing scenic beauty. The trek to the top of the mountain will provide awestruck views of the whole place which will make you feel as if you are in heaven.",
    },
    "shillong": {
        "place": "Shillong",
        "state": "Meghalaya",
        "places": "Umiam Lake, Elephant Falls, Shillong Peak, Don Bosco Museum, Police Bazar, Meghalaya State Museum",
        "hotels": "   ",
        "details": "Nestled amidst the pine-clad hills, Shillong, the capital of Meghalaya, unfolds like a picturesque canvas at an elevation of 1496 meters. Revered as the 'Scotland of the East,' the city offers a delightful blend of captivating landscapes, pleasant weather, and rich traditions.\n\nShillong derives its name from Lei Shyllong, an idol worshipped at the Shillong Peak, and is home to diverse tribal communities like Khyrim, Mylliem, Maharam, Mallaisohmat, Bhowal, and Langrim, each contributing to the vibrant cultural tapestry.\n\nProminent attractions include Umiam Lake, a sprawling reservoir surrounded by hills that offer a serene escape, and the tranquility of the Elephant Falls, cascading gracefully amidst lush greenery. For adventure enthusiasts, the Laitlum Canyons unveil breathtaking panoramic views, making it a must-visit for trekking.\n\nShillong is not just a haven for nature lovers; it boasts museums and cultural gems like the Don Bosco Museum, showcasing the indigenous cultures of the Northeast. The Meghalaya State Museum is another treasure trove, delving into the state's heritage through artifacts and exhibits. The bustling Police Bazar, a vibrant market, captures the pulse of Shillong with its lively atmosphere and diverse shopping experiences.\n\nVenturing beyond the city limits, Mawphlang stands as a testament to Meghalaya's cultural heritage, known for its sacred groves and traditional rituals. On the other hand, Mawlynnong, acclaimed as the cleanest village in Asia, beckons with its living root bridges and pristine landscapes.\n\nShillong's musical heartbeat resonates through its title as the 'music capital of India.' The city's westernized culture and youthful vibe contribute to its dynamic music scene. Throughout the year, music events and festivals celebrate Shillong's rich musical heritage. The city's charm lies not just in its natural beauty but also in the warmth of its people, making it a destination that lingers in the hearts of those who explore its scenic wonders and cultural richness."
    },
    "elephanta": {
        "place": "Elephant Falls",
        "state": "Meghalaya",
        "places": "",
        "hotels": "Woodland Hill Stay, Mid Pine Homestay",
        "details": "Named after an Elephant-like stone at its foot, the Elephant Falls are amongst the most popular falls in the North-East, situated next to Shillong. It is a tourists' paradise with three layers of the falls accessible to the layman from different vantage points. The Britishers named this fall so owing to the presence of an elephant-shaped rock on one side of the fall. However, the stone disintegrated and was washed away due to an earthquake in 1897.\n\nElephant Waterfalls is a superb place for spending some time in the midst of nature while capturing the incredible moments for your keepsake.\n\nThe breathtaking Elephant falls were referred to as 'Ka Kshaid Lai Pateng Khohsiew' by the local Khasi people, which means 'The Three Step Waterfalls,' as these falls consist of three mesmerizing falls in succession. The first of the three waterfalls is tucked between the dense trees and is very broad. The second waterfall reduces to thin strands of water and is almost negligible in winters due to the receding water levels. The third and the most visible waterfall is the tallest with clear water flowing like a sheet of milk on the dark rocks in the backdrop. Out of the three, the third waterfall tends to strike the visitors as the most impressive. Elephant Falls is a great stopover destination before one heads for further journeys into Meghalaya. Located 12 km away from the capital city of Shillong, it is one of the most visited falls in the beautiful state."
    },

    "double_decker": {
        "place": "Double Decker Living Root Bridge",
        "state": "Meghalaya",
        "places": "Dawki, Nohkalikai Waterfalls, Mawlynnong, Mawsmai Falls, The Eco Park, Krem Phyllut, Mawsmai Cave, Thangkharang Park and Ka Khah Ramhah, Nongsawlia",
        "hotels": "7 Sisters Falls View Inn, Goshen Homestay",
        "details": "Hidden deep in the lush, green forests of the wettest place in India, Cherrapunjee, Meghalaya; one can find the magnificent Jingkieng Nongriat Double Decker Living Root Bridge, more commonly known as the Umshiang Double Decker Living Root Bridge or simply just the Double Decker Root Bridge. This area is famous for root bridges made of Indian Rubber Tree, but the Double Decker Bridge is the most famous of all due to its large size. It is 3 kilometers long and placed at a height of 2400 feet! A unique attraction and quite an innovative mix of nature and engineering. The Umshiang River flows beneath the bridge."
    },
    "cherrapunji": {
        "place": "Cherrapunji",
        "state": "Meghalaya",
        "places": "Double Decker Living Root Bridge, Dawki, Nohkalikai Waterfalls, Mawlynnong, Mawsmai Cave, Mawsmai Falls",
        "hotels": "Sulawado Resort, Polo Orchid Resort"
    },

    "mawsynram": {
        "place": "Mawsynram",
        "state": "Meghalaya",
        "places": "Mawsmai Caves, Mawsmai Falls, Nohkalikai Falls, Mawlyngbna, Cherrapunjee",
        "hotels": "Polo Orchid Resort, Aisha Guest House Bed and Breakfast"
    },
    "balpakram": {
        "place": "Balpakram National Park",
        "state": "Meghalaya",
        "places": "Siju Caves, Siju Wildlife Sanctuary, Nokrek National Park, Tura Peak, Rongbang Dar Waterfalls, Naphank Lake, Pelga Falls, Garo Hills",
        "hotels": "Hotel Polo Orchid Tura, Karlyansa Homestay",
        "details": "Located in the southern Garo Hills in Meghalaya, about 167 Kms from Tura, Balpakram National Park lies at an elevation of about 3,000 feet above sea level. The Park is a famous national park well known for its pristine beauty. The word Balpakram means the 'land of perpetual winds,' and the national park is blessed with charming grace and breathtaking scenes.\n\nThe government of Meghalaya created the Balpakram National Park on 15 February 1986. Today, the area boasts a myriad of species of fauna and flora, including the rare Lesser Panda, the Indian Bison, and the Stag-like Serow. A variety of very rare medicinal herbs, locally known as 'dikges,' also grow abundantly in Balpakram. One can find a deep gorge in Balpakram, popularly compared to the Grand Canyon of the United States. The gorge is referred to as the 'land of the spirits,' believed to be where the spirits of the dead live temporarily before embarking on the journey towards their final abode. The Balpakram National Park is rightly termed as a traveler's paradise and is a must-visit while in Meghalaya."
    },
    "william": {
        "place": "Williamnagar",
        "state": "Meghalaya",
        "places": "Simsang River, Naka Chiklong, Domre Falls, Mrik Wari, Siju Caves, Simsang Festival",
        "hotels": "",
        "details": "Williamnagar, located 244 Kms from Shillong, was formed around the former town of Simsanggre, based on the large plains of the Simsang River. A very remote area known for its abundance of natural beauty, being flanked by mountains and having a rich composition of both water and vegetation. Williamnagar, the headquarters of the East Garo Hills district of Meghalaya, was named after Captain Williamson A. Sangma, the first Chief Minister of the State of Meghalaya. Williamnagar is of immense historical importance as it was here that the Garos made their last major resistance to the British invasion into Garo Hills during the year 1837."
    },

    "nohkalikai": {
        "place": "Nohkalikai Waterfalls",
        "state": "Meghalaya",
        "places": "Nongsawlia, Mawsmai Cave, Krem Phyllut, Dainthlen Waterfall, The Eco Park, Thangkharang Park and Khoh Ramahah, Wabaka Falls, Mawsmai Falls",
        "hotels": "7 Sisters Falls View Inn, Goshen Homestay",
        "details": "Tallest Waterfall in India, Nohkalikai Waterfalls is the fourth-highest waterfalls in the world, plunging some 335 meters from a verdant cliff to the ground, giving the portrayal of immense and natural magnificence. The falls are one of the most beautiful and grand waterfalls in the country, tucked between the evergreen rainforest of the Khasi Hill. The falls plunge into a lagoon that is as blue as the afternoon sky. Nohkalikai Falls is one of the most popular and significant places to see in the North-East. The falls are attached to a sad story of a woman named Ka Likai, making it a place of historical significance."
    },

    "mawsmai": {
        "place": "Cherrapunjee",
        "state": "Meghalaya",
        "places": "Dawki, Nohkalikai Waterfalls, Mawlynnong, Mawsmai Falls, The Eco Park, Krem Phyllut, Mawsmai Cave, Thangkharang Park and Ka Khah Ramhah, Nongsawlia",
        "hotels": "7 Sisters Falls View Inn, Aisha Guest House",
        "details": "Meghalaya is home to some amazing and mysterious cave systems, and Mawsmai Cave is by far the most popular of the lot. Located just 6 km away from the heart of Cherrapunjee, Mawsmai cave is a breathtaking maze of caves in the East Khasi Hills of Meghalaya. The well-lit caves are a view to behold when the glistening lights meet with the limestone to create countless hues and patterns of light. There is plenty of flora and fauna within the cave to catch one's attention. The length of the cave is just 150 meters, which is not the longest compared to the other caves in the region, but it surely provides one a glimpse of life underground. Mawsmai Caves are best seen on a trip to Cherrapunjee or Shillong. Start your trip with Cherrapunjee, not missing the caves while here and follow it with a trip to Shillong."
    },


    "dwaki": {
        "place": "Meghalaya",
        "state": "Meghalaya",
        "places": "Cherrapunjee, Shillong, Jowai",
        "details": "Dawki, a small town in India located in the Jaintia Hills district of Meghalaya, has become a hotspot for travelers looking to explore the unexplored. Tourists visit here for its unique landscape, crystal-clear river, and beautiful greenery. The main reason why anyone should visit Dawki is to experience its pristine beauty and the crystal-clear Umngot River. The river is so clean that you can even see the riverbed from the surface. A popular activity here is to go for a boat ride along the river and witness the beautiful landscape. There are many tourist spots and attractions in Dawki that are worth exploring. One of the main attractions is the living root bridge, which is made by the local people from the roots of the rubber tree. The bridge is a unique example of nature's beauty and can be reached after a short trek. Other attractions include the Khasi Hills, the local markets, and the nearby rainforests. One of the highlights of Dawki is the Dawki-Shnongpdeng border, which is the only legal border between India and Bangladesh. Tourists can also visit the Shnongpdeng village and explore the local culture. When visiting Dawki, there are some things that travelers should keep in mind. It is advised to carry a valid ID proof and a travel permit from the local authorities. It is also important to dress accordingly and respect the local customs. Lastly, it is advisable to travel with a local guide who can provide valuable insights into the local culture and attractions. Overall, Dawki is a great place to explore the unexplored and experience nature's beauty. From the river to the local markets, there are plenty of attractions and activities to keep visitors entertained. With its pristine beauty, it is sure to become a favorite spot for travelers in the coming years.",
        "hotels": ""
    },
    "imphal": {
        "place": "Imphal",
        "state": "Manipur",
        "places": "Loktak Lake and Sendra Island, Kangla Fort, Tharon Cave, Shaheed Minar, INA Memorial, Keibul Lamjoa National Park",
        "hotels": "Manipur House, Nature's Retreat Homestay, John House, Hill View Homestay",
        "details": "Imphal has an untouched charm surrounding its natural beauty, sceneries, and landscapes as well as significant history leaving hints of the past around the city. The lush green landscapes, beautiful surroundings, unexplored territories, and undulating rivers of Imphal make for a great tourist destination. This site of the battle of Imphal during World War II assumes a certain importance, derived from history. The two together give Imphal a number of tourist destinations which include INA memorial, Manipur State museum, Kangla Fort, Langthabal, war cemeteries, Shri Govindjee temple as well as the Waithou and Loktal lake. Manipur Zoological gardens and Keibul Lamjao National park are also places one might not want to miss."
    },
    "thoubal": {
        "place": "Manipur",
        "state": "Manipur",
        "places": "Ikop, Khongjom, Loktak Lake, Lousi, Pumlen",
        "hotels": "",
        "details": "A well-developed city, Thoubal is a good holiday destination for those looking for a pleasant climate and numerous activities. Thoubal is almost ideal for trekking, hiking, and picnics given the abundance in flora and green landscapes as well as the various facilities available here. This city is most famous for the temples and the numerous water bodies all together making it a pretty much perfect getaway which will strike the right balance of urban and a lesser-known destination. Just to add in the environment a dash of activity and vibrancy, are the popular bazaars of the town such as the Ningombam Laxmi Bazaar and Athokpam Bazaar."
    },
    "tamenglong": {
        "place": "Manipur",
        "state": "Manipur",
        "places": "Barak Waterfalls, Zeilad Lake, Buning Meadows, Tharon Cave, Forests Nearby, Local Festivals",
        "hotels": ""
    },
    "chandel": {
        "place": "Manipur",
        "state": "Manipur",
        "places": "Yangoupokpi Lokchao Wildlife Sanctuary, Tengnoupal, Moreh",
        "hotels": "",
        "details": "Chandel, also known as Lamka is a tiny but scenic district in the North-Eastern state of Manipur. It is one of the main nine districts in the state and also the second least populous of all. Situated along the lines of the international border separating India and Myanmar, it has come to be known as Gateway to Myanmar. It lies about 64 kms away from Imphal, with NH-39 passing through. It’s famous for being home to more than 20 native tribes. Chandel is a wisp of culture and traditions, given the huge number of tribes that live here. Each tribe offers a unique identity to the area, where colours of their cultures are blown out in all directions. Travelers visiting Chandel can soak in the alluring art forms along with sprightly music and dance."
    },
    "loktak": {
        "place": "Imphal",
        "state": "Manipur",
        "places": "Keibul Lamjao National Park, Phubala, INA Memorial, Moirang, Ebudhou Thangjing, Khongjom, Langthabal, Three Mothers Art Gallery",
        "details": "The largest freshwater lake in the country, Loktak Lake, and the Sendra Island on it are one of the most beautiful attractions of the state. Situated about 50 km from Imphal, Loktak Lake is situated in the valley of Imphal and is home to all the rivers and rivulets that run in the state of Manipur. Loktak Lake and Sendra Island present a combination of beauty unmatched anywhere else in the country. One is the largest freshwater lake in India while the other a floating island made of organic waste on the very same lake, housing the only tourist home in the area. The lake consists within itself many other floating islands which sustain fishermen villages and are also made of organic waste. The pristine water, the labyrinth of boat routes, the greenery of the surroundings, and the riveting crimson sunset provide one a mesmerizing site. Loktak Lake and Sendra Island are treasures of a dynamic ecosystem and demand protection and preservation. In recent years human encroachment has led to shrinkage of the lake.",
        "hotels": "Classic Grande, Shalom Farmhouse by the Hillside"
    },

    "gwalior": {
        "place": "Madhya Pradesh",
        "state": "Madhya Pradesh",
        "places": "Gwalior Fort, Jai Vilas Palace, Gujari Mahal, Man Mandir Palace, Tomb of Tansen, Teli Ka Mandir",
        "details": "Gwalior has a history of being passed on from one dynasty to the other. In as early as 1231, Iltutmish, the third ruler of the Delhi Sultanate captured the Gwalior fort, and it remained under Muslim rule till the 13th century. In 1375, the founder of the Tomar clan, Raja Veer Singh was made the ruler. 1730 saw Gwalior come under the Scindia rule in the 17th and 18th century (Maratha Dynasty) and remained a Princely State during the British rule in the 19th and 20th century. It is also famous for being non-cooperative in the 1857 Battle of Rebellion. The first occurrence of zero as a written number is recorded in the Chaturbhuj Temple of Gwalior. Hence, Gwalior has the dual historical importance of being ruled by different dynasties as well as being a centre of scientific and mathematical significance.Gwalior is a historic city located in the state of Madhya Pradesh. Popular because of the hilltop fort, Gwalior is full of palaces and glorious temples giving this city a majestic charm which speaks volumes of its glorious past. A historic city founded by king Surajesan, Gwalior is a city where India's most eminent royalty once resided. Jai Vilas Pala has the largest carpet in the world which took almost 12 years to weave and two most massive chandeliers in the world that weight close to 3.5 tonnes. The great Indian musician Tansen was born in Gwalior, and the tomb of Tansen is also an important place here. Every year, in November/December, a four-day Tansen Music festival is celebrated in the city where various classical musicians from all over the country perform on the stage near the tomb itself. Visit the various monuments and museums, eat the local delicacies like namkeen and go boating in Tighra Dam while you are in the city.",
        "hotels": "Taj Usha Kiran Palace, Clarcks Inn Suites Gwalior, Neemrana"
    },
    "kanha": {
        "place": "Madhya Pradesh",
        "state": "Madhya Pradesh",
        "places": "Bhedaghat, Jabalpur, Amarkantak",
        "details": "Kanha National Park is famous for its wildlife safaris and attracts tourists from all over the world. Other important animals in this park are leopards, wild dogs, wild cats, foxes, sloth bears, hyenas, langurs, wild boars and jackals. Reptiles including pythons, cobras, krait and other varieties of snakes are also found in this National Park.",
        "hotels": "Surwahi Social Ecoestate Kanha, Sterling Kanha"
    },
    "bandhavgarh": {
        "place": "Madhya Pradesh",
        "state": "Madhya Pradesh",
        "places": "",
        "details": "Bandhavgarh National Park used to be a former hunting preserve of the Maharaja of Rewa which is presently famous for its heritage and white tigers. This place is legendary and owns an abundance of historically abundant landmarks within the park. The city of Bandhavgarh has been demolished and flourished through several ages since the age of Ramayana, and thus reasons or its copper tinted air and stone wind fragrances. The National Park was given the name of Bandhavgarh because of an ancient fort in a hillock in Umaria along with the Vindhya ranges. The name Bandhavgarh is derived from the word 'bandhav' which means brother and ‘Garh’ meaning fort. The legend has it that Lord Rama was passing the forests of Bandhavgarh after defeating Ravana and decided to build a fort. It was to symbolize his love for his brother Lakshman.",
        "hotels": "Aranyak Resort, Hotel Jungle Palace"


    },
    "ujjain": {
        "place": "Madhya Pradesh",
        "state": "Madhya Pradesh",
        "places": "Mahakaleshwar Jyotirling, Kal Bhairava Temple, Ram Mandir Ghat, Kumbha Mela",
        "details": "The history of Ujjain can be traced back to the time of Mahabharat and Ramayana. Lost in the midst of antiquity, this place holds the tales of Lord Ram and Sita of the time when they used to visit this place to perform “Pind-Daan” for father Dasharat at Ramghat. A sacred pilgrimage destination, it was once the residence of Great Emperor Ashoka. During his ruling in the western provinces as a viceroy, it was this place where he came to know about the teachings of Buddha. Ujjain, considered to be one of the holiest cities of India, is an ancient city situated on the eastern bank of the Shipra River in the Malwa region of Madhya Pradesh. Ujjain is one of the four sites for the Kumbh Mela, the largest peace-time gathering on the planet that attracts 100 million people to the festival. This makes Ujjain an important place of Hindu Pilgrimage. To add to that, it is also home to the Mahakaleshwar Jyotirlinga, one of the twelve Jyotirlinga shrines to the god Shiva. Ujjain is one of the most glorious cities of ancient India as it was also known to be the educational hub of various Indian scholars. The immense wealth of Ujjain in terms of religion, architecture, and educational value makes this is a top attraction amongst not only Indian travellers but also amongst foreign tourists as well. Ujjain is located at a distance of 52 km from Indore, which is also the nearest major airport.",
        "hotels": "Solitaire Hotel and Resorts, Rudraksh Club and Resorts, Hotel Ambika Elite, Ratnapriya Hotel and Resort"
    },
    "kuno": {
        "place": "Madhya Pradesh",
        "state": "Madhya Pradesh",
        "places": "",
        "details": "The Kuno National Park is located in the Morena and Sheopur districts in Madhya Pradesh. One of the many gems of the state, the Kuno National Park is nestled near the Vindhyan Hills. With an area of 748 sq. km, the park is located within the larger Kuno Wildlife Division. It boasts of rich biodiversity. However, there were no lions, tigers, giraffes or cheetahs. The recent addition of cheetahs has put Kuno National Park on the global map of conservation and rehabilitation. 8 Asiatic cheetahs arrived from Namibia and were released into Kuno National Park on 17th September 2022 by the Prime Minister. The 5 female and 3 male cheetahs named Freddy, Savannah, Alton, Sasha, Cibli, Obaan, Saisa and Asha are aged 30 – 66 months and are reported to be in good health. Soon the cheetah safari will be open for the public to view these magnificent creatures in their natural habitat. Apart from lush green vegetation and varied wildlife species, Kuno has ancient structures and forts, making it an abode of both the natural and historical. Home to the Kardhai, Salai and Khair trees, and being known for the high density of avian creatures, the Kuno National Park is every nature and wildlife lover’s delight. Named after the Kuno River that cuts across it, Kuno is primarily a grassland region, though a few rocky outcrops are found here too. The protected area of the forest is home to the jungle cat, Indian leopard, sloth bear, Indian wolf, striped hyena, golden jackal, Bengal fox and dhole, along with more than 120 bird species. Initially established as a wildlife sanctuary, it was only in 2018 that the government changed its status into a national park. The Kuno National Park is closed during the monsoon season from 1st July to 15th October. Kuno National Park will continue to be under the spotlight, to check on the progress of the cheetahs and hopefully once the cheetahs are out of quarantine, the safaris will also include cheetah spotting. Until then, wildlife enthusiasts can still enjoy the many aspects of nature and history the national park offers.",
        "hotels": ""
    },
    "indore": {
        "place": "Indore",
        "state": "Madhya Pradesh",
        "places": "Rajwada, Lal Bagh Palace, Khajrana Temple, Sarafa Bazar, Indore Museum, Patalpani Waterfalls",
        "details": "Indore witnessed the conflict between the Mughals, Marathas, and the British who wanted to gain domination of Central India. Located in the Malwa Region, the city of Indore was founded by Rao Nandlal Chaudhary. On his visit to the Indreshwar temple, he found the area to be sheltered and secured by natural boundaries on all sides. He established the city of Indrapur and built a fortress there. The name Indore is a change of Indrapur. When the Marathas became powerless after they lost the third battle of Panipat to Ahmad Shah Abdali, an Afghan invader, they had to sue for peace in order to resist the British. After this, the Holkars established their rule on Indore. The Holkar Dynasty was founded by one of the greatest warriors of his time, Maharaja Malhar Rao Holkar I. Even during the British Raj, Indore remained as part of the Holkar Dynasty. During the Independence of India, it joined a few other Princely States and became a part of Madhya Bharat. Later, it became a part of Madhya Pradesh on November 1, 1956.'The food city' famous for its Poha and Immarti. Indore is the largest and the most populous city of Madhya Pradesh. Located on the Malwa Plateau, the charm of this city lies in its rich cultural heritage, which has been preserved over centuries and along with the hints of urbanization. Indore has been one of the fore-runners in the development of the country in the era of modernization. One of the educational hubs in the country, Indore has both an IIT and an IIM. Indore is also the cleanest city of India. Indore has over the years established itself as the hub of trading and industrial practices in the state. The city of Indore gets its name from Indreshwar Mahadev temple. It is believed that Lord Indra meditated on this land and led Swami Indrapuri to establish this temple. Try out some local delicacies like Indori Poha at Sarafa Bazaar while you are in Indore.",
        "hotels": "Crescent Spa and Resorts, Simcha Island, Aaram Baagh Maheshwar, The Red Maple Mashal"
    },
    "bhopal": {
        "place": "Bhopal",
        "state": "Madhya Pradesh",
        "places": "Upper Lake, Van Vihar, Indira Gandhi Rashtriya Manav Sangrahalaya, Lower Lake, Bhimbetka Rock Shelters, Gohar Mahal",
        "details": "Known as Bhojpal in the 11th century, Bhopal was ruled by Parmara King Bhojpal. He was said to have built many lakes that surround the city today. This city was improved upon by Dost Mohammed Khan, who established rule upon this city after the death of Emperor Aurangzeb in 1707. Bhopal is known for its culture, arts, and architecture, which was polished upon during the reign of the Begums. In the 19th century, Bhopal came to be ruled by Muslim women which led the city to great prosperity. Mamola Bai, the first Begum, looked after the administration of the city after her husband's death. She was then succeeded by Qudsia Begum who took over after her husband was assassinated. Her daughter, Sikander ruled the kingdom after her. During this reign of the Begums, there was peace in the kingdom which gave rise to a mixed culture in Bhopal where people observing different religious existed in harmony. Arts, culture, education, and architecture flourished which made Bhopal into the beautiful city that it is today,City of lakes. The capital city of Madhya Pradesh, Bhopal is famous for the pair of artificial lakes (Upper Lake and Lower Lake) that split the city. Towards the north of the lakes lie the intriguing old town with rustic mosques, bustling bazaars, serpentine alleys, and exquisite havelis. To its south is the new town with swanky infrastructure, shopping complexes, and wide roads. It is this contrast that makes Bhopal an exquisite blend of the old and the new, the past and the present, the rustic and the classy. Bhopal is replete with majestic mosques which showcase classic Mughal architecture exemplified by the Taj-Ul-Masjid (one of the largest in India, built by the third female ruler Bhopal had, Shah Jahan Begum), and Moti Masjid. The city will catch your attention through its breathtakingly beautiful havelis and museums as well as Nawabi food that is an absolute delight for foodies. Tragically, Bhopal is also a reminiscence of the world's worst industrial disaster in the chemical plant of Union Carbide that was responsible for at least 8000 deaths from the explosion alone.",
        "hotels": "Taj Lakefront Bhopal, Jahan Numa Palace, Courtyard by Marriott Bhopal, Shetaon Grand Palace"
    },




    "maheshwar": {
        "place": "Maheshwar",
        "state": "Madhya Pradesh",
        "places": "Holkar Fort, Madleshwar, Rajwada, Shopping in Maheshwar, Narmada Ghat, Jaleshwar Temple",
        "details": "Located on the banks of the River Narmada, this gorgeous town is largely referred to as the temple town of Madhya Pradesh. It also holds a lot of mythological and historical importance given the fact that it has found a mention in the epics of Ramayana and Mahabharata. This was the capital of Queen of the Maratha Malwa kingdom Rani Ahilyabai province, Holkar. She beautified the city with many buildings and public works, the Maratha architecture and this city was also home to her extravagant palace. Maheshwar is a renowned hub for its production of Maheshwari sarees, which makes this place a paradise for shopaholics.",
        "hotels": "Ahila Fort, Aamantrana at Fort Maheshwar"
    },


    "jabalpur": {
        "place": "Jabalpur",
        "city": "Jabalpur",
        "state": "Madhya Pradesh",
        "places": "Bhedaghat, Dhuandhar Falls, Marble Rocks, Madan Mahal Fort",
        "details": "Jabalpur has a rich historical and cultural heritage, with various dynasties leaving their mark on the city. It was an important center during the Gondwana rule and later became part of the Maratha and British empires.Jabalpur is known for its natural beauty, historical sites, and cultural significance. The Dhuandhar Falls and Marble Rocks on the Narmada River are major attractions, offering breathtaking views.",
        "hotels": "Villas in Jabalpur"
    },
    "shivpuri": {
        "place": "Shivpuri",
        "city": "Shivpuri",
        "state": "Madhya Pradesh",
        "places": "Madhav National Park, George Castle, Bhadaiya Kund",
        "details": "Shivpuri has historical importance, serving as a summer capital for the Scindia rulers of Gwalior. The town has witnessed various historical events and is known for its regal past.Shivpuri is a serene town known for its wildlife sanctuary, historical monuments, and natural beauty. Madhav National Park is a prominent tiger reserve and offers opportunities for wildlife enthusiasts.",
        "hotels": "Castle Inn, Tranquility"
    },








    

    "kunonationalpark": {
        "place": "Kuno National Park",
        "state": "Madhya Pradesh",
        "places": "Kuno National Park",
        "details": "Kuno National Park is known for its conservation efforts and is a part of the larger landscape aimed at protecting wildlife. Kuno National Park is a wildlife sanctuary known for its diverse flora and fauna, including various species of mammals and birds.",
        "hotels": ""
    },




    
   
    "kochi": {
        "place": "Kochi",
        "state": "Kerala",
        "places": "Fort Kochi, Mattancherry Palace, Chinese Fishing Nets",
        "details": "Kochi has a long history as a spice trading center and was influenced by various cultures, including Portuguese, Dutch, and British. Kochi is a vibrant city known for its historical sites, cultural diversity, and scenic waterfront. It reflects a blend of traditional and modern influences.",
        "hotels": "Forte Kochi, Le Meridien Kochi, Trident Cochin, Tea Bungalow"
    },

    "wayanad": {
        "place": "Wayanad",
        "state": "Kerala",
        "places": "Chembra Peak, Edakkal Caves, Banasura Sagar Dam",
        "details": "Wayanad has a rich tribal history and is known for its natural beauty and biodiversity. Wayanad is a lush green district in the Western Ghats, offering a mix of wildlife, trekking opportunities, and scenic landscapes.",
        "hotels": "Flora Vythiri Resort, Vistara Resort, Mount Xanadu Resort, Karapuzha Village Resort"
    },
  
    "kumarakom": {
        "place": "Kumarakom",
        "state": "Kerala",
        "places": "Kumarakom Bird Sanctuary, Vembanad Lake, Aruvikkuzhi Waterfall",
        "details": "Kumarakom is known for its backwaters and was once a popular retreat for British colonizers. Kumarakom is a backwater destination with serene landscapes, houseboats, and abundant birdlife in the Kumarakom Bird Sanctuary.",
        "hotels": "Coconut Lagoon, Taj Kumarakom Resort, Rhythm Kumarakom, Kumarakom Lake Resort"
    },

    
    "kovalam": {
        "place": "Kovalam",
        "state": "Kerala",
        "places": "Kovalam Beach, Vizhinjam Lighthouse, Samudra Beach",
        "details": "Kovalam gained popularity as a beach destination in the 1930s and has since been a favorite among tourists. Kovalam is a renowned beach destination with crescent-shaped beaches, lighthouses, and a vibrant seaside atmosphere.",
        "hotels": "Swapnatheeram Beach Resort, Amara Ayurveda Retreat, Little Elephant Beach Resort, Ideal Ayurvedic Resort"
    },

   

    "kollam": {
        "place": "Kollam",
        "state": "Kerala",
        "places": "Ashtamudi Lake, Thangasseri Lighthouse, Palaruvi Waterfall",
        "details": "Kollam has a historical connection as a major port city in the past and is known for its trade and cultural heritage. Kollam is a bustling city with a rich maritime history, offering attractions like serene lakes, historic lighthouses, and waterfalls.",
        "hotels": "Fragrant Nature Backwater Resort, Quilon Beach Inn, Samiira on Ashtamudi Lake, The Raviz Ashtamudi"
    },

 
    "sabarimala": {
        "place": "Sabarimala",
        "state": "Kerala",
        "places": "Sabarimala Temple, Malikappuram Devi Temple",
        "details": "Sabarimala is a famous pilgrimage center with a history deeply rooted in Hindu mythology and traditions. Sabarimala is known for the Sabarimala Temple, dedicated to Lord Ayyappa. It attracts millions of pilgrims during the annual pilgrimage season.",
        "hotels": "Thekkady Gavi Suites, Whispering Pine Woods"

    },
    "bekal": {
        "place": "Bekal",
        "state": "Kerala",
        "places": "Bekal Fort, Bekal Beach, Ananthapura Lake Temple",
        "details": "Bekal is known for its historic fort, which is believed to have been built in the 17th century by Shivappa Nayaka of Keladi. Bekal is a coastal town known for its imposing fort, beautiful beaches, and serene backwaters. It's a picturesque destination offering a blend of history and natural beauty.",
        "hotels": "Taj Bekal Resort, Kanan Beach Resort, Malabar Ocean Front Resort, Shri Go Bekal Fort Resort"

    },
    "palakkad": {
        "place": "Palakkad",
        "state": "Kerala",
        "places": "Palakkad Fort, Malampuzha Dam, Silent Valley National Park",
        "details": "Palakkad has a historical significance with its well-preserved fort and cultural heritage. Palakkad is known for its fort, dams, and proximity to the Silent Valley National Park. It offers a mix of historical sites and natural attractions.",
        "hotels": "Udaya Resort, Diga Vista Resort, Hasco Tower, KTDS Garden House"

    },
    "trivandrum": {
        "place": "Trivandrum",
        "state": "Kerala",
        "places": "Sree Padmanabhaswamy Temple, Kovalam Beach, Napier Museum",
        "details": "Thiruvananthapuram, the capital of Kerala, has a rich history as an ancient city with cultural and historical significance. Thiruvananthapuram is a vibrant city with temples, museums, and beautiful beaches. It serves as the political, cultural, and educational center of Kerala.",
        "hotels": "Nivriti Heritage, New Thriphala Ayurveda, Spot on 76900 Dream Palace, Reuben Villa"
    },
    "vythiri": {
        "place": "Vythiri",
        "city": "Kalpetta",
        "state": "Kerala",
        "places": "Pookode Lake, Lakkidi Viewpoint, Chembra Peak",
        "details": "Vythiri is a part of the Wayanad district and is known for its scenic landscapes and plantations. Vythiri is a hill station surrounded by lush greenery, tea estates, and serene lakes. It's a popular destination for nature lovers and those seeking a peaceful getaway.",
        "hotels": "Pepper Trail, Wayanad Wild, Serene Crest Resort, Mount Xanadu Resorts"

    },
    "ponmudi": {
        "place": "Ponmudi",
        "state": "Kerala",
        "places": "Ponmudi Hill Station, Golden Valley, Peppara Wildlife Sanctuary",
        "details": "Ponmudi is known for its pristine hills and is a popular hill station near Thiruvananthapuram. Ponmudi is a charming hill station with winding roads, dense forests, and panoramic views. It's a favorite destination for nature enthusiasts and trekking.",
        "hotels": "Westn Resorts, Green Garden Resort"

    },
    "peerumedu": {
        "place": "Peerumedu",
        "state": "Kerala",
        "places": "Grampi, Peeru Hills, Parunthumpara",
        "details": "Peerumedu is known for its plantations and has historical connections to the erstwhile princely state of Travancore. Peerumedu is a hill station with tea and cardamom plantations, offering a serene escape with its rolling hills and viewpoints.",
        "hotels": ""
    },
    "guruvayur": {
        "place": "Guruvayur",
        "state": "Kerala",
        "places": "Guruvayur Temple, Mammiyoor Temple, Punnathur Kotta Elephant Sanctuary",
        "details": "Guruvayur is a sacred town with a rich history and is famous for the Guruvayur Temple dedicated to Lord Krishna. Guruvayur is a major pilgrimage center with the Guruvayur Temple being a significant attraction. The town is known for its religious and cultural significance.",
        "hotels": "Manjira Lodge, Ambalath Malpe Leavesa Home, Remanika Regency, Rajavalsam Guruvayur"
    },
    "malampuzha": {
        "place": "Malampuzha",
        "state": "Kerala",
        "places": "Malampuzha Dam, Malampuzha Gardens, Yakshi Statue",
        "details": "Malampuzha is known for its dam and gardens, and its history is associated with irrigation and water management. Malampuzha is a popular destination with a dam, gardens, and recreational facilities. It's a family-friendly place with beautiful landscapes.",
        "hotels": "Hydepark Residency, Four N Square Residency"

    },
    "kasaragod": {
        "place": "Kasaragod",
        "state": "Kerala",
        "places": "Bekal Fort, Ananthapura Lake Temple, Chandragiri Fort",
        "details": "Kasaragod is known for its forts and temples, and its history is linked to various dynasties that ruled the region. Kasargod is a small coastal town in Northern Pary of Kerala displaying a delightful blend of various religions, culture and bounty of nature. Blessed with majestic forts, lofty hills, beautiful offbeat backwaters, temples and pristine beaches, the town oozes charm and tranquillity from every aspect. It is gaining popularity among people from nearby cities owing to the presence of luxury resorts.\n\nKasargod is also known for its rich and glorious past, is considered to be home to some of the best-preserved forts in Kerala. The variety of art and culture of the town speaks volume about its diversity. In fact, one can hear about seven languages spoken in the town, Tulu, Malayalam, Kannada, Tamil and Konkani being the most famous ones. Adorned with several tourist attractions, this family-friendly destination with booming coir and handloom industry is worth a visit.",
        "hotels": "Taj Bekal Resort, Kanan Beach Resort, Malabar Ocean Front Resort, The Lalit Resort"
    },
    "thenmala": {
        "place": "Thenmala",
        "city": "Punalur",
        "state": "Kerala",
        "places": "Thenmala Dam, Leisure Zone, Butterfly Safari Park",
        "details": "Thenmala is known for being India's first planned eco-tourism destination, emphasizing sustainable tourism. Thenmala offers a unique experience with its eco-tourism initiatives, nature trails, and recreational activities. It's a tranquil destination surrounded by lush greenery.",
        "hotels": "Kandhamath Heritage Resort, Thenmala Hormuz Inn"
    },
    "kottayam": {
        "place": "Kottayam",
        "state": "Kerala",
        "places": "Vembanad Lake, Kumarakom, Ettumanoor Mahadeva Temple",
        "details": "Kottayam has a rich history as a trading center and is known for its cultural and religious diversity. Kottayam is a district known for its backwaters, religious sites, and educational institutions. It serves as a gateway to the backwater destinations of Kumarakom and Alleppey.",
        "hotels": "Lemon Dew Beach House, Kalathil Lake, Mistywind Valley, The World Backwaters"

    },
    "kumily": {
        "place": "Kumily",
        "state": "Kerala",
        "places": "Periyar Wildlife Sanctuary, Thekkady Lake, Abraham's Spice Garden",
        "details": "Kumily is the gateway to the Periyar Tiger Reserve and has a history linked to spice cultivation and trade. Kumily is a town known for its spice plantations and its proximity to the Periyar Wildlife Sanctuary. It's a popular destination for nature walks and spice tours.",
        "hotels": "Amritara Shalimar Spice Garden, Niraamaya Retreats Cardamom Club, Cardamom Country by Xandari, Elephant Court Thekkady"
    },
    "ponnani": {
        "place": "Ponnani",
        "state": "Kerala",
        "places": "Ponnani Beach, Ponnani Juma Masjid, Biyyam Kayal",
        "details": "Ponnani has a history deeply rooted in trade, and it was a significant port for maritime activities. Ponnani is a coastal town known for its beaches, mosques, and the confluence of Bharathapuzha River and the Arabian Sea. It offers a mix of cultural and natural attractions.",
        "hotels": "Avanti Castello, Sopanam Heritage"
    },
    "thekkady": {
        "place": "Thekkady",
        "state": "Kerala",
        "places": "Periyar Wildlife Sanctuary, Thekkady Lake, Mangala Devi Temple",
        "details": "Thekkady is known for its wildlife sanctuary and has a history linked to conservation and eco-tourism initiatives. Thekkady is famous for the Periyar Wildlife Sanctuary, offering boat safaris and trekking opportunities. It's a scenic destination surrounded by hills and dense forests.",
        "hotels": "Abad Green Forest, Spice Village CGH Earth, Forest Canopy, Amrita Shalimar Spice Garden"
    },
    "muthanga": {
        "place": "Muthanga Wildlife Sanctuary",
        "state": "Kerala",
        "places": "Muthanga Wildlife Sanctuary",
        "details": "Muthanga Wildlife Sanctuary is part of the Nilgiri Biosphere Reserve and has a history of wildlife conservation and biodiversity protection. It is known for its diverse flora and fauna, including elephants, tigers, and various species of birds. The sanctuary offers wildlife safaris to explore the natural beauty of the Western Ghats.",
        "hotels": "Pepper Trail, The Woods Resorts Wayanad"

    },
    "devikulam": {
        "place": "Devikulam",
        "state": "Kerala",
        "places": "Devikulam Lake, Pallivasal Waterfall, Attukal Waterfalls",
        "details": "Devikulam is associated with the legend of Goddess Sita and is known for its pristine landscapes. It is a hill station with a tranquil lake and waterfalls, offering a serene environment for nature lovers. An ideal destination for those seeking peace and natural beauty.",
        "hotels": "The Windy Mist Resort, Riverbench Homestay Munnar"
    },
    "thoipetty": {
        "place": "Thoipetty",
        "state": "Kerala",
        "places": "Thoipetty Dam, Idukki Arch Dam, Idukki Wildlife Sanctuary",
        "details": "Thoipetty is known for its dams and wildlife sanctuary, contributing to the region's hydroelectric power generation. A scenic location with dams and wildlife sanctuaries, offering panoramic views of the Western Ghats. A destination for nature enthusiasts and those interested in dam architecture.",
        "hotels": "Evolve Back Kabini, Parisons Plantation Experience by Abad"

    },
    "jamshedpur": {
        "place": "Jamshedpur",
        "state": "Jharkhand",
        "places": "Jubilee Park, Tata Steel Zoological Park, Dalma Wildlife Sanctuary",
        "details": "Jamshedpur, also known as Tatanagar, has a significant industrial history and is recognized for being the first planned industrial city in India. It was established by Jamsetji Tata, the founder of the Tata Group, and the city grew around the Tata Steel plant. Jamshedpur is an industrial city known for its well-planned layout, green spaces, and educational institutions. The Tata Steel plant, established in the early 20th century, played a crucial role in the city's development. Jubilee Park, a sprawling public park, is a popular recreational spot, and the city hosts various cultural and sporting events. With a blend of industry and nature, Jamshedpur stands as a testament to the vision of industrialist Jamsetji Tata.",
        "hotels": "KC Manor, Hotel Nataraj, Ramada Jamshedpur, The Sonnet Jamshedpur"
    },
    "ranchi": {
        "place": "Ranchi",
        "state": "Jharkhand",
        "places": "Rock Garden, Jagannath Temple, Ranchi Lake, Hundru Falls",
        "details": "Ranchi, the capital city of Jharkhand, has a history associated with the Chotanagpur plateau and the indigenous tribes of the region. The city gained prominence during the British colonial period and later became the capital of the newly formed state of Jharkhand in 2000. Ranchi is known for its picturesque landscapes, hills, and waterfalls. The Rock Garden, created out of industrial and domestic waste, is a unique attraction. The Jagannath Temple is a significant religious site. Ranchi Lake offers a serene environment, and Hundru Falls showcases the natural beauty of the region. The city serves as an administrative, cultural, and educational hub in Jharkhand.",
        "hotels": "Radisson Blu Hotel, Capitol Hill, Le Lac Sarovar Portico, Chanakya BNR Hotel"
    },
    "betla": {
        "place": "Betla National Park",
       
        "state": "Jharkhand",
        "places": "Betla National Park, Palamau Fort",
        "details": "Betla National Park is part of the Palamau Tiger Reserve and has a history rooted in wildlife conservation. It was initially established as a wildlife sanctuary in 1974 and later declared a national park to protect the diverse flora and fauna of the region. Palamau Fort, located within the park, has historical significance and dates back to the Chero dynasty. Betla National Park is one of the first national parks in India and is known for its rich biodiversity. The park is home to various species of flora and fauna, including tigers, elephants, leopards, and a variety of deer and bird species. Visitors can explore the dense forests, grasslands, and water bodies within the park. Palamau Fort adds a historical touch to the natural beauty of Betla National Park.",
        "hotels": ""

    },
    "massanjore": {
        "place": "Massanjore Dam",
        
        "state": "Jharkhand",
        "places": "Massanjore Dam, Pakur",
        "details": "Massanjore Dam, also known as Canada Dam, is a significant hydraulic engineering project located in Dumka district, Jharkhand. The dam was built across the Mayurakshi River and completed in 1955 with assistance from the Canadian government, hence the name 'Canada Dam.' The project aimed at irrigation, flood control, and hydroelectric power generation. Massanjore Dam is a large reservoir surrounded by picturesque landscapes. The dam has contributed to agricultural development in the region by providing water for irrigation. The serene surroundings and the water body make it a popular spot for tourists seeking a peaceful environment. The town of Pakur, known for its scenic beauty and cultural heritage, is often visited by those exploring the area around Massanjore Dam.",
        "hotels": ""
    },
    "hazaribagh": {
        "place": "Hazaribagh",
       
        "state": "Jharkhand",
        "places": "Hazaribagh National Park, Hazaribagh Lake, Canary Hill",
        "details": "Hazaribagh has a historical background associated with its name, which means 'a thousand gardens.' The region was historically known for its lush greenery and natural beauty. The town gained prominence during the British colonial period and later developed as a district in the state of Jharkhand. Hazaribagh is a town surrounded by hills, forests, and lakes, offering a serene environment. Hazaribagh National Park is a major attraction, known for its wildlife, including tigers, leopards, and various bird species. Hazaribagh Lake is a picturesque water body, and Canary Hill provides panoramic views of the surroundings. The town is an ideal destination for nature lovers, offering opportunities for wildlife safaris, trekking, and relaxation.",
        "hotels": ""
    },


    "bokaro": {
        "place": "Bokaro Steel Plant",
        "state": "Jharkhand",
        "places": "Bokaro Steel Plant, Garga Dam, Jawaharlal Nehru Biological Park",
        "details": "Bokaro Steel City is a planned city and industrial hub that developed around the Bokaro Steel Plant, one of the largest steel manufacturing units in India. The city was planned in the 1960s to accommodate the needs of the steel industry, and it has since grown into a major urban center in Jharkhand. Bokaro Steel City is known for its industrial significance, particularly the Bokaro Steel Plant, which plays a crucial role in the economic development of the region.",
        "hotels": "Cacoon Luxury Business Hotel, Pearl Hotels and Resorts"
    },
    
    "dhanbad": {
        "place": "Dhanbad",
        "state": "Jharkhand",
        "places": "Shakti Mandir, Jharia Coal Mines, Maithon Dam",
        "details": "Dhanbad has a history deeply rooted in coal mining and industrial activities. The region is known for its coal reserves, and Dhanbad has emerged as the 'Coal Capital of India.' The city's growth is closely tied to the development of coal mines, which attracted settlers and industrial establishments. Dhanbad is a city known for its coal mining industry and is a major contributor to India's coal production. Shakti Mandir is a prominent religious site in the city. Jharia, a town near Dhanbad, is famous for its coal mines and is one of the most fire-prone areas due to underground coal seam fires. Maithon Dam, located on the Barakar River, is a popular destination for boating and water sports. Dhanbad is an important industrial and educational hub in Jharkhand, offering a mix of urban amenities and natural attractions.",
        "hotels": "OYO Flagship, OYO Hotel Anandam Residency, OYO Flagship 27A Hotel, OYO Sonora Hotel"
    },
    "kurukshetra": {
        "place": "Kurukshetra",
        "city": "Kurukshetra",
        "state": "Haryana",
        "places": "Brahma Sarovar, Sannihit Sarovar, Bhishma Kund, Kurukshetra Panorama and Science Centre",
        "details": "Kurukshetra holds immense historical and religious significance, primarily associated with the Hindu epic, the Mahabharata. The great battle of Kurukshetra, as described in the Mahabharata, took place in this region. The city is also believed to be the birthplace of the Bhagavad Gita, a sacred Hindu scripture. Kurukshetra is a pilgrimage destination with numerous sacred tanks and historical sites. Brahma Sarovar and Sannihit Sarovar are large tanks believed to be auspicious for a holy dip. Bhishma Kund is associated with Bhishma Pitamah from the Mahabharata. The Kurukshetra Panorama and Science Centre provide insights into the Mahabharata and the historical events that unfolded in the region. The city attracts pilgrims, scholars, and tourists interested in exploring its rich cultural and religious heritage.",
        "hotels": "JB Hotel and Lodge, OYO Hotel Sarovar"

    },
    "panipat": {
        "place": "Panipat",
        "state": "Haryana",
        "places": "Panipat Museum, Kabuli Bagh Mosque, Ibrahim Lodhi's Tomb, Devi Temple",
        "details": "Panipat is known for its historical significance, particularly the three major battles of Panipat that took place in the 16th and 18th centuries. The city has witnessed pivotal moments in Indian history and has been a battleground for various rulers and dynasties. Panipat is a city with a rich historical and cultural heritage. The Panipat Museum showcases artifacts and exhibits related to the battles fought in the region. Kabuli Bagh Mosque is an ancient mosque built by Babur. Ibrahim Lodhi's Tomb is dedicated to the last sultan of the Lodhi dynasty. The city also has religious sites like the Devi Temple. Panipat attracts history enthusiasts, scholars, and tourists interested in exploring its historical landmarks.",
        "hotels": "KK Guest House, OYO Murliwala Wedding Palace and Resort, OYO Flagship Sunrise, OYO Flagship Hotel Kiran"
    },
    "rohtak": {
        "place": "Rohtak",
        "state": "Haryana",
        "places": "Tilyar Lake, Mansa Devi Temple, Banni Khera Farm, Rohtak Zoo",
        "details": "Rohtak has a historical background dating back to ancient times, with references in the Mahabharata. The city has witnessed the rule of various dynasties and played a role in historical events. Rohtak has grown into an important urban center with a mix of historical sites and modern amenities. Rohtak is known for its cultural and recreational attractions. Tilyar Lake is a popular spot for boating and picnics. Mansa Devi Temple is a revered Hindu shrine. Banni Khera Farm offers a rural experience with agricultural activities. Rohtak Zoo is a wildlife park with diverse fauna. The city serves as an educational and industrial hub, attracting students and professionals. Rohtak's blend of history and contemporary developments makes it an interesting destination.",
        "hotels": "Hotel Vishal Imperial, Hotel Joy Chottu Ram Chowk Rohtak Haryana"
    },
    "morni": {
        "place": "Morni Hills",
        "state": "Haryana",
        "places": "Morni Fort, Morni Lake, Tikkar Taal, Thakurdwara Temple",
        "details": "Morni Hills is known for its scenic beauty and is believed to have derived its name from a Queen named Morni. The region has historical significance and was once ruled by the Rajputs. Morni Hills offers a tranquil environment away from the hustle and bustle of city life. Morni Hills is a hill station in Haryana, known for its lush greenery and pleasant climate. Morni Fort is a historical structure with panoramic views of the surrounding hills. Morni Lake is a popular spot for boating and picnics. Tikkar Taal is another picturesque lake in the area. Thakurdwara Temple is a revered shrine with religious significance. Morni Hills is a serene destination for nature lovers, adventure enthusiasts, and those seeking a peaceful getaway.",
        "hotels": "Golden Tulip Chandigarh, Ana Clarks Inn"
    },
    "damdama": {
        "place": "Damdama Lake",
        "state": "Haryana",
        "places": "Damdama Lake",
        "details": "Damdama Lake is a natural reservoir near Gurgaon, formed by a check dam on a local stream. The lake has become a popular destination for recreational activities and water sports. It provides a serene getaway for locals and tourists from nearby urban areas. Damdama Lake is one of the largest natural lakes in Haryana, surrounded by the Aravalli Hills. It offers a peaceful environment and various activities for visitors. Boating, kayaking, and paddle boating are popular water sports at the lake. The lush greenery around the lake adds to its natural charm. Damdama Lake serves as an ideal day trip destination for families, adventure seekers, and nature enthusiasts, providing a break from the city's hustle.",
        "hotels": "The Western Sohna Resort, The Gateway Resort"
    },
    "manesar": {
        "place": "Manesar",
        "state": "Haryana",
        "places": "Heritage Transport Museum, Sultanpur National Park, Wet 'n' Wild Resorts",
        "details": "Manesar, historically an agricultural area, has witnessed significant industrial and infrastructural development in recent decades. The region has become an industrial hub with the establishment of manufacturing units, IT parks, and commercial complexes, contributing to the economic growth of the area. Manesar is known for its blend of industrial and leisure attractions. The Heritage Transport Museum showcases the evolution of transportation in India. Sultanpur National Park is a bird sanctuary attracting nature enthusiasts. Wet 'n' Wild Resorts provides water-based recreational activities. Manesar is strategically located near Delhi and Gurgaon, making it a destination for business, industry, and leisure. The city has witnessed rapid urbanization, and its development continues to shape the economic landscape of the region.",
        "hotels": "OYO 71370 White House, Palette JPS Residency"
    },
    "kalesar": {
        "place": "Kalesar National Park",
        "state": "Haryana",
        "places": "Kalesar National Park",
        "details": "Kalesar National Park is a protected area known for its rich biodiversity and ecological significance. The park was established to conserve the diverse flora and fauna of the region and provide a natural habitat for various species. It is a part of the Shivalik Elephant Reserve. Kalesar National Park is located in the Shivalik Hills and is characterized by dense forests, hilly terrain, and diverse wildlife. The park is home to species like elephants, leopards, deer, and a variety of bird species. It offers opportunities for nature walks, trekking, and wildlife safaris. The scenic beauty and natural landscapes make Kalesar National Park a popular destination for nature lovers and wildlife enthusiasts."
    },
    "chandigarh": {
        "place": "Chandigarh",
        "state": "Union Territory (shared capital of Haryana and Punjab)",
        "places": "Rock Garden, Sukhna Lake, Rose Garden, Capitol Complex",
        "details": "Chandigarh, designed by the renowned architect Le Corbusier, is a planned city and the capital of both Haryana and Punjab. It was conceived after the partition of India in 1947 to serve as a new capital for the states. The city's planning and architecture reflect modernist principles and urban design. Chandigarh is known for its well-planned layout, green spaces, and modernist architecture. The Rock Garden is a unique sculpture garden created from industrial and home waste. Sukhna Lake is a serene water reservoir offering boating and recreational activities. Rose Garden is one of the largest rose gardens in Asia. The Capitol Complex is a UNESCO World Heritage site with significant government buildings. Chandigarh is a vibrant city with a mix of cultural, artistic, and urban attractions.",
        "hotels": "Holiday Inn Chandigarh, Hotel Shagun Chandigarh, Park Plaza Chandigarh, Mandarin Square"
    }






#extra places can be added
}














def search_place():
    #global nm
    

    place = entry.get()
    place=place.lower()
    if place in data:

        
        info_text.delete(1.0, tk.END) 
        info_text.insert(tk.END, f"Place: {data[place]['place']}\n\n"
                                  f"State: {data[place]['state']}\n\n"
                                  f"Places: {data[place]['places']}\n\n"
                                  f"Hotels: {data[place]['hotels']}\n\n"
                                  f"Details: {data[place]['details']}")
        
        


        global image_label
        #nm=place
        img = tk.PhotoImage(file=dic_1[place])
        image_label = tk.Label(window, image =img)
        image_label.place(x=750, y=280)
        engine.say(info_text.get(1.0, tk.END))
        engine.runAndWait()

    else:
       



        def pop():
            info_text.delete(1.0, tk.END)
            image_label.destroy()
            messagebox.showinfo('sorry',"Place Not Found\n\n\nCheck the spelling or enter different place")
        pop()

def clear_entry():
    entry.delete(0, tk.END)
    info_text.delete(1.0, tk.END)
    image_label.destroy()


window = tk.Tk()
window.title("Place Guide")

custom_font = ("Arial", 16)
a=tk.PhotoImage(file="C:\\Users\\Abhishek Patil\\python\\mini project\\bg1.png")
l1=tk.Label(window,image=a).pack()


#hariyana
image_path ="C:\\Users\\Abhishek Patil\\python\\mini project\\west bengal\\MIDNAPORE1.png"
sanctuary="C:\\Users\\Abhishek Patil\\python\mini project\\Haryana\\bird sanctuary 2)1.png"
chandigarh="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\Chandigarh (2)1.png"
damdama="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\damdama lake (2)1.png"
kurukshetra="C:\\Users\\Abhishek Patil\\python\\mini project\Haryana\\download (1)1.png"
kalesar="C:\\Users\Abhishek Patil\\python\mini project\\Haryana\\kalesar national park1.png"
manesar="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\manesar2)1.png"
morni="C:\\Users\\Abhishek Patil\\python\mini project\\Haryana\\morni hills)1.png"
panipat="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\panipat)1.png"
rohtak="C:\\Users\\Abhishek Patil\\python\\mini project\\Haryana\\rohtak)1.png"


#jarkhand
betla="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\betla national park1.png"
bokaro="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\bokaro steel cityd (1)1.png"
dhanbad="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\dhanbad (1)1.png"
hazaribagh="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\hazariribagh (1)1.png"
jamshedpur="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\jamshedpur1)1.png"
massanjore="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\massanjore dam (1)1.png"
ranchi="C:\\Users\\Abhishek Patil\\python\\mini project\\Jharkhand\\ranchi1)1.png"


#kerla
bekal="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\bekal (1)1.png"
devikulam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\devikulam(1)1.png"
guruvayur="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\guruvayur1.png"
kasaragod="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kasaragod)1.png"
kochi="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kochi(2)1.png"
kollam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kollam)1.png"
kottayam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kottayyam (1)1.png"
kovalam="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kovalam1)1.png"
kumarakom="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kumarakom2)1.png"
kumily="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\kumuly1)1.png"
malampuzha="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\malampuja)1.png"
muthanga="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\muthanga wildlife)1.png"
palakkad="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\palakkad)1.png"
peerumedu="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\peerumedu(1)1.png"
ponmudi="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\ponmudi(1)1.png"
ponnani="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\ponnani(1)1.png"
sabarimala="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\sabarimalad (1)1.png"
thekkady="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\thekkady1)1.png"
thenmala="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\thenmala1)1.png"
thoipetty="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\thiolpetty1)1.png"
trivandrum="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\trivandram1)1.png"
wayanad="C:\\Users\\Abhishek Patil\\python\\mini project\\kerla\\wayanand(2)1.png"






#manipur
chandel="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Manipur\\chandel (1)1.png"
imphal="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Manipur\\inphal)1.png"
loktak="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Manipur\\loktak lake (1)1.png"
tamenglong="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Manipur\\tamengolong(1)1.png"
thoubal="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Manipur\\thoubal (1)1.png"



#meghalay
balpakram="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Meghalaya\\balakram national park1).png"
cherrapunji="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Meghalaya\\cherrapunjee (1)1.png"
double_decker="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\double decker bridge1)1.png"
dwaki="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\dwaki(1)1.png"
elephanta="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\elephant falls (1)1.png"
mawsmai="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\mawsmai caved (1)1.png"
nohkalikai="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\nahkoli waterfalls (1)1.png"
shillong="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\\Meghalaya\\shillong1)1.png"
william="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\William nagar1)1.png"


#mizoram
aizawl="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\aizawl.png"
champhai="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\Mizoram\\champhai (1)1.png"
lunglei="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\lunglei(1)1.png"
phawnpui="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\phawngpui(1)1.png"
saiha="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\saiha (1)1.png"
serchhip="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\serchhipd (1)1.png"
vantawng="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mizoram\\vanthawng falls1)1.png"
mawsynram="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Meghalaya\\mawsynram (1).jpeg1.png"


#mp
bandhavgarh="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\bandhavgarh national park(1)1.png"
bhopal="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\bhopal (1)1.png"
dharampuri="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\dharampuri1)1.png"
gwalior="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\gwalior (1)1.png"
indore="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\indore(1)1.png"
jabalpur="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\jabalpur (1)1.png"
kanha="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\kanha national park (1)1.png"
kuno="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\kuno national park)1.png"
maheshwar="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\maheshwar1)1.png"
shivpuri="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\shivapuri (1)1.png"
ujjain="C:\\Users\\Abhishek Patil\\python\\mini project\\abhay\\Mp\\uzzain (1)1.png"








dic_1={"elephanta":elephanta,"aizawl":aizawl,"serchhip":serchhip,"lunglei":lunglei,"champhai":champhai,"saiha":saiha,"vantawng":vantawng,"phawnpui":phawnpui,"shillong":shillong,"elephanta":elephanta,"double_decker":double_decker,"cherrapunji":cherrapunji,"mawsynram":mawsynram,"balpakram":balpakram,"william":william,"nohkalikai":nohkalikai,"mawsmai":mawsmai,"dwaki":dwaki,"imphal":imphal,"thoubal":thoubal,"tamenglong":tamenglong,"chandel":chandel,"loktak":loktak,"gwalior":gwalior,\
       "kanha":kanha,"bandhavgarh":bandhavgarh,"ujjain":ujjain,"kuno":kuno,"indore":indore,"bhopal":bhopal,"maheshwar":maheshwar,"jabalpur":jabalpur,"shivpuri":shivpuri,"kochi":kochi,"wayanad":wayanad,"kumarakom":kumarakom,"kovalam":kovalam,"kollam":kollam,"sabarimala":sabarimala,"bekal":bekal,"palakkad":palakkad,"trivandrum":trivandrum,"ponmudi":ponmudi,"peerumedu":peerumedu,"guruvayur":guruvayur,"malampuzha":malampuzha,"kasaragod":kasaragod,"thenmala":thenmala,"kottayam":kottayam,"kumily":kumily,"ponnani":ponnani,"thekkady":thekkady,"muthanga":muthanga,"devikulam":devikulam,"thoipetty":thoipetty,"jamshedpur":jamshedpur,"ranchi":ranchi,"betla":betla,"massanjore":massanjore,"hazaribagh":hazaribagh,"bokaro":bokaro,"dhanbad":dhanbad,"kurukshetra":kurukshetra,"panipat":panipat,"rohtak":rohtak,"morni":morni,"damdama":damdama,"manesar":manesar,"kalesar":kalesar,"chandigarh":chandigarh}






  
#img = tk.PhotoImage(file=place)



entry_label = tk.Label(window, text="Enter Place:",font=custom_font)
entry_label.place(x=80,y=110)

entry = tk.Entry(window ,width=30,borderwidth=10,fg="black",font=custom_font)
entry.place(x=200,y=100)



search_button = tk.Button(window, text="Search",bg='gray',fg='blue', command=search_place)
search_button.place(x=350,y=150)


info_text = tk.Text(window, width=50, height=22,bg='lightgrey',borderwidth=10,font=custom_font)
info_text.place(x=120,y=220)

clear_button = tk.Button(window, text="Clear",bg='gray',fg='red', command=clear_entry)
clear_button.place(x=600, y=110)





window.mainloop()