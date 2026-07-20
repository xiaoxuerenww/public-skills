# Harvey Algorithm Coding Raw Comments By Question

Source corpus: local scrape under `outputs/raw_posts/`.

Rule: raw post/reply content is preserved. No rewriting or summarization inside quoted blocks.

## Source Highlighting / Citation Tagging

### Source: `1122459`

Original post: https://www.1point3acres.com/bbs/thread-1122459-1-1.html

```text
没有在地里看到面经 分享一下
Harvey AI 是一个做法律LLM的startup，hr在LinkedIn reachout
创始人是有legal背景但是没有tech背景
面的是senior/staff，第一轮电面面经:
一共是三道小题，有相关性。需要在codepad里面run。
第一部分：给了一个LLM的output，给了一些sources (list of strings), 需要返回每个source match的次数
第二部分：一样的input 这次需要给match的地方加上<tag></tag>, 要注意考虑overlap的情况
第三部分：在tag后面加上这个highlight对应的哪个source，比如 [1][3]
题目内容太多而且都是很难搞的parse操作，比较没意思
求加米~~~
```

### Source: `1116604`

Original post: https://www.1point3acres.com/bbs/thread-1116604-1-1.html

```text
问题和地里其他帖子很像，我再提供些细节。
题目背景是给一个model response （一个长string），和sources（list of string）作为inputs，做word level match。
Part 1：
数每一个source有几次match，然后返回一个list
Part 2:
给source加tag，这个和其他帖子一样。
Part 3:
在加过tag的基础上添加citation，比如<yellow>balabala</yellow>[1][0]。citation根据source被cited次数降序排列。
```

### Source: `1144173`

Original post: https://www.1point3acres.com/bbs/thread-1144173-1-1.html

```text
加tag的那个题。地里的面经都没有说到这个题目的难点上。
给定一段文字 we will have a big beautiful bill
和一列关键词组["big beautiful", "beautiful bill"]
给关键字加上标注。比如这个例子，结果是 we will have a <tag>big beautiful bill</tag>.
注意到了没？词组是可以重叠的，然后重叠的这些我们加tag的时候，就要一直延续到cover最长的重叠。词组也不一定是两个words的长度，重叠也不一定是一个词。比如 who lets the dog, the dog out。是可以match文字里面的who lets the dog out的。当然文字里面的who lets the dog in，也可以match成<tag>who lets the dog</tag> in。
我的写法是扫一遍，做几个状态转移。但是细节没搞对，还是出了bug。
面试官有自己的test cases。
TA貌似也有自己的做法，一开始还跟不上我的做法的思路。也因此没办法在早期就给到比较高效的feedback。在听到我的解法和他预想的不一样的时候，就开始沉默不置可否了。直到后来看到我写的大概，加上我的不断解释，才开始跟上思路的，变得比较helpful。但也不够时间debug了。
另一个思路是先过一遍关键词组，把能延长的都延长了，这样子在文字里面就直接lookup就完了。
```

### Source: `1173099`

Original post: https://www.1point3acres.com/bbs/thread-1173099-1-1.html

```text
地里老题，给matched source加tag <yellow></yellow>，注意是exact match
solution是先找到对应的match，记录index，然后merge interval，最后根据interval的start 和end来加tag
follow up是count source的occurance然后对每个tag给出source的citation
solution也比较简单，用一个hashmap记录count，然后每个interval都记录有哪些source就行
面试官是华人小姐姐，非常漂亮，也很nice，帮我point out了一个edge case
总体面试体验非常不错
第二天通知过了 约VO
```

### Source: `1168021`

Original post: https://www.1point3acres.com/bbs/thread-1168021-1-1.html

