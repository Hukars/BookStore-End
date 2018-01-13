#往数据库添加书籍信息的脚步，需要管理员权限，故你需要先在StoreAdmin对应表中添加一条元组'adminId': 1,、'password': 'hukars',
# coding=utf8
import http.client,urllib.parse


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "设计中的设计",
    'bookAuthor': "原研哉 (作者),‎ 朱锷 (译者)",
    'bookISBN': "7209041060, 9787209041065",
    'bookType': "ART",
    'bookPress': "山东人民出版社; 第1版",
    'bookPublishDate': "2006年11月1日",
    'bookPrice': "36.60",
    'bookNumbers': "2890",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/41mwxg7p1NL._SX338_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"原研哉，日本平面设计大师原研哉先生，日本设计中心代表，武藏野美术大学教授，无印良品咨询委员会委员他以一双无视外部世界飞速发展变化的眼睛面对“日常生活”，以谦虚但同时尖锐的目光寻找其设计被需要的所在，并将自己精确地安置在他的意图能够被赋予生命的地方。当我们的日常生活正在越来越陷入自身窠臼之时，他敏锐地感知到了设计的征候和迹象，并且自觉自主地挑战其中的未知领域。他的设计作品显现出来的不落陈规的清新，在于他找到了设计被需求的空间并在其中进行设计。在这样的态度下，他拓展了设计的视野和范畴，在他所经历之处，崭新的地平线不停地被发现和拓展。",
    'bookIntroduction':"《设计中的设计》自二00三年出版以来，在日本先后加印十七次，二O0四年荣获由SUNTORY财团颁发的第二十六届文学艺术大奖，二00五年，在台湾出版后，迅速登上诚品书店、金石堂艺术类图书排行榜，蝉联多期，畅销至今。当你们因为读完这本观念设计书而感到越来越不懂没计时，这并不意味着你对于设计的认识倒退了，而是证明你在设计的世界里又更往深处迈进了一步。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "孩子们的诗",
    'bookAuthor': "朵朵 (作者),‎ 姜二嫚 (作者),‎ 姜馨贺 (作者),‎ 陈科全 (作者),‎ 王子乔 (作者),‎ 茗芝 (作者)",
    'bookISBN': "9787533949716",
    'bookType': "CHILDREN'S BOOK",
    'bookPress': " 浙江文艺出版社; 第1版",
    'bookPublishDate': "2017年9月1日",
    'bookPrice': "53.40",
    'bookNumbers': "200",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/41M9UjImA6L._AC_SX60_CR,0,0,60,60_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/81FHHWOaB9L.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/71ivqgF94kL.jpg",
    'bookAuthorIntroduction':"我的眼睛很小很小／有时遇到心事／就连两行泪／也装不下——陈科全，八岁",
    'bookIntroduction':"果麦版编写的这本《孩子们的诗》不同于一般的儿童诗集。书中的每一首诗都是真正由3－13岁孩子创作的。虽然他们或许还不明白什么是诗，还不认为自己写的是诗，但他们是天生的诗人。简单的语言，能击中每个人心中都有的诗意。不论什么年龄的读者，都会被这些诗句感动。因为这些诗表达自然而直接的情绪，富有天马行空的想象力，不受格式束缚，真诚而灵动。果麦还邀请了Starry阿星、飞行猴CF、九个妖、木可子、黄雷蕾Linali、苏寒、Lett Yice等二十多位国内知名插画家，为书中每一首诗歌创作了兼具美感与奇趣的插画。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)

