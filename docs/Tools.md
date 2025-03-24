## ABtest计算

<div id="container" style="width: 500px; height: 500px; margin: 0 auto; padding: 10px; border: 1px solid black; font-family: '楷体',sans-serif; font-size: 16pt;border-radius: 5px;">
        <label for="id_input">输入要计算的ID：多个ID使用空格隔开</label>
        <input type="text" id="id_input" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;border-radius: 5px;">
        <label for="mod_input_1">模一：</label>
        <input type="number" id="mod_input_1" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;border-radius: 5px;">
        <label for="mod_input_2">模二：</label>
        <input type="number" id="mod_input_2" value="2" style="font-size: 14pt; padding: 5px; margin-bottom: 10px; border-radius: 5px;">
        <button id="calculate_button" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;background-color: green; border-radius: 5px;">计算</button>
        <label for="output_text" style="font-size: 10pt;">数据展示：</label>
        <textarea id="output_text" style="font-size: 10pt; width: 100%; height: 100px; margin-top: 10px; resize: none;"></textarea>
        <script type="text/javascript">
            // 获取 DOM 元素
            const idInput = document.getElementById('id_input');
            const modInput1 = document.getElementById('mod_input_1');
            const modInput2 = document.getElementById('mod_input_2');
            const outputText = document.getElementById('output_text');
            const calculateButton = document.getElementById('calculate_button');
            // 计算 ID 所属的 AB 分组
            function ABtest() {
                const idList = idInput.value.split(' ').map(Number);
                const divideNumber1 = parseInt(modInput1.value) || 1;
                const divideNumber2 = parseInt(modInput2.value) || 2;
                let outputStr = '';
                idList.forEach(function(id) {
                    outputStr += `${id} ÷ ${divideNumber1} ÷ ${divideNumber2} = ${id % divideNumber1 % divideNumber2}\n`;
                });
                outputText.value = outputStr;
            }
            // 绑定计算事件
            calculateButton.addEventListener('click', ABtest);
            // 绑定回车键事件
            document.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    ABtest();
                }
            });
        </script>
    </div>

<!-- ## 时间戳转换

<div id="timestamp-converter" style="width: 400px; height: auto; margin: 0 auto; padding: 10px; border: 1px solid black; font-family: '楷体',sans-serif; font-size: 16pt;">
    <label for="timestamp-input">输入时间戳（毫秒）：</label>
    <br>
    <input type="text" id="timestamp-input" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;">
    <br>
    <button id="timestamp-to-date" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;">时间戳转日期</button>
    <br>
    <label for="date-input">输入日期（YYYY-MM-DD HH:MM:SS）：</label>
    <br>
    <input type="text" id="date-input" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;">
    <br>
    <button id="date-to-timestamp" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;">日期转时间戳</button>
    <br>
    <button id="get-current-timestamp" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;">获取当前时间戳</button>
    <br>
    <button id="get-current-date" style="font-size: 14pt; padding: 5px; margin-bottom: 10px;">获取当前时间</button>
    <br>
    <label for="output-text" style="font-size: 10pt;">转换结果：</label>
    <br>
    <textarea id="output-text" style="font-size: 10pt; width: 100%; height: 50px; margin-top: 10px; resize: none;"></textarea>
    <script type="text/javascript">
        // 获取 DOM 元素
        const timestampInput = document.getElementById('timestamp-input');
        const dateInput = document.getElementById('date-input');
        const outputText = document.getElementById('output-text');
        const timestampToDateButton = document.getElementById('timestamp-to-date');
        const dateToTimestampButton = document.getElementById('date-to-timestamp');
        const getCurrentTimestampButton = document.getElementById('get-current-timestamp');
        const getCurrentDateButton = document.getElementById('get-current-date');
        // 时间戳转日期
        timestampToDateButton.addEventListener('click', function() {
            const timestamp = parseInt(timestampInput.value);
            if (!isNaN(timestamp)) {
                const date = new Date(timestamp);
                const formattedDate = date.toLocaleString();
                outputText.value = formattedDate;
            } else {
                outputText.value = '请输入有效的时间戳';
            }
        });
        // 日期转时间戳
        dateToTimestampButton.addEventListener('click', function() {
            const dateStr = dateInput.value;
            const date = new Date(dateStr);
            if (!isNaN(date.getTime())) {
                const timestamp = date.getTime();
                outputText.value = timestamp;
            } else {
                outputText.value = '请输入有效的日期（YYYY-MM-DD HH:MM:SS）';
            }
        });
        // 获取当前时间戳
        getCurrentTimestampButton.addEventListener('click', function() {
            const currentTimestamp = Date.now();
            outputText.value = currentTimestamp;
        });
        // 获取当前时间
        getCurrentDateButton.addEventListener('click', function() {
            const currentDate = new Date();
            const formattedDate = currentDate.toLocaleString();
            outputText.value = formattedDate;
        });
    </script>
    </div> -->

