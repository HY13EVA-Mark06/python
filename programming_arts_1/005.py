#問1
#未婚と既婚のどちらの受注合計金額が多いか調べてください。
#【問1】
#会員マスタ の[既婚]列 0→未婚 1→既婚
#• 表の結合やグループ集計処理など、データフレーム操作のプログラムを 作成して調べてください。
#• データフレーム操作のプログラムを提出してください。 また、理由と結果を具体的にコメント(#)で記述してください。
#(解答例) #〇〇〇〇〇により、未婚のほうが多い • 使用する変数名は自由。

#問2
#男性と女性、未婚と既婚の組合せの内、最も受注合計金額が多い組合せはどれか調べてください。
#[性別]列 1→男性 2→女性
#[既婚]列 0→未婚 1→既婚

import pandas as pd
df_item = pd.read_excel("order.xlsx", sheet_name="商品マスタ")
df_member = pd.read_excel("order.xlsx", sheet_name="会員マスタ")
df_order = pd.read_excel("order.xlsx", sheet_name="受注データ")
df_item.head()
df_member.head()
df_order.head()

#問1解答
df_1 = pd.merge(df_order, df_member, on="会員ID", how="left")
married_grp = df_1.groupby(["既婚"]).sum()
married_grp = married_grp.sort_values("金額",ascending=False)
married_grp
#既婚列でグループ集計し金額が降順になるように並び替えをした結果
#1→既婚が先頭になったため、既婚のほうが多い。

#問2解答
married_grp = df_1.groupby(["性別","既婚"]).sum()
married_grp = married_grp.sort_values("金額",ascending=False)
married_grp
#性別列と既婚列でグループ集計し金額が降順になるように並び替えをした結果
#1→男性、0→未婚が先頭になったため、男性で未婚の受注金額が最も多い。