data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "我们仨",
    'bookAuthor': "杨绛 (作者)",
    'bookISBN': "7108042452, 9787108042453",
    'bookType': "LITERATURE",
    'bookPress': "生活•读书•新知三联书店; 第2版",
    'bookPublishDate': "2012年9月1日",
    'bookPrice': "17.80",
    'bookNumbers': "3000",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/41pi7pBzTcL._SX348_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/61KQ8ypzZDL.jpg",
    'bookAuthorIntroduction':"杨绛(1911—)，原名杨季康，江苏无锡人。1932年苏州东吴大学毕业，同年入清华大学研究院研习。1934年开始发表作品。1935年留学英国、法国，1938年回国。先后任上海震旦女子文理学院教授、清华大学西语系教授。1949年后，任中国社会科学院外国文学所研究员。主要作品有剧本《称心如意》、《弄假成真》，论文集《春泥集》、《关于小说》，散文集《干校六记》。长篇小说《洗澡》．短篇小说集《倒影集》等。主要译著有《堂·吉诃德》、《小癞子》、《吉尔·布拉斯》等。",
    'bookIntroduction':"《我们仨》讲述了九十二岁的杨绛以简洁而沉重的语言，回忆先她而去的女儿钱媛、丈夫钱钟书，回忆一家三口那些快乐而艰难、爱与痛的日子。这个三口之家的动人故事证明：家庭是人生好的庇护所。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "人类简史:从动物到上帝",
    'bookAuthor': "尤瓦尔·赫拉利 (作者),‎ 林俊宏 (译者)",
    'bookISBN': "9787508660752, 7508660757",
    'bookType': "HISTORY",
    'bookPress': "中信出版社; 第2版",
    'bookPublishDate': "2017年2月16日",
    'bookPrice': "48.50",
    'bookNumbers': "2000",
    'bookImageUrl': "https://images-cn-4.ssl-images-amazon.com/images/I/51scxbZQs2L._AC_SY60_CR,0,0,60,60_.jpgjpg,https://images-cn-4.ssl-images-amazon.com/images/I/51lLQLgNJnL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"尤瓦尔·赫拉利，1976年生，牛津大学历史学博士，现为耶路撒冷希伯来大学的历史系教授，青年怪才，全球瞩目的新锐历史学家。他擅长世界历史和宏观历史进程研究。在学术领域和大众出版领域都有很大的兴趣。他的《人类简史》一书让他一举成名，成为以色列超级畅销书，目前这本书已授43个国家版权，在历史学之外，人类学、生态学、基因学等领域的知识信手拈来，根据图书改变的课程上传YOUTUBE后风靡全球，拥有大批青年粉丝。写书，视频课程之外，他还开设有专栏。",
    'bookIntroduction':"《人类简史 从动物到上帝》是以色列新锐历史学家的一部重磅作品。从十万年前有生命迹象开始到21世纪资本、科技交织的人类发展史。十万年前，地球上至少有六个人种，为何今天却只剩下了我们自己？我们曾经只是非洲角落一个毫不起眼的族群，对地球上生态的影响力和萤火虫、猩猩或者水母相差无几。为何我们能登上生物链的顶端，最终成为地球的主宰？"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)

data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "经济学原理(第7版):微观经济学分册+宏观经济学分册(套装共2册)",
    'bookAuthor': "曼昆 (N.Gregory Mankiw) (作者),‎ 梁小民 (译者),‎ 梁砾 (译者)",
    'bookISBN': "9789900161998",
    'bookType': "MANAGEMENT",
    'bookPress': "北京大学出版社; 第1版",
    'bookPublishDate': "2015年5月1日",
    'bookPrice': "103.10",
    'bookNumbers': "1990",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/61bJjkRPR6L._SX356_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51WXj0xzEDL._AC_SY60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"N. 格里高利•曼昆（N. Gregory Mankiw）， 哈佛大学经济学教授，曾在普林斯顿大学和麻省理工学院学习经济学。他讲授过宏观经济学、微观经济学、统计学和经济学原理等课程。曼昆教授还是美国国家经济研究局（NBER）的合作研究人员，国会预算办公室、波士顿和纽约联邦储备银行的顾问，以及美国教育考试服务中心（ETS）的经济学先修课程考试研发委员会成员。2003—2005年，他曾担任美国总统经济顾问委员会的主席。",
    'bookIntroduction':"《经济学原理（第7版）：微观经济学分册+宏观经济学分册》是目前国内市场上很受欢迎的引进版经济学教材之一，其特点是它的“学生导向”，它更多地强调经济学原理的应用和政策分析，而非经济学模型。第7版在延续该书一贯风格的同时，对第6版作了全面修订和改进。大幅更新了“新闻摘录”“案例研究”等专栏，拓展了章后习题。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)





