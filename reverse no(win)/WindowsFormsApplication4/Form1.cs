using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int n, rev = 0, remainder;
            n=Convert.ToInt16(textBox1.Text);
    
            while (n != 0) {
                remainder = n % 10;
                rev = rev * 10 + remainder;
                n /= 10;
            }
            MessageBox.Show("Press OK for reverse the NUMBER");
            textBox2.Text = Convert.ToString(rev);
           
            
 
}

        }
    }
