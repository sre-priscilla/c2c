# Yaml to Properties Converter

```
# 周末不想加班卖苦力，搜遍全网没有好用的，手撕了一个这玩意
# 地狱空荡荡，草神在人间

# 使用文件重定向完成转换
python convert.py {yaml file} > {properties file}

# 没办法搭python环境可以用我的docker镜像
docker run -it --rm -v $PWD/test:/test --entrypoint bash registry.cn-shanghai.aliyuncs.com/ayane/c2c -c 'python convert.py /test/config.yaml > /test/config.properties'
```