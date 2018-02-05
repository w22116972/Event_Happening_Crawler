# 台北市活動分佈爬蟲程式

## 目標

提供台北市各種活動資訊的種類和分佈，提供市府規劃行政區的決策參考

## 對象網站

- kktix (https://kktix.com)
- accupass (https://www.accupass.com)

## 相關技術

- 使用Scrapy框架和BeautifulSoup來爬蟲
- 當出現js渲染問題時，以selenium來解決
- 清理資料後再把地址丟給Google Geocode API得到座標
- 導入MIT開源的視覺化軟體

---

# Event Happening Crawler

## Goal

Provide information for category and distribution of activities in 
Taipei city to help government make better decision for planning resources.

## Target Address

- kktix (https://kktix.com)
- accupass (https://www.accupass.com)

## Relative Skill

- use Scrapy framework and BeautifulSoup to crawl data
- when javascript becomes problem, we use selenium instead
- clean the data and use google geocode API to get location
- feed data into MIT open source for visualization