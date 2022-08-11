# Quest

    level等级到达 4 级时，触发新手quest！
    新手ABtest：ID 的十位数，奇数为:A组对照组，偶数为:B组实验组

    
`first_quest_end_ts`: 新手quest结束时间（修改为过去时间戳可跨过新手quest）<br>
`another_first_quest_flag`：新手ABtest,`0`是对照组,`1`是实验组<br>
## first_quest

    A组用户：完成新手quest 或者倒计时结束跨过新手期

`_task_index`：当前所在第几个主题位置，从0开始<br>
`_prize_index`：当前所在第几个主题后的奖励位置，从0开始<br>
`_task_list`：6个主题的数据<br>

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

`_prize_list`：6个奖励的数据<br>

## Another First Quest

    B组用户：倒计时结束跨过新手期，且quest关卡无尽轮次

`prize_index`：当前所在第几个主题后的奖励位置，从0开始<br>
`prize_list`：6个奖励的数据<br>
`round`：quest通关轮次<br>
`task_index`：当前所在第几个主题位置，从0开始<br>
`task_list`：6个主题的数据<br>

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
## 新手基金

    level等级到达 3 级时，触发新手基金活动！
![新手基金数据](images/Q_novice.png)  
`novice_end_first_login`: 最后一次login 弹出的结束时间 (时间戳)  
`novice_reward`: 领奖数据  
`novice_end_time`: 新手基金倒计时 (时间戳)  

