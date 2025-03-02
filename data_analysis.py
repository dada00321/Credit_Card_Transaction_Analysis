import pandas as pd
import matplotlib.pyplot as plt

# 假設你的資料已儲存為純文字檔案 'credit_card_data.csv'，或直接貼入程式中
# 這裡我直接使用你提供的完整資料作為範例

# 將資料讀入 DataFrame
df = pd.read_csv("NCCC_TWN_IDSUM.CSV")

# 將年月轉換為 datetime 格式
df['年月'] = pd.to_datetime(df['年月'], format='%Y%m')

# 篩選出需要的欄位
#df = df[['年月', '信用卡產業別', '信用卡處理中心處理筆數']]
df = df[['年月', '信用卡產業別', '信用卡處理中心處理金額[新臺幣]']]

# 按照產業別分組並轉換為寬格式
#pivot_df = df.pivot(index='年月', columns='信用卡產業別', values='信用卡處理中心處理筆數')
pivot_df = df.pivot(index='年月', columns='信用卡產業別', values='信用卡處理中心處理金額[新臺幣]')

# 設置中文字體 (如果你使用中文環境，需要設置字體)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 使用微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 繪製圖表
plt.figure(figsize=(14, 8))
for column in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[column], label=column, marker='o', markersize=4)

# 設置圖表標題和標籤
#plt.title('信用卡處理中心處理筆數趨勢 (按產業別)', fontsize=16)
plt.title('信用卡處理中心處理金額趨勢 (按產業別)', fontsize=16)
plt.xlabel('年月', fontsize=14)
#plt.ylabel('處理筆數', fontsize=14)
plt.ylabel('處理金額', fontsize=14)
plt.legend(title='信用卡產業別', loc='upper left', bbox_to_anchor=(1, 1))  # 將圖例移到右邊
plt.grid(True)

# 調整 X 軸顯示間隔 (每隔 6 個月顯示一次)
plt.xticks(pivot_df.index[::6], rotation=45)

# 調整佈局以避免標籤被裁切
plt.tight_layout()

# 顯示圖表
plt.show()