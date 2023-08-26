Public Class Form1

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click

        'Set the Filter.

        OpenFileDialog1.Filter = "Bitmap |*.bmp| JPG | *.jpg | GIF | *.gif | All Files|*.*"



        'Clear the file name

        OpenFileDialog1.FileName = ""



        'Show it

        If OpenFileDialog1.ShowDialog(Me) = DialogResult.OK Then

            'Get the image name

            string(Image = OpenFileDialog1.FileName)


            'Create a new Bitmap and display it

            PictureBox1.Image = System.Drawing.Bitmap.FromFile(img)

        End If

    End Sub



End Class
