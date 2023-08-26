using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient; 

namespace WindowsFormsApplication16
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
                        SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=final_practical;Integrated Security=True");            
                        con.Open(); 
                        SqlCommand cmd = new SqlCommand();             
                        cmd.Connection = con;             
                        cmd.CommandText = "insert into final(name,class)values(@name,@class)";             
                        cmd.Parameters.AddWithValue("@name",textBox1.Text);             
                        cmd.Parameters.AddWithValue("@class",textBox2.Text);                       
                        int i; 
                        i = cmd.ExecuteNonQuery();             
                       if (i > 0) 
                       { 
                        MessageBox.Show("Data Submitted Successfully!"); 
                       } 
 

        }
    }
}