data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "花间集 平装",
    'bookAuthor': "温庭筠 (作者),‎ 赵崇祚 (编者)",
    'bookISBN': "9787559407795, 755940779X",
    'bookType': "Sinology",#国学
    'bookPress': "江苏凤凰文艺出版社; 第1版",
    'bookPublishDate': "2017年8月1日",
    'bookPrice': "31.60",
    'bookNumbers': "3110",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/51vysAc7LYL._SX352_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/31LyfLkAJpL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"赵崇祚，字弘基，五代后蜀人。后蜀开国功臣赵廷隐之子，编集《花间集》。《花间集》一直被认为是现存最早的词集。",
    'bookIntroduction':"《花间集》是我国现存最早的诗词总集。它收录了晚唐时期温庭筠、韦庄、薛昭蕴等十八家词，共五百首。所收词包含男女相思、史事古迹、风物人情、边塞旧事、山水花鸟等。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "时间简史（插图本）",
    'bookAuthor': "史蒂芬·霍金 (作者),‎ 许明贤 (译者),‎ 吴忠超 (译者)",
    'bookISBN': "B017U53N1A",
    'bookType': "SCIENCE",
    'bookPress': "湖南科学技术出版社; 第1版",
    'bookPublishDate': "2015年2月1日",
    'bookPrice': "34.30",
    'bookNumbers': "1910",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/51%2Bb28C2jmL.jpg",
    'bookAuthorIntroduction':"史蒂芬·霍金 (Stephen Hawking)，于1942年1月8日生于牛津，那一天刚好是伽利略逝世三百年。可能因为他出生在第二次世界大战的时代，所以小时候对模型特别着迷。他十几岁时不但喜欢做模型飞机和轮船，还和学友制作了很多不同种类的战争游戏，反映出他研究和操控事物的渴望。这种渴望驱使他攻读博士学位，并在黑洞和宇宙论的研究上获得重大成就。。",
    'bookIntroduction':"《时间简史(插图本)》尽管霍金教授的著述极为清晰而机智，有些读者仍然觉得难以掌握复杂的概念。为了使读者加深理解，《时间简史》还增加了240多幅彩色插图，包括卫星图像和照片。这些都应归功于诸如哈勃空间望远镜和电脑三维和四维实体成像等技术进步之赐。详细的插图说明使读者能体验到星系际太空的广漠、黑洞的奇妙性质以及物质和反物质碰撞的粒子物理的微观世界。作为一本飨以读者宇宙学的最新理解的经典著作，《时间简史》插图本是探索时间和空间核心秘密的引人入胜的故事。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "大国宪制:历史中国的制度构成",
    'bookAuthor': "苏力 (作者)",
    'bookISBN': "9787301288955",
    'bookType': "LEGAL",
    'bookPress': "北京大学出版社; 第1版 ",
    'bookPublishDate': "2017年12月1日",
    'bookPrice': "62.50",
    'bookNumbers': "3410",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/41fjqMFHeHL._SX375_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"苏力，北京大学博雅讲席教授，北京大学法学院天元讲席教授，长江学者。祖籍江苏，1955年愚人节出生于安徽合肥。少年（1970年）从军，再当工人；1978年恢复高考后，复员军人进了北大法学院，获学士学位；1985年读研期间，赴美留学，先后获硕士、博士学位。1992年起任教北大法学院至今。先后独立发表论文200余篇，出版个人独著、文集和译著20余种。",
    'bookIntroduction':"中国古代宪制作为人类历史上持久存在的制度经验，有其自己的逻辑和合理之处。但近年来社科领域特别是法学领域，对于中国自己的制度研究较少。作者从法学、社会学、历史学等多个学科的宏观视角出发，对历史中国的宪制经验进行了总体把握和深度总结，揭示了历史中国千年传承、具有强大活力的原因，并力图阐释中国在制度文明上独有的贡献。本研究从历史中国所面临的至关重要的核心政治问题出发，逐一阐释了“齐家”“治国”“平天下”等构成制度，以及军事制度、官僚体系、经济制度等，从而重构了历史中国的制度图景。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)

data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "世界美术名作二十讲(修订版)(彩色典藏版) 平装",
    'bookAuthor': "傅雷 (作者)",
    'bookISBN': " 7539985569, 7301286481,9787539985565",
    'bookType': "ART",
    'bookPress': "江苏凤凰文艺出版社; 第1版 ",
    'bookPublishDate': "2017年4月1日",
    'bookPrice': "46.80",
    'bookNumbers': "3510",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/51XJlnTUZbL._SX388_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51QJinp1t4L._AC_SY60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"傅雷： 1908年4月7日－1966年9月3日，中国著名的翻译家、作家、教育家、美术评论家，中国民主促进会（民进）的重要缔造者之一。早年留学法国巴黎大学，他翻译了大量的法文作品，其中包括巴尔扎克、罗曼•罗兰、伏尔泰等名家著作。20世纪60年代初，傅雷因在翻译巴尔扎克作品方面的卓越贡献，被法国巴尔扎克研究会吸收为会员。代表作：《傅雷家书》、《约翰•克里斯多夫》、巨人三传（《贝多芬传》、《米开朗琪罗传》、《托尔斯泰传》、巴尔扎克全系列、《世界美术名作二十讲》。",
    'bookIntroduction':"《世界美术名作二十讲》围绕文艺复兴以来西方近二十位艺术大师及其名作展开讨论，着重介绍了文艺复兴初期自乔托以来，经过“三杰”（达•芬奇、米开朗基罗、拉斐尔），十七世纪的伦勃朗、鲁本斯，到十八、十九世纪的近二十位画坛巨匠及其名作。讲解其艺术特点、绘画技巧，又辅以大师生平、时代思潮等内容，从艺术风格延至人格操守，行文生动洗练，深入浅出，形象解读，娓娓道来，紧扣每讲内容，或全貌，或局部，或对比，形象解读，感情表达，易于领悟，融文学、音乐、哲学、社会、时代于一体，给人以丰富而优美的精神享受。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)





