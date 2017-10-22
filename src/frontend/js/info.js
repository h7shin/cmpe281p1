function populateBannerFields( id, readonly ) {
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
			// for update page we should also prepoopulate, it is easier that way
			console.log( 'isReadOnly' + readonly );
			if ( !readonly ) {
			   document.getElementById( 'new_filename' ).value = info.result.filename_;
			}
			document.getElementById( 'updated' ).innerHTML = info.result.updated_;
			document.getElementById( 'description' ).innerHTML = info.result.description_;
			// for update page we should also prepoopulate, it is easier that way
			if ( !readonly ) {
			   document.getElementById( 'new_description' ).value = info.result.description_;
			}
	     }
	  }
   }
}
