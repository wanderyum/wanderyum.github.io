function page_swit(para){
	switch (para){
		case "home":{
			document.getElementById("ifra").src = "home.html";
			break;
		}
		case "note":{
			document.getElementById("ifra").src = "note/note_index.html";
			break;
		}
		case "program":{
			document.getElementById("ifra").src = "prog/program.html";
			break;
		}
		case "scitific_research":{
			document.getElementById("ifra").src = "scitificr/scitificr.html";
			break;
		}
		case "resume":{
			document.getElementById("ifra").src = "resume/resume.html";
			break;
		}
	}
}

function note_goto(path){
    document.getElementById("body").innerHTML = "<iframe id='subifra' src=\""+path+"\" ></iframe>";
}
