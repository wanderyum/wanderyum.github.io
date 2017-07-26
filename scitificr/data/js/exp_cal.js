function cal_mass()
{
	var u_m;
	var u_c;
	var u_v;
	var mass;
	var conc = Number(document.getElementById("conc").value);
	var volu = Number(document.getElementById("volu").value);
	var mol_wei = Number(document.getElementById("mol_wei").value);
	
	var n;
	n = document.getElementById("unit_mass").value;
	switch (n)
	{
		case "ug":
			u_m = 1e-6;
			break;
		case "g":
			u_m = 1;
			break;
		default:
			u_m = 1e-3;
	}
	n = document.getElementById("unit_conc").value;
	switch (n)
	{
		case "uM":
			u_c = 1e-6;
			break;
		case "M":
			u_c = 1;
			break;
		default:
			u_c = 1e-3;
	}
	n = document.getElementById("unit_volu").value;
	switch (n)
	{
		case "uL":
			u_v = 1e-6;
			break;
		case "L":
			u_v = 1;
			break;
		default:
			u_v = 1e-3;
	}
	
	mass = u_c * conc * u_v * volu * mol_wei / u_m;
	mass = Math.round(mass*1e6)/1e6;
	
	document.getElementById("mass").innerHTML = mass;
	if (mass == 0)
	{
		alert("超出精度范围！");
	}
}