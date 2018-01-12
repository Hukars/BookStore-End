#往数据库添加书籍信息的脚步，需要管理员权限，故你需要先在StoreAdmin对应表中添加一条元组'adminId': 1,、'password': 'hukars',
# coding=utf8
import http.client,urllib.parse

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
    'bookNumbers': "3210",
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
    'bookAuthorIntroduction':"《世界美术名作二十讲》围绕文艺复兴以来西方近二十位艺术大师及其名作展开讨论，着重介绍了文艺复兴初期自乔托以来，经过“三杰”（达•芬奇、米开朗基罗、拉斐尔），十七世纪的伦勃朗、鲁本斯，到十八、十九世纪的近二十位画坛巨匠及其名作。讲解其艺术特点、绘画技巧，又辅以大师生平、时代思潮等内容，从艺术风格延至人格操守，行文生动洗练，深入浅出，形象解读，娓娓道来，紧扣每讲内容，或全貌，或局部，或对比，形象解读，感情表达，易于领悟，融文学、音乐、哲学、社会、时代于一体，给人以丰富而优美的精神享受。",
    'bookIntroduction':"傅雷： 1908年4月7日－1966年9月3日，中国著名的翻译家、作家、教育家、美术评论家，中国民主促进会（民进）的重要缔造者之一。早年留学法国巴黎大学，他翻译了大量的法文作品，其中包括巴尔扎克、罗曼•罗兰、伏尔泰等名家著作。20世纪60年代初，傅雷因在翻译巴尔扎克作品方面的卓越贡献，被法国巴尔扎克研究会吸收为会员。代表作：《傅雷家书》、《约翰•克里斯多夫》、巨人三传（《贝多芬传》、《米开朗琪罗传》、《托尔斯泰传》、巴尔扎克全系列、《世界美术名作二十讲》。"
}

pararms = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request('POST', '/books/creation/', pararms, headers)
response = conn.getresponse()
print(response.status, response.reason)
res = response.read()
print(res)












