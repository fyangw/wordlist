document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    let total = 0;

    // 异步加载单词数据
    async function loadWord(index) {
        try {
            // 调用后端API获取单词数据
            const response = await fetch(`/api/words/${index}`);
            const data = await response.json();
            
            // 更新DOM元素内容
            document.getElementById('word').textContent = data.word;
            document.getElementById('phonetic').textContent = data.phonetic;
            document.getElementById('translation').textContent = data.translation;
            document.getElementById('counter').textContent = `${data.current_index + 1}/${data.total}`;
            
            // 更新当前索引和总数
            currentIndex = data.current_index;
            total = data.total;
        } catch (error) {
            console.error('获取数据失败:', error);
        }
    }

    // 上一页按钮点击事件
    document.getElementById('prev-btn').addEventListener('click', (e) => {
        e.preventDefault();
        if (currentIndex > 0) loadWord(currentIndex - 1);
    });

    // 下一页按钮点击事件
    document.getElementById('next-btn').addEventListener('click', (e) => {
        e.preventDefault();
        if (currentIndex < total - 1) loadWord(currentIndex + 1);
    });

    // 初始加载第一个单词
    loadWord(0);
});