```text
电面和onsite的coding地里细节都有，一题是加tag， 有一个注意事项是如果句子里有blueprint,但是单词是blue不能算match，另一题是filesystem
SD也和地里一样，可以看一下他们自己的产品，vault
followup当时面试官和我说有四个方向，有两个不记得了，有两个是scaling和access control
然后会问large file怎么办，怎么确定每个上传到s3的chunk是自己上传的东西
project deep dive会问一些背后的decision是怎么make的，怎么trade off之类的
behavior比较标准，和hr让你准备的差不多，比较有印象的问题是有没有协调过组和组之间的矛盾之类的
```

```text
**#10 匿名用户-DWOPM** | `2026-3-24 13:28:45`

匿名用户 发表于 2026-3-22 13:23
感谢🙏请问加tag那道是和地理的面经一样的吗还是有变种
变的部分就是这个
有一个注意事项是如果句子里有blueprint,但是单词是blue不能算match
```

## Spreadsheet / Cell Formula Engine

### Source: `1181256`

Original post: https://www.1point3acres.com/bbs/thread-1181256-1-1.html

```text
The phonescreen round had multipart excel spreadsheet question.
Part 1 - Implement excel spreadsheet class with 2 functions - get_cell() and set_cell(). Input would be just cell id and integer value. Simple hashmap would work.
Part 2 - Now the set_cell() can accept integers and formulas. Assume valid input of formulas. The question clearly mentioned we need to calculate the values in write time for all the affected cells. Simple DFS and calculation of formula would work.
Part 3 - In this part, the get_cell() function is called very less compared to set_cell() as per the requirements. How will the code change for above requirements. We need to basically calculate the formula during read time instead of write time.
Part 4 - In this part, the set_cell() can get invalid inputs or cyclic dependency. Expectation is to apply topological sort to calculate values. I wasn't able to complete this question
```

### Source: `1180964`

Original post: https://www.1point3acres.com/bbs/thread-1180964-1-1.html

```text
4年没刷Leetcode， 也没有米。裸考上阵。
题目是Excel表。
第一问
set_cell(“A1”, “10”)
get_cell(“A1”)
第二问
set_cell(“=A1+A2”)
这里面set cell可以update，get cell必须是constant access， AKA需要存cache的value。
一些Edge cases：
更改重复的reference
reference可以一层套一层
可以删除reference
第三问
handle cycle
所有的题都自己写test cases
Senior TC:600K
感谢各位大侠 求米🙏🙏
```

### Source: `1176703`

Original post: https://www.1point3acres.com/bbs/thread-1176703-1-1.html

```text
类似力扣 散死吧死
第一问: 实现setCell 和getCell，这一问没有formula，只有int数值。面试官说要好好思考用什么数据结构保存最合理。这里我就用dict<cell_name, cell_val>存了
第二问: setCell是formula， e.g. setCell("A1", "=B1+5")。可以假设只有+，没有-*%。formula肯定是=开头
这里要想到在setCell的时候要直接更新所有依赖这个cell的cell。e.g.更新B1的时候A1也需要更新，就跟spreadseet是一样的。
解法就是记录每一个cell的被依赖关系，e.g. B1的被依赖cell是{"A1"}，然后当B1的值被修改时，依次修改所有被依赖的cell
cell的值有时是formula有时是int，这个比较麻烦，建议提前写熟练
第三问: circular dependency detection。如果setCell的时候出现circular dependency的话能探测到
```

```text
**#3 匿名用户-YPHKU** | `2026-6-12 16:24:57`

匿名用户 发表于 2026-6-9 17:41
请问这题可以dfs post order 来做拓扑吗， 还是in degree 最好
我用dfs做的，但是忘了是不是post order了。只要能解出来，面试官不管是不是post order或者in degree
```

### Source: `1176644`

Original post: https://www.1point3acres.com/bbs/thread-1176644-1-1.html

```text
Design spreadsheet 类似 仐寺捌巳
Part 1 实现
- set_cell(label, value)和
- get_cell(label)。
Label 形如
"A1",
"B10"(字母 + 数字)
Value 是 integer
Part 2: Formula 支持
Cell value 可以是 formula，例如:
set_cell("A1", "10")
set_cell("A2", "A1+20") # → get_cell("A2") == 30
set_cell("A3", "A1+A2+5") # → get_cell("A3") == 45
Formula 只支持+(不考虑-、*、/)
Part 3: Cycle Detection 例如
A1 = B1+1,
B1 = A1+1→ 必须检测并报错
```

