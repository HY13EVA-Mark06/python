#問題
#埼京線、京浜東北線、武蔵野線の駅番号と駅名のdict変数 st_dict がある。 
#駅名に"浦和"を含む駅名と件数を表示せよ。
#また、京浜東北線(JK..)の駅数を求め表示せよ。

st_dict = {
"JA08":"大崎 (埼京線)","JA09":"恵比寿 (埼京線)","JA10":"渋谷 (埼京線)",
"JA11":"新宿 (埼京線)","JA12":"池袋 (埼京線)","JA13":"板橋 (埼京線)",
"JA14":"十条 (埼京線)","JA15":"赤羽 (埼京線)","JA16":"北赤羽 (埼京線)",
"JA17":"浮間舟渡 (埼京線)","JA18":"戸田公園 (埼京線)","JA19":"戸田 (埼京線)",
"JA20":"北戸田 (埼京線)","JA21":"武蔵浦和 (埼京線)","JA22":"中浦和 (埼京線)",
"JA23":"南与野 (埼京線)","JA24":"与野本町 (埼京線)","JA25":"北与野 (埼京線)","JA26":"大宮 (埼京線)",
"JK01":"大船 (京浜東北線)","JK02":"本郷台 (京浜東北線)","JK03":"港南台 (京浜東北線)",
"JK04":"洋光台 (京浜東北線)","JK05":"新杉田 (京浜東北線)","JK06":"磯子 (京浜東北線)",
"JK07":"根岸 (京浜東北線)","JK08":"山手 (京浜東北線)","JK09":"石川町 (京浜東北線)",
"JK10":"関内 (京浜東北線)","JK11":"桜木町 (京浜東北線)","JK12":"横浜 (京浜東北線)",
"JK13":"東神奈川 (京浜東北線)","JK14":"新子安 (京浜東北線)","JK15":"鶴見 (京浜東北線)",
"JK16":"川崎 (京浜東北線)","JK17":"蒲田 (京浜東北線)","JK18":"大森 (京浜東北線)",
"JK19":"大井町 (京浜東北線)","JK20":"品川 (京浜東北線)","JK22":"田町 (京浜東北線)",
"JK23":"浜松町 (京浜東北線)","JK24":"新橋 (京浜東北線)","JK25":"有楽町 (京浜東北線)",
"JK26":"東京 (京浜東北線)","JK27":"神田 (京浜東北線)","JK28":"秋葉原 (京浜東北線)",
"JK29":"御徒町 (京浜東北線)","JK30":"上野 (京浜東北線)","JK31":"鶯谷 (京浜東北線)",
"JK32":"日暮里 (京浜東北線)","JK33":"西日暮里 (京浜東北線)","JK34":"田端 (京浜東北線)",
"JK35":"上中里 (京浜東北線)","JK36":"王子 (京浜東北線)","JK37":"東十条 (京浜東北線)",
"JK38":"赤羽 (京浜東北線)","JK39":"川口 (京浜東北線)","JK40":"西川口 (京浜東北線)",
"JK41":"蕨 (京浜東北線)","JK42":"南浦和 (京浜東北線)","JK43":"浦和 (京浜東北線)",
"JK44":"北浦和 (京浜東北線)","JK45":"与野 (京浜東北線)","JK46":"さいたま新都心 (京浜東北線)","JK47":"大宮 (京浜東北線)",
"JM10":"西船橋 (武蔵野線)","JM11":"船橋法典 (武蔵野線)","JM12":"市川大野 (武蔵野線)",
"JM13":"東松戸 (武蔵野線)","JM14":"新八柱 (武蔵野線)","JM15":"新松戸 (武蔵野線)",
"JM16":"南流山 (武蔵野線)","JM17":"三郷 (武蔵野線)","JM18":"新三郷 (武蔵野線)",
"JM19":"吉川美南 (武蔵野線)","JM20":"吉川 (武蔵野線)","JM21":"越谷レイクタウン (武蔵野線)",
"JM22":"南越谷 (武蔵野線)","JM23":"東川口 (武蔵野線)","JM24":"東浦和 (武蔵野線)",
"JM25":"南浦和 (武蔵野線)","JM26":"武蔵浦和 (武蔵野線)","JM27":"西浦和 (武蔵野線)",
"JM28":"北朝霞 (武蔵野線)","JM29":"新座 (武蔵野線)","JM30":"東所沢 (武蔵野線)",
"JM31":"新秋津 (武蔵野線)","JM32":"新小平 (武蔵野線)","JM33":"西国分寺 (武蔵野線)",
"JM34":"北府中 (武蔵野線)","JM35":"府中本町 (武蔵野線)"
}

char = "浦和"
kensuu = 0
for key in st_dict:
  if char in st_dict[key]:
    print(st_dict[key])
    kensuu = kensuu + 1
print(kensuu,"駅")
print("")
char = "京浜東北線"
kensuu = 0
for key in st_dict:
  if char in st_dict[key]:
    kensuu = kensuu + 1
print("京浜東北線は",kensuu,"駅")
