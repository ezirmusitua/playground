### 在 Idea 中编辑和查看 UML 图例  
#### 安装和配置 PlantUML 插件
##### 安装 graphViz
```shell 
sudo apt install graphViz   
```  
##### 在 Idea 中安装 PlantUML
1. 打开设置
2. 搜索 PlantUML(repositories) 中  
3. 安装插件并重启 idea  
#### 基本使用  
新建 PlantUML 相关的文件, 开始使用  

### PlantUML 通用语法  

#### 线和箭头  

#### skinparam 设置  

#### creole 和 HTML 格式支持  

#### 添加备注  

#### 利用 newpage 分割图例  

#### 利用 as 参数设置别名  

#### 利用 autonumber 自动为消息编号  

### 类图  
#### dot/line  
|dot|line|  
|---|----|  
|.. |\-\-|  

#### relation  
|association|extension|composition|aggregation|  
|-----------|---------|-----------|-----------|  
|<..........|<\|......|*..........|o----------|  
改变方向:  
--/.. 垂直  
-/.   水平  
-left->  
-right->  
-up->  
-down->  

#### 关系上的标识
对元素的说明, 在每一边使用 "" 来说明:  
ClassA -- "demo" ClassB  
在关系之间使用标签来说明时, 使用 ":"后接`标签文字`:  
ClassA <-- ClassB: Contains  
在标签的开始或结束位置添加`<`或`>`表明对象作用关系上:  
ClassA <-- ClassB: Contains <  

#### 添加方法  
为了声明域或者方法，你可以使用`后接域名`或`方法名`  
系统检查是否有括号来判断是方法还是域  
ClassA <-- ClassB  
ClassA : equals()  
ClassB : Object[] elementData  
ClassB : size()  
或者使用更像编程语言的方式  
class ClassA {  
  String data  
  void methods()  
}  
class ClassB {  
   field1: Integer  
   field2: Date  
}  

#### 可访问性  
|Character	|Visibility     |  
|-----------|---------------|  
|-			|private        |  
|#			|protected      |  
|~			|package private|  
|+			|public         |  

如  
class ClassA {  
  -sex  
  -character  
  +eat  
}  

#### 抽象和静态  
通过修饰符{static}({classifier})或者{abstract}，可以定义静态或者抽象的方法或者属性  
这些修饰符可以写在行的开始或者结束  
class ClassA {  
  {static}     language  
  {abstract}   speak  
  {classifier} speak  
}  

#### 类体修饰符  
`../__/--/== separator text ==/--/__/..`  

#### 备注和模板  
模板: `<< & >>`  
注释: note [top of, ... as noteName, Class>left/right/top/bottom]  
链接注释:  
```  
A LinkTo B  
note on link #color: noteText  
```  
注释中可以使用 html tag  

#### 抽象类和接口  
关键字:  
1. `abstract`/`abstract class`  
2. interface  
3. annotation  
4. enum  

#### as 关键字  
在类或者枚举的显示中使用非字母符号  

#### 隐藏  
使用命令`hide/show`可以用参数表示类的显示方式  

#### 泛型  
关键字: `< & >`  


### 状态图  
#### 合成状态  
```  
state StateName {  
  // state transfer  
}  
```  

#### 长名字  
```  
state "This is a very long state name" as ls1;  
```  

#### 并发状态  
关键字: --  
```  
  // sync states 1  
  --  
  // sync states 2  
```  


### 时序图  
#### 参与者  
`participant`, `actor`, `boundary`, `control`, `entity`, `database`  
使用`as`设置别名  
可以把关键字`create`放在第一次接收到消息之前, 以强调本次消息实际上是在创建新的对象  
```  
participant "A humours man" as Bob #colorOfParticipant  
```  

#### Message to self  
A -> A  

#### Arrow styles  
A -[lineColor]-> B: message  

