import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont
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







}

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







def search_place():
    place = entry.get().lower()
    if place in data:
        # Clear previous content
        info_text.delete(1.0, tk.END)
        
        # Insert place data
        info_text.insert(tk.END, f"Place: {data[place]['place']}\n\n"
                                  f"State: {data[place]['state']}\n\n"
                                  f"Top Attractions: {data[place]['places']}\n\n"
                                  f"Recommended Hotels: {data[place]['hotels']}\n\n"
                                  f"Details: {data[place]['details']}")
        
        # Display image if available
        try:
            img = tk.PhotoImage(file=dic_1[place])  # Update path to your image folder
            image_label.config(image=img)
            image_label.image = img
        except:
            image_label.config(image='', text="No image available")
        
    else:
        info_text.delete(1.0, tk.END)
        image_label.config(image='', text="No image available")
        messagebox.showinfo('Sorry', "Place Not Found. Check the spelling or enter a different place.")


def clear_entry():
    entry.delete(0, tk.END)
    info_text.delete(1.0, tk.END)
    image_label.config(image='', text="No image available")


# Initialize the main window
window = tk.Tk()
window.title("Place Guide - Explore India")
window.geometry("1100x750")
window.config(bg='#f0f0f0')  # Light background color

# Custom fonts
custom_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
button_font = tkFont.Font(family="Helvetica", size=12)

# Set background image
bg_image = tk.PhotoImage(file="C:\\Users\\Abhishek Patil\\python\\mini project\\bg1.png")  # Update to your image path
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Title Label
title_label = tk.Label(window, text="Welcome to India Place Guide", font=title_font, fg="#4B4B4B", bg='#f0f0f0')
title_label.pack(pady=20)

# Frame for entry and buttons
input_frame = tk.Frame(window, bg='#e0e0e0', bd=5, relief='groove')
input_frame.place(relx=0.5, y=100, anchor='n', width=1000, height=80)

# Label and entry field inside input_frame
entry_label = tk.Label(input_frame, text="Enter Place:", font=custom_font, bg='#e0e0e0', fg='#333333')
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(input_frame, width=30, font=custom_font, borderwidth=5, relief='groove')
entry.grid(row=0, column=1, padx=10, pady=10)

# Search and Clear buttons inside input_frame
search_button = tk.Button(input_frame, text="Search", font=button_font, command=search_place, bg='#5CB85C', fg='white', relief='raised', padx=20)
search_button.grid(row=0, column=2, padx=10, pady=10)

clear_button = tk.Button(input_frame, text="Clear", font=button_font, command=clear_entry, bg='#D9534F', fg='white', relief='raised', padx=20)
clear_button.grid(row=0, column=3, padx=10, pady=10)

# Frame for place details and image
output_frame = tk.Frame(window, bg='#f9f9f9', bd=5, relief='groove')
output_frame.place(relx=0.5, y=200, anchor='n', width=1200, height=600)

# Info Text box for displaying place details
info_text = tk.Text(output_frame, width=60, height=20, font=custom_font, wrap='word', bg='#f7f7f7', relief='ridge', padx=10, pady=10)
info_text.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

# Image label for place images
image_label = tk.Label(output_frame, text="Image will appear here", font=custom_font, relief="sunken", width=30, height=15, bg='#f7f7f7')
image_label.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

# Adjust column and row weights in output_frame for proper resizing
output_frame.grid_columnconfigure(0, weight=3)
output_frame.grid_columnconfigure(1, weight=2)



# Tooltips for buttons (enhanced UX)
def create_tooltip(widget, text):
    tooltip = tk.Label(window, text=text, bg='#333333', fg='white', padx=5, pady=3, font=("Helvetica", 10, "normal"))
    tooltip.place_forget()

    def on_enter(event):
        tooltip.place(x=event.x_root + 20, y=event.y_root + 10)

    def on_leave(event):
        tooltip.place_forget()

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)


create_tooltip(search_button, "Click to search the place")
create_tooltip(clear_button, "Click to clear the entry and details")

# Run the application
window.mainloop()

