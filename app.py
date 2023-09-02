import json
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader, DirectoryLoader
from sqlalchemy import null
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

template_dir = os.path.abspath("Frontend")
static_dir = os.path.abspath("Frontend/src")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)


os.environ["OPENAI_API_KEY"] = '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'


@app.get("/")
def loginPage_get():
    return render_template("index.html")


@app.post("/gptit")
def getAnswer():
    resived = request.get_json()

    file = resived['file']
    query = "This is a Exel sheet converted to JSON, containting informations about patients in my hospital " + \
        resived['msg']
    g = json.dumps(file['Sheet1'])
    f = open("slaw.txt", "w")
    f.write(g)
    f.close()
    loader2 = TextLoader("slaw.txt")
    loader = DirectoryLoader(".", "*.txt")
    index = VectorstoreIndexCreator().from_loaders([loader2])

    response = index.query(query, llm=ChatOpenAI(model="gpt-3.5-turbo-16k"))
    reply = {"responce": response}
    return jsonify(reply)


if __name__ == "__main__":
    print(template_dir)

    app.run(host='0.0.0.0', port=5454, debug=False)
