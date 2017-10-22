<?php
  $fileId = $_GET['id'];
?>
<html>
   <head>
      <title>
      CloudFront Project 1
      </title>
      <script type="text/javascript" src="js/delete.js"></script>     
      <link rel="stylesheet" href="css/main.css">
   </head>
   <body onload="populateBannerFields( <? echo $fileId ?> )">
        <div id="banner">
            File to Be Deleted
        </div>
		<div class="file">
		    <b> File Name to Be Deleted: </b><div id="filename" class="field"></div>
			<b> File Owner: </b><div id="username"  class="field"></div>
			<b> Last Updated: </b><div id="updated"  class="field"></div>
			<b> Description: </b><div id="description"  class="field"></div>
        </div>
		 <div id="response">
		    <button class="clicker" onclick="deleteFile( <? echo $fileId ?> )">Confirm Delete</button>
		 </div>
   </body>
</html>