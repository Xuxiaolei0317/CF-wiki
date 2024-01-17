    `在Admin网站修改任何数据，一定要确定好 “服务器端口” 选择的对不对！！！`

---
## Quest

    level等级到达 4 级时，触发新手quest！
<!-- 新手ABtest: ID 的十位数，奇数为:A组对照组，偶数为:B组实验组 -->

    
`first_quest_end_ts`: 新手quest结束时间（修改为过去时间戳可跨过新手quest）<br>
<!-- `another_first_quest_flag`: 新手ABtest,`0`是对照组,`1`是实验组<br> -->
---
## first_quest

    完成新手quest 或者倒计时结束跨过新手期

`_task_index`: 已完成第几个主题，从0开始,完成一关就 + 1<br>
`_prize_index`: 已经收取第几个主题后的奖励，从0开始,领取一个奖励就 + 1<br>
`_task_list`: 6个主题的数据<br>

    例：
        共有6个主题，前3个主题2个任务，后3个主题3个任务
        
    [{"tid": 122, # 主题id
      "tasks": [ # 主题对应的任务
            {# 任务1
                "tid": 122, # 主题id
                "current": 30, # 任务当前进度，和目标值相同即为完成
                "type": 1, # 任务属性
                "target": 30}, # 任务目标值
            {# 任务2
                "tid": 122, 
                "current": 1800000, 
                "type": 6, 
                "target": 1800000}], 
        "bet": 60000}, # 当前主题默认的bet

    {"tid": 242}], # 未进入的主题显示状态

`_prize_list`: 6个奖励的数据<br>

全部主题完成的数据: 

    [
        {"tid": 122, "tasks": [
            {"tid": 122, "current": 30, "type": 1, "target": 30}, 
            {"tid": 122, "current": 1800000, "type": 6, "target": 1800000}], 
            "bet": 60000}, 
        {"tid": 340, "tasks": [
            {"tid": 340, "current": 10, "type": 4, "target": 10}, 
            {"tid": 340, "current": 3750000, "type": 6, "target": 3750000}], 
            "bet": 100000}, 
        {"tid": 276, "tasks": [
            {"tid": 276, "current": 30, "type": 4, "target": 30}, 
            {"tid": 276, "current": 30000000, "type": 2, "target": 30000000}], 
            "bet": 300000}, 
        {"tid": 326, "tasks": [
            {"tid": 326, "current": 40, "type": 1, "target": 40}, 
            {"tid": 326, "current": 12000000, "type": 6, "target": 12000000}, 
            {"tid": 326, "current": 9000000, "type": 2, "target": 9000000}], 
            "bet": 360000}, 
        {"tid": 255, "tasks": [
            {"tid": 255, "current": 15, "type": 4, "target": 15}, 
            {"tid": 255, "current": 25000000, "type": 6, "target": 25000000}], 
            "bet": 750000}, 
        {"tid": 331, "tasks": [
            {"tid": 331, "current": 73, "type": 1, "target": 75}, 
            {"tid": 331, "current": 2, "type": 3, "target": 2}, 
            {"tid": 331, "current": 87500000, "type": 6, "target": 87500000}], 
            "bet": 1000000}]
            
---
## Novice 新手基金

    level等级到达 3 级时，触发新手基金活动！
![新手基金数据](images/Q_novice.png)  
`novice_end_first_login`: 最后一次login 弹出的结束时间 (时间戳)  
`novice_reward`: 领奖数据  
`novice_end_time`: 新手基金倒计时 (时间戳)  

