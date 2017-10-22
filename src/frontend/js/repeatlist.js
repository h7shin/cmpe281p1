function submit() {
   requester =  new XMLHttpRequest();
   var data = new FormData();
   requester.open( 'POST', 'http://dock2:8000', true );
   data.append( 'filetoupload', document.getElementById("filetoupload").files[0] );
   requester.setRequestHeader( 'Content-type', 'multipart/mixed' );
   requester.setRequestHeader( 'Username', 'charles01' );
   requester.send( data );
   console.log( requester.status );
   console.log( requester.response );
   console.log( requester.responseText );
}

function fetchurl( id ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://dock2:8000?action=fetchurl&id=' + id, true );
   requester.send( null );
   requester.onreadystatechange = function() {
      var info;
	  if ( requester.readyState == XMLHttpRequest.DONE ) {
	     console.log( requester.status );
         console.log( 'response :' +  requester.response );
		 if ( requester.status == 200 ) {
		    console.log( 'Received an OK response' );
		    console.log( JSON.parse( requester.response ) );
	     }
	  }
   }
}
		
function populate() {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://dock2:8000?action=list&username=charles01', true );
   requester.send( null );
   requester.onreadystatechange = function() {
       var info;
	   var i;
      if ( requester.readyState == XMLHttpRequest.DONE ) {
	     console.log( requester.status );
         console.log( 'response :' +  requester.response );
		 if ( requester.status == 200 ) {
		    console.log( 'Received an OK response' );
		    info = JSON.parse( requester.response );
			var requesters = [];
			for ( i = 0; i < info.result.length; i++ ) {
				
				
				
			    document.getElementById( 'files' ).innerHTML += '<div class="file" id="file' + i 
				+ '" onmouseover="highlight(this)" onmouseleave="recover(this)"'
				+ '" onclick="fetchurl( \'' + info.result[i].id_ + '\')"'
                + '>'
				+ info.result[i].filename_
				+ '     [update] [delete]</div>';
		    }
         } else {
		    console.log( 'Received NOT OK response' );
         }		 
	  }
   }
   document.getElementById( 'uploadbox' ).innerHTML += '<div class="file" '
         + '" onmouseover="highlight(this)" onmouseleave="recover(this)">'
		 + ''
		 +    '<input type="file" id="filetoupload"/>'
		 +    '<input type="submit" name="action" value="upload" onclick="submit()"/>'
		 + ''
		 + '</div>';
}

function highlight(e) {
   e.style.backgroundColor = 'white';

   e.style.color = '#8eb7ce';
}

function recover(e) {
   e.style.backgroundColor = '#8eb7ce';
   e.style.color = 'white';
}
