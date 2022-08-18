[sflt]:images/sflt.png 
[stb]:images/stb.png "set today begin"
[rlwc]:images/rlwc.png "reset_lucky_winner_collected"

## Spin Up Boost
`progress`：super spin up 积累次数<br>

## Repeat Win
`Repeat Win: 60000000`：赢钱数量<br>
`Deadline: 2022-08-10`：倒计时，`改成过去式的时间戳，可以重置活动数据并收奖`<br>

## Repeat Win Plus
`Repeat Win Plus: 0`：赢钱数量<br>
`Deadline: 1660190399`：倒计时，`改成过去式的时间戳，可以重置活动数据并收奖`<br>
`Uper Limit: 1055700000`：奖励上限值<br>
`Repeat Aid 20102`

## Jackpot Again
`Total Win: 0`：赢钱数量<br>
`Limit Times: 0`：奖励上限值<br>
`End Time: 0`：倒计时，`改成过去式的时间戳，可以重置活动数据并收奖`<br>

## Boosted Win
`Boosted Win: 0`：赢钱数量<br>
`Boosted Win Ratio: 0%`：赢钱后乘以的倍率<br>
`Boosted Win Limit: 0`：奖励上限值<br>
`Deadline: 0`：倒计时，`改成过去式的时间戳，可以重置活动数据并收奖`<br>

# lucky winner
   [注意]：`修改数据时一定要修改正确后再登录`

<!-- ![Activity: Lucky Winner I/II](images/C_lucky_winner.png "lucky_winner数据图")   -->

`Tickets`：彩票数量<br>
`Deadline`：活动倒计时<br>
`Lucky Winner type`：对应某个 Lucky Winner 活动的值<br>
![rlwc]：清除Lucky Winner活动的中奖状态
### 1.登录收奖
 1. 配上活动
 2. 完成购买得到`tickets`
 3. 下线
 4. 联系后端发奖
 5. 修改数据
    1. （`Activity: Lucky Winner I/II` 的 `Deadline` 修改为当前时间）
    2. 点击 ![sflt] 按钮
 6. 下掉活动（等待约30s，活动配置完全刷新）
 7. 登录
### 2.跨天在线收奖
1. 配上活动
2. 完成购买得到tickets
3. 下线
4. 联系后端发奖
5. 修改数据 （`Activity: Lucky Winner I/II` 的 `Deadline` 修改为当前时间）
6. 登录
7. 下掉活动（最多等待约30s，活动配置完全刷新）
8. 点击 Admin 的 ![stb] 按钮  


   服务器发奖后，活动中心会展示Lucky Winner活动的`中奖状态`！  
   点击 `Activity: Lucky Winner I/II` 的 ![rlwc] 可以清除活动中心的中奖状态显示

