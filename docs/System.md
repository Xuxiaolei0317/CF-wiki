# 系统活动

## Mission Pass

    需要重置mission pass时，可以直接将Season数据改为上个赛季进游戏即可  

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
`Mission Pass Prize {}`：pass奖励数据  
    
    {"0": [0],"1": [0] ,"2": [0]~ "100": [0]} 
    Prize 数据是这种类型，
    "0" : 代表着0~100级，
    [0] : 奖励领取状态 [0] 未领取, [1] 已领取
`Store Info {}`
`Free Player Flag 0`
`Time Limited Prize []`：限时奖励

    由10个 [0,0,0] list组成
    第一位为1时，代表该限时奖励已解锁
    第二位为1时，代表该限时奖励已领取
    第三位为时间戳，该限时奖励的倒计时
    例：[1, 1, 1659628802]

`Chest Level 0`：mission pass宝箱等级  
`Chest Prize {}`：mission pass宝箱奖励  
`Boosters [0, 0]`：mission star booster的倒计时  
`Booster Multi [2, 2.5]`：mission star booster的倍率  
`Chest exp 0`：mission pass宝箱经验

## Mission Pass Plus
`season 0`：赛季  
`level 0`：等级  
`exp 0`：经验值  
`mission_pass_plus_type 0`：0未解锁，1 or 2 or 3 or 4解锁  
`mission_pass_plus_prize_data {}`：与普通Mission Pass数据一样  
`available_reward_data []`：与普通Mission Pass数据一样  
`chest_exp 0`：super pass 宝箱经验
`chest_level 0`：super pass 宝箱等级
`chest_prize_data {}`：super pass 宝箱奖励
`last_mp_plus_type 0`：上赛季 super pass 激活数据

## mission pass购买界面作弊
![解锁弹窗配置](images/S_mission_pass_boost.png)  
    
    在后台修改对应字段配置，可以切换不同状态的解锁弹窗
    共有5种状态！

## 广告用户
### Persona
`purchase_type: 1`
`new_ad_3h_counter 12`
`new_ad_soc_premium_ts 0`
`new_ad_pachinko_premium_ts 0`
`new_ad_atw_ts 0`
`new_ad_b_token_ts 1640923072`
`new_ad_wheel_multi_fq 1`
`new_ad_wheel_multi_dm`
`new_ad_wheel_multi_hm`
`new_ad_hm_multi_count 3`