using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int n, sum=0;
            n = Convert.ToInt16(textBox1.Text);
            while (n != 0)
            {
                sum = sum + (n % 10);
                n = n / 10;
            }
            textBox2.Text = Convert.ToString(sum);
        }
    }
}
