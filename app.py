from flask import Flask, render_template, request

app = Flask(__name__)

import json
import os

# 加载单词数据文件
with open('data/word_list.json', 'r', encoding='utf-8') as f:
    word_list = json.load(f)

@app.route('/')
def index():
    """渲染首页模板"""
    return render_template('index.html')

@app.route('/api/words/<int:index>')
def get_word(index):
    """
    获取指定索引的单词数据
    参数: index - 单词索引号
    返回: JSON格式的单词数据包含单词、音标、翻译和分页信息
    """
    index = max(0, min(index, len(word_list)-1))
    return {
        'word': word_list[index][0],
        'translation': word_list[index][1],
        'phonetic': word_list[index][2],
        'current_index': index,
        'total': len(word_list)
    }

if __name__ == '__main__':
    app.run(debug=True)