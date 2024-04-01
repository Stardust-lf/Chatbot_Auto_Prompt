# Chatbot_Auto_Prompt
A chatbot with auto-generated prompt


## web
1. install Nodejs
```python
# Ubuntu directly install node 14
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2. install yarn
```python
npm install --global yarn
```

3. 首先进入项目目录web-1, 安装前端项目依赖

```python
yarn install
```

4. 运行前端项目
```python
<<<<<<< HEAD
yarn run dev
```
=======
yarn run serve
```

## Rebuild/Update Webpage
1. Change to dir /web-1
```commandline
npm run build
```
2. Move css and js folder into /static
```commandline
mv /dist/css/ /static/css
mv /dist/js /static/js
mv /dist/favicon.ico /static
mv /dist /templates/dist
```
3. Run app.py
>>>>>>> d4f06961 (add main logic)