```text
**#2 匿名用户-QKTLS** | `2026-5-13 19:06:10`

也碰到了这题， 提醒一下接下来面的人 - 所有的logic 要在set cell 里做， 不能在get cell 里做。 建议chatgpt 一下怎么在get cell 里实现。
```

### Source: `1174996`

Original post: https://www.1point3acres.com/bbs/thread-1174996-1-1.html

```text
整了道新题：蠡口 三丝巴斯, 和题有点不一样的是setCell是可以设置int或者设置一个formula. followup是检查 formula和formula的circular dependency， 比如A1=B1+C1, C1=A1
因为是新题有点懵逼，所以写的有点磕巴，不知道过没。求米求米
```

```text
**#2 匿名用户-NUT3P** | `2026-5-4 11:12:25`

我也面到这一题了 也是写得磕磕绊绊
我的part1是简单的set和get
part2是根据formula infer and populate values
比如 A1=B1+C1，修改B1的value，A1也会自动populate
```

### Source: `1178950`

Original post: https://www.1point3acres.com/bbs/thread-1178950-1-1.html

```text
spreadsheet design.  和这个一样
https://www.1point3acres.com/bbs/thread-1178687-1-1.html
第一问就是简单hashmap, get_cell, set_cell
第二问是value包括公式，需要用拓扑
```

## File System / Folder-File Trie

### Source: `1129151`

Original post: https://www.1point3acres.com/bbs/thread-1129151-1-1.html

```text
这家做llm+法律的 startup跟 hr 聊的时候产品感觉很不错，电面体验巨差。细节很多很烦，要跑 test cases
面试官沟通和整体 vibe 也不是很合得来，感觉沟通有点费劲，他自己完全没准备，clarify questions好多他解释的都前后不一致
以下内容需要积分高于 188 您已经可以浏览
地里没出现的题，类似一个 file system, 实现两个功能
addFile(String path) 给一个 string “path/to/somewhere/file.txt" 存入这个 file
getFile(String path) 输入 ”path/to/somewhere“ 返回 file.text, 输入 ”path/to“ 返回somewhere 这个 folder
上来没什么自我介绍，直接开始，面试官是个美国人但是表达真的很不顺畅（还不如烙印），讲了一遍题没听懂，直接自己看，介绍很直接。自己加一个 dict of dict 然后一层层传下去就好。
followup1: 每层最多 5 个东西（包括 folder 和 file）就是当前层 key 超过 5 个key，就不能新增 folder 或者 file，哪怕只是一个新路径也不行，直接无脑 count keys 就好
followup2：如果有重复的名字就要像电脑系统一样file.txt, file(1).txt, file(2).txt 直接 parse 一下（把"." 的前后分开，然后维护一个当前的 counter递增就好。其中一个 test case 是 add(file.txt), add(file.txt), add(file(1).txt) 返回的应该是 file.txt, file(1).txt, file(1)(1).txt （这个 test case 的时候面试官自己搞了很久，然后跑完之后问我你知道这几个 test cases 在干嘛吗？全程这个要求没有提及，询问的时候也没说，他自己吭哧吭哧写的时候也不说话（我怎么知道你要干嘛？）但是我的答案是对的
追问（不用写代码）如果放到 production 怎么办？怎么 implement 到实际的 code 里面？完全不知道他想问什么？解释了存储结构，nosql，db 里放地址什么的，他好像没懂。最后问了一个怎么判断 2 个 file 是一样的内容？metadata 那些都不一样，最后我说了个单独的 service 去做内容检索？我也不知道自己在说什么.....他说 make sense 然后就到点了
全程面试官没准备过一样，中间test cases 质疑我好多次，然后我解释思路，跑了 test 之后他说 oh nvm 他自己搞错了......
```

