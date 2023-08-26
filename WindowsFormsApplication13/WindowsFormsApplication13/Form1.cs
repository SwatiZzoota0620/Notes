using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication13
{
    public partial class Form1 : Form
    {
        public static string l1;
        public static string l2;
        public static string l3;
        public static string l4;

        public Form1()
        {
            InitializeComponent();
        }

        

        private void Button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog opnfd = new OpenFileDialog();
            opnfd.Filter = "Image Files (*.jpg;*.jpeg;.*.gif;)|*.jpg;*.jpeg;.*.gif";
            if (opnfd.ShowDialog() == DialogResult.OK)
            {
                PictureBox1.Image = new Bitmap(opnfd.FileName);
            }  
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            l1 = TextBox1.Text;
            l2 = TextBox2.Text;
            l3 = TextBox3.Text;
            l4 = TextBox4.Text;
            Form2 frm2 = new Form2(PictureBox1.Image);

            frm2.Show();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
