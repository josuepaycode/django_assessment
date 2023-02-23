function viewPayments(customer_id){
    
    var table = document.getElementById(customer_id);
    const tables = document.querySelectorAll('.table-hover');
    
    if (table.style.display == "block"){
    	table.style.display = "none";
    }else{
   

		tables.forEach(t => {
	  		t.style.display = 'none';
		});
		if(table.style.display == "block"){

        	table.style.display = "none";

   		}else  if (table.style.display == "none"){
        
        	table.style.display = "block";
    	}
    }
    
	    
}

function editCustomer(id){
	const requestOptions = {
		method : "GET"
	}
	const url = "/app/customer/get/"+id;
	fetch(url, requestOptions)
	.then(function(response){
		return response.json();
	})
   	.then(function(result){
   		var modal = document.getElementById("editModal");
   		document.getElementById('id').value = result['id'];
		document.getElementById('name').value = result['name'];
		document.getElementById('paternal_surname').value = result['surname'];
		document.getElementById('email').value = result['email'];
		var span = document.getElementById("editClose");

		modal.style.display = "block";
		span.onclick = function() {
		  	modal.style.display = "none";
		}
		window.onclick = function(event) {
		  	if (event.target == modal) {
		    	modal.style.display = "none";
		  	}
		}
   	})
}
function addCustomer(){
	var modal = document.getElementById("addModal");
	var span = document.getElementById("addClose");
	modal.style.display = "block";
	span.onclick = function() {
	  	modal.style.display = "none";
	}
	window.onclick = function(event) {
	  	if (event.target == modal) {
	    	modal.style.display = "none";
	  	}
	}
}

function deleteCustomer(id, name){
	document.getElementById('deleteid').value = id;
	document.getElementById('d_name').innerHTML = name;
	var modal = document.getElementById("deleteModal");
	var span = document.getElementById("deleteClose");
	modal.style.display = "block";
	span.onclick = function() {
	  	modal.style.display = "none";
	}
	window.onclick = function(event) {
	  	if (event.target == modal) {
	    	modal.style.display = "none";
	  	}
	}

}
