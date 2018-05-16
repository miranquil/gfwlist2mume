# gfwlist2mume

[![GenPAC](https://img.shields.io/badge/workwith-genpac-brightgreen.svg)](https://github.com/JinnLynn/GenPAC) [![License](https://img.shields.io/badge/license-GPL--3.0-brightgreen.svg)](https://github.com/yorushika/gfwlist2mume/blob/master/LICENSE)

A script transforms gfwlist to rules which can be imported directly to Mume&amp;寒梅 at iOS.

在线获取GFWList并转换为寒梅&Mume规则的脚本，可直接用于App内URL导入功能。

## Deploy

### 使用Docker

#### 本地构建

```docker
docker build -t gfwlist2mume .
docker run --rm -it -p 8000:8000 gfwlist2mume
```

#### Docker Hub

```docker
docker pull yorushika/gfwlist2mume
docker run --rm -it -p 8000:8000 yorushika/gfwlist2mume
```
