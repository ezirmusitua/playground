## HTTP 代理原理    

### 测试  
```bash  
# 普通代理  
curl -x "localhost:8000" "http://www.baidu.com"  

# 隧道代理  
export https_proxy=https://localhost:8888  
curl "https://baidu.com"  
``` 