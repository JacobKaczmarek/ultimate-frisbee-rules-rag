# Ultimate Frisbee Rules Rag

## Run instructions
To run this app locally environment variables have to be set either in .env file or by seting them in the environment
``` bash
PINECONE_API_KEY=
PINECONE_ENV=
OPENAI_API_KEY=
```
After that is set the app can be ran with these commands
``` bash
pip install -r requirements.txt
python main.py
streamlit run app.py 
```

After these commands were ran successfully the web interface should be available at <http://localhost:8501>