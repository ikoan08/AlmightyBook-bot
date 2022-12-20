# 全知全能の書bot
discord向け胡乱ミーム自動化bot
 
## Features
discord.pyで簡単な記述。
dockerコンテナで環境もすぐに揃う
 
## Requirement
* docker

## Installation
https://www.docker.com/ に飛んで、dockerを導入する。
windowsかmacならデスクトップアプリが良い。

ルートディレクトリに`.env`ファイルを作成して
```code
DISCORD_TOKEN=***
```
と書き込んで保存

作業ディレクトリに飛んで
```bash
docker-compose up -d --build
```
でイメージビルドとコンテナ立ち上げが出来る。

```bash
docker exec -it python3 bash
```
でコンテナに入れるのでアプリ起動やライブラリの試験導入で使う

コンテは停止はデスクトップアプリで操作するか
```bash
docker-compose down
```
## Note
 
接続トークンは主に連絡取って聞いてください（絶対に公開された場所に書き込まないこと！）
