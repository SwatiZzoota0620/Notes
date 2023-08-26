<%@ Page Language="vb" AutoEventWireup="false" CodeBehind="WebForm1.aspx.vb" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style>
        #txtUserName , #txtPWD{
 padding: 14px 20px;
  margin: 8px 0;
  border: 1px solid #ccc;
    width: 90%;
  
        }
#btnSubmit {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

 .avatar
        {
            height: 216px;
            width: 282px;
        }
.container
{
    height:635px;
    width:100%;
}




        #Form1
        {
            height: 589px;
        }




    </style>
</head>
<body class="container" style="text-align:center; background-color: #008000;">
  
<div style="border:2px solid black; text-align:center;" width:auto;" >

 <form id="Form1"  runat="server">
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <img src="images\img_avatar2.png" alt="Avatar" class="avatar" style="text-align:center;" /><br /> <br /><br />
<asp:Label ID="Label1" runat="server" Text="USERNAME"></asp:Label>
 <br />
<asp:TextBox ID="txtUserName" runat="server"  />
<asp:RequiredFieldValidator ID="rfvUser" ErrorMessage="Please enter Username" ControlToValidate="txtUserName" runat="server" />

    <br />
    <asp:Label ID="Label2" runat="server" Text="PASSWORD"></asp:Label>
&nbsp;<br />
      <asp:TextBox ID="txtPWD" runat="server" TextMode="Password"/>
<asp:RequiredFieldValidator ID="rfvPWD" runat="server" ControlToValidate="txtPWD" ErrorMessage="Please enter Password"/>

    <br />

<asp:Button ID="btnSubmit" runat="server" Text="Submit"  />
<a href="#">Forget password</a>&nbsp;&nbsp;&nbsp;&nbsp;
 <br />
 <br />
 <br />
</form>


</div>

</body>
</html>
