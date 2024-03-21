

$(function(){
	if ($("#chercher_image_mf").length > 0){
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
	}
	if ($(".lucemessage").length > 0){
	$(".lucemessage").click(function(){
		var formdata= new FormData();
		formdata.set("messageid",$(this)[0].dataset.id);
		$.ajax({
			url:"/lucemessage",
			   type: "post",

			  // Form data
			     data: formdata,
			
			         // Tell jQuery not to process data or worry about content-type
			             // You *must* include these options!
			                 cache: false,
			                     contentType: false,
			                         processData: false,
			success:function(data){
				//
				//alert(data);
				window.location="/messages";
			}
		});
		return false;
	});

	}
});
