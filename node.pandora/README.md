## Pandora Demo  
Pandora.js 的基本使用  

### Pandora 是什么？  
阿里开发的 Node 应用启停工具   
提供了通用的 Node 应用运行时模型和相关基础设施  
提供了标准的 Node 应用 DevOps 流程  

### 目标  
 - [ ] Pandora 的基本配置和使用

### pandora 基本使用  
```bash  
# installation
yarn global add pandora
npm install -g pandora  
# init app
pandora init ./demo-proj --name demo
# start app(daemon)
pandora start ./demo-proj --name demo --env="NODE_ENV=production"  
# list running app
pandora list  
# show demo process info  
pandora ps demo  
# log process  
pandora log demo  --follow --lines --full --daemon  
# stop app  
pandora stop demo  
# start app 
pandora dev ./demo-proj --name demo --env="NODE_ENV=production"  
# restart app
pandora restart demo  
pandora exit  
```

