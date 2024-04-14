# Chatbot_Auto_Prompt
A chatbot with auto-generated prompt

## Run Sofeware Directly
```commandline
python app.py YOUR_OPEN_AI_KEY
```

## Web Development
1. install Nodejs
```python
# Ubuntu directly install node 14
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2. install yarn
```commandline
npm install --global yarn
```

3. Install packages

```commandline
cd web-1
yarn install
```

4. Debug/Run the UI part
```commandline
yarn run dev
yarn run serve
```

## Rebuild/Update Whole Website
1. Rebuild
```commandline
cd web-1
npm run build
```
2. Move css and js folder into /static
```commandline
mv /dist/css /static/css
mv /dist/js /static/js
mv /dist/favicon.ico /static
mv /dist /templates/dist
```
3. Run site script with OPENAI-KEY
```commandline
python app.py YOUR_OPEN_AI_KEY
```