data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "宝宝第一套高情商养成书:皮特猫(第二辑)",
    'bookAuthor': "金柏莉•迪安 (Kimberly Dean) (作者),‎ 詹姆斯•迪安 (James Dean) (作者)",
    'bookISBN': "9787549621095",
    'bookType': "CHILDREN'S BOOK",
    'bookPress': "文汇出版社; 第1版",
    'bookPublishDate': "2017年6月1日",
    'bookPrice': "80.28",
    'bookNumbers': "3022",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51k6HIPfPhL._SX389_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/61vJTgL-IqL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"詹姆斯・迪安（James Dean）《纽约时报》畅销书作者，也是一位杰出的艺术家，詹姆斯的作品在横跨全美的90多家画廊和商店出售。他和艾瑞克•利温一起创造了皮特猫这一经典形象。目前，《皮特猫》系列已畅销全球1000万册, 在美国和中国都是最受孩子们欢迎的绘本之一。这一次，詹姆斯亲自操刀，参与故事的文字创作，为我们带来了皮特猫和他的家人、朋友的动人故事。",
    'bookIntroduction':"《宝宝第一套高情商养成书:皮特猫(第二辑)》 内容简介：《皮特猫》是一套在美国家喻户晓、几乎每个孩子必读的经典绘本，已在全球畅销1000万册，在美国和中国都是最受孩子们欢迎的绘本之一。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "人间词话 平装",
    'bookAuthor': "王国维 (作者),‎ 周兴泰 (注译)",
    'bookISBN': "7511357733, 9787511357731",
    'bookType': "LITERATURE",
    'bookPress': "中国华侨出版社; 第1版",
    'bookPublishDate': "2016年4月1日",
    'bookPrice': "19.08",
    'bookNumbers': "1984",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51ZGg1L3QUL._SX353_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/61fiD9gVpkL._AC_SY60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"王国维（1877—1927）字静安，号观堂，文学家、美学家、哲学家、古文字学家。曾赴日本留学，并担任清政府学部总务司行走、图书馆编译、名词馆协韵等职，著有《人间词话》等3部著作。1911年辛亥革命后，王国维避居日本。1922年受聘北京大学担任教授。1927年6月，王国维投颐和园昆明湖自尽。",
    'bookIntroduction':"《人间词话》是中国近代最负盛名的词话著作。在这部著作中，一代国学大师王国维在传统的词话形式及传统的概念、术语和思维逻辑中，十分自然巧妙地融入了新的观念和方法，他总结的理论问题具有相当普遍的意义，在中西文艺思想交流融合的道路上迈出了坚实的一步，《人间词话》在新旧两代的读者中产生了巨大的反响，在中国近代文学批评史上具有崇高的地位。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "人间草木 平装",
    'bookAuthor': "汪曾祺 (作者)",
    'bookISBN': "756991354X, 9787569913545",
    'bookType': "LITERATURE",
    'bookPress': "北京时代华文书局; 第1版",
    'bookPublishDate': "2017年4月1日",
    'bookPrice': "24.91",
    'bookNumbers': "2128",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51piDkGgW9L._SX403_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51-9bBtd53L._AC_SY60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"汪曾祺（1920-1997），江苏高邮人，当代著名作家、散文家、京派小说创作的代表人物，被誉为“抒情的人道主义者” “中国最后一位士大夫”。他在短篇小说和散文创作上成就颇高。擅长从生活琐事入手，文字平淡质朴，深得自然之妙趣，于不经意间渗透出睿智、从容的生活智慧。",
    'bookIntroduction':"《人间草木》是汪曾祺先生的经典小品文集，他用极简的笔，极淡的墨写出了草木山川、花鸟虫鱼的人味，写出了乡情民俗、凡人小事温润的乡土味；以一颗从容豁达的心写出了世间的美好与灵动。他的笔尖下总是有着一连串的惊喜：清晨薄雾里带着露珠的洁白的缅桂花，明亮、丰满而使人丰满的昆明的雨，饱涨着花骨朵的木香，自得其乐的栀子花，巷子里卖杨梅的苗族女子柔柔的声音，联大那些令人难以忘却的师友，抑或是没有大喜大忧、没有烦恼、无欲望亦无追求、天然恬淡、抱膝闲看一切的“活庄子”般的闹市闲民。汪曾祺先生一生都对生活投入真情，那水洗般的文字有种洗涤一切红尘世俗的力量，赋予了作品无限的生命力。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)

data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "史记(精注全译)(套装共6册)",
    'bookAuthor': "司马迁 (作者),‎ 李翰文 (编者)",
    'bookISBN': "9787550280496",
    'bookType': "HISTORY",
    'bookPress': "北京联合出版公司; 第1版",
    'bookPublishDate':"2016年8月1日",
    'bookPrice': "116.82",
    'bookNumbers': "298",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51kw201FUSL._SY498_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51wdP1wPMiL._AC_SY60_CR,0,0,60,60_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/61a4JjKvPlL._AC_SY60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"司马迁，字子长，中国西汉伟大的史学家、文学家、思想家。被后世尊称为史迁、太史公、历史之父。他以其“究天人之际，通古今之变，成一家之言”的史识创作了中国第 一部纪传体通史《史记》。",
    'bookIntroduction':"《史记(精注全译)(套装共6册)》主要包括《史记（第1册）》《史记（第二册）》《史记（第三册）》《史记（第四册）》《史记（第五册）》《史记（第六册）》共6册。《史记(精注全译)(套装共6册)》是一部贯穿占令的通史，从传说中的黄帝开始，一直写到汉武帝元狩元年（前122年），叙述了三千年左右的历史。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)