1. 表示一条丢失的消息: 末尾加 x  
2. 让箭头只有上半部分或者下半部分: 将<和>替换成\或者 /  
3. 细箭头: 将箭头标记写两次 (如 >> 或 //)  
4. 虚线箭头: 用 -- 替代 -  
5. 箭头末尾加圈: ->o  
6. 双向箭头: <->  

#### 箭头自动编号  
关键字: autonumber  
```
autonumber "<b>[000]"  
```  

#### 分组  
1. alt/else  
2. opt  
3. loop  
4. par  
5. break  
6. critical  
7. group, 后面紧跟着消息内容  

#### 引用  
`ref over`  

#### 延迟  
`...`  
```  
Alice -> Bob: Authentication Request  
...  
Bob --> Alice: Authentication Response  
```  

#### 空间  
`|||`  
```  
Bob --> Alice: ok  
|||  
Alice -> Bob: message 2  
```  

#### 生命线的激活与撤销  
`activate`和`deactivate`  
`destroy`表示一个参与者的生命线的终结  
```  
User -> A: DoWork  
activate A  

A -> B: << createRequest >>  
activate B  
  
B -> C: DoWork  
activate C  
C --> B: WorkDone  
destroy C  

B --> A: RequestCreated  
deactivate B  

A -> User: Done  
deactivate A  
```  

#### 嵌套的生命线  
```  
User -> A: DoWork  
activate A #FFBBBB  

A -> A: Internal call  
activate A #DarkSalmon  

A -> B: << createRequest >>  
activate B  

B --> A: RequestCreated  
deactivate B  
deactivate A  
A -> User: Done  
deactivate A  
```

#### 进入和发出消息  
```
[-> Bob  
[o-> Bob  
[o->o Bob  
[x-> Bob  

[<- Bob  
[x<- Bob  

Bob ->]  
Bob ->o]  
Bob o->o]  
Bob ->x]  

Bob <-]  
Bob x<-]  
```  

#### 包裹参与者  
`box` & `end box`  
还可以在`box`关键字之后添加标题或者背景颜色  
```  
box "Internal Service" #LightBlue  
	participant Bob  
	participant Alice  
end box  
participant Other  

Bob -> Alice : hello  
Alice -> Other : hello  
```  

#### 移除脚注  
`hide footbox`  
```  
hide footbox  
title Footer removed  

Alice -> Bob: Authentication Request  
Bob --> Alice: Authentication Response  
```  


### 活动图  
活动标签以冒号开始, 以分号结束  
文本格式支持`creole wiki`语法  
活动默认安装它们定义的顺序就行连接  
```
colorOfActivity:ActivityText  
-[#colorOfArrow,styleOfArrow]->  
```  

#### 开始\结束  
```  
start // activity start  
// activities  
stop // or end // activity end  
```  

#### 条件语句  
`if`, `then`, `else`  
```
if (condition1) then (yes)  
  // process 1  
elseif (condition2) then (yes)  
  // process 2  
else (no)  
  // process 3  
endif  
```  

#### 循环  
`repeat - repeat white(cond)`  
```  
repeat  
  // process  
repeat while (more data?)
// while  
while (data available?)
  // process
endwhile  
```  

#### 并行处理  
`fork`  
```  
fork  
  :Treatment 1;  
fork again  
  :Treatment 2;  
end fork  
```  

#### 组合  
`partition`  
```  
partition PartitionName {  
    // activities  
}  
```  

#### 泳道  
关键词`|`  
```  
|#SwimLaneColor|SwimLaneName|  
```  

#### 移除箭头  
`detach`  
```  
:foo6;  
detach  
:foo7;  
```  

#### SDL  
通过修改活动标签最后的分号分隔符(;), 可以为活动设置不同的形状  
1. |  
2. <  
3. >  
4. /  
5. ]  
6. }  


### 包图  
类似类图  
**包之间的关系类似类图**  
关键字:  
```  
package "PackageName" HexPackageColor PackageStyle[<<Node\Rectangle\Folder\Frame\Cloud\Database>>]{  
  // ... content  
}  
```  

#### 名空间  
类似`包图`的语法  
关键词: namespace  
设置分隔符: set namespaceSeparator ::  


### 对象图  
很类似类图  
关键词 object  

### 用例图  
关键词: usecase  
```  
usecase useCaseName as AliasName  
```  

#### 角色  
关键词: actor  
```  
:First Actor:  
:Another\nactor: as Men2  
actor Men3  
actor :Last actor: as Men4  
```  

#### 用例描述  
```  
usecase UC1 as "You can use  
several lines to define your usecase.  
You can also use separators.  
--  
Several separators are possible.  
==  
And you can add titles:  
..Conclusion..  
This allows large description."  
```  

#### 角色继承  
类似 类图  

#### 构造类型  
关键词: `<< & >>`  

#### 分割图示  
关键词: newpage  


### 组件图  
不知道哪里会用到...  
[Read Manual Here](http://plantuml.com/component-diagram)  


### Reference    
[PlantUML Official Site](http://plantuml.com)  

