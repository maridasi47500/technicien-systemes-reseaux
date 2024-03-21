$(function(){
	$("#chercher_image_mf").change(function(){
		$.ajax({
			url:"/photos?mf="+$(this).val(),
			success:function(data){
				var pic1=$("#image_id");
				pic1[0].innerHTML="";
				var foto=data.photos;
				for(var i = 0;i<foto.length;i++){
				pic1[0].innerHTML+="<option value=\""+foto[i].id+"\">"+foto[i].text+"</option>";
					
				}
			}
		});
	});
});
