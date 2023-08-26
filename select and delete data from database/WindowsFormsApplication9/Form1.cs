using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WindowsFormsApplication9
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
            con.Open();
            SqlCommand cmd = new SqlCommand("select * from employee where Eid=" + textBox1.Text, con);
            SqlDataReader dr = cmd.ExecuteReader();
            if (dr.HasRows)
            {
                dr.Read();
                MessageBox.Show("Fetching the record of ::::" + textBox1.Text + "Eid");
                textBox2.Text = Convert.ToString(dr["Ename"]);
                textBox3.Text = Convert.ToString(dr["Esalary"]);
                textBox4.Text = Convert.ToString(dr["Eaddress"]);
            }
            else
            {
                MessageBox.Show("No record of ::::" + textBox1.Text + "Eid");
                textBox1.Text = "";
            }

            con.Close();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
            con.Open();

            SqlCommand comm = new SqlCommand("delete from employee where Eid=" + textBox1.Text, con);
            comm.ExecuteNonQuery();
            MessageBox.Show("Deleted...");
               
            
            con.Close();
        }
    }
}
