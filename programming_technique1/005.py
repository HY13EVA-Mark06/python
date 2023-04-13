import pandas as pd
df_item = pd.read_excel("order.xlsx", sheet_name="商品マスタ")
df_member = pd.read_excel("order.xlsx", sheet_name="会員マスタ")
df_order = pd.read_excel("order.xlsx", sheet_name="受注データ")
df_item.head()
df_member.head()
df_order.head()

#問1
df_1 = pd.merge(df_order, df_member, on="会員ID", how="left")
married_grp = df_1.groupby(["既婚"]).sum()
married_grp = married_grp.sort_values("金額",ascending=False)
married_grp
#既婚列でグループ集計し金額が降順になるように並び替えをした結果
#1→既婚が先頭になったため、既婚のほうが多い。

#問2
married_grp = df_1.groupby(["性別","既婚"]).sum()
married_grp = married_grp.sort_values("金額",ascending=False)
married_grp
#性別列と既婚列でグループ集計し金額が降順になるように並び替えをした結果
#1→男性、0→未婚が先頭になったため、男性で未婚の受注金額が最も多い。