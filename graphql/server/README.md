### GraphQL Demo server with express    
用 Express 搭建的一个简单的 GraphQL 服务器  

#### 使用  
```bash  
npm install  
// or nodemon  
node index.js  
```    

#### 测试  
```bash  
curl -XPOST -H "Content-Type:application/graphql" -d 'query RootQueryType { count }' http://localhost:3002/graphql    
curl -XPOST -H 'Content-Type:application/graphql' -d '{__schema { queryType { name, fields { name, description} }}}' http://localhost:3002/graphql
curl -XPOST -H 'Content-Type:application/graphql' -d 'mutation RootMutationType { updateCount }' http://localhost:3002/graphql
curl -XPOST -H 'Content-Type:application/graphql' -d '{ pokemon { name } }' http://localhost:3000/graphql  
curl -XPOST -H 'Content-Type:application/graphql' -d '{ user(name: "jferroal") { name, caught, created } }' http://localhost:3002/graphql  
curl -XPOST -H 'Content-Type:application/graphql' -d 'mutation M { upsertUser(name: "newUser") { name, caught, created } }' http://localhost:3002/graphql
curl -XPOST -H 'Content-Type:application/graphql' -d 'mutation M { caughtPokemon(name: "newUser" pokemon: "Snorlax") { name, caught, created } }' http://localhost:3002/graphql
``` 


### 参考  
[Your First GraphQL Server](https://medium.com/@clayallsopp/your-first-graphql-server-3c766ab4f0a2#.pkab58j87)  
[Writing a Basic API with GraphQL](http://davidandsuzi.com/writing-a-basic-api-with-graphql)  
  