data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "未来简史 平装",
    'bookAuthor': "尤瓦尔•赫拉利 (作者),‎ 林俊宏 (译者)",
    'bookISBN': "7508672062, 9787508672069",
    'bookType': "HISTORY",
    'bookPress': "中信出版社; 第1版",
    'bookPublishDate': "2017年2月1日",
    'bookPrice': "49.00",
    'bookNumbers': "1899",
    'bookImageUrl':"https://images-cn-4.ssl-images-amazon.com/images/I/41LbG0WghWL._SX366_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"尤瓦尔•赫拉利，1976年生，青年怪才，全球瞩目的新锐历史学家，牛津大学历史学博士，耶路撒冷希伯来大学历史系教授，著有国际畅销书《人类简史》。其新作《未来简史》，以宏大视角审视人类未来的终极命运，甫一出版就在全球掀起一股风潮，引起广泛关注。",
    'bookIntroduction':"《未来简史:从智人到智神》进入21世纪后，曾经长期威胁人类生存、发展的瘟疫、饥荒和战争已经被攻克，智人面临着新的待办议题：永生不老、幸福快乐和成为具有“神性”的人类。在解决这些新问题的过程中，科学技术的发展将颠覆我们很多当下认为无需佐证的“常识”，比如人文主义所推崇的自由意志将面临严峻挑战，机器将会代替人类做出更明智的选择。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "金字塔原理:麦肯锡40年经典培训教材",
    'bookAuthor': "芭芭拉.明托 (作者),‎ 汪洱 高愉 (译者)",
    'bookISBN': "7544268500, 9787544268509",
    'bookType': "MANAGEMENT",
    'bookPress': "南海出版公司; 第2版",
    'bookPublishDate': "2013年10月1日",
    'bookPrice': "30.90",
    'bookNumbers': "3490",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51mUTgdfGAL._SX335_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/41M0Szt6dGL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"作者:（美）芭芭拉.明托 译者:汪洱 高愉",
    'bookIntroduction':"《金字塔原理》内容简介：金字塔原理是一种重点突出、逻辑清晰、主次分明的逻辑思路、表达方式和规范动作。金字塔的基本结构是：中心思想明确，结论先行，以上统下，归类分组，逻辑递进。先重要后次要，先全局后细节，先结论后原因，先结果后过程。金字塔训练表达者：关注、挖掘受众的意图、需求、利益点、关注点、兴趣点和兴奋点，想清内容说什么、怎么说，掌握表达的标准结构、规范动作。金字塔帮助达到沟通效果：重点突出，思路清晰，主次分明，让受众有兴趣、能理解、能接受、记得住。搭建金字塔的具体做法是：自上而下表达，自下而上思考，纵向疑问回答／总结概括，横向归类分组／演绎归纳，序言讲故事，标题提炼思想精华。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)

