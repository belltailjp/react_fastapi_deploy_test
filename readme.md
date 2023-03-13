frontendをreactに、apiをpython+fastapiな構成にしたときAPIエンドポイントから直接フロントエンド配信したければできるのか確認したかった。


```bash
cd frontend
npm install
npm run build
```

```bash
cd ../api
uvicorn app:app
```

これでindex.htmlはAPIサーバの/から配信される
