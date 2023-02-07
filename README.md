# emojiman

_This codebase is a simple fullstack AI application that takes in a movie name and uses OpenAI API to convert that movie name to emojis_

This is a generic template and can be expanded and used to create Fullstack AI web apps using OpenAI APIs

## How to use the codebase
1. pip install --user pipenv
2. pipenv install -r path/to/requirements. txt
3. Create a `.env` with the line `OPENAI_API_KEY=<Your API key>`
4. `python manage.py runserver 9000` (you can replace the port number with any that is available)
5. Open any browser and go to `http://127.0.0.1:9000/demo/?movie=avatar` 
    1. Replace `movie` value with any movie name of your choice
    2. Use the following line in a python console to determine how to make URL safe string for the `movie` string value 
    
    ```
    import urllib.parse;
    urllib.parse.quote("mission impossible")
    ```