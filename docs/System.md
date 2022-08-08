# 系统
## 个人数据

`Last Login Date`: 账号最后一次login时间戳<br>
`First Login`: 账号创建时间<br>
`Last Login`: 账号最后一次login时间<br>
`last Logout`：账号最后一次下线时间<br>
`Lounge Points`: 高级房点数<br>
`Lounge Ts`:高级房倒计时<br>
`Free Lounge Points`:<br>
`ranking_level` 4<br>
`b_season` 164<br>
`level_burst_bug_flag`<br>
`lounge_reward_points` 0<br>
`ooc_coin_count` 84<br>
`last_ranking_level` 4<br>
`pick_bonus_disconnection` []<br>
`mp last season purchase` [mission pass debug](#mission-pass-debug)<br><br>
`mp current season purchase` 3<br>
`user status` 3<br>
`first_quest_end_ts`：[新手基金](quest.md)<br>
`user_icon_id`：正在使用的头像ID<br>
`nick_name` XXL 10666<br>
`inbox bonus ts` 1659756669<br>
`store_free_bonus_ts` 1649972625<br>
`lounge_reward_coef` 165<br>
`starter_kit_normal`<br>
`icon_list` 已拥有的头像ID list<br>
`vip_points` 3372907<br>
`flag6`：国内ip进不去游戏时，将此数据改成`10`<br>
`store_bonus_prompt_ts` 1659856557<br>
`client_resources_flag` []<br>
`first_quest_finish_prize` {}<br>
`weekend_tournament_ranking_level` 1<br>
`weekend_tournament_last_ranking_level` 1<br>
`tc_bonus_flag` {}<br>
`lobby_list` [0, 8]<br>
`current_lobby_ui_id` 0<br>
`tc_challenge_end_ts` 0<br>
`last_b_season` 194<br>
`max_purchase` 200<br>
`selected_favourite_theme` [233, 239, 276, 181, 248, 122, 191]<br>
`first_get_b_token` {"bingo": 0, "rocket": 0, "cooking": 0, "mow": 0, "makeover": 0, "archer": 1, "tower": 0, "blast": 0, "journey": 0}<br>
`first_play_b_system` {"bingo": 0, "gof": 0, "rocket": 0, "cooking": 0, "mow": 0, "makeover": 0, "journey": 0, "archer": 1, "tower": 0, "blast": 0}
`lounge_guide` {"p2": 1, "p3": 1, "p1": 1, "p6": 1, "p7": 1, "p4": 1, "p8": 1, "free_pass": 1}<br>
`lounge_free_collected` 1<br>
`lounge_transform_info` {}<br>
`mp_send_free_booster_flag` 0<br>
`novice_end_first_login` [新手基金](quest.md)<br>
`novice_reward` [新手基金](quest.md)<br>
`novice_end_time` [新手基金](quest.md)<br>
`store_stamp_count` lucky chames的数量<br>
`lounge_store_week_ts` 1660276800<br>
`mp_buy_bundle_season` 46<br>
`stamp_easter_egg_ts` 0<br>

## frenzy_vault
a_data [6394, 335, 80]<br>
[`archer`,`bingo`,`blast`,`cooking`,`gof`,`journey`,`rocket`,`sail`,`tower`,`mow`]<br> 
[`349`, `355`, `1404`, `5062`, `0`, `601`, `1109`, `400`, `51`, `303`, `28`, `321`]<br>
`b_store_data` {"`b_store`": 65385, "is_get_lucky_loot": 1}<br>
chips 45091<br>
frenzy_spin 974

## Mission Pass

    需要重置mission pass时，可以直接将Season数据改为上个赛季进游戏即可<br>

`Exp 0`：经验值<br>
`Level 0`：等级<br>
`Season 0`：赛季<br>
`Mission Pass Type 0`：0未解锁，对应r_level+1值解锁解锁<br>
`Available Free Reward []`：free level 数据<br>
`Available High Reward []`：pass level 数据

    level 数据初始 [0] 有个0级的, 升到5级显示[0,1,2,3,4,5]
    下面是python的迭代 0 ~ 100
    a = [i for i in range(101)] #迭代0 ~ 100
`Free Pass Prize {}`：free奖励数据<br>
`Mission Pass Prize {}`：pass奖励数据<br>

    {"0": [0],"1": [0] ,"2": [0]~ "100": [0]} ：Prize 数据是这种类型，
    "0" : 代表着0~100级，[0] : 奖励领取状态 [0] 未领取, [1] 已领取
`Store Info {}`<br>
`Free Player Flag 0`<br>
`Time Limited Prize []`：限时奖励<br>

    限时奖励:
        由10个 [0,0,0] list组成，第一位为1时，代表该限时奖励已解锁，
        第二位为1时，代表该限时奖励已领取，第三位为时间戳，该限时奖励的倒计时
        例：[1, 1, 1659628802]
`Chest Level 0`：mission pass宝箱等级<br>
`Chest Prize {}`：mission pass宝箱奖励<br>
`Boosters [0, 0]`：mission star booster的倒计时<br>
`Booster Multi [2, 2.5]`：mission star booster的倍率<br>
`Chest exp 0`：mission pass宝箱经验<br>

## Mission Pass Plus

`season 0`：赛季<br>
`level 0`：等级<br>
`exp 0`：经验值<br>
`mission_pass_plus_type 0`：0未解锁，对应r_level+1值解锁<br>
`mission_pass_plus_prize_data {}`：与普通Mission Pass数据一样<br>
`available_reward_data []`：与普通Mission Pass数据一样<br>
`chest_exp 0`：super pass 宝箱经验<br>
`chest_level 0`：super pass 宝箱等级<br>
`chest_prize_data {}`：super pass 宝箱奖励<br>
`last_mp_plus_type 0`：上赛季 super pass 激活数据<br>

## mission pass debug
![解锁弹窗配置](images/S_mission_pass_boost.png)<br>

    在后台修改对应字段配置，可以切换不同状态的解锁弹窗，共有5种状态！

## Persona 广告用户

    LL 广告用户为真正0付费玩家广告用户
    HH-OO 用户有固定逻辑才会开启广告
    

`purchase_type: 1`：（HH用户 = 1，LL用户 = 2 ，OO用户 = 3）0=非广告用户<br>
`new_ad_3h_counter 12`：<br>
`new_ad_soc_premium_ts 0`：soc广告倒计时<br>
`new_ad_pachinko_premium_ts 0`：博青哥广告倒计时<br>
`new_ad_atw_ts 0`：atw广告倒计时<br>
`new_ad_b_token_ts 0`：B级token 广告倒计时<br>
`new_ad_wheel_multi_fq 1`：影响的新手做完任务之后奖励金币的数量<br> 
`new_ad_hm_multi_count 3`：影响的是看广告的奖励<br>