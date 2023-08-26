Imports System.Data.OleDb
Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim connection As OleDbConnection = New OleDbConnection()
        connection.ConnectionString = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\Users\HP\Documents\Food_management_system.accdb"
        connection.Open()
        Dim adp As OleDbDataAdapter = New OleDbDataAdapter("select * from SignIn", connection)
        Dim ds As DataSet = New DataSet()
        adp.Fill(ds)
        DataGridView1.DataSource = ds.Tables(0)

        
       


    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim connection As OleDbConnection = New OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\Users\HP\Documents\Food_management_system.accdb")
        connection.Open()
        Try
            Dim cmd As OleDbCommand = New OleDbCommand("insert into SignIn(user_name, Email, Phone_number, password) VALUES('" + TextBox1.Text + "','" + TextBox2.Text + "','" + Convert.ToInt16(TextBox3.Text) + "','" + TextBox4.Text + "')", connection)
            cmd.ExecuteNonQuery()
            connection.Close()
            MsgBox(" Successfull")
        Catch ex As Exception
            MsgBox(ex)
        End Try
    End Sub



End Class
