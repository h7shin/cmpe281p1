function deleteFile( id ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://elbbackend.hyunwookshin.com:8000?action=delete&id=' + id, true );
   requester.send( null );
   requester.onreadystatechange = function() {
	   console.log( requester.status );
	   console.log( 'response :' +  requester.response );
	   if ( requester.status == 200 ) {
		  console.log( 'Received an OK response' );
		  info = JSON.parse( requester.response );
		  console.log( 'error is ' + info.error );
		  console.log( 'result is ' + info.result );
	   }
	    window.location.href = "index.html";
   }
}