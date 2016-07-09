function page_swit(a)
{
	switch (a)
	{
	case "home":
	{
		document.getElementById("ifra").src = "home.html";
		document.getElementByClassName("switch").style.border = "0px solid red";
		document.getElementById("home").style.border = "2px solid red";
	}
	break;
	case "cv":
	{
		document.getElementById("ifra").src = "cv.html";
		document.getElementByClassName("switch").style.border = "0px solid red";
		document.getElementById("cv").style.border = "2px solid red";
	}
	break;
	case "publ":
	{
		document.getElementById("ifra").src = "publication.html";
		document.getElementByClassName("switch").style.border = "0px solid red";
		document.getElementById("publ").style.border = "2px solid red";
	}
	break;
	default:
		document.getElementById("ifra").src = "home.html";
	}
	document.getElementById("asd").value = a;
}