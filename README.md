# gfwlist2mume
A script transforms gfwlist to rules which can be imported into Mume&amp;寒梅 at iOS.



在线获取GFWList并转换为寒梅&Mume规则的脚本，可直接用于App内URL导入功能。



## 部署

###  使用Docker

#### 你需要部署在一台服务器上用来导入。

```docker build -t gfwlist2mume .
docker build -t gfwlist2mume .
docker run --rm -it -p 8000:8000 gfwlist2mume
```