data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "影响力(经典版)",
    'bookAuthor': "罗伯特·B.西奥迪尼 (作者),‎ 闾佳 (译者)",
    'bookISBN': "7550284539, 9787550284531",
    'bookType': "MANAGEMENT",
    'bookPress': "北京联合出版公司; 第1版",
    'bookPublishDate': "2016年9月1日",
    'bookPrice': "38.80",
    'bookNumbers': "2022",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51JJmLKwm1L._SX334_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51m0nr3LTyL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"",
    'bookIntroduction':"本书是西奥迪尼的社会心理学经典作品，在书中，作者从专业角度为读者阐释了顺从他人行为背后的六大基本原则：互惠、承诺和一致、社会认同、喜好、权威和稀缺，为我们解释了为什么有些人极具说服力，而我们总是容易上当受骗。本书对于商业人士以及广大普通读者有深远的意义，教你学会对顺从业人士说“不”，帮助你成为一个真正对他人有影响力的人。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "学会提问(原书第10版) ",
    'bookAuthor': "尼尔•布朗 (Neil Browne) (作者),‎ 斯图尔特•基利 (Stuart Keeley) (作者)",
    'bookISBN': "9787111406594, 7111406591",
    'bookType': "PSYCHOLOGY",
    'bookPress': "机械工业出版社; 第1版",
    'bookPublishDate': "2013年5月1日",
    'bookPrice': "28.01",
    'bookNumbers': "3001",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/41d1V0Vwz6L._SX348_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"尼尔•布朗（Neil Browne），博林格林州立大学（Bowling Green State University）的杰出经济学教授。获有托雷多大学法学博士学位和德州大学的博士学位。曾经合著七本书，并在专业期刊发表一百余篇研究论文。数十所学院和大学曾经聘请布朗教授，协助教职员培养批判性思考技巧。他也任职于《韩国批判性思考期刊》的编辑委员会。一九八九年，荣获教育促进支持协调会的“全国年度杰出教授”银牌奖章。同年也获“俄亥俄州年度杰出教授”荣衔。曾获颁无数地方性和全国性的教学奖。",
    'bookIntroduction':"《学会提问(原书第10版)》内容简介：如果在你的家乡投资建一座核电厂，你会支持还是反对？如果学校出于安全考虑要对每一个学生进行安全检查，你会高兴还是愤怒？如果你的兄弟姐妹做了父母明令禁止的事，你会告诉父母还是隐瞒不说？无数专家都说股市要跌、房价要涨，或者激烈地唱着反调，你相信谁？质疑谁？"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "梦的解析(经典全译本)",
    'bookAuthor': "西格蒙德·弗洛伊德 (Sigmund Freud) (作者),‎ 江月 (译者)",
    'bookISBN': "9787554608708",
    'bookType': "PSYCHOLOGY",
    'bookPress': "古吴轩出版社; 第1版",
    'bookPublishDate': "2017年2月1日",
    'bookPrice': "23.92",
    'bookNumbers': "2563",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51BbRWzkJUL._SY498_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51raQ6duvZL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"西格蒙德·弗洛伊德（Sigmund Freud，1856－1939），奥地利医生兼心理学家、哲学家、精神分析学的创始人。弗洛伊德终生从事写作和临床治疗。他的思想极为深刻，在探讨问题时，往往引述历代文学、历史、医学、哲学、宗教等材料。主要著作：《歇斯底里研究》《梦的解析》《多拉的分析》《性学三论》《精神分析运动史》《图腾与禁忌》《论无意识》《焦虑问题》《幻想的未来》等。",
    'bookIntroduction':"《梦的解析》是一本能让自己了解自己的书，人所有的行为习惯都跟童年有关，与梦和潜意识有关！心理学大师弗洛伊德将这本《梦的解析》写给每个人的精神世界关怀书，完全忠实于英文原版的经典译本；揭开梦与潜意识的深层奥秘，改变人类历史的划时代经典，荣格、舒尔茨、马斯洛等心理学大家诚挚推荐！"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "《鬼谷子》智慧全解",
    'bookAuthor': "丁一 (作者)",
    'bookISBN': "9787568028998, 7568028992",
    'bookType': "Sinology",
    'bookPress': "华中科技大学出版社; 第1版",
    'bookPublishDate': "2017年8月1日",
    'bookPrice': "33.00",
    'bookNumbers': "2300",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/41LcAgNscQL._SX340_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"鬼谷子，生卒年不详，姓王名诩，又名王禅，春秋战国时期卫国朝歌（今河南淇县）人，也有人说他是楚国人，纵横家之鼻祖，有名的思想家、谋略家、军事家。因他常入云梦山采药修道，隐居周阳城清溪之鬼谷，故自称鬼谷先生，世称鬼谷子。",
    'bookIntroduction':"《鬼谷子》智慧全解一书，收录了《鬼谷子》原文，并依据权wei注本，辅之以注解和译文，采用通俗化语言，强化可读性，实现轻松障碍阅读。另外，为了强化本书的现实指导意义，文中还收录了大量经典案例，辅以分析。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "儒林外史(作家榜插图珍藏版•2018全新未删节足本) ",
    'bookAuthor': "吴敬梓 (作者),‎ 作家榜经典 (编者)",
    'bookISBN': "9787533948481",
    'bookType': "Sinology",
    'bookPress': "浙江文艺出版社; 第1版",
    'bookPublishDate': "2017年5月1日",
    'bookPrice': "26.55",
    'bookNumbers': "3299",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51ME%2BcHd4hL._SX398_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/41OXLjfh3kL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"吴敬梓（1701-1754），清代小说家。生于安徽全椒的科举世家，自幼博览群书，善作诗文辞赋。18岁考取秀才。21岁时家道中落，目睹官场斗争险恶、亲历家族争产风波。33岁时移居南京，卖文为生。数次参加科考，名落孙山。35岁潜心写作长篇小说《儒林外史》，历时十年终于完稿。54岁时逝于扬州。胡适自称是敬重吴敬梓先生的“吴迷”，鲁迅称他是曹雪芹外“伟大”的古典作家。《儒林外史》至今深受读者喜爱。",
    'bookIntroduction':"一部写透中国古代官场的百科全书式小说：执金杯饮酒的狂狷儒士，只身逃婚的叛逆才女，酷爱男风的名门基友，隐居山林的真儒贤人，死磕科考的哭号童生，招摇撞骗的冒牌诗人，劝女殉夫的礼教狂徒，从淳朴上进的孝子变为贪婪虚伪的卑鄙之徒……全书有名有姓的人物多达九十多位，一张张面孔似曾相识，一个个故事独立又精彩，读起来轻松畅快，犹如身临其境。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)