### Source: `1180969`

Original post: https://www.1point3acres.com/bbs/thread-1180969-1-1.html

```text
總共3 rounds
Coding: File system 地裡出現過的原題, implement create file/folder and list files under folder. 需要處理file name duplication. 比如已經有a.txt, 然後要再生成一個a.txt的話, file name要變成 a (1).txt
SD: Law firm memo Q&A system:  要求設計一個 AI Agent根據big law firms的memo來回答問題
考點為RAG + LLM + Web crawling (crawling memos from law firm websites and chunking)
Project deep dive + behavioral questions:
前45分鐘是project deep dive, 自己準備一個technical complexity高的project講, 後15分鐘是core values相關的behavioral questions.
一周後收到拒信 大概率是SD沒有面好,本來以為會考祖傳的google drive所以準備了那個
沒有抓到這種LLM system相關的SD的重點是什麼 花了很多時間講RAG
```

### Source: `1180650`

Original post: https://www.1point3acres.com/bbs/thread-1180650-1-1.html

```text
就是那道filesystem的题 用trie做 跟这个帖子一模一样
https://www.1point3acres.com/interview/thread/1129151
每个part都做出来了 然后莫名其妙挂了
国人面试官全程不在线在忙自己的事 问他问题还要让我重复 才知道我在问啥
move on 祝大家好运
```

### Source: `1138730`

Original post: https://www.1point3acres.com/bbs/thread-1138730-1-1.html

```text
地里的那道file system。面经在这里：
https://www.1point3acres.com/bbs/thread-1129151-1-1.html
follow up 也问了怎么判断两个文件是一样的。 多亏了面经，准备了一下 回答用的 file hashing 例如sha256 和md5
过了，约了onsite 求好运🍀
```

### Source: `1176870`

Original post: https://www.1point3acres.com/bbs/thread-1176870-1-1.html

```text
**#4 楼主**

匿名用户 发表于 2026-06-10 23:09:40
文件系统这题 感觉是他们题库里最简单的一道，有什么trick question吗？为什么我感觉就是hashmap
tricky 的 part 就是如何处理重复的 file name。比如已经有个文件叫 A,那么当我再次插入一个新文件 A，应该把新文件名字改成 A(1)
```

## Expression Map / Symbol Evaluation

### Source: `1175246`

Original post: https://www.1point3acres.com/bbs/thread-1175246-1-1.html

```text
Harvey Onsite分为两部分
1. coding + value: VO
2. SD + experience deepdive: in office
coding:有点类似于这个经典的DFS：https://www.hack2hire.com/companies/instacart/coding-questions/68811adbf96758aa78e1d686/practice?questionId=68811ae3f96758aa78e1d687
给一个expression map，算每个symbol的最后的value
follow up是有cycle的情况下raise exception
code和solution都要在codepad上自己写
LZ当时想用DFS+三色标记做cycle detection，但没写完
这题主要浪费在和面试官交流花费太多时间，面试官看起来是个华人小哥，全程非常distractive，在忙自己的东西，LZ每次都要问两遍对方才给回应，最后也没有提问环节就走了，如果挂那大概率挂在这一轮
Value: 经典BQ，因为只有30分钟，所以不要deepdive太多东西
SD：google drive，讲清楚metadata store和blob store就好。follow up是file太大需要拆分file，那就再加一个metadata store的DB，用file id做FK。面试官比较nice，一直竖大拇指，情绪价值满分了
exp deepdive：和eng lead 聊了聊过去的项目，人比较nice，问的问题也蛮，感觉聊得还行
一周后recruiter说招到别人了，没给feedback
总之Onsite体验不错，VO体验比较差，说好的国人帮助国人呢，唉
```

## DB Connection Pool

### Source: `1175006`

Original post: https://www.1point3acres.com/bbs/thread-1175006-1-1.html

