from flask import Flask, render_template, request

app = Flask(__name__)

import json
import os

# 加载单词数据文件
with open('word_list.json', 'r', encoding='utf-8') as f:
    word_list = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/words/<int:index>')
def get_word(index):
    index = max(0, min(index, len(word_list)-1))
    return {
        'word': word_list[index][0],
        'phonetic': word_list[index][2] if len(word_list[index])>2 else '',
        'translation': word_list[index][1],
        'current_index': index,
        'total': len(word_list)
    }

if __name__ == '__main__':
    app.run(debug=True)