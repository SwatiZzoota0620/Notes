<?php
if (isset($_POST["Submit"])) {

    // Get Image Dimension

    $fileinfo = @getimagesize($_FILES["file-input"]["tmp_name"]);   


    $width = $fileinfo[0];
    $height = $fileinfo[1];


    $allowed_image_extension = array(
        "png",
        "jpg",
        "jpeg",
        "gif"
    );
    
    // Get image file extension
    $file_extension = pathinfo($_FILES["file-input"]["name"], PATHINFO_EXTENSION);  
  



    // Validate file input to check if is not empty
    if (! file_exists($_FILES["file-input"]["tmp_name"])) {
        $response = array(
            "type" => "error",
            "message" => "Please select file."
        );
    }   
    
    
    // Validate file input to check if is with valid extension
    else if (! in_array($file_extension, $allowed_image_extension)) {
        $response = array(
            "type" => "error",
            "message" => "Upload valiid images. Only PNG and JPEG are allowed."
        );
        echo $result;




    }    // Validate image file size
    else if (($_FILES["file-input"]["size"] > 2000000)) {
        $response = array(
            "type" => "error",
            "message" => "Image size exceeds 2MB"
        );
    }    // Validate image file dimension
    else if ($width > "300" || $height > "200") {
        $response = array(
            "type" => "error",
            "message" => "Image dimension should be within 300X200"
        );
    } else {
        $target = "image/" . basename($_FILES["file-input"]["name"]);
        if (move_uploaded_file($_FILES["file-input"]["tmp_name"], $target)) {
            $response = array(
                "type" => "success",
                "message" => "Image uploaded successfully."
            );
        } else {
            $response = array(
                "type" => "error",
                "message" => "Problem in uploading image files."
            );
        }
    }
}
?>
<html>
<head>
<title>PHP Image Upload with Size Type Dimension Validation</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>
    <h2>PHP Image Upload with Size Type Dimension Validation</h2>
    <form id="register" action="index.php" name='register'
        method="post" enctype="multipart/form-data">
<table>
<tr>
	<td>First Name</td>
	<td><input type="text" name="fn" placeholder="Enter first name" required></td>
</tr>
<tr>
	<td>Last Name</td>
	<td><input type="text" name="ln" placeholder="Enter last name"></td>
</tr>
<tr>
	<td>E-Mail ID</td>
	<td><input type="email" name="em" placeholder="Enter email" required></td>
</tr>
<tr>
	<td>Password</td>
	<td><input type="password" name="ps" placeholder="Enter password" required></td>
</tr>
<tr>
	<td>Confirm Password</td>
	<td><input type="password" name="ps1" placeholder="Enter password" required></td>
</tr>
<tr>
	<td>Gender</td>
	<td style="font-weight: normal;"><input type="radio" name="gen" value="Male">Male
	    <input type="radio" name="gen" value="Female">Female</td>
</tr>
<tr>
	<td>Date of Birth</td>
	<td><input type="Date"></td>
</tr>
<tr>
	<td>Contact</td>
	<td><input type="text" maxlength=10></td>
</tr>
<tr>
	<td>Address</td>
	<td><textarea size=30></textarea></td>
</tr>
<tr>
	<td>State</td>
	<td><select><option>-select-</option>
		    <option>Chandigarh</option>
		    <option>Haryana</option>
		    <option>Punjab</option>
		    <option>Himachal</option>
	</select></td>
</tr>
<tr>
	<td>Image</td>
	<td><input type="file" class="file-input" name="file-input"></td>
</tr>
<tr>
	<td><input type="Submit" value="Submit"></td>
	<td><input type="reset" value="Reset"></td></tr>
</table>
</form>
    <?php if(!empty($response)) { ?>
    <div class="response <?php echo $response["type"]; ?>"><?php echo $response["message"]; ?></div>
    <?php }?>
</body>
</html>