```text
店面
地理的tag/citation 题
昂赛
以下内容需要积分高于 200 您已经可以浏览
coding： db connection pool, 已经有db.query的模拟，只要完成acuqire/release connection
SD：google drive. 细节：权限管理，大文件上传下载，有文件夹怎么搞，security 怎么搞
project
BQ； 一个value 一个问题
```

```text
**#3 2026-4-29 20:04:11**

能展开讲讲这个嘛：db connection pool, 已经有db.query的模拟，只要完成acuqire/release connection
```

```text
**#4 匿名用户-UHORX** | `2026-5-1 13:11:29`

bzzzzzzzzz 发表于 2026-4-29 20:04
能展开讲讲这个嘛：db connection pool, 已经有db.query的模拟，只要完成acuqire/release connection
只要自己写锁就好。
```

```text
**#8 匿名用户-UHORX** | `2026-5-7 17:49:08`

jamesyin 发表于 2026-5-5 20:16
请问db connection pool，你是先写了一个非多线程的基础版本还是直接要求写多线程的版本呢？谢谢
我直接写多线程的。他们也不管。关键是他们test case 是AI写的，还有错在里面。真是草台班子。希望他们之后修改好。
```

## Log And Query / Sliding Window

### Source: `1146376`

Original post: https://www.1point3acres.com/bbs/thread-1146376-1-1.html

```text
Coding - Log and query, DD经典题，注意query fully match, 用set，用inverted index，不用考虑deduplicate query。
HM round - project deep dive. 这个组是做AI agent所以找了个很相关的project。HM问的很deep，得给解释清楚why，how和各种trade off。聊了整整一小时就围绕这个project，平时要做好准备。
SD - 老题，设计mint。主要focus在怎么去schedule external call （只能用pull），怎么handle call failure，大量数据时queue怎么做partition等等
Coding - 也是老题，固定滑窗，timestamp滑窗。地里有原题：
https://www.1point3acres.com/bbs/thread-1098044-1-1.html
他们家给feedback还是挺透明的，事后问到只有第一轮给了no，很可惜但尽力了，LLM 相关方向发展很快，没有什么规范的考察框架。其他轮中规中矩，难度适中，哪怕不是top priority也是个很好的拿来练手的公司。
```

## Cursor / String Editing

### Source: `1175027`

Original post: https://www.1point3acres.com/bbs/thread-1175027-1-1.html

```text
Live Coding: 耳饰尔就是刘，鼠标编辑字符串，很注重时间复杂度
Harvey Values:
https://www.harvey.ai/blog/harvey-values
跟这三条相关的经历
System Design: Data room, 核心就是google drive，默认只有PDFs，重点考organization level的ACL
Recruiter很热情每一轮都有prep call，会透coding题，但最终挂了没给feedback。需要办身份的朋友慎重考虑，他们家要求入职6个月根据performance决定要不要给你办perm。
```

```text
**#2 匿名用户-CPTVD** | `2026-5-7 06:53:57`

匿名用户 发表于 2026-5-7 00:17
求问  “Live Coding: 耳饰尔就是刘”   是 蠡口 的 尔尔久留 吗？  还是 尔似尔， 尔尔 或者  酒肆留， 久 ...
尔尔久留
```

## Web Crawler

### Source: `1072711`

Original post: https://www.1point3acres.com/bbs/thread-1072711-1-1.html

```text
Harvey是个好公司，去了onsite一共有四轮：
第一轮是跟product manager的cross-functional面试
第二轮是project deep dive，就是讲你以前做过的project
第三轮是coding，问了一个web crawler的问题，做多线程
第四轮是system design，design Google drive
```

## RAG Notebook / ML Coding

### Source: `1179903`

Original post: https://www.1point3acres.com/bbs/thread-1179903-1-1.html

```text
一共三轮
ML Coding，就是notebook补充RAG的一些实现
System Desing。也是RAG相关，毕竟是他们家的基本盘
Project deep dive，dive中会问你他们的value作为behavior signal
求米！
```
