## 个人数据
`Last Login Date`: 账号最后一次login时间戳<br>
`First Login`: 账号创建时间<br>
`Last Login`: 账号上次一次login时间<br>
`last Logout`：账号上次下线时间<br>
`Level`: 等级<br>
`VIP`: VIP等级<br>
`Credits`: 拥有的`coins`数量<br>
`Lounge Points`: 高级房点数<br>
`Lounge Ts`:高级房倒计时<br>
`Free Lounge Points`:：待确认<br>
`ranking_level`：排行榜房间等级<br>
`is_admin`: 为`3`时是可以手动调整r level的等级；为`0`时是模仿真实用户登录情况<br>
`b_season`：当前B级赛季<br>
`level_burst_bug_flag`：待确认<br>
`lounge_reward_points`：待确认<br>
`ooc_coin_count`：总付费次数<br>
`last_ranking_level`：上次排行榜房间<br>
`pick_bonus_disconnection`：pick_bonus 断线数据<br>
`new_b_used`：待确认<br>
`old_b_used`：待确认<br>
`next_today_begin`：待确认<br>
`next_first_login`：待确认<br>
`stamp_round`：待确认<br>
`bc_avg_bet_ls`：待确认<br>
`behaviour_data_bug_fix`：待确认<br>
`mistery_bank_breaker_flag`：待确认<br>
`over_mp_chest_user_start_ts`：待确认<br>
`last_birthday`: 改成`[0,0,0]`可触发生日周年弹窗<br>
`mp last season purchase`：上赛季的MP解锁状态<br>
`mp current season purchase`：当前赛季的MP解锁状态<br>
`user status`：默认值为:`0`，改成`3`后，自身r level不会随购买变动了<br>
`first_quest_end_ts`：[新手期倒计时](quest.md)<br>
`user_icon_id`：正在使用的头像ID<br>
`nick_name`：游戏内编辑的name<br>
`inbox bonus ts`：待确认<br>
`store_free_bonus_ts`：store bonus的收奖倒计时，改成过去式时间戳，可重置<br>
`lounge_reward_coef`：待确认<br>
`starter_kit_normal`：待确认<br>
`icon_list` 已拥有的头像ID list<br>
`vip_points`：VIP点数<br>
`flag6`：国内ip进不去游戏时，将此数据改成`10`<br>
`store_bonus_prompt_ts`：待确认<br>
`client_resources_flag`：待确认<br>
`first_quest_finish_prize`：新手期奖励<br>
`weekend_tournament_ranking_level`：周末锦标赛，排行榜房间<br>
`weekend_tournament_last_ranking_level`：周末锦标赛，上次排行榜房间<br>
`tc_bonus_flag` {}<br>
`lobby_list：[0, 8]`：拥有的大厅UI<br>
`current_lobby_ui_id`：当前使用的大厅UI<br>
`tc_challenge_end_ts` 0<br>
`last_b_season`：最后一次的B级赛季<br>
`max_purchase`：最高付费金额<br>
`selected_favourite_theme`：喜欢主题的list<br>
`supplement_chips_status`: 改成`0`重置第二货币用尽促销<br>
`first_get_b_token`：B级免费token的领取状态<br>
`first_play_b_system`：B级九选一的选中游玩状态<br>
`lounge_guide`：高级房引导<br>
`lounge_free_collected`：高级房引导中的free pass卡领取状态<br>
`lounge_transform_info`：待确认<br>
`mp_send_free_booster_flag`：赠送免费的mission star booster弹窗<br>
`novice_end_first_login`：[新手基金](quest.md)<br>
`novice_reward`：[新手基金](quest.md)<br>
`novice_end_time`：[新手基金](quest.md)<br>
`store_stamp_count` lucky chames的数量<br>
`lounge_store_week_ts`：lounge兑换商店道具刷新倒计时<br>
`mp_buy_bundle_season`：待确认<br>
`stamp_easter_egg_ts`：待确认<br>
`no_adv_return_end`：7天内免费看广告的结束时间戳<br>
`total_purchase `：用户的全部付费额<br>
`another_first_quest_flag`：[新手ABtest](quest.md)<br>

## frenzy_vault
<!-- `a_data` ：[6394, 335, 80]<br> -->
[archer,bingo,blast,cooking,gof,journey,rocket,sail,tower,mow] <br>
[330, 355, 1404, 5062, 0, 601, 1109, 400, 51, 303, 28, 321]：对应B级的token数量<br>
`c_data` ：[]<br>
`a_type` ：[]<br>
`b_store_data` {"`b_store`": `lucky_loot数量`, "is_get_lucky_loot": 1}<br>
<!-- `c_type` ：[]<br> -->
`chips`：第二货币数量<br>
`frenzy_spin`：邮票里frenzy spin的次数<br>

