# Run 作弊调试
> 适用场景：本地调试 / 测试服验证。  
> 风险提示：以下脚本可能绕过正常触发条件或 CD，避免在正式服账号执行。

## CF Run 作弊调试

### 1) Facebook 点位弹窗相关
`检测是否满足 FB 点位弹窗条件`
```lua
bole.showMessageBox(json.encode({
Facebook:getInstance():isLoggedIn() ,
UserGuideControl:getInstance():getCollectStoreFreeCoinsRecord() ,
User:getInstance():isFBEnterFlag() ,
LobbyControl:getInstance():canPopUGFacebook(),
}))
```

`重置 FB 绑定弹窗 CD`
```lua
LobbyControl:getInstance().canShowUGFacebook = 1
LobbyControl:getInstance().binding_type_pop_time = 0
```

`无视 CD 直弹 3 种 FB 点位弹窗`
```lua
PopupController:getInstance():popupDialogDirectly("userguide_facebook_inbox", {fromDaily = true, delay = 0.5, from = "test"}, callback)
PopupController:getInstance():popupDialogDirectly("userguide_facebook_store", {fromDaily = true, delay = 0.5, from = "test"}, callback)
PopupController:getInstance():popupDialogDirectly("userguide_facebook_stamp", {fromDaily = true, delay = 0.5, from = "test"}, callback)
```

### 2) 广告触发与次数限制
`将主题赢钱广告触发概率改为 100%`
```lua
ADSControl:getInstance():setWinTypePR()
```

`重置前端每天 5 次广告限制`
```lua
ADSControl:getInstance():clearBigwinAdTag()
```

`deal 弹窗后广告弹窗无 CD（强制可弹）`
```lua
function StoreControl:canShowStoreOrSpAdAd()
    do return true end
end
```

### 3) 资源与本地标记重置
`重进游戏后检查删除 B 级老赛季资源（过去时间戳）`
```lua
libMM.setStringForKey("b_season_clear_ts", 1725530111)
```

`重置 loading 下载气泡标记`
```lua
cc.UserDefault:getInstance():setIntegerForKey("saved_send_update_long_reward_time", 0)
```

`清除新手 coupon 首次进店弹出标记`
```lua
libMM.setValueForCurrUser(libMM.VALUE.INTEGER, "beginner_coupon_first_enter_store", 0)
```

`清除 B 级内公会挑战弹出标记`
```lua
libMM.setIntegerForKey("last_club_challenge_pop", 0)
```

`清除个人中心头像红点标记`
```lua
libMM.setValueForCurrUser(libMM.VALUE.INTEGER, "fv_header_red", 1)
```

### 4) 活动资源与调试信息输出
`打印所有活动类型对应资源名`
```lua
local ActivityCenterControl = ActivityCenterControl or {}
local config = ActivityCenterControl.getInstance and ActivityCenterControl:getInstance():getActivityConfig() or {}
local data = {}
local max_len_type = 0
local max_len_res = 0

if type(config) == "table" and next(config) then
    for _, v in pairs(config) do
        if type(v) == "table" then
            local resource_key = v.resource_key or "未配置资源名"
            local activity_types = v.activity_type or {}
            if type(activity_types) == "table" then
                for _, id in pairs(activity_types) do
                    if type(id) == "string" or type(id) == "number" then
                        local type_str = tostring(id)
                        local res_str = tostring(resource_key)
                        table.insert(data, {type_str, res_str})
                        max_len_type = math.max(max_len_type, #type_str)
                        max_len_res = math.max(max_len_res, #res_str)
                    end
                end
            else
                local type_str = "无活动类型"
                local res_str = tostring(resource_key)
                table.insert(data, {type_str, res_str})
                max_len_type = math.max(max_len_type, #type_str)
                max_len_res = math.max(max_len_res, #res_str)
            end
        end
    end
end

if #data > 0 then
    local header_fmt = string.format("%%-%ds | %%-%ds", max_len_type, max_len_res)
    print(string.format(header_fmt, "活动类型", "资源名"))
    print(string.rep("-", max_len_type + max_len_res + 3))
    local row_fmt = string.format("%%-%ds | %%-%ds", max_len_type, max_len_res)
    for _, row in ipairs(data) do
        print(string.format(row_fmt, row[1], row[2]))
    end
else
    print("未获取到有效活动配置数据")
end
```

`打印 OpenGL 版本`
```lua
print("openGL Version：", bole.getGLESVersion())
```

### 5) 弹窗与主题实验
`本地推送弹出（60s 后；仍需满足业务弹窗条件）`
```lua
DeepLinkControl:getInstance():setLocalNotificationTestDelayTime(delay, "test", true)
```

`弹出主题内 MB 首次集满气泡`
```lua
UserGuideControl:getInstance():createUserGuideMoneyBankTips()
```

`主题结算弹窗（out_theme_rating_pop）`
```lua
local data = {
score = 80, -- 分数
settlement_level = 1, -- 结算等级
max_win = 9223372036856, -- 最大赢钱
tid = 357, -- 主题id
total_win = 239223372036854, -- 总赢钱
total_bet = 239223372036, -- 总下注
}
PopupController:getInstance():addDialogToPopupTail("out_theme_rating_pop", data)
```

`主题选 bet 实验组强制开启`
```lua
function LobbyThemeControl:isLobbyBetShowTestB()
    return true
end
```

### 6) Cash Go 专项调试
`Cash Go 转盘倒计时改为 86455`
```lua
local DataConfig = CashGoController:getInstance():getObjectClassFromRes("data/DataConfig")
local RollBallData = CashGoController:getInstance():getDataMgr():getDataByKey(DataConfig.Enum.DataKey.RollBallData)
RollBallData.getActivationRollCd = function(this)
    return 86455
end
```

## MT Run 作弊调试

### 1) 好友列表与请求数据
`打印 inbox 好友列表`
```lua
bole.showMessageBox(json.encode(FriendsCtl:getInboxList()))
```

`分别打印好友 / 请求 / 推荐列表`
```lua
local friends_list = FriendsCtl:getFriendsList()
local request_list = FriendsCtl:getRequestList()
local recommended_list = FriendsCtl:getRecommendedList()
local ret = "好友:  "
for i, v in ipairs(friends_list) do
    ret = ret .. tostring(v.user_id) .. ", "
end
ret = ret .. "\n请求:  "
for i, v in ipairs(request_list) do
    ret = ret .. tostring(v.user_id) .. ", "
end
ret = ret .. "\n推荐:  "
for i, v in ipairs(recommended_list) do
    ret = ret .. tostring(v.user_id) .. ", "
end
bole.showMessageBox(ret)
```

### 2) Inbox 与资料编辑弹窗
`请求一次 inbox 奖励数据`
```lua
SettingCtl:getTycoonInboxList()
```

`弹出首次更改头像/昵称引导弹窗`
```lua
SettingCtl:popupEditProfileRenameHotpopDialog()
```

### 3) 气泡与本地 CD 重置
`重置 Max bet 气泡 CD`
```lua
libMM.setValueForCurrUser(libMM.VALUE.STRING, "slot_bet_tip_cd", "0")
```
