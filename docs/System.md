# 系统活动

## Mission Pass Sql
`Exp 0`：经验值  
`Level 0`：等级  
`Season 0`：赛季  
`Mission Pass Type 0`：0未解锁，1 or 2 or 3 or 4解锁  
`Available Free Reward []`：free level 数据  
`Available High Reward []`：pass level 数据

    level 数据初始 [0] 有个0级的, 升到5级显示[0,1,2,3,4,5]
    下面是python的迭代 0 ~ 100
    a = [i for i in range(101)] #迭代0 ~ 100
`Free Pass Prize {}`：free奖励数据  
`Mission Pass Prize {}`：free奖励数据  
    
    {"0": [0],"1": [0] ,"2": [0]~ "100": [0]} 
    Prize 数据是这种类型，
    "0" : 代表着0~100级，
    [0] : 奖励领取状态 [0] 未领取, [1] 已领取
`Store Info {}`
`Free Player Flag 0`
`Time Limited Prize []`
`Chest Level 0`
`Chest Prize {}`
`Boosters [0, 0]`
`Booster Multi [2, 2.5]`
`Chest exp 0`

## Mission Pass Plus Sql
season 0
level 0
exp 0
mission_pass_plus_type 0
mission_pass_plus_prize_data {}
available_reward_data []
chest_exp 0
chest_level 0
chest_prize_data {}
last_mp_plus_type 0

## mission pass解锁弹窗
![解锁弹窗配置](images/S_mission_pass_boost.png)  
    
    在后台修改对应字段配置，可以切换不同状态的解锁弹窗