## Mission
`Reset Ts`：mission倒计时间戳，改成过去时间可以重置daily mission的完成状态<br>
`Wheel Collected`：Mission Points领奖状态<br>
`Mission Points`：Mission Points点数<br>
`Index`：第几个mission任务<br>
`Type`：当前mission任务的Type<br>
`Target`：当前mission任务的目标值<br>
`Current`：当前mission任务的进度值<br>
`Target Special`：待确认<br>
`Target M7 Special`：待确认<br>
`Target M7 Retry`：待确认<br>
`Wager`：待确认<br>
`Index_prize`：当前mission任务的奖励数据<br>
`Avg Bet`：待确认<br>
`Disconnection`：断线数据<br>
`Wheel Extra Chance`：待确认<br>
`Wheel Unused Chance`：待确认<br>
`Guide`：引导<br>
`Glory Mission Reset Ts`：待确认<br>
`Glory Mission Type`：当前HONOR Mission任务的Type<br>
`Glory Mission Target`：当前HONOR Mission任务的目标值<br>
`Glory Mission Current`：当前HONOR Mission任务的进度值<br>
`Glory Mission Wager`：待确认<br>
`Glory Mission Prize`：当前HONOR Mission任务的奖励数据<br>
`box_collected`：待确认<br>
`Glory Mission Finish Flag`：待确认<br>
`Glory Mission Unlock Flag`：待确认<br>

## Mission Pass

    需要重置mission pass时，可以直接将Season数据改为上个赛季进游戏即可<br>

`Exp 0`：经验值<br>
`Level 0`：等级<br>
`Season 0`：赛季<br>
`Mission Pass Type 0`：0未解锁，对应r_level+1值解锁解锁<br>
`Available Free Reward []`：free level 数据<br>
`Available High Reward []`：pass level 数据

    Reward level 数据初始 [0] 有个0级的, 升到5级显示[0,1,2,3,4,5]
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
    
## Smash Egg
`Gold Hammer Status`：每天领取金锤子的数量<br>
`Gold Hammer Extra`：购买金锤子的数量<br>
`Gold Hammer Disconnection`：断线数据<br>
`Gold Hammer Flag`：`1` = 已经砸过蛋了，`0` = 未砸蛋<br>
`Silver Hammer Status`：每天领取银锤子的数量<br>
`Silver Hammer Extra`：购买银锤子的数量<br>
`Silver Hammer Disconnection`：断线数据<br>
`Silver Hammer Flag`：`1` = 已经砸过蛋了，`0` = 未砸蛋<br>
<!-- `Hammer Reset Ts`：待确认<br>
`Old Player Flag`  ：待确认<br>
`Gold Shell Pos LIst`  ：待确认<br>
`Gold Shell Win List`  ：待确认<br>
`Gold Shell Round`：待确认<br>
`Gold Shell Pick`：待确认<br>
`Gold Shell Status`：待确认<br>
`Silver Shell Pos LIst`：待确认<br>
`Silver Shell Win List`：待确认<br>
`Silver Shell Round`：待确认<br>
`Silver Shell Pick`：待确认<br>
`Silver Shell Status`：待确认<br>
`Special Chips Purchased`：待确认<br>
`Reset Feature Ts`：待确认<br> -->

## Blazing Challenge
EXP:：待确认<br>
Level:：待确认<br>
Season:：待确认<br>
Season End:：待确认<br>
Missions:：待确认<br>
Mission End:：待确认<br>
Prizes:：待确认<br>
Bonus Game Disconnection:：待确认<br>
Ranking Prize Disconnection:：待确认<br>
Avg Bet:：待确认<br>
Mini Theme Next Time:：待确认<br>
EXP Activity 31002:：待确认<br>
END Time Activity 31002:：待确认<br>
Boosters:：待确认<br>
Commodities:：待确认<br>
History Rank:：待确认<br>


