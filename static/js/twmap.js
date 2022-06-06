var place_data=[
	{
	 tag: "taipei",
	 place: "臺北市",
	},
  
	{
	 tag: "newtaipei",
	 place: "新北市",
	},
  
	{
	 tag: "taichung",
	 place: "台中市",
	},
  
	{
	 tag: "tainan",
	 place: "臺南市",
	},
  
	{
	 tag: "kaohsiung",
	 place: "高雄市",
	},
  
	{
	 tag: "keelung",
	 place: "基隆市",
	},
  
	{
	 tag: "taoyuan",
	 place: "桃園市",
	},
  
	{
	 tag: "hsinchucity",
	 place: "新竹市",
	},
  
	{
	 tag: "hsinchu",
	 place: "新竹縣",
	},
  
	{
	 tag: "miaoli",
	 place: "苗栗縣",
	},
  
	{
	 tag: "changhua",
	 place: "彰化縣",
	},
  
	{
	 tag: "nantou",
	 place: "南投縣",
	},
  
	{
	 tag: "yunlin",
	 place: "雲林縣",
	},
  
	{
	 tag: "chiayicity",
	 place: "嘉義市",
	},
  
	{
	 tag: "chiayi",
	 place: "嘉義縣",
	},
  
	{
	 tag: "pingtung",
	 place: "屏東縣",
	},
  
	{
	 tag: "yilan",
	 place: "宜蘭縣",
	},
  
	{
	 tag: "hualien",
	 place: "花蓮縣",
	},
  
	{
	 tag: "taitung",
	 place: "台東縣",
	},
  ];

function reset() {
	for(i=0 ; i < place_data.length ;i++){
		document.getElementById(place_data[i].tag).style.fill = "rgb(227, 185, 44)" ;
	}
}

// id="pingtung"
//loc = document.getElementById("pingtung");
$(function(){
//   $("#none").click(function(){
//     location.reload();
//   });
	$(".twt-map-path").click(
		function(){
			var select = document.getElementById("selectLocation")
			reset()
			document.getElementById("newtaipei").addEventListener("click", function(){ 
				if (document.getElementById("newtaipei").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "新北市"
					reset()
					select.value = "新北市"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("keelung").addEventListener("click", function(){ 
				if (document.getElementById("keelung").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "基隆市"
					reset()
					select.value = "基隆市"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("taipei").addEventListener("click", function(){ 
				if (document.getElementById("taipei").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "台北市"
					reset()
					select.value = "台北市"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("taoyuan").addEventListener("click", function(){ 
				if (document.getElementById("taoyuan").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "桃園市"
					reset()
					select.value = "桃園市"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("hsinchu").addEventListener("click", function(){ 
				if (document.getElementById("hsinchu").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "新竹市"
					reset()
					select.value = "新竹市"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("miaoli").addEventListener("click", function(){ 
				if (document.getElementById("miaoli").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "苗栗縣"
					reset()
					select.value = "苗栗縣"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("taichung").addEventListener("click", function(){ 
				if (document.getElementById("taichung").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "台中市"
					reset()
					select.value = "台中市"
					$(this).css('fill',"#901E2E");
				}
			});
			
			document.getElementById("changhua").addEventListener("click", function(){ 
				if (document.getElementById("changhua").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "彰化縣"
					reset()
					select.value = "彰化縣"
					$(this).css('fill',"#901E2E");
				}
			});
			
			document.getElementById("nantou").addEventListener("click", function(){ 
				if (document.getElementById("nantou").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "南投縣"
					reset()
					select.value = "南投縣"
					$(this).css('fill',"#901E2E");
				}
			}); 

			document.getElementById("yunlin").addEventListener("click", function(){ 
				if (document.getElementById("yunlin").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "雲林縣"
					reset()
					select.value = "雲林縣"
					$(this).css('fill',"#901E2E");
				}
			});
			
			document.getElementById("chiayi").addEventListener("click", function(){ 
				if (document.getElementById("chiayi").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "嘉義市"
					reset()
					select.value = "嘉義市"
					$(this).css('fill',"#901E2E");
				}
			}); 

			document.getElementById("tainan").addEventListener("click", function(){ 
				if (document.getElementById("tainan").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "台南市"
					reset()
					select.value = "台南市"
					$(this).css('fill',"#901E2E");
				}
			});
			
			document.getElementById("kaohsiung").addEventListener("click", function(){ 
				if (document.getElementById("kaohsiung").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "高雄市"
					reset()
					select.value = "高雄市"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("pingtung").addEventListener("click", function(){ 
				if (document.getElementById("pingtung").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "屏東縣"
					reset()
					select.value = "屏東縣"
					$(this).css('fill',"#901E2E");
				}
			}); 

			document.getElementById("yilan").addEventListener("click", function(){ 
				if (document.getElementById("yilan").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "宜蘭縣"
					reset()
					select.value = "宜蘭縣"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("hualien").addEventListener("click", function(){ 
				if (document.getElementById("hualien").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "花蓮縣"
					reset()
					select.value = "花蓮縣"
					$(this).css('fill',"#901E2E");
				}
			});

			document.getElementById("taitung").addEventListener("click", function(){ 
				if (document.getElementById("taitung").style.fill == "rgb(227, 185, 44)"){
					select.innerText = "台東縣"
					reset()
					select.value = "台東縣"
					$(this).css('fill',"#901E2E");
				}
			});

			
		}
	);

});

function getVal() {
	var val = document.querySelector('input').value;
	console.log(val);
}

