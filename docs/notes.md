\# Git \& Linux 笔记



\## 2026-06-26



\### Git 每天用的命令



| 命令 | 什么意思 |

|------|---------|

| git clone <url> | 把远程仓库下载到本地 |

| git status | 看看改了哪些文件 |

| git add . | 把所有改动加入暂存区（准备提交） |

| git commit -m "消息" | 提交，拍个快照 |

| git push | 推送到 GitHub |

| git pull | 从 GitHub 拉取最新版本 |

| git log | 查看提交历史 |



\### Linux 每天用的命令



| 命令 | 什么意思 |

|------|---------|

| pwd | 我在哪个目录 |

| ls | 当前目录有什么文件 |

| cd <目录> | 进入某个目录 |

| cd .. | 回到上一层 |

| mkdir <名字> | 新建文件夹 |

| touch <名字> | 新建空文件 |

| cp a b | 复制文件 |

| mv a b | 移动/重命名文件 |

| rm <文件> | 删除文件（小心） |

| grep "关键词" <文件> | 在文件里搜关键词 |



### 今天学到的新命令
- git status  → 查看当前仓库状态（哪些文件改过）
- git diff    → 查看具体改了什么内容



每天必做	命令
看看改了什么	git status
看看具体改动	git diff
全部暂存	git add .
提交	git commit -m "说明"
推送	git push
拉取最新	git pull

分支操作	命令
新建并切换分支	git checkout -b 分支名
切换分支	git checkout 分支名
查看所有分支	git branch
推送分支	git push origin 分支名

救命操作	命令
丢弃未提交的改动	git checkout -- 文件名
撤销最近一次提交	git reset --soft HEAD~1
查看历史	git log --oneline