---
layout: default
title: Flask 缓存相关
description: 
tags: ['python']
---
<div id='mainContent' class='span8'>
	<h1 class='text-center'>Flask 缓存相关</h1>
	<hr style="border-top:1px solid #aaa;">
	<span class='font_large'><strong>关键词:</strong></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
	<span class='muted font_large'>python</span>
	<hr style="border-top:1px solid #aaa;">
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;最近在搭建的API平台中，整体采用的是Nginx 
	+ Flask + MongoDB，在最初的版本中，未加入认证等，而在Nginx中加入了Cache，这样是为了Client读取数据
	速度较快点，但在最近的新版本中，加入了认证，这里出现了问题，认证是在Flask中判定的，而Cache在Nginx转发
	前判定，这样会造成一个问题，在最初的认证完成后，同样的Client端在后续的读取中会得到缓存的内容，而不是先
	进行认证。这点显然是不行的，对应的解决方案也是有的，由于是两层结构</p>
	<img src='{{ site.localurl }}/assets/post_imgs/flask_cache/flask_cache_1.png'/>
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
	<p class='blog'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
</div>