data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "反物质 平装",
    'bookAuthor': "弗兰克·克洛斯 (Frank Close) (作者),‎ 羊奕伟 (译者)",
    'bookISBN': "7562495564, 9787562495567",
    'bookType': "SCIENCE",
    'bookPress': "重庆大学出版社; 第1版",
    'bookPublishDate': "2016年4月1日",
    'bookPrice': "23.30",
    'bookNumbers': "2790",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/511YtP6gYTL._SX394_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"作者：弗兰克•克洛斯（Frank Close）英国人，牛津大学物理学教授，埃克塞特大学研究员，曾任卢瑟福•阿普尔顿实验室的理论物理学部门负责人，曾荣获了大英帝国官佐勋章（OBE）、英国物理学会开尔文奖。他还担任过欧洲核子研究中心公共教育和通讯部的负责人，因其在促进物理学的公众理解和科普写作方面的突出贡献，他获得了英国媒体评出的2007年最佳科普写作奖（“Sygenta Prize”）。他的其他作品有：《路西法的遗产》（2000）、《奥德赛粒子》（2002）、《虚空》（2007）等。",
    'bookIntroduction':"探究神奇的物质世界，厘清科幻与真实的界限；《最初三分钟》《宇宙波澜》《弦理论》科普系列。黑洞、弯曲时空、奇异粒子、夸克……物理学的所有令人费解的发现中，反物质的存在无疑是最神奇的一个，也给科幻作家们提供了很好的创作空间。本书就是一本关于反物质相关知识的译著。本书以反物质炸弹为切入点，结合科学实验、实例及现象，用通俗的语言介绍了人类对反物质逐步深入的研究历程，让读者能清楚地了解反物质的存在、产生、湮灭、存储、利用及影响等科学知识，是一部系统而通俗的反物质科普书"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "最好的辩护",
    'bookAuthor': "(美)德肖维茨(A.M. Dershowitz) (作者),‎ 唐交东 (译者)",
    'bookISBN': "B00WM94YTA",
    'bookType': "LEGAL",
    'bookPress': "法律出版社; 第1版 ",
    'bookPublishDate':"2014年5月1日",
    'bookPrice': "40.00",
    'bookNumbers': "3800",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51yUqYw6HFL.jpg",
    'bookAuthorIntroduction':"作者艾伦•德肖维茨是美国哈佛大学著名法学教授、作家，又是美国当代著名辩护律师，曾为辛普森杀妻案、克林顿绯闻案与弹劾案、泰森案等一系列轰动全球的大案担任辩护律师。代表作《最好的辨护》是他的辩护实录，每个曲折的案子几乎都是一部惊悚小说，富有争议、影响颇大，作者将案件背景及诉讼过程进行深入浅出、生动形象的叙述和描写。书中不乏精彩的辩护场面，纯熟的辩护技巧，曲折迭宕的案情发展，令人吃惊的诉讼结局。精彩动人的情节中向读者传递出律师职业的精彩、坎坷和挑战。",
    'bookIntroduction':"本书是美国当代律师辩护实录中的经典。作者艾伦•德肖维茨是美国哈佛大学著名法学教授、作家，又是美国当代著名辩护律师，曾为辛普森杀妻案、克林顿绯闻案与弹劾案、泰森案等一系列轰动全球的大案担任辩护律师。代表作《最好的辨护》是他的辩护实录，每个曲折的案子几乎都是一部惊悚小说，富有争议、影响颇大，作者将案件背景及诉讼过程进行深入浅出、生动形象的叙述和描写。书中不乏精彩的辩护场面，纯熟的辩护技巧，曲折迭宕的案情发展，令人吃惊的诉讼结局。精彩动人的情节中向读者传递出律师职业的精彩、坎坷和挑战。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "西窗法雨 精装 ",
    'bookAuthor': "刘星 (作者)",
    'bookISBN': "9787511850157",
    'bookType': "LEGAL",
    'bookPress':"法律出版社; 第3版",
    'bookPublishDate': "2013年9月1日",
    'bookPrice': "29.60",
    'bookNumbers': "3190",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51kxMQVKCwL._SX325_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51QIzxaHz8L._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':"刘星，毕业于中山大学法学院、中国政法大学研究生院，在美国法学院做过访问学者。现为中国政法大学教授、博士生导师。出版法学著作多部，发表论文若干，并在《南方周末》、《法制日报》、《文汇报》等报刊辟有法学随笔专栏。",
    'bookIntroduction':"本书以亲切家常、平和幽默的手法漫谈西方法律文化，对似乎是信手拈来的法律现象材料进行点拨评说，说的是西方法律文化现象，却时时启蒙着中国人的法律意识和法治观念，不着痕迹地调动着读者的思维，去思考中国的问题。文章短小、精彩，通过讲故事的方式使读者在不知不觉中领略作者颇为尖端、颇为前沿的研究心得，在这样的论说里，进入法律的智慧天地，享受智慧的乐趣。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "乌合之众(经典全译本)",
    'bookAuthor': "古斯塔夫·勒庞 (作者)",
    'bookISBN': "978720108370401, 9787201083704",
    'bookType': "PSYCHOLOGY",
    'bookPress': "天津人民出版社; 第1版",
    'bookPublishDate': "2017年10月1日",
    'bookPrice': "103.10",
    'bookNumbers': "2110",
    'bookImageUrl': "https://images-cn.ssl-images-amazon.com/images/I/51V5fgqm1qL._SX359_BO1,204,203,200_.jpgjpg,https://images-cn.ssl-images-amazon.com/images/I/51e7H0xNXcL._AC_SX60_CR,0,0,60,60_.jpg",
    'bookAuthorIntroduction':" 古斯塔夫·勒庞（Gustave Le Bon, 1841-1931），法国社会心理学大师，群体心理学创始人，被誉为“群体社会学界的马基雅维利”。著有《乌合之众》、《各民族进化的心理学规律》、《法国大革命与革命心理学》、《战争心理学》等，著作被翻译成近二十种语言，在国际学术界有着广泛影响。",
    'bookIntroduction':"《乌合之众--大众心理研究》是一本杰出的心理学名著，颠覆了通常对群体的认识，《乌合之众--大众心理研究》将群体的特点剖析得淋漓尽致。勒庞以18世纪的法国大革命为背景，《乌合之众--大众心理研究》深入地剖析了群体的种种特点及其成因，为众多常见而令人称奇的社会现象及群体行为开创了独特的观察视角，即群体创造了人类社会的文明与繁荣，但群体心理与行为也会给人类社会带来难以预料的灾难。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)



