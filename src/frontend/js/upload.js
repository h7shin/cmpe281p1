function addUploadBox(uploadtype, id) {
   document.getElementById( 'uploadbox' ).innerHTML += '<div class="uploader" >'
		 + 'Upload a new file :   '
		 +    '<input type="file" id="filetoupload"/>'
		 +    '<input type="submit" name="action" value="upload" onclick="submit(\'' + uploadtype + '\',\''+ id +'\')"/>'
		 + ''
		 + '</div>';
}		

function submit(uploadtype, id) {
   requester =  new XMLHttpRequest();
   var data = new FormData();
   document.getElementById( 'status' ).innerHTML = 'Uploading... Please Wait'
   requester.open( 'POST', 'http://elbbackend.hyunwookshin.com:8000', true );
   data.append( 'filetoupload', document.getElementById("filetoupload").files[0] );
   requester.setRequestHeader( 'Content-type', 'multipart/mixed' );
   requester.setRequestHeader( 'Username', 'charles01' );
   requester.setRequestHeader( 'Uploadtype', uploadtype );
   requester.setRequestHeader( 'Fileid', id );
   requester.send( data );
   console.log( requester.status );
   console.log( requester.response );
   console.log( requester.responseText );
   requester.onreadystatechange = function() {
      // refresh the page
      if ( requester.readyState == XMLHttpRequest.DONE ) {
         window.location.href = "index.html";
		 document.getElementById( 'status' ).innerHTML = 'Finished Uploading the file'
	  }
   }
}
