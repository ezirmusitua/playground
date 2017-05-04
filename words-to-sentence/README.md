## Words to sentences
使用给定的词汇生成这些词汇所有组合的语句，或者随机选择词语生成
### dependencies
```bash
pip install yaml
```
### Usage
指定 输入文件，默认`example_input.yml`
```bash
python main.py -i data.yml
```
指定 输出文件，默认`example_result.yml`
```bash
python main.py -o result.md
```
指定 功能，默认`words2sentences`
```bash
# 词语组合
python main.py -f word2sentences
# 随机选择
python main.py -f random2sentences
```
### Words to sentences Example
输入 yml 格式的文件，比如内容如下:
```yml
-
  -
    name: 社会
    words:
      -
        word: 安宁
        weight: 1

  -
    name: 人类
    words:
      -
        word: 不再无知
        weight: 1
      -
        word: 不再愤怒
        weight: 1
```
可以生成:
```markdown
- [ ] 我希望`世界`是`和平`的.
- [ ] 我希望`世界`是`美好`的.
- [ ] 我希望`世界`是`爱满人间`的.
- [ ] 我希望`世界`是`和平`, `美好`的.
- [ ] 我希望`世界`是`和平`, `爱满人间`的.
- [ ] 我希望`世界`是`美好`, `爱满人间`的.
- [ ] 我希望`人类`是`不再无知`的.
- [ ] 我希望`人类`是`不再愤怒`的.
```
如果你实现了愿望，请打勾 ~

### Random word to sentences Example
输入 yml 格式同上，可能的输出如下：
```markdown
和平 的 世界
安宁 的 社会
不再无知 的 人类
```
