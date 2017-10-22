<?php
  $fileId = $_GET['id'];
?>
<html>
   <head>
      <title>
      CloudFront Project 1
      </title>
	  <script type="text/javascript" src="js/info.js"></script>
	  <script type="text/javascript" src="js/delete.js"></script>
      <link rel="stylesheet" href="css/main.css">
   </head>
   <body onload="populateBannerFields( <? echo $fileId ?>, true ); addUploadBox() ">
        <div id="banner">
            File to Be Deleted
        </div>
		<? include 'fileinfo.php'; ?>
		 <div id="response">
		    <button class="clicker" onclick="deleteFile( <? echo $fileId ?> )">Confirm Delete</button>
			<button class="clicker" onClick="window.location.href= 'index.html'">Cancel</button>
		 </div>
   </body>
</html>