using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WindowsFormsApplication5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
            con.Open();
            SqlCommand cmd = new SqlCommand("select * from login where username='" + TextBox1.Text + "' and password='" + TextBox2.Text + "'", con);
            SqlDataReader dr = cmd.ExecuteReader();
            if (dr.Read())
            {
                MessageBox.Show(" WELCOME " + TextBox1.Text);
                Class1.uname = TextBox1.Text;
                Container contain = new Container();
                contain.Show();
                this.Visible = false;


            }
            else
            {
                MessageBox.Show("Incorrect Username and Password");
                TextBox1.Text = "";
                TextBox2.Text = "";

            }
        }

        private void LinkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Forget_password frgt = new Forget_password();
            frgt.Show();
            this.Visible = false;
        }
    }
}
