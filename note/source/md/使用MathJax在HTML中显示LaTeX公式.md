[//]: # (20180912)
[//]: # (在HTML中显示LaTeX公式。)
# 使用MathJax在HTML中显示LaTeX公式

LaTeX($\LaTeX$)是一种基于ΤeΧ的排版系统, 利用这种格式，即使使用者没有排版和程序设计的知识也可以充分发挥由TeX所提供的强大功能生成很多具有书籍质量的印刷品。对于生成复杂表格和数学公式，这一点表现得尤为突出。因此它非常适用于生成高印刷质量的科技和数学类文档。而HTML原生不支持LaTex格式的数学符号, 这就需要Mathjax这个JavaScript显示引擎了。

### 步骤
在head部分引入MathJax.js：
``` html
<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```

添加行内显示公式:
``` html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$', '$']]},
    messageStyle: "none"});
</script>
```

### 示例代码
latex.html:
``` html
<html>
  <head>
    <meta charset="utf-8">
    <script type="text/javascript" 
      src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
    </script>
    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({
        tex2jax: {inlineMath: [['$', '$']]},
        messageStyle: "none"});
    </script>
</head>
<body>
<p>这是一个行内公式: $e=mc^2$</p>
<p>这是一行公式: $$tan(\alpha) = \frac{sin(\alpha)}{cos(\alpha)}$$</p>
</body>
</html>
```
### 参考链接:
[MathJax在页面中正常显示公式](https://blog.csdn.net/u013291057/article/details/52861215)

[使用MathJax在HTML中显示LaTeX](https://blog.csdn.net/LiJiancheng0614/article/details/47069817)