## Mansion Quest
name：待确认<br>
stars：待确认<br>
room：待确认<br>
room mission：待确认<br>
finish current phase：待确认<br>
mission：待确认<br>
disconnection room mission：待确认<br>
home_phase：待确认<br>
boosters_data：待确认<br>
skip_card：待确认<br>
mission_stage_data：待确认<br>
flash tag：待确认<br>
stage prize：待确认<br>
房间奖励数据：待确认<br>
当前房间奖励：待确认<br>
房间奖励断线数据：待确认<br>
新主题任务：待确认<br>
新主题idx：待确认<br>

## Mansion Quest Ranking
mq tid：待确认<br>
round index：待确认<br>
round points：待确认<br>
round target：待确认<br>
season：待确认<br>
mansion lv：待确认<br>
mission：待确认<br>
round prize：待确认<br>
rank prize：待确认<br>

## level_up_party
index：待确认<br>
tasks：待确认<br>
reset_ts：待确认<br>
has_game：待确认<br>
bet：待确认<br>
first_flag：待确认<br>
today_ts：待确认<br>
common_game：待确认<br>

## Login Bonus
week count：待确认<br>
week type：待确认<br>
week base coins：待确认<br>
month count：待确认<br>
month type：待确认<br>
month base coins：待确认<br>
last login：待确认<br>
has checked in：待确认<br>
month status：待确认<br>
ab flag：待确认<br>

## Weekend Tournament
`store_booster_ts`：待确认<br>
`store_booster_multi`：待确认<br>
`daily_bonus_booster_ts`：待确认<br>
`daily_bonus_booster_multi`：待确认<br>
`medal_booster`：待确认<br>
`is_collected`：待确认<br>
`season`：待确认<br>
`race`：待确认<br>
`points`：待确认<br>
`end_ts`：待确认<br>
`disconnection`：待确认<br>
`ranking_level`：待确认<br>
`last_ranking_level`：待确认<br>
wt_season：待确认<br>
last_send_inbox_ts：待确认<br>

## Coupon New
`Store Coupon Id`: 手动清除list内coupon时，此数据改`-1`<br>
`Store Coupon List`：inbox内的`Store coupon`<br>
`Piggy Coupon Id`: 手动清除list内coupon时，此数据改`-1`<br>
`Piggy Coupon list`：inbox内的`Money bank coupon`<br>
`coupon_7days_no_purchase_last_get_ts`：待确认<br>
`Emerald Coupon Id`: 手动清除list内coupon时，此数据改`-1`<br>
`Emerald Coupon List`：inbox内的`Emerald coupon`<br>
`Chips Bank Coupon Id`: 手动清除list内coupon时，此数据改`-1`<br>
`Chips Bank Coupon List`：inbox内的`Emerald bank coupon`<br>

## Discount coupon
`Store Discount Coupon Id`：手动清除list内coupon时，此数据改`-1`<br>
`Store Discount Coupon List`：inbox内的`降价coupon`的list<br>

## inbox sp product
`last_sp_store_end_ts`：inbox内Money bank促销，倒计时间戳<br>
`sp_piggy_product`：inbox内商店促销：`0`没有，`1`有<br>
`sp_store_product`：inbox内Money bank促销：`0`没有，`1`有<br>
`last_sp_piggy_end_ts`：inbox商店促销，倒计时间戳<br>

## Lobby Bonus
Megaball Progress：待确认<br>
SoC Progress：待确认<br>
Multiplier：待确认<br>
Golden Multiplier：待确认<br>
Turbo ts：待确认<br>
Instant ts：待确认<br>
Soc Count：待确认<br>
Turbo Speedy ts：待确认<br>
Last Multipler ts：待确认<br>
Slot Blast ts：待确认<br>

## Purchase: Piggy Bank (New)
`Piggy Bank Balance`: 当前bank数量<br>
`Piggy Price LV`: 价格等级<br>
`Piggy Config LV`: 配置等级<br>
`Piggy Bank Down LV`: 降档（0=不降，1=降一档，2=降两档）最大2<br>
`Piggy Bank Up LV`: 升档（0=不降，1=降一档，2=降两档）最大2<br>
`Piggy Bank Max Days`: 未登录天数（7天降价）<br>
`Piggy First Purchase`: 1<br>
`Piggy Bank AB Test`: 0<br>
`Piggy Bank Data Migration`:<br>

## Emerald Bank
`Emerald Bank`: 当前bank数量<br>
`Config Level`: 配置等级<br>
`Price Level`: 价格等级<br>
`Level up`: 升档（0=不降，1=降一档，2=降两档）最大2<br>
`Level Down`: 降档（0=不降，1=降一档，2=降两档）最大2<br>
`Max Days`: 未登录天数（7天降价）<br>


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