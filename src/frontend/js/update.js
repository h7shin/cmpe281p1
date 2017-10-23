function updateFile( id ) {
   console.log( 'updating ' + id );
   newfilename = document.getElementById("new_filename").value;
   newdescription = document.getElementById("new_description").value;
   console.log( 'Will transmit new filename:', newfilename );
   console.log( 'Will transmit new file description:', newdescription );
   requester =  new XMLHttpRequest();
   var data = new FormData();
   requester.open( 'PUT', 'http://elbbackend.hyunwookshin.com:8000', true );
   data.append( 'fileid', id );
   data.append( 'filename', newfilename );
   data.append( 'description', newdescription );

   requester.send( data );
   requester.onreadystatechange = function() {
	   console.log( requester.status );
	   console.log( 'response :' +  requester.response );
	   if ( requester.status == 200 ) {
		  console.log( 'Received an OK response' );
		  info = JSON.parse( requester.response );
		  console.log( 'error is ' + info.error );
		  console.log( 'result is ' + info.result );
	   }
	   console.log( 'Returning to main page' );
	   window.location.href = "index.html";
   }
}