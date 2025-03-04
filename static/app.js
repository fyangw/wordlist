document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    let total = 0;

    async function loadWord(index) {
        try {
            const response = await fetch(`/api/words/${index}`);
            const data = await response.json();
            
            document.getElementById('word').textContent = data.word;
            document.getElementById('phonetic').textContent = data.phonetic;
            document.getElementById('translation').textContent = data.translation;
            document.getElementById('counter').textContent = `${data.current_index + 1}/${data.total}`;
            
            currentIndex = data.current_index;
            total = data.total;
        } catch (error) {
            console.error('获取数据失败:', error);
        }
    }

    document.getElementById('prev-btn').addEventListener('click', (e) => {
        e.preventDefault();
        if (currentIndex > 0) loadWord(currentIndex - 1);
    });

    document.getElementById('next-btn').addEventListener('click', (e) => {
        e.preventDefault();
        if (currentIndex < total - 1) loadWord(currentIndex + 1);
    });

    loadWord(0);
});