function page_swit(a)
{
	switch (a)
	{
	case "home":
	{
		document.getElementById("ifra").src = "home.html";
		hide_border();
		document.getElementById("home").style.border = "2px solid red";
	}
	break;
	case "cv":
	{
		document.getElementById("ifra").src = "cv.html";
		hide_border();
		document.getElementById("cv").style.border = "2px solid red";
	}
	break;
	case "publ":
	{
		document.getElementById("ifra").src = "publication.html";
		hide_border()
		document.getElementById("publ").style.border = "2px solid red";
	}
	break;
	case "sett":
	{
		document.getElementById("ifra").src = "setting.html";
		hide_border()
		document.getElementById("sett").style.border = "2px solid red";
	}
	break;
	case "link":
	{
		document.getElementById("ifra").src = "link.html";
		hide_border()
		document.getElementById("link").style.border = "2px solid red";
	}
	break;
	default:
		;
	}
	document.getElementById("asd").value = a;
}

function hide_border()
{
var list=document.getElementById("menu");
var str=list.getElementsByTagName("td");
for(var i=0;i<str.length;i++)
	if(str[i].className=="switch")
		str[i].style.border = "0px solid red";   
}
