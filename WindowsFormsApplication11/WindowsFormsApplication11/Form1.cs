using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WindowsFormsApplication11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

      
        private void button1_Click(object sender, EventArgs e)
        {
            /*----SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
            SqlDataAdapter adp = new SqlDataAdapter("select * from employee", con);
            DataSet ds = new DataSet();
            adp.Fill(ds);
            textBox1.Text = ds.Tables[0].Rows[0][0].ToString();
            textBox2.Text = ds.Tables[0].Rows[0][1].ToString();
            textBox3.Text = ds.Tables[0].Rows[0][2].ToString();
            textBox4.Text = ds.Tables[0].Rows[0][3].ToString();------*/
            SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
            con.Open();
            SqlCommand cmd = new SqlCommand();
            cmd.Connection = con;
            cmd.CommandText = "insert into emp(Eid,Ename,Esalary)values(@Eid,@Ename,@Esalary)";
            cmd.Parameters.AddWithValue("@Eid",textBox1.Text);
            cmd.Parameters.AddWithValue("@Ename",textBox2.Text);
            cmd.Parameters.AddWithValue("@Esalary", textBox3.Text);
            
            int i;
            i = cmd.ExecuteNonQuery();
            if (i > 0)
            {
               MessageBox.Show("Data is  Submitted Successfully!!!!");
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        } 
    }
}
