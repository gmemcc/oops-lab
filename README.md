# 初始化仓库

```shell
git init
echo "venv\n.idea\n.local" > .gitignore
git add .
git commit -m "initial commit"
```

# 安装基于Python的后端的依赖

首先需要初始化venv环境

```shell
python3 -m venv venv
source venv/bin/activate
```
如果您使用IDE，可以基于IDE的功能来初始化venv环境。注意，本实验基于Python 3.11。

然后安装依赖

```shell
pip install fastapi==0.103.1 uvicorn==0.23.2 pydantic==2.3.0 SQLAlchemy==2.0.20 pydantic-settings==2.0.3
# output the installed dependencies to requirements.txt
pip freeze > requirements.txt
```

# 后端骨架代码

代码内容参见`backend`目录。使用如下命令启动后端服务：

```shell
cd backend
uvicorn main:app --reload --port 6001
```

测试后端服务是否正常运行：

```shell
curl http://127.0.0.1:6001
# {"message":"Welcome to OverseasOps Lab"}
```