data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "心画:中国文人画五百年",
    'bookAuthor': "卜寿珊 (Susan Bush) (作者),‎ 皮佳佳 (译者)",
    'bookISBN': "9787301287699",
    'bookType': "ART",
    'bookPress': "北京大学出版社; 第1版",
    'bookPublishDate': "2017年11月1日",
    'bookPrice': "45.80",
    'bookNumbers': "3450",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51IXHteCOzL._SX333_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"卜寿姗，美国著名艺术史家，现为哈佛大学费正清研究中心研究员。自上世纪60年代开始就一直致力于中国文人画研究。她的主要著作还有与孟克文（Christian Murck）合著的《中国艺术理论》。",
    'bookIntroduction':"《心画：中国文人画五百年》是研究中国文人画的经典之作。海外美术史学生了解中国艺术史的必读书。美国著名艺术史家谢伯轲、方闻、高居翰 推荐。国内著名学者朱良志和高建平推荐。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "给孩子的中国历史故事:作家榜经典插图珍藏本",
    'bookAuthor': "汤芸畦 (作者),‎ 作家榜经典 (编者)",
    'bookISBN': "9787533950835",
    'bookType': "CHILDREN'S BOOK",
    'bookPress': " 浙江文艺出版社; 第1版 ",
    'bookPublishDate': "2017年11月1日",
    'bookPrice': "34.22",
    'bookNumbers': "2234",
    'bookImageUrl':"https://images-cn.ssl-images-amazon.com/images/I/51aXQ9lDavL._SX398_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"汤芸畦，民国传奇学者，性耽文史，大隐于市。本书为其代表作，深入浅出，将枯燥单调的历史变得生动有趣，被誉为“故事版极简中国史”，问世后妇孺皆喜，流传至今，一版再版，历久弥新。",
    'bookIntroduction':"畅销70年的历史启蒙必读经典，让孩子轻松读懂五千年中国史！70年口碑相传，40篇锦绣文章，民国传奇学者汤芸畦，以人物和事件为主线，用讲故事的方式为孩子讲述中国历史，将知识性与趣味性完美结合，让孩子不知不觉开拓眼界。从尧舜时代到春秋战国，从秦并天下到三国争霸，从魏晋南北朝到隋唐两宋，从元明清朝到民国北伐，千年历史事件的来龙去脉，变得通俗易懂，生动有趣，让孩子在充满趣味的阅读中，全面了解从远古到近代的历史大事件，奠定一生的历史知识基础！"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)

data={
    'adminId': 1,
    'password': 'hukars',
    'bookName': "人工智能简史 精装",
    'bookAuthor': "刘韩 (作者)",
    'bookISBN': "9787115473530",
    'bookType': "SCIENCE",
    'bookPress': "人民邮电出版社,中国工信出版集团; 第1版",
    'bookPublishDate': "2018年1月1日",
    'bookPrice': "35.40",
    'bookNumbers': "3490",
    'bookImageUrl':"https://images-cn-4.ssl-images-amazon.com/images/I/61s2e%2BnEP7L._SY498_BO1,204,203,200_.jpg",
    'bookAuthorIntroduction':"作者：刘韩，出生于中国福建省的一个教师家庭，在福安市和宁德市度过了幸福的少年时光。1986年就读于中国科学技术大学，主修计算机科学。1991年开始在北京工作和生活，先后就职于中国科学院、SAP、Informix、华润集团、首创网络等公司",
    'bookIntroduction':"《人工智能简史》从多个角度介绍人工智能的发展历史，重点介绍人工智能领域杰出的科学家，以及他们创造非凡成果的有趣故事。透过搜索引擎、网上购物、社交网络、智能家居等应用，人工智能已经开始影响所有人的工作和生活，未来这种影响还会越来越大，最终人工智能将会像电力一样，成为一个无所不在的基础设施"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)


