## 金币计算
<div id="container">
        <!-- 内联 CSS 样式 -->
        <style>
            body {
                font-family: '微软雅黑', sans-serif;
            }
            #container {
                width: 400px;
                height: 300px;
                border: 1px solid #ccc;
                padding: 10px;
            }
            label {
                display: block;
                margin-bottom: 5px;
            }
            input {
                width: 100%;
                padding: 5px;
                margin-bottom: 10px;
            }
            textarea {
                width: 100%;
                height: 75px;
                padding: 5px;
                margin-bottom: 10px;
            }
            button {
                padding: 5px 10px;
                background-color: yellow;
                border: none;
            }
        </style>
        <label for="coins_input">输入商店 100$ 的金币值:</label>
        <input type="text" id="coins_input" value="8400000">
        <label for="coins_cash_input">计算多少 $:</label>
        <input type="text" id="coins_cash_input" value="1">
        <label for="config_text">结果显示:</label>
        <textarea id="config_text" readonly></textarea>
        <button id="calculate_button">计算</button>
        <!-- 内联 JavaScript 代码 -->
        <script>
            // 获取 DOM 元素
            const coinsInput = document.getElementById('coins_input');
            const coinsCashInput = document.getElementById('coins_cash_input');
            const configText = document.getElementById('config_text');
            const calculateButton = document.getElementById('calculate_button');
            // 集成打印到文本框里
            function cg_ps(name, str) {
                name.value = str;
            }
            // 转换单位
            function float_en(num, num_digits = 1) {
                const units = ['', 'K', 'M', 'B', 'T'];
                function flo_str(num) {
                    const s = num.toString();
                    if (s.endsWith('0')) {
                        return s.slice(0, -2);
                    }
                    return s;
                }
                function strofsize(num, level) {
                    if (level >= units.length - 1) {
                        return [num, level];
                    } else if (Math.abs(num) >= 1000) {
                        num /= 1000;
                        level += 1;
                        return strofsize(num, level);
                    } else {
                        return [num, level];
                    }
                }
                const [result, level] = strofsize(num, 0);
                return `${flo_str(Math.round(result * Math.pow(10, num_digits)) / Math.pow(10, num_digits))}${units[level]}`;
            }
            // 计算金币值
            function Coins(buy_100, cash = 1) {
                return Math.floor(buy_100 / 100 * cash);
            }
            // 计算函数
            function coins_item() {
                try {
                    const num = parseInt(coinsInput.value);
                    const cash = parseFloat(coinsCashInput.value);
                    const result = Coins(num, cash);
                    const text = `商店100$价值：${num.toLocaleString()}\n${cash}$ 价值：${result.toLocaleString()} = ${float_en(result)}`;
                    cg_ps(configText, text);
                } catch (error) {
                    if (coinsCashInput.value === '' && coinsInput.value === '') {
                        cg_ps(configText, "ValueError 输入金币值");
                    } else if (coinsCashInput.value === '') {
                        const num = parseInt(coinsInput.value);
                        const cash = 1;
                        const result = Coins(num, cash);
                        const text = `商店100$价值：${num.toLocaleString()}\n${cash}$ 价值：${result.toLocaleString()} = ${float_en(result)}`;
                        cg_ps(configText, text);
                    } else {
                        cg_ps(configText, "ValueError 输入金币值");
                    }
                }
            }
            // 绑定计算事件
            calculateButton.addEventListener('click', coins_item);
        </script>
</div>