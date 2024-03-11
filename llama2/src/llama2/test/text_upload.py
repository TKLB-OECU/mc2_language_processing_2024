import base64
import json
import requests

# エンコードしたいテキスト
text = """
大阪電気通信大学（おおさかでんきつうしんだいがく、英語: Osaka Electro-Communication University）は、大阪府寝屋川市初町18-8（寝屋川キャンパス内）に本部を置く日本の私立大学。1941年創立、1961年大学設置。大学の略称は大阪電通大、阪電通大、大電大、OECU。
沿革
大阪電気通信大学は、1941年に創設された東亜電気通信工学校を直接の起源としている。創立に際し、大阪無線電信学校の関係者が多く関わったことなどから、両校は近い関係にあったが、組織としては別である。1956年に大阪無線電気学校は大阪電気通信高等学校に統合された。

1924年（大正13年） 大阪無線電信電話学校開設
1932年（昭和7年） 大阪無線電気学校として認可される
1934年（昭和9年） 室戸台風による校舎倒壊のため、泉北郡千舌鳥村の仮校舎で授業再開
1936年（昭和11年） 東住吉区の新校舎に移転
1941年（昭和16年） 東亜電気通信工学校ならびに大阪高等通信工学院が認可され、設置される
1943年（昭和18年） 東亜電気通信工学校が甲種工業学校に昇格し、東亜電気通信工業学校と改称。財団法人東亜電気通信工業学校が認可。同年9月、国家総動員法により、大阪無線電気学校、大阪高等通信工学院が官立無線電信講習所大阪支所に移管され、廃校となる[注 1]
1948年（昭和23年） 東亜電気通信工学校が新制工業高等学校に昇格し、東亜電気通信高等学校に校名変更。同時に付属中学校を開設
1951年（昭和26年） 財団法人から学校法人に法人組織を改編。東亜電気通信高等学校及び付属中学校を、大阪電気通信高等学校、大阪電気通信中学校[要検証 – ノート]と改称。大阪無線電気学校は再開を申請し認可される
1954年（昭和29年） 東亜電気通信中学校を休校。[要検証  ノート]
1956年（昭和31年） 大阪無線電気学校を大阪電気通信高等学校に統合
1958年（昭和33年） 法人名を大阪電気通信学園と改称する。大阪電気通信短期大学を設置。電子工学科を開設
1959年（昭和34年） 大阪電気通信短期大学に電子工学科第2部を開設
1960年（昭和35年） 大阪電気通信中学校を再開
1961年（昭和36年） 大阪電気通信大学開学。工学部電子工学科設置
1962年（昭和37年） 工学部に通信工学科増設。大阪電気通信短期大学を大阪電気通信大学短期大学部に名称変更
1965年（昭和40年） 工学部に電子物性工学科、電子機械工学科、経営工学科増設
1973年（昭和48年） 法人名学校法人大阪電気通信学園を学校法人大阪電気通信大学と改称する
1975年（昭和50年） 工学部に精密工学科、応用電子工学科増設
1987年（昭和62年） 四条畷キャンパスを開設（1月より）。当初は各学科大学1年次のみの講義を開講
1990年（平成2年） 大学院工学研究科総合電子工学、制御機械工学、情報工学専攻の修士課程開設。短期大学部電子工学科を電子情報学科に改称
1992年（平成4年） 大学院工学研究科総合電子工学、制御機械工学、情報工学専攻の博士後期課程開設
1995年（平成7年） 工学部の経営工学科（情報工学コース、経営工学コース）の改組・転換により情報工学部情報工学科開設。短期大学部に専攻科・電子情報工学専攻を開設
1996年（平成8年） 工学部精密工学科を知能機械工学科に改称
1997年（平成9年） 工学部電子物性工学科を電子材料工学科に、応用電子工学科を光システム工学科に改称
1998年（平成10年） 工学部第2部（電子工学科、知能機械工学科）開設。工学部を工学部第1部に改称。文部省私立大学学術フロンティア推進拠点に選定される
1999年（平成11年） 大学工学部第1部の経営工学科を廃止
2000年（平成12年） 大学情報工学部を「総合情報学部」に改称。総合情報学部にメディア情報文化学科増設。（詳細は「大阪電気通信大学総合情報学部」を参照）
2001年（平成13年） 短期大学部専攻科電子情報工学専攻を廃止。工学部第1部に医療福祉工学科増設。四條畷キャンパスにコナミホールを新設
2002年（平成14年） 工学部第1部及び第2部の知能機械工学科を機械工学科に改称。短期大学部電子情報工学科第1部を短期大学部電子情報学科に改称。短期大学部第2部を廃止
2003年（平成15年） 総合情報学部にデジタルゲーム学科を増設
2004年（平成16年） 工学部医療福祉工学科を医療福祉工学部医療福祉工学科に改組（工学部第1部医療福祉工学科を廃止）。大学院総合情報学研究科メディア情報文化学専攻修士課程開設
2005年（平成17年） 工学部第1部通信工学科、光システム工学科、総合情報学部情報工学科を改組し、情報通信工学部メディアコンピューターシステム学科開設。大学院医療福祉工学研究科医療福祉工学専攻、総合情報学研究科デジタルゲーム学専攻修士課程増設。
2006年（平成18年） 工学部第1部に環境技術学科を増設。医療福祉工学部に理学療法学科を増設。工学部第1部の電子材料工学科を応用化学科に改称。情報通信工学部の光システム工学科を光・エレクトロニクス学科に改称。総合情報学部のメディア情報文化学科をデジタルアート・アニメーション学科に改称。大学院工学研究科に電子通信工学専攻博士前期・後期課程設置。大学院総合情報学研究科にコンピュータサイエンス専攻修士課程設置。寝屋川キャンパスに6階建ての「新学生ホール」が完成
2007年（平成19年） 工学部第1部を工学部に改称。工学部に基礎理工学科を増設。大学院医療福祉工学研究科博士後期課程開設。総合情報学研究科博士後期課程開設。大学院総合情報学研究科メディア情報文化学専攻をデジタルアート・アニメーション学専攻に名称変更
2008年（平成20年） 医療福祉工学部に健康スポーツ科学科を増設。寝屋川キャンパスに7階建ての「エデュケーションセンター」が完成
2009年（平成21年） 工学部の電子工学科を電気電子工学科に改称。金融経済学部アセット・マネジメント学科を開設
2011年（平成23年） 大学開学50周年。工学部環境科学科を開設。寝屋川市駅前に「駅前キャンパス」を開設
2012年（平成24年） 大学院工学研究科総合電子工学専攻を先端理工学専攻に名称変更
2013年（平成25年） 総合情報学部のメディアコンピュータシステム学科を情報学科に名称変更
2014年（平成26年） 金融経済学部のアセット・マネジメント学科を資産運用学科に名称変更
2015年（平成27年） 総合情報学部のデジタルアート・アニメーション学科をデジタルゲーム学科に統合
2018年（平成30年） 工学部に建築学科を増設。総合情報学部のデジタルゲーム学科を廃止し、総合情報学部デジタルゲーム学科とゲーム＆メディア学科に改組。金融経済学部資産運用学科を学生募集停止
学部
従来は、各学科の略称としてアルファベットによる学科記号を使用していたが、2011年度に行われた学籍番号の変更に伴い、各学部についても略称表記（学部記号）が導入された。

E 工学部[1]
C 建築学科[2]（2024年4月学生募集停止）
E 電気電子工学科[3]
H 電子機械工学科[4]
J 機械工学科[5]
U 環境科学科[6]（2024年4月学生募集停止）
N 基礎理工学科[7]
G 情報通信工学部[8]
P 情報工学科[9]
F 通信工学科[10]
H 総合情報学部[11]
W デジタルゲーム学科[12]
B ゲーム&メディア学科[13]
T 情報学科[14]
F 医療健康科学部[15]
L 医療科学科[16]
Y 理学療法学科[17]
S 健康スポーツ科学科[18]
大学院
従来は、課程記号として博士前期課程（修士）にM、博士後期課程（博士）にDを使用していたが、2011年度の学籍番号の変更に伴い、各専攻についても略称表記（専攻記号）が導入された。

工学研究科
先端理工学専攻（旧・総合電子工学専攻）（博士（前期・後期）課程）
F 電子通信工学専攻（博士（前期・後期）課程）
M 制御機械工学専攻（博士（前期・後期）課程）
I 情報工学専攻（博士（前期・後期）課程）
医療福祉工学研究科
L 医療福祉工学専攻（博士（前期・後期）課程）
総合情報学研究科
Q デジタルアート・アニメーション学専攻（旧：メディア情報文化学専攻）（博士前期課程）
W デジタルゲーム学専攻（博士前期課程）
T コンピュータサイエンス専攻（博士（前期・後期）課程）
施設
寝屋川キャンパス
メディアコミュニケーションセンター
図書館
実験センター
3D造形先端加工センター
メカトロニクス基礎研究所
衛星通信研究施設
情報学研究所
エレクトロニクス基礎研究所
自由工房
エコラボ
四條畷キャンパス
先端マルチメディア合同研究所
臨床工学実習室
運動解析実習室
図書館
コナミホール
KOZUKIホール
第1グラウンド
第2グラウンド（全天候型陸上競技場）
取り組み
研究
1998年に文部科学省より私立大学学術フロンティア推進拠点に選定されている。
教育
大阪電気通信大学チャンネル
大阪電気通信大学ドラマチャンネル「電ch（でんチャン）」とは、同学の学生が、テレビ局やプロスタッフの協力のもと、監督を始め主なスタッフを務める、産学連携による連続テレビドラマを制作・放映するプロジェクトである。

同学の産学連携に対する中心的施設である先端マルチメディア合同研究所“Joint Institute for Advanced Multimedia Studies”（JIAMS：ジェイムス）の産学連携プロジェクトの一環として、現役の学生が監督や脚本を含む演出や各技術パートにおける主だったスタッフを務め、学外プロスタッフ（映像制作会社）や学内プロスタッフ(教員やJIAMS所属研究員)らの指導と協力のもとに企画・制作を行う制作体制で行われている。日頃コンテンツ分野の研究教育を柱とした、総合情報学部のデジタルアート・アニメーション学科や、デジタルゲーム学科に所属する学生や教員が中心となり、制作・放映が行われている。

第1作目・2作目は、関西の地上波テレビ放送局で放映された。

「恋するユーレイ」 制作著作：サンテレビジョン 2006年10月6日～12月29日（全13回）毎週金曜日夕方6時放送

「弘恵の道しるべ」 制作著作：テレビ大阪 2008年7月7日～8月25日（全8回）毎週月曜日深夜1時10分放送

第3作目の「おかっぱちゃん旅に出る」（Boojil著のイラストエッセーを自らの主演でドラマ化したもの）は、2010年7月12日よりネットドラマとして、インターネット上で動画が公開されている。

2011年に恋愛シミュレーションゲーム風の大学案内アプリケーション「おいでよ?!DENTSU!!」をiTunesで配信している[19]。

商品開発
ベリーベリープロジェクトの一環で｢ソルティ・ラズベリー｣という炭酸飲料を製造販売している。

大学関係者と組織
大学関係者一覧
大阪電気通信大学の人物一覧
同窓会組織
友電会
対外関係
他大学等との連携・協定
大学コンソーシアム大阪加盟
北京科技大学（中国）
ブリティッシュコロンビア大学（カナダ）
湖西大学校（韓国）
ユトレヒト芸術大学（オランダ）
アムステルダム応用科学大学（オランダ）
江南大学（中国）
サン・カルロス大学（フィリピン）
地方公共団体との連携・協定
以下の地方公共団体、企業等と連携・協定を締結している。

寝屋川市 - 包括連携協定（大学および学校法人との間で）
四條畷市 - 包括連携協定（学校法人との間で）
茨城県教育委員会 - プログラミング教育に係る連携協力に関する基本協定
大阪市教育委員会 - プログラミング教育に係る連携協力に関する連携協定
寝屋川市教育委員会 - プログラミング教育に係る連携協力に関する連携協定
四條畷市教育委員会 - プログラミング教育に係る連携協力に関する連携協定
寝屋川キャンパス
学部 - 工学部、情報通信工学部

大学院 - 工学研究科

京阪本線 寝屋川市駅から徒歩約7分。
京阪バス「電通大寝屋川キャンパス」下車。
駅前キャンパス
[icon]	
この節の加筆が望まれています。
京阪本線 寝屋川市駅下車すぐ。
四條畷キャンパス
学部 - 医療福祉工学部、総合情報学部

研究科 - 医療福祉工学研究科、総合情報学研究科

JR西日本学研都市線 忍ケ丘駅から徒歩約20分。
JR西日本学研都市線 四条畷駅から近鉄バスで「四條畷電通大」下車。
京阪本線 大和田駅・寝屋川市駅から京阪バスで「電通大四條畷キャンパス」下車。

寝屋川キャンパス
大学設置	1961年
創立	1941年
学校種別	私立
設置者	学校法人大阪電気通信大学
本部所在地	大阪府寝屋川市初町18-8（寝屋川キャンパス内）
北緯34度45分37.2秒 東経135度37分37.1秒座標: 北緯34度45分37.2秒 東経135度37分37.1秒
キャンパス	寝屋川(大阪府寝屋川市)
駅前(大阪府寝屋川市)
四條畷(大阪府四條畷市)
学部	工学部
情報通信工学部
医療福祉工学部
総合情報学部
研究科	工学研究科
医療福祉工学研究科
総合情報学研究科

"""

#ベクトルデータベースを保存する
output_file = "./tmp_1/combined.json"

#ベクトルデータベースURL
url = "http://127.0.0.1:49152/database_to_create/"

response = requests.get(url+f"?text={text}")
response_json = json.loads(response.text)

#vector_json = response.decode('utf-8')

#print(vector_json)
print(type(response_json))
#print(response_json)
with open(output_file, 'w') as file:
    json.dump(response_json, file, indent=4)