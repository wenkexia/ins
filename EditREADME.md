# INS 🍭

开源**灵感**数据库，免费无广告，Github Actions自动检测网址访问速度~

本仓库克隆自(https://github.com/zhaoolee/ins)
## 目录

(点击可直达)

--tagIndexInfoStart----tagIndexInfoEnd--

## INS项目运作机制（￣︶￣）↗
EditREADME.md是模板信息,用于生成固定README.md

你只需要往项目根目录的 [website_info.csv](https://github.com/wenkexia/ins/blob/main/website_info.csv) 添加数据源, 数据源被提交到Github 后, Github Action 将运行爬虫, 实时检测Url状态, 如果收到响应, 则Name后追加一个绿灯🟢, 否则为红灯🔴 ;

Github Action每天6点定时运行, 检测Url的状态, 绿灯后面会显示响应的毫秒数, 值越小, 说明网站响应速度越快(经费充足); 响应速度慢的大多是公益项目，如果你很喜欢某个公益项目，可以赞助一波，让站长提升网站打开速度。

新增推送信息到ntfy,如果没有设置,请在main.py中删掉相应代码


## INS项目的墓碑复活机制(╯-_-)╯~╩╩

显示红灯的项目，可能本身是个好项目，但由于种种原因搞不下去了，如果你能搞出替代品，欢迎在[issues](https://github.com/zhaoolee/ins/issues)中留言，本项目会积极收录。



## 推荐打开的正确姿势

将[https://github.com/wenkexia/ins#%E7%9B%AE%E5%BD%95](https://github.com/wenkexia/ins#%E7%9B%AE%E5%BD%95) 存入书签, 访问书签即可快速访问目录

如果某些网站无法访问, 可以参考[一款快捷签到领魔法上网天数的小工具](https://www.v2fy.com/p/109-glados-2021-06-09/)


--insStart----insEnd--

--tagStart----tagEnd--

## 欢迎贡献╰(￣▽￣)╭

贡献方法: Fork本项目, 在项目根目录的 website_info.csv **末尾**添加数据, 提交Pr即可!

