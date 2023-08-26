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
    public partial class Forget_password : Form
    {
        public Forget_password()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
            con.Open();
            SqlCommand cmd = new SqlCommand("select * from login where username='" + TextBox1.Text + "' and dob='" + Convert.ToString(dateTimePicker1.Text) + "'", con);
            SqlDataReader dr = cmd.ExecuteReader();
            if (dr.Read())
            {
                MessageBox.Show(" Your Identity is verified ");
                Label2.Visible = false;
                dateTimePicker1.Visible = false;
                Button1.Visible = false;
                GroupBox2.Visible = true;

            }
            else
            {
                MessageBox.Show("Identity is not Verified");
                TextBox1.Text = "";
            }
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            if (TextBox3.Text == TextBox4.Text)
            {

                SqlConnection con = new SqlConnection("Data Source=.\\sqlexpress;Initial Catalog=employee;Integrated Security=True");
                con.Open();
                SqlCommand cmd = new SqlCommand("update login set password ='" + TextBox3.Text + "'  where username='" + TextBox1.Text + "'", con);
                cmd.ExecuteNonQuery();
                con.Close();
                MessageBox.Show("  SUCCESSFULLY UPDATED PASSWORD ");

                // int dr = cmd.ExecuteNonQuery();
                //con.Close();
                //(if (dr == 0)
                // {
                // MessageBox.Show("  NOT PASSWORD ");
                //}
                //else
                //{
                // MessageBox.Show("  SUCCESSFULLY UPDATED PASSWORD ");
                //}
                Form1 login = new Form1();
                login.Show();
                this.Visible = false;
            }
            else
            {
                MessageBox.Show("  NOT UPDATED PASSWORD ");
                Form1 login = new Form1();
                login.Show();
                this.Visible = false;
            }

        }
    }
}
