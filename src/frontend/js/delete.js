function populateBannerFields( id ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://dock2:8000?action=about&id=' + id, true );
   requester.send( null );
   requester.onreadystatechange = function() {
      var info;
	  if ( requester.readyState == XMLHttpRequest.DONE ) {
	     console.log( requester.status );
         console.log( 'response :' +  requester.response );
		 if ( requester.status == 200 ) {
		    console.log( 'Received an OK response' );
			info = JSON.parse( requester.response );
			console.log( 'id is ' + id );
		    console.log( 'info is' + info );
			console.log( 'file name is ' + info.result.filename_ );
			console.log( 'key ' + info.result.bucketkey_ );
			document.getElementById( 'banner' ).innerHTML += ' - <b>' + info.result.filename_ + '</b>' ;
			document.getElementById( 'username' ).innerHTML = info.result.username_;
			document.getElementById( 'filename' ).innerHTML = info.result.filename_;
			document.getElementById( 'updated' ).innerHTML = info.result.updated_;
			document.getElementById( 'description' ).innerHTML = info.result.description_;
	     }
	  }
   }
}

function deleteFile( id ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://dock2:8000?action=delete&id=' + id, true );
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