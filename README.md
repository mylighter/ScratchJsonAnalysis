# Scratch Json Analysis
### Analy sb3 by Python
  梦幻联动！
  这个本来是我在[A营](https://aerfaying.com)里看到的，然后看到有人做了[Python版](https://github.com/GuYan1024/SJA)，我突然来了兴趣，然后..就做了
  
  scratch文件夹是我编写的一个库，就是解析程序，使用时把scratch文件夹拿出来用。
  Show.py 需要 PygameTool 文件夹，用于显示解析结果
### 大致原理
  在 .sb3 文件中，project.json用于存放每个scratch角色的脚本和信息，利用这一点，借助Python标准库json，还原scratch脚本，并使用还原后的脚本进行统计，输出分析结果
  
	
