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

## Usage

### 起動
```bash
docker-compose up -d --build
```

### ログ確認
```bash
docker logs discord-bot
```

### 停止
```bash
docker-compose down
```

### コンテナに入る（デバッグ用）
```bash
docker exec -it discord-bot bash
```
## Note
 
接続トークンは主に連絡取って聞いてください（絶対に公開された場所に書き込まないこと！）
