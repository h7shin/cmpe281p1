function fetchurl( id ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://elbbackend.hyunwookshin.com:8000?action=fetchurl&id=' + id, true );
   requester.send( null );
   requester.onreadystatechange = function() {
      var info;
	  if ( requester.readyState == XMLHttpRequest.DONE ) {
	     console.log( requester.status );
         console.log( 'response :' +  requester.response );
		 if ( requester.status == 200 ) {
		    console.log( 'Received an OK response' );
			info = JSON.parse( requester.response );
			console.log( 'id is' + id );
		    console.log( 'info is' + info );
			document.getElementById( 'download' + id ).innerHTML = '<a href="' + info.result + '"> [download] </a>';
	     }
	  }
   }
}

function populate() {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://elbbackend.hyunwookshin.com:8000?action=list&username=charles01', true );
   requester.send( null );
   requester.onreadystatechange = function() {
       var info;
	   var i;
      if ( requester.readyState == XMLHttpRequest.DONE ) {
	     console.log( requester.status );
         console.log( 'response :' +  requester.response );
		 if ( requester.status == 200 ) {
		    console.log( 'Received an OK response' );
			console.log( requester.response );
		    info = JSON.parse( requester.response );
			var requesters = [];
			for ( i = 0; i < info.result.length; i++ ) {
				
				
				
			    document.getElementById( 'files' ).innerHTML += '<div class="file" id=' + info.result[i].id_ 
				+ ' onmouseover="highlight(this)" onmouseleave="recover(this)"'
                + '>'
				+ info.result[i].filename_
				+ ' -  <a id=download'+ info.result[i].id_ +' onclick="fetchurl( \'' + info.result[i].id_ + '\')">[Get Link]</a> '
				+ '<a href="update.php?id=' + info.result[i].id_ + '">[Update]</a> '
				+ '<a href="delete.php?id=' + info.result[i].id_ + '">[Delete]</a></div>';
		    }
         } else {
		    console.log( 'Received NOT OK response' );
         }		 
	  }
   }
}

function highlight(e) {
   e.style.backgroundColor = 'white';

   e.style.color = '#8eb7ce';
}

function recover(e) {
   e.style.backgroundColor = '#8eb7ce';
   e.style.color = 'white';
